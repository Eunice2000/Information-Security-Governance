# GRC103 — Social Engineering and Phishing Campaign Simulation

**Student:** Adediran Eunice Adebukola  
**Registration Number:** C11-26-CGRCE-17595  
**Lab Date:** 8 November 2026

## Overview

This practical demonstrates the configuration, execution and analysis of a controlled GoPhish simulation on a Kali Linux VM. Five fictional lab identities were used with a local SMTP capture service and a loopback-only landing page.

## Campaign results

| Metric | Count | Share of 5 lab identities |
|---|---:|---:|
| Emails recorded as sent | 5 | 100% |
| Opens recorded | 1 | 20% |
| Clicks recorded | 1 | 20% |
| Fictional reference submitted | 1 | 20% |
| Reports recorded | 0 | 0% |

The recorded open, click and form submission resulted from deliberate local functional testing. They do not measure real employee susceptibility or external email delivery. No real passwords or personnel were involved.

## Contents

- `Report/` — final report in PDF and editable DOCX, including risk assessment table and executive recommendations.
- `Screenshots/Selected_Evidence/` — seven principal screenshots.
- `Screenshots/Complete_Lab_Capture/` — 60 additional screenshots showing the lab workflow in chronological order, stored as compact JPEGs.
- `Supporting_Data/` — evidence file manifest and notes about the exported CSV.

## Lab implementation

- GoPhish admin interface: `127.0.0.1:3333`
- GoPhish landing page: `127.0.0.1:8080`
- Local SMTP capture: `127.0.0.1:1025`

The results and interpretation are based on the observed local GoPhish dashboard. The five identities were fictional, and the submitted value was a fictional lab reference, not a password.
