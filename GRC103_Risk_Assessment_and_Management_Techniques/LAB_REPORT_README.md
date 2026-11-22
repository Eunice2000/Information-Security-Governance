# Practical Risk Monitoring with Wazuh

**Course:** GRC103 — Risk Assessment and Management Techniques  
**Lab:** Practical Risk Assessment Workshop  
**Date:** 22 November 2026  
**Participant:** Adediran Eunice Adebukola

## Objective

Implement a detective control for changes to a sensitive financial forecast folder and establish a centrally accessible audit trail of file creation, modification, and deletion.

## Lab environment

- **Wazuh manager, indexer, and dashboard:** Ubuntu Server 24.04.5 ARM64, UTM, Wazuh 4.14.10
- **Monitored endpoint:** Apple Silicon macOS, Wazuh agent `Finance-Dept-MacBook` (agent `001`)
- **Monitored folder:** `/Users/macbook/SensitiveFiles`
- **Monitoring method:** Scheduled File Integrity Monitoring scans at 60-second intervals

The course's Windows/VirtualBox workflow was adapted to the available macOS/UTM environment. It achieved the core file-change detection outcomes, but did not replicate real-time Windows monitoring.

## Control verification

| Scenario | Event | Rule | Observed time, 22 Nov 2026 | Result |
|---|---|---|---|---|
| Create `Q4_Financial_Forecast.txt` | `added` | 554 (level 5) | 19:03:15 | Passed |
| Amend forecast contents | `modified` | 550 (level 7) | 19:08:59 | Passed |
| Delete the training document | `deleted` | 553 (level 7) | 19:11:17 | Passed |

All three alerts were recorded for the same file by Wazuh and displayed in the File Integrity Monitoring Events view.

## Contents

- `GRC103_Wazuh_Practical_Risk_Monitoring_Report.pdf` — assessment and workshop responses
- `GRC103_Wazuh_Practical_Risk_Monitoring_Report.docx` — editable report
- `Evidence/` — ten lab screenshots covering setup, monitoring results, and troubleshooting
- `README_Evidence.txt` — image register and assessment boundary

## Assessment

The control passed the three controlled functional tests. Operational limitations remain: the 60-second scan interval can miss transient changes between scans; endpoint availability, permissions, ingestion, and alert response need ongoing oversight. The report explains business impact, complementary preventive and corrective controls, metrics, centralised auditability, and compliance evidence.

Only training documents were used in the test. No passwords, installer credential archives, or private keys are included.
