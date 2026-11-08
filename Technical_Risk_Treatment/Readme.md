# Technical Risk Treatment — GRC103 Module 3

**Lab:** Implementing and Validating Controls on a Local Linux Server  
**Organisation:** Northbridge Services (fictional)  
**Performed:** 8 November 2026 | **Platform:** UTM, Ubuntu Server 24.04.5 LTS (ARM64) and Kali Linux (ARM64)  
**Prepared by:** Adediran Eunice Adebukola  
**Scope:** Isolated host-only VM lab with dummy data. **No production systems were tested.**

## Executive overview

This practical demonstrates risk treatment with implementation and observable verification, not simply recommendations. The baseline showed an approved Nginx portal on TCP/80, an unnecessary Python legacy endpoint on TCP/8080, HTTP directory listings, and directly retrievable dummy archive content. The final state preserves the approved portal while retiring the legacy endpoint, removing the archive from the web root, restricting inbound HTTP to the approved test client, recording blocked attempts, and demonstrating backup recovery.

### Test results

| Control/test | Baseline | Treatment validation |
|---|---|---|
| TCP/8080 legacy endpoint | Open; HTTP 200 | Closed after retirement; rollback tested and re-retired |
| TCP/80 approved portal | Open; HTTP 200 | Open; HTTP 200 |
| `/archive/` | HTTP 200, listing visible | HTTP 403 |
| `/archive/dummy-records.txt` | HTTP 200, content retrieved | HTTP 403 |
| `/` directory listing | HTTP 200, directory listing | HTTP 403 |
| Network policy | UFW inactive | Default deny inbound; only 192.168.128.4 allowed to TCP/80 |
| Approved client (192.168.128.4) | HTTP 200 | HTTP 200 |
| Unapproved test client (192.168.128.11) | Not tested at baseline | TCP connection timed out; correlated `UFW BLOCK` kernel logs |
| Accidental deletion of portal file | No verified recovery control | HTTP 403 during deletion; SHA-256 `OK` after restore; HTTP 200 |

**Measured final recovery exercise:** 19:57:27 UTC exercise start; 19:57:53 UTC failed external HTTP check; 19:58:17 UTC restoration/hash-check completion; 19:58:23 UTC successful external HTTP check. **50 seconds to recorded restoration completion; 56 seconds to verified service response.** These measurements are specific to the local lab and should not be represented as production SLA outcomes.

## Lab environment and boundary

| Machine | Role | IP/interface | Network |
|---|---|---|---|
| Kali Linux | Approved test client | 192.168.128.4 / `eth0` | UTM Host Only |
| Ubuntu Server 24.04.5 LTS | Document server | 192.168.128.5 / `enp0s1` | UTM Host Only |
| Kali temporary alias | Unapproved test source | 192.168.128.11 / `eth0` | Added only for blocked-source test; removed afterward |

Ubuntu ran Nginx 1.24.0, UFW, Python 3 and curl. Nmap and curl tests originated from Kali. Internet-enabled UTM shared networking was used temporarily for Nginx installation and changed back to Host Only **before** establishing the intentionally exposed lab baseline. A clean disk-only UTM snapshot was captured before the deliberately vulnerable configuration was created.

## Treatment design

1. **Avoidance (R1):** Stop and disable `grc-legacy.service`. Simulated IT Service Owner approval, test of the approved portal and a controlled rollback were documented. This removes the retired workflow's exposure, not all server risk.
2. **Mitigation (R2/R3/R4):** Move archive to `/srv/grc-private/archive`, restrict group/other access, disable directory listing, explicitly deny `/archive/`, allow only approved Kali IP to port 80 using UFW, enable logging, and back up/restore the dummy portal with SHA-256 verification.
3. **Transfer proposal (R4):** Compare local-only backup with a hypothetical managed-backup service; duties and liability remain shared. No contract was purchased or activated.
4. **Acceptance proposal (HTTP):** Time-box isolated plain HTTP with dummy data only, subject to a **simulated** decision, proposed 14-day expiry and immediate withdrawal on expanded connectivity, real data or broader use. **This is not a production exception.**

## Documentation

- [Technical assessment and management report](REPORT.md)
- [Evidence inventory and reproduction guide](EVIDENCE_README.md)

**Submission status:** The Markdown report is published here; the required PDF, calculation workbook, raw command-output files, redacted logs and screenshots should accompany the submission ZIP. Screenshots referenced in the report were observed during the live lab; they are not automatically transferred from the chat into this GitHub repository.

## Safety and limitations

This is a fictional, host-only learning environment. No credentials, private keys, real records, VM disk images or unredacted sensitive logs should be committed. IPs in this documentation are local training addresses. Risk ratings, service costs and ALE assumptions are classroom exercises rather than empirical risk probabilities or quotations.
