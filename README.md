<div align="center">

# Ivan William Harsono

**MD · MCS · PhD · CPHIMS · FISQua**

Clinical pathologist in training at FKUI–RSCM · health-data infrastructure · FHIR & clinical terminology · clinical AI

[![Website](https://img.shields.io/badge/ivanwilliamharsono.com-111?style=flat-square&logo=googlechrome&logoColor=white)](https://ivanwilliamharsono.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ivanwilliammd/)
[![Google Scholar](https://img.shields.io/badge/Google%20Scholar-4285F4?style=flat-square&logo=googlescholar&logoColor=white)](https://scholar.google.com/citations?user=TMuoV-AAAAAJ)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-00CCBB?style=flat-square&logo=researchgate&logoColor=white)](https://www.researchgate.net/profile/Ivan-Harsono)
[![XERJ Corpus Hub](https://hub.xerj.org/contributors/ivanwilliammd/badge.svg)](https://hub.xerj.org/contributors/ivanwilliammd)
[![Email](https://img.shields.io/badge/email-ivanwilliam.md@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:ivanwilliam.md@gmail.com)

</div>

I build the plumbing that health systems quietly depend on: the interoperability layer between hospital
systems and the national platform, the terminology that makes two systems mean the same thing, and the
checks that stop bad data before it becomes a rejected claim or a wrong result. Medicine gives me the
domain; computer science gives me the tools.

What I care about is **shipped and verifiable** — a library running in a hospital, a service answering at
3 a.m., a paper with a DOI. If it has not run outside my laptop, it is not finished.

---

## What I work on

**Interoperability that hospitals actually run.** Product manager for SATUSEHAT DTO standardisation at
Indonesia's Ministry of Health (2022–2023), and author of the open-source
[SATUSEHAT integration library](https://github.com/ivanwilliammd/satusehat-integration) — PHP, Node.js,
Python and Go, MIT-licensed, for EMR teams who would otherwise hand-write FHIR JSON.

**Terminology as infrastructure.** [SmarTerm](https://terminology.ivanmd.id) puts ICD-10, ICD-9-CM,
LOINC, SNOMED CT, KFA and KPTL v1.7 into one search-and-mapping engine, shared by every service in the
ecosystem instead of copied per app.

**Clinical AI with a safety rail.** [SmartClaim](https://claim.ivanmd.id) reads an episode file and
checks whether diagnosis, procedure and financing codes agree *before* the claim is submitted — not
after it bounces. IvanMD's LLM decision support and the WISH receipt assistants follow the same rule:
the model proposes, deterministic rules and the clinician decide.

**Diagnostics and laboratory informatics.** As a clinical pathology resident I read haematology,
chemistry, immunology and molecular results all day, which is why the software I write for laboratories
starts from the report rather than from the schema.

---

## Selected work

| Project | What it does | Link |
|---|---|---|
| **SmartClaim** | Claim-integrity checks (ICD-10 / ICD-9-CM / INA-CBG) on episode files before submission | [claim.ivanmd.id](https://claim.ivanmd.id) |
| **SmarTerm** | Shared terminology service: ICD-10, ICD-9-CM, LOINC, SNOMED CT, KFA, KPTL | [terminology.ivanmd.id](https://terminology.ivanmd.id) |
| **SATUSEHAT SDK** | FHIR R4 payload builders + OAuth client + durable queue, four languages | [PHP](https://github.com/ivanwilliammd/satusehat-integration) · [Node](https://github.com/ivanwilliammd/satusehat-integration-node) · [Python](https://github.com/ivanwilliammd/satusehat-integration-python) · [Go](https://github.com/ivanwilliammd/satusehat-integration-go) |
| **IvanMD** | Medical record, teleconsultation and appointment system (web + Android) | [ivanmd.id](https://ivanmd.id) |
| **WISH** | Receipt photo → structured expense; one dataset feeding three AI assistants | [wish.ivai.app](https://wish.ivai.app) |
| **IDeRare** | Phenotype + exome pipeline for germline rare-disease diagnosis | [repo](https://github.com/ivanwilliammd/IDeRare) · [JAMIA Open](https://doi.org/10.1093/jamiaopen/ooae052) |
| **I3DR-Net** | 3D lung-nodule detection on LIDC-IDRI with transfer-learning RetinaNet | [repo](https://github.com/ivanwilliammd/I3DR-Net-Transfer-Learning) · [paper](https://doi.org/10.1016/j.jksuci.2020.03.013) |
| **SPECTRA** | Multitenant stock / ERP / POS / CRM — specification complete, build in progress | [spectra.meditechku.com](https://spectra.meditechku.com) |
| **Clinix** | Clinical-pathology portfolio and laboratory reporting workflow | [clinix.meditechku.com](https://clinix.meditechku.com) |
| **IVAI Link** | Invitation-only URL shortener with QR and click analytics | [link.ivai.app](https://link.ivai.app) |

The full list — 22 projects back to 2019 — lives on [my portfolio site](https://ivanwilliamharsono.com).

---

## Output telemetry

Most profile READMEs measure editor time. That number stopped being honest once agents started writing
code alongside me: hours went down while shipped work went up. So this block measures **what landed** —
commits, pull requests, reviews, repositories touched — and whether the services behind them are
actually answering right now.

<!--METRICS:START-->
**Window:** last 30 days · updated 2026-10-29 13:29 UTC

| Shipped | Count |
|---|---:|
| Commits | **51** |
| Pull requests opened | **0** |
| Pull requests merged | **0** |
| Reviews given | **0** |
| Active days | **30/30** |
| Repositories touched | **4** |

**Where the work landed**

```
satusehat-integration                12  ██████████████████
satusehat-integration-node            3  ████░░░░░░░░░░░░░░
satusehat-integration-python          2  ███░░░░░░░░░░░░░░░
satusehat-integration-go              1  ██░░░░░░░░░░░░░░░░
```

**Languages by bytes in those repositories**

```
PHP          ██████████████████    1.57 MB
Python       █████░░░░░░░░░░░░░    0.44 MB
TypeScript   ████░░░░░░░░░░░░░░    0.39 MB
Go           ████░░░░░░░░░░░░░░    0.31 MB
```

**Live services** (HTTP code · latency, checked now)

| Service | Code | Latency |
|---|---:|---:|
| Portfolio site | OK | 150 ms |
| IVAI | OK | 140 ms |
| IVAI Link | OK | 89 ms |
| SmarTerm | OK | 319 ms |
| SmartClaim | OK | 234 ms |
| WISH | OK | 78 ms |
| Clinix | OK | 298 ms |
| SPECTRA | OK | 899 ms |
| Pay | OK | 406 ms |
| IvanMD Identity | OK | 377 ms |

<sub>Measured from the GitHub API and real HTTP responses — what shipped, not how long an editor was open. Refreshed daily by [`.github/workflows/metrics.yml`](.github/workflows/metrics.yml).</sub>
<!--METRICS:END-->

---

## Research

Six first-author papers, from a case report in medical school to a Q1 methods paper:

- **IDeRare**: lightweight open-source phenotype and exome analysis pipeline for germline rare disease diagnosis — *JAMIA Open* 7(2), 2024 · [doi](https://doi.org/10.1093/jamiaopen/ooae052)
- Clinical phenotype and trio whole-exome sequencing data in glycogen storage disease IV — *Data in Brief*, 2024 · [doi](https://doi.org/10.1016/j.dib.2024.111231)
- Disease modelling advances in inborn errors of metabolism — *International Medical Journal* 31(6), 2024
- Lung nodule detection and classification from thorax CT using RetinaNet with transfer learning — *J. King Saud Univ. Computer & Information Sciences*, 2020 · [doi](https://doi.org/10.1016/j.jksuci.2020.03.013)
- Lung nodule texture detection and classification using 3D CNN — *CommIT Journal* 13(2), 2019 · [doi](https://doi.org/10.21512/commit.v13i2.5995)
- The importance of immunohistochemical analysis in silent pituitary adenoma — *MEDICINUS* 6(3), 2017 · [doi](https://doi.org/10.19166/med.v6i3.1150)

---

## How I build

<details>
<summary><b>Stack and conventions</b> (click to expand)</summary>

<br>

**Domain** — HL7 FHIR R4, SATUSEHAT, ICD-10 / ICD-9-CM / INA-CBG, SNOMED CT, LOINC, KFA, KPTL, HPO, OMIM, ORPHA, OMOP, DICOM.

**Backend** — PHP 8 / Laravel, Python (FastAPI, Django, Streamlit), Node.js, Go; PostgreSQL, MySQL/MariaDB, SQLite, Redis; Passport/OIDC, Sanctum.

**Frontend** — Next.js, Vue 3 + Inertia, React, Tailwind, Vite.

**Data & AI** — pandas, scikit-learn, PyTorch/Keras, LangChain, RAG, prompt engineering, n8n and RPA.

**Infrastructure** — Docker, GitHub Actions, Vercel, Cloudflare, aaPanel; zero-build deploys where the
server may only `git pull`.

**Conventions I hold to** — code symbols in English, UI text in Indonesian; every change carries a test
whose numbers are quoted before and after; a feature is done when it can be triggered through the API,
not only through a dashboard.

</details>

---

<div align="center">

**Open to collaboration on FHIR and terminology infrastructure, clinical decision support, and
laboratory informatics.** The fastest way to reach me is [email](mailto:ivanwilliam.md@gmail.com) or
[LinkedIn](https://www.linkedin.com/in/ivanwilliammd/).

<sub>© 2019–2026 Ivan William Harsono · Founder of <a href="https://meditechku.com">PT Meditech Konsulindo Utama</a> · <a href="https://ivai.app">IVAI</a></sub>

</div>
