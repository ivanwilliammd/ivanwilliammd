<div align="center">

<img src="https://raw.githubusercontent.com/ivanwilliammd/ivanwilliammd.github.io/master/assets/img/mark.svg" width="96" alt="Ivan William Harsono">

# Ivan William Harsono

**MD · MCS · PhD · CPHIMS · FISQua**

### Health AI Architect & Strategist

Bridging clinical multiomics with scalable technology · HL7 FHIR interoperability · agentic AI · precision-medicine systems

[![Portfolio](https://img.shields.io/badge/portfolio-ivanwilliamharsono.com-25c69d?style=flat-square&logo=googlechrome&logoColor=white)](https://ivanwilliamharsono.com)
[![Live services](https://img.shields.io/badge/live%20services-pit%20stop-0b1512?style=flat-square&logo=statuspage&logoColor=25c69d)](https://ivanwilliammd.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ivanwilliammd/)
[![Google Scholar](https://img.shields.io/badge/Scholar-4285F4?style=flat-square&logo=googlescholar&logoColor=white)](https://scholar.google.com/citations?user=TMuoV-AAAAAJ)
[![ResearchGate](https://img.shields.io/badge/ResearchGate-00CCBB?style=flat-square&logo=researchgate&logoColor=white)](https://www.researchgate.net/profile/Ivan-Harsono)
[![XERJ](https://hub.xerj.org/contributors/ivanwilliammd/badge.svg)](https://hub.xerj.org/contributors/ivanwilliammd)

</div>

I bridge two worlds that usually do not talk to each other: **clinical medicine** and **scalable
engineering**. My work turns agentic AI, multiomics and hard interoperability standards into systems that
hospitals can run on a Monday morning — not slideware that impresses on a Friday.

The turning point of that work was leading **data standardisation for SATUSEHAT**, Indonesia's national
health interoperability platform. That is where FHIR R4, terminology mapping and master data management
stopped being theory and became a national contract between thousands of facilities. Everything I have
built since inherits that constraint: *the payload must be right, in production, for people who will never
read the spec.*

<div align="center">

**🧠 Health AI** · **🔗 Interoperability** · **🧬 Multiomics** · **🏥 Clinical platforms**

</div>

---

## 🧠 What I architect

<table>
<tr>
<td width="50%" valign="top">

### 🧠 Health AI that a clinician can audit
Agentic assistants and decision support where **the model proposes and deterministic rules decide**.
[SmartClaim](https://claim.ivanmd.id) checks diagnosis, procedure and financing codes *before* a claim is
submitted; IvanMD's CDS grounds suggestions in the encounter's SOAP; [WISH](https://wish.ivai.app) turns a
receipt photo into structured spending that three different assistants can reason over.

### 🔗 Interoperability as a product
Author of the open-source [SATUSEHAT integration library](https://github.com/ivanwilliammd/satusehat-integration)
— PHP, Node.js, Python and Go — plus [SmarTerm](https://terminology.ivanmd.id), one terminology engine for
ICD-10, ICD-9-CM, LOINC, SNOMED CT, KFA and KPTL. Running against the national platform, not a sandbox.

</td>
<td width="50%" valign="top">

### 🧬 Multiomics into clinical workflows
[IDeRare](https://github.com/ivanwilliammd/IDeRare) — phenotype-driven exome analysis, published in
*JAMIA Open* — and OMOP↔FHIR exchange for GWAS risk stratification. Genomic data is only useful when it
reaches the clinician who is making the decision, in the format their system already speaks.

### 🏥 Clinical platforms & laboratory informatics
EMR, LIS and ERP surfaces built for real hospital workflows: [IvanMD](https://ivanmd.id),
[Clinix](https://clinix.meditechku.com), [SPECTRA](https://spectra.meditechku.com). My clinical pathology
practice — laboratory interpretation and whole-exome sequencing — is what keeps these architectures honest.

</td>
</tr>
</table>

---

## 🚀 Selected systems

| | System | What it does | Link |
|---|---|---|---|
| 🧠 | **SmartClaim** | Claim-integrity checks (ICD-10 / ICD-9-CM / INA-CBG) before submission | [claim.ivanmd.id](https://claim.ivanmd.id) |
| 🔗 | **SmarTerm** | Shared terminology service: ICD-10, ICD-9-CM, LOINC, SNOMED CT, KFA, KPTL | [terminology.ivanmd.id](https://terminology.ivanmd.id) |
| 📦 | **SATUSEHAT SDK** | FHIR R4 builders + OAuth client + durable queue, four languages | [PHP](https://github.com/ivanwilliammd/satusehat-integration) · [Node](https://github.com/ivanwilliammd/satusehat-integration-node) · [Python](https://github.com/ivanwilliammd/satusehat-integration-python) · [Go](https://github.com/ivanwilliammd/satusehat-integration-go) |
| 🩺 | **IvanMD** | Medical record, teleconsultation and appointments (web + Android) | [ivanmd.id](https://ivanmd.id) |
| 🧾 | **WISH** | Receipt → structured expense, feeding three AI assistants | [wish.ivai.app](https://wish.ivai.app) |
| 🧬 | **IDeRare** | Phenotype + exome pipeline for germline rare-disease diagnosis | [repo](https://github.com/ivanwilliammd/IDeRare) · [JAMIA Open](https://doi.org/10.1093/jamiaopen/ooae052) |
| 🫁 | **I3DR-Net** | 3D lung-nodule detection on LIDC-IDRI with transfer-learning RetinaNet | [repo](https://github.com/ivanwilliammd/I3DR-Net-Transfer-Learning) · [paper](https://doi.org/10.1016/j.jksuci.2020.03.013) |
| 🏗️ | **SPECTRA** | Multitenant stock / ERP / POS / CRM — spec complete, build in progress | [spectra.meditechku.com](https://spectra.meditechku.com) |
| 🔬 | **Clinix** | Clinical-pathology portfolio and laboratory reporting workflow | [clinix.meditechku.com](https://clinix.meditechku.com) |
| 🔗 | **IVAI Link** | Invitation-only short links with QR and click analytics | [link.ivai.app](https://link.ivai.app) |

📚 The full list — **22 projects back to 2019**, publications and experience — lives on
[ivanwilliamharsono.com](https://ivanwilliamharsono.com).
🛰️ Every live instance, with its own status light, sits on my [production pit stop](https://ivanwilliammd.github.io).

---

## 📊 Output telemetry

Editor-time metrics stopped being honest the moment agents started writing code with me: hours fell while
shipped work rose. This block therefore measures **what landed** — commits, pull requests, reviews,
repositories touched — and whether the services behind them are answering right now.

<!--METRICS:START-->
**Window:** last 30 days · updated 2026-10-30 01:00 UTC

| Shipped | Count |
|---|---:|
| Commits | **1363** |
| Pull requests opened | **12** |
| Pull requests merged | **11** |
| Reviews given | **0** |
| Active days | **30/30** |
| Private contributions | **0** (names withheld) |
| Repositories touched | **31** |

**Where the work landed**

*Private — names withheld*

```
private repo #1                     270  ██████████████████
private repo #2                     215  ██████████████░░░░
private repo #3                     200  █████████████░░░░░
private repo #4                     117  ████████░░░░░░░░░░
private repo #5                      81  █████░░░░░░░░░░░░░
```

*Public*

```
satusehat-integration                20  ██████████████████
ivanwilliammd.github.io               4  ████░░░░░░░░░░░░░░
satusehat-integration-node            4  ████░░░░░░░░░░░░░░
satusehat-integration-python          4  ████░░░░░░░░░░░░░░
satusehat-integration-go              2  ██░░░░░░░░░░░░░░░░
```

26 private repositories · 1397 commits (names withheld)

**Languages by bytes in those repositories**

```
PHP          ██████████████████   10.59 MB
Vue          ████░░░░░░░░░░░░░░    2.41 MB
Blade        ████░░░░░░░░░░░░░░    2.41 MB
TypeScript   ██░░░░░░░░░░░░░░░░    1.40 MB
Python       ██░░░░░░░░░░░░░░░░    1.04 MB
HTML         █░░░░░░░░░░░░░░░░░    0.72 MB
```

**Live services** (HTTP code · latency, checked now)

| Service | Code | Latency |
|---|---:|---:|
| Portfolio site | OK | 908 ms |
| IVAI | OK | 904 ms |
| IVAI Link | OK | 1300 ms |
| SmarTerm | OK | 1105 ms |
| SmartClaim | OK | 1106 ms |
| WISH | OK | 358 ms |
| Clinix | OK | 1195 ms |
| SPECTRA | OK | 1420 ms |
| Pay | OK | 2560 ms |
| IvanMD Identity | OK | 1763 ms |

<sub>Measured from the GitHub API and real HTTP responses — what shipped, not how long an editor was open. Refreshed daily by [`.github/workflows/metrics.yml`](.github/workflows/metrics.yml).</sub>
<!--METRICS:END-->

---

## 📄 Research

Six first-author papers — from a medical-school case report to a Q1 methods paper.

| Year | Paper | Venue |
|---|---|---|
| 2024 | **IDeRare**: phenotype + exome pipeline for germline rare disease · [doi](https://doi.org/10.1093/jamiaopen/ooae052) | *JAMIA Open* 7(2) · Q1 |
| 2024 | Phenotype and trio WES data in glycogen storage disease IV · [doi](https://doi.org/10.1016/j.dib.2024.111231) | *Data in Brief* · Q3 |
| 2024 | Disease modelling in inborn errors of metabolism | *Int. Medical Journal* 31(6) |
| 2020 | Lung nodule detection with RetinaNet transfer learning · [doi](https://doi.org/10.1016/j.jksuci.2020.03.013) | *J. King Saud Univ.* · Q1 |
| 2019 | Lung nodule texture detection with 3D CNN · [doi](https://doi.org/10.21512/commit.v13i2.5995) | *CommIT* 13(2) |
| 2017 | Immunohistochemistry in silent pituitary adenoma · [doi](https://doi.org/10.19166/med.v6i3.1150) | *MEDICINUS* 6(3) |

---

## 🧰 How I build

<details>
<summary><b>Stack, standards and conventions</b> (click to expand)</summary>

<br>

**Standards** — HL7 FHIR R4, SATUSEHAT, ICD-10 / ICD-9-CM / INA-CBG, SNOMED CT, LOINC, KFA, KPTL, HPO, OMIM, ORPHA, OMOP, DICOM.

**AI** — agentic pipelines, RAG, prompt engineering, LangChain; scikit-learn, PyTorch/Keras for imaging and omics.

**Backend** — PHP 8 / Laravel, Python (FastAPI, Django, Streamlit), Node.js, Go; PostgreSQL, MariaDB, Redis; OIDC (Passport), Sanctum.

**Frontend** — Next.js, Vue 3 + Inertia, React, Tailwind, Vite.

**Platform** — Docker, GitHub Actions, Vercel, Cloudflare, aaPanel; zero-build deploys where the server may only `git pull`.

**Conventions** — code symbols in English, UI text in Indonesian; every change carries a test quoted before
and after; a feature is done when it can be triggered through the API, not only through a dashboard.

</details>

---

<div align="center">

### 🤝 Let's build something that has to work

Advisory, architecture review, or hands-on delivery for health AI, FHIR/terminology infrastructure and
clinical data platforms.

[![Email](https://img.shields.io/badge/email-ivanwilliam.md@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:ivanwilliam.md@gmail.com)
[![LinkedIn](https://img.shields.io/badge/message-LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ivanwilliammd/)

<sub>© 2019–2026 Ivan William Harsono · Founder of <a href="https://meditechku.com">PT Meditech Konsulindo Utama</a> · <a href="https://ivai.app">IVAI</a></sub>

</div>
