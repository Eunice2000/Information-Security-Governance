# GRC103 — Social Engineering and Phishing Campaign Simulation

**Student:** Adediran Eunice Adebukola  
**Registration number:** C11-26-CGRCE-17595  
**Lab date:** 8 November 2026

## Overview

This practical covers the setup, execution and governance assessment of a controlled GoPhish phishing-awareness simulation. The test used five fictional recipients, a local SMTP capture listener and a loopback-only training landing page. No real staff members or credentials were involved.

## Recorded results

| Metric | Events | Rate |
|---|---:|---:|
| Emails sent to local SMTP capture | 5 | 100% |
| Opens recorded | 1 | 20% |
| Clicks recorded | 1 | 20% |
| Fictional lab reference submissions | 1 | 20% |
| Reports recorded | 0 | 0% |

A single lab interaction was performed to test tracking. These are **simulated event rates**, not evidence of workforce phishing susceptibility, credential loss or delivery to external inboxes.

## Report and evidence

- [Phishing Risk Assessment and Executive Summary](Report/Phishing_Risk_Assessment_and_Executive_Summary.md) — methodology, quantitative results, risk analysis, control assessment, recommendations, and limitations.
- [Campaign Results Summary](Supporting_Data/Campaign_Results_Summary.csv) — summary of the five GoPhish dashboard metrics.
- [Final Campaign Results Screenshot](Screenshots/Selected_Evidence/Final_Campaign_Results.png) — cropped dashboard evidence of 5 sent, 1 opened, 1 clicked, 1 fictional data submission and 0 reports.

The final GoPhish campaign-results screenshot is available above. The full-sized original screenshot, PDF, editable Word report and the rest of the chronological lab screenshots remain in the separately prepared local evidence package and have not yet been uploaded to this repository.

## Lab configuration

| Component | Configuration |
|---|---|
| Virtual machine | Kali Linux, UTM |
| Administration | `127.0.0.1:3333` |
| Landing page | `127.0.0.1:8080` |
| SMTP capture | `127.0.0.1:1025` |
| Simulation | HR benefits record review |
| Form input | Fictional lab reference only |

The demonstration confirms local campaign delivery to the SMTP capture service and event tracking; it does not evaluate an enterprise security awareness programme.
