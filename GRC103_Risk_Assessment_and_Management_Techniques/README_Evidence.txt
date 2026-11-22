GRC103 | PRACTICAL RISK MONITORING WITH WAZUH
Evidence register | 22 November 2026
Adediran Eunice Adebukola

SCOPE
Central Wazuh monitoring platform: Ubuntu Server 24.04.5 ARM64 in UTM.
Monitored endpoint: Apple Silicon macOS; Wazuh agent Finance-Dept-MacBook (001).
FIM scope: /Users/macbook/SensitiveFiles
Scan configuration: scheduled interval of 60 seconds.

TEST RESULTS
19:03:15  Added     Rule 554 (level 5)
19:08:59  Modified  Rule 550 (level 7)
19:11:17  Deleted   Rule 553 (level 7)
Test file: /Users/macbook/SensitiveFiles/Q4_Financial_Forecast.txt
All three events are visible in the central FIM Events view.

EVIDENCE INDEX
E01  Wazuh central dashboard
E02  macOS agent registered and active
E03  Agent startup and FIM configuration log
E04  File creation event
E05  File modification event and earlier creation event
E06  Complete three-event audit trail
E07  FIM reporting dashboard showing event distribution
E08  UTM/QEMU storage exhaustion incident
E09  Wazuh installation diagnostics and configuration recovery
E10  macOS agent installation record

ASSESSMENT BOUNDARY
These screenshots establish three successful controlled file-change tests; they do not
establish ongoing production effectiveness, continuous real-time monitoring, or an
absence of unrecorded file changes. Raw index exports and before/after file checksums
were not separately preserved. The observed file changes used training-only data.
