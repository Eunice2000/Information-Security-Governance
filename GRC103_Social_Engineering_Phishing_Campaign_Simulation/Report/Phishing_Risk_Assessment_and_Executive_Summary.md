# GRC103 — Controlled Phishing Awareness Simulation

**Student:** Adediran Eunice Adebukola  
**Registration number:** C11-26-CGRCE-17595  
**Date:** 8 November 2026  
**Audience:** CISO, Head of HR and Executive Management

## 1. Executive summary

A controlled phishing-awareness exercise was conducted in a Kali Linux lab using GoPhish, five fictional recipient records and a local SMTP capture service. The campaign employed an HR benefits review theme and a locally hosted training page. The purpose was to validate campaign configuration, event capture and governance reporting in a simulated environment.

GoPhish recorded five **Email Sent** events, one **Email Opened** event, one **Clicked Link** event, one **Submitted Data** event and zero **Email Reported** events. The tested recipient submitted a **fictional lab reference**, not a password. One observed event divided by five recipient records is 20%, but these figures do not demonstrate external email delivery, employee susceptibility or any actual security-control failure.

## 2. Campaign setup

- **Platform:** Kali Linux VM running GoPhish
- **Administrative interface:** `127.0.0.1:3333`
- **Landing-page listener:** `127.0.0.1:8080`
- **SMTP test listener:** `127.0.0.1:1025`
- **Campaign:** GRC103 HR Benefits Awareness Simulation
- **Recipients:** Five fictional identities with reserved `.example` email addresses
- **Landing page:** Employee Benefits Record Review; dummy lab reference input
- **Data collection:** Submitted dummy data enabled; password capture disabled
- **Safety boundary:** Local test only; no organisational users targeted

## 3. Results and calculated rates

| Metric | Recorded count | Calculation | Rate |
|---|---:|---|---:|
| Emails recorded as sent | 5 | 5 / 5 | 100% |
| Opens recorded | 1 | 1 / 5 | 20% |
| Link clicks recorded | 1 | 1 / 5 | 20% |
| Fictional lab reference submissions | 1 | 1 / 5 | 20% |
| Reports recorded | 0 | 0 / 5 | 0% |

All rates use the five simulated recipients as the denominator. The actual click and submission were manually performed to validate event tracking.

## 4. Phishing risk assessment

| Metric | Observed result | Risk interpretation | Control assessment |
|---|---|---|---|
| Email opened | 1/5 (20%) | Engaging with a themed message can be an entry point for social engineering. | Training effectiveness cannot be established from fictional identities. |
| Link clicked | 1/5 (20%) | A clicked untrusted link may lead to a spoofed service or malicious content in a real attack. | Email filtering and real-user link verification were not tested. |
| Data submitted | 1/5 (20%) | Submitting sensitive information to a deceptive page could lead to disclosure in a real attack. | This was a fictional lab reference. No password compromise occurred and MFA was not evaluated. |
| Email reported | 0/5 (0%) | Timely reporting is useful for detection and containment. | No human reporting behaviour was tested; a zero event count does not indicate a reporting-control failure. |

## 5. Risk analysis

The exercise demonstrated that a personalised message, recipient-linked URL and test landing page could be configured, tracked and reported using GoPhish in a local environment. In an actual organisation, phishing attacks can contribute to credential theft, unauthorised access, fraud, disclosure of sensitive data and incident-response costs. None of these consequences were demonstrated in this exercise.

The results have substantial limits: fictional recipients, local SMTP capture instead of external mail delivery, and manually generated engagement. Therefore, the percentage figures represent local workflow telemetry only and must not be extrapolated to the workforce.

## 6. Recommendations

| Priority | Recommendation | Owner | Verification evidence |
|---|---|---|---|
| High | Deploy phishing-resistant MFA on sensitive services and periodically review exceptions. | Identity and Access Management | MFA coverage reports, configuration reviews, exception register |
| High | Offer practical phishing-awareness training with HR-themed examples, sender validation and safe link handling. | Security Awareness and HR | Completion statistics, knowledge checks, subsequent simulation |
| Medium | Provide a simple Report Phishing process with clear triage and response timelines. | Security Operations | Reporting workflow test, incident tickets, response SLAs |
| Medium | Review SPF, DKIM, DMARC, email security policies, and anti-phishing detection in an authorised environment. | Messaging and Security Engineering | Configuration and test evidence |
| Medium | Conduct periodic authorised simulations with documented scope, approved recipients, baseline metrics and privacy safeguards. | GRC and Security Awareness | Scope approvals, aggregate results, remediation and retest records |

## 7. Conclusion

The practical successfully verified locally contained campaign execution and event tracking for a simulated phishing workflow. The principal governance lesson is to distinguish measured technical events from a defensible assessment of human risk. A real awareness assessment requires authorised recipients, confirmed delivery, sufficient sample size, reliable observation methods and post-remediation retesting.

## Evidence

The final GoPhish dashboard displayed **5 sent, 1 opened, 1 clicked, 1 submitted, 0 reported**, as documented in the student's captured lab screenshots. The locally exported final CSV remains in the Kali lab until it is added to this repository.
