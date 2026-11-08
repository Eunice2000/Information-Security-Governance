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

The original campaign dashboard screenshot, final PDF and editable Word report are part of the locally prepared evidence package and will be added to the corresponding folders as binary files. The complete lab capture contains 60 timestamped screenshots, with 7 key evidence images selected for the final report.

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
