#!/usr/bin/env python3
"""Isi blok telemetri di README profil dengan angka NYATA dari GitHub + status layanan.

Kenapa bukan WakaTime: waktu editor mengukur mengetik, bukan keluaran. Sejak kerja
dibantu agen, angka WakaTime turun padahal hasil yang dikirim justru bertambah — metrik
itu jadi menyesatkan. Yang diukur di sini adalah yang benar-benar mendarat:

  1. Keluaran   : commit, PR dibuka/merge, review, hari aktif, repo tersentuh (30 hari).
  2. Permukaan  : bahasa menurut byte kode di repo yang tersentuh.
  3. Produksi   : kode HTTP + latensi tiap layanan yang memang hidup di internet.

Semua angka berasal dari API GitHub dan HTTP sungguhan. Tidak ada nilai yang dikarang:
bagian yang gagal diisi "n/a" dan alasannya ditulis di berkas, bukan disembunyikan.

Dipakai oleh .github/workflows/metrics.yml. Lokal: GITHUB_TOKEN=... python3 metrics.py
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

OWNER = "ivanwilliammd"
README = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")
README = os.path.normpath(README)
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""

# Layanan publik yang memang dijalankan (bukan rencana). Diperiksa sungguhan tiap hari.
SERVICES = [
    ("Portfolio site", "https://ivanwilliamharsono.com"),
    ("IVAI", "https://ivai.app"),
    ("IVAI Link", "https://link.ivai.app"),
    ("SmarTerm", "https://terminology.ivanmd.id"),
    ("SmartClaim", "https://claim.ivanmd.id"),
    ("WISH", "https://wish.ivai.app"),
    ("Clinix", "https://clinix.meditechku.com"),
    ("SPECTRA", "https://spectra.meditechku.com"),
    ("Pay", "https://pay.meditechku.com"),
    ("IvanMD Identity", "https://auth.ivanmd.id"),
]

LANG_LABEL = {
    "PHP": "PHP", "Blade": "Blade", "Python": "Python", "TypeScript": "TypeScript",
    "JavaScript": "JavaScript", "Vue": "Vue", "Shell": "Shell", "Go": "Go",
    "CSS": "CSS", "HTML": "HTML", "Dockerfile": "Docker", "SQL": "SQL",
    "Java": "Java", "Kotlin": "Kotlin", "R": "R", "Jupyter Notebook": "Notebook",
}


def api(path: str, method: str = "GET", payload: dict | None = None) -> dict:
    url = path if path.startswith("http") else "https://api.github.com" + path
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "ivanwilliammd-profile-metrics")
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.load(resp)


def graphql(query: str, variables: dict) -> dict:
    return api("/graphql", "POST", {"query": query, "variables": variables})


def collect_activity(days: int = 30) -> dict:
    """Commit/PR/review/hari aktif dari contribution graph — angka resmi GitHub."""
    until = dt.datetime.now(dt.timezone.utc)
    since = until - dt.timedelta(days=days)
    q = """
    query($login:String!, $from:DateTime!, $to:DateTime!) {
      user(login:$login) {
        contributionsCollection(from:$from, to:$to) {
          totalCommitContributions
          totalPullRequestContributions
          totalPullRequestReviewContributions
          restrictedContributionsCount
          contributionCalendar { totalContributions weeks { contributionDays { date contributionCount } } }
          commitContributionsByRepository(maxRepositories:100) {
            repository { nameWithOwner isPrivate stargazerCount }
            contributions { totalCount }
          }
        }
      }
    }"""
    out = graphql(q, {"login": OWNER, "from": since.isoformat(), "to": until.isoformat()})
    cc = ((out.get("data") or {}).get("user") or {}).get("contributionsCollection") or {}
    if not cc:
        raise RuntimeError("kontribusi tidak terbaca: " + json.dumps(out)[:200])

    days_active = sum(
        1
        for w in cc["contributionCalendar"]["weeks"]
        for d in w["contributionDays"]
        if d["contributionCount"] > 0
    )
    repos = []
    for item in cc["commitContributionsByRepository"]:
        r = item["repository"]
        repos.append({
            "name": r["nameWithOwner"],
            "private": bool(r["isPrivate"]),
            "commits": int(item["contributions"]["totalCount"]),
        })
    # Repo profil ini sendiri hanya berisi commit bot metrik — bukan pekerjaan.
    repos = [r for r in repos if r["name"] != f"{OWNER}/{OWNER}"]
    repos.sort(key=lambda x: -x["commits"])

    # Nama repo privat TIDAK pernah ditulis: README profil ini publik. Yang tampil
    # hanya jumlah repo dan total commit-nya.
    private_count = sum(1 for r in repos if r["private"])
    private_commits = sum(r["commits"] for r in repos if r["private"])
    public_repos = [r for r in repos if not r["private"]]

    merged = 0
    try:
        since_date = since.date().isoformat()
        res = api(
            "/search/issues?q="
            + urllib.parse.quote(f"author:{OWNER} is:pr is:merged merged:>={since_date}")
            + "&per_page=1"
        )
        merged = int(res.get("total_count") or 0)
    except Exception:
        merged = -1  # pencarian dibatasi/diblokir → ditandai n/a, bukan dikarang

    return {
        "window": days,
        "commits": int(cc.get("totalCommitContributions") or 0),
        "prs": int(cc.get("totalPullRequestContributions") or 0),
        "reviews": int(cc.get("totalPullRequestReviewContributions") or 0),
        "private": int(cc.get("restrictedContributionsCount") or 0),
        "private_repos": private_count,
        "private_commits": private_commits,
        "merged": merged,
        "active_days": min(days_active, days),
        "repos": public_repos,
        "touched": len(public_repos) + private_count,
    }


def collect_languages(repos: list[dict], limit: int = 12) -> list[tuple[str, int]]:
    """Byte kode per bahasa di repo yang benar-benar disentuh — bukan jumlah repo."""
    total: dict[str, int] = {}
    for r in repos[:limit]:
        try:
            langs = api(f"/repos/{r['name']}/languages")
        except Exception:
            continue
        for name, size in (langs or {}).items():
            total[name] = total.get(name, 0) + int(size)
    return sorted(total.items(), key=lambda kv: -kv[1])


def probe(url: str, timeout: int = 12) -> tuple[int, int]:
    """Kode HTTP + latensi (ms). 000 = tidak menjawab."""
    started = time.time()
    req = urllib.request.Request(url, method="GET")
    req.add_header("User-Agent", "Mozilla/5.0 (compatible; ivanwilliammd-metrics)")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            resp.read(512)
            code = resp.status
    except urllib.error.HTTPError as err:
        code = err.code
    except Exception:
        code = 0
    return code, int((time.time() - started) * 1000)


def bar(value: int, biggest: int, width: int = 18) -> str:
    if biggest <= 0:
        return ""
    filled = max(1, round(value / biggest * width)) if value else 0
    return "█" * filled + "░" * (width - filled)


def render(activity: dict, langs: list[tuple[str, int]], services: list[tuple[str, int, int]]) -> str:
    w = activity["window"]
    merged = "n/a" if activity["merged"] < 0 else str(activity["merged"])
    rows = [
        f"**Window:** last {w} days · updated {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "| Shipped | Count |",
        "|---|---:|",
        f"| Commits | **{activity['commits']}** |",
        f"| Pull requests opened | **{activity['prs']}** |",
        f"| Pull requests merged | **{merged}** |",
        f"| Reviews given | **{activity['reviews']}** |",
        f"| Active days | **{activity['active_days']}/{w}** |",
        f"| Repositories touched | **{activity.get('touched', len(activity['repos']))}** |",
    ]

    if activity["repos"]:
        rows += ["", "**Where the work landed**", "", "```"]
        top = activity["repos"][:8]
        biggest = top[0]["commits"] or 1
        for r in top:
            rows.append(f"{r['name'].split('/')[-1]:<34} {r['commits']:>4}  {bar(r['commits'], biggest)}")
        rows.append("```")

    if activity.get("private_repos"):
        rows += [
            "",
            f"{activity['private_repos']} private repositories · "
            f"{activity['private_commits']} commits (names withheld)",
        ]

    shown = [(n, v) for n, v in langs if v >= 10_000][:6]
    if shown:
        biggest = shown[0][1]
        rows += ["", "**Languages by bytes in those repositories**", "", "```"]
        for name, size in shown:
            label = LANG_LABEL.get(name, name)
            rows.append(f"{label:<12} {bar(size, biggest)} {size / 1e6:7.2f} MB")
        rows.append("```")

    rows += ["", "**Live services** (HTTP code · latency, checked now)", "", "| Service | Code | Latency |", "|---|---:|---:|"]
    for name, code, ms in services:
        mark = "OK" if 200 <= code < 400 else "DOWN" if code == 0 else str(code)
        rows.append(f"| {name} | {mark} | {ms} ms |")

    rows += [
        "",
        "<sub>Measured from the GitHub API and real HTTP responses — what shipped, not how long "
        "an editor was open. Refreshed daily by [`.github/workflows/metrics.yml`](.github/workflows/metrics.yml).</sub>",
    ]
    return "\n".join(rows)


def main() -> int:
    try:
        activity = collect_activity(30)
    except Exception as err:  # jangan pernah menulis angka palsu
        print("GAGAL membaca aktivitas GitHub:", err, file=sys.stderr)
        return 1

    langs = collect_languages(activity["repos"])
    services = [(name, *probe(url)) for name, url in SERVICES]
    block = render(activity, langs, services)

    with open(README, encoding="utf-8") as fh:
        readme = fh.read()
    start, end = "<!--METRICS:START-->", "<!--METRICS:END-->"
    if start not in readme or end not in readme:
        print("Penanda telemetri tidak ada di README.", file=sys.stderr)
        return 1
    new = re.sub(
        re.escape(start) + r".*?" + re.escape(end),
        start + "\n" + block + "\n" + end,
        readme,
        flags=re.S,
    )
    if new != readme:
        with open(README, "w", encoding="utf-8") as fh:
            fh.write(new)
        print("README diperbarui.")
    else:
        print("Tidak ada perubahan.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
