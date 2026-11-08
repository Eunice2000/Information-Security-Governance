# GRC103 Module 3 — Technical Risk Treatment Assessment

**Case:** Northbridge Services internal document server  
**Analyst:** Adediran Eunice Adebukola  
**Execution date:** 8 November 2026  
**Basis:** ICDFA GRC103 Module 3 Technical Risk Treatment Lab  
**Classification:** Fictional training exercise; dummy records only

## 1. One-page management summary

**Objective.** Reduce technical exposure on an internal document server without disrupting the approved portal. Establish an auditable baseline, apply controls, verify both authorised and denied behaviour, and determine which remaining risks should be mitigated, avoided, transferred or temporarily accepted.

**Initial exposure.** Kali Nmap identified open TCP ports 80 and 8080. HTTP requests returned 200 for the web root, the archive listing, the dummy-record file and the legacy service. UFW was inactive. These observations demonstrate avoidable service exposure, information disclosure and insufficient source restrictions within the lab boundary.

**Completed treatment.** The unnecessary service was retired (TCP/8080 closed), with successful simulated rollback and reapplication. The archive was moved outside the document root, file access was restricted, Nginx listings were disabled and an explicit `/archive/` denial applied. UFW was enabled with default-deny inbound traffic and a single source-specific permit for 192.168.128.4 to TCP/80.

**Validation.** Approved-client requests continued to return HTTP 200. Archive paths and the root listing returned HTTP 403. A separate, unused Kali source address 192.168.128.11 timed out, and Ubuntu kernel/UFW logs recorded corresponding `UFW BLOCK` events for destination 192.168.128.5 TCP/80. Nginx recorded successful and denied web requests from the approved client.

**Recovery.** A same-host archive of the approved portal was made before deletion. After the file was deliberately removed, an HTTP 403 was captured. Restore from the archive produced SHA-256 `OK`, and Kali again received HTTP 200 with original dummy content. Recorded restoration completion: 50 seconds after start; successful external HTTP verification: 56 seconds after start.

**Decision and residual risk.** Maintain retirement of TCP/8080, archive isolation, source allowlisting and logging. Evaluate the fictional managed-backup option to reduce host-loss exposure. Plain HTTP is eligible only for a simulated, revocable 14-day classroom exception involving dummy data on the isolated network. No actual insurance, vendor agreement or production risk acceptance occurred. Residual risk scores are analyst assessments and must be reviewed by designated fictional owners.

**Management action requested (simulated):** Endorse the implemented lab controls; nominate owners for continued monitoring; decide whether to purchase a managed backup in a real analogue; and require TLS or immediate stop if the environment moves outside the lab boundary.

## 2. Scope, method and environment

Two UTM ARM64 VMs were used: Kali Linux (`192.168.128.4/24`, `eth0`) and Ubuntu Server 24.04.5 LTS (`192.168.128.5/24`, `enp0s1`). Both used the UTM Host Only network during exposure testing. Ubuntu ran Nginx 1.24.0 on TCP/80 and a Python HTTP training service on TCP/8080. Only fictional dummy content was used. Baseline and later tests used `nmap -sT`, `curl -i`, `ss -lntp`, UFW status, Nginx logs and UFW logs. A clean disk-only snapshot was made before vulnerable services were configured.

Risk scoring: **likelihood (1–5) × impact (1–5)**. Low 1–4; Medium 5–9; High 10–16; Critical 17–25. Scores are **ordinal, illustrative judgements**, not empirical probabilities, calibrated financial losses or ratings prescribed by ISO standards.

## 3. Baseline risk register

| ID | Asset / threat event | Observed weakness and evidence | Impact (business consequence) | L | I | Score / band | Treatment owner (proposed) |
|---|---|---|---|---:|---:|---|---|
| R1 | Legacy endpoint; unnecessary service misuse or compromise | TCP/8080 open; HTTP 200 retrieved legacy training endpoint (`baseline-ports.txt`, `baseline-legacy.txt`) | Increased attack surface and unsupported workflow exposure | 4 | 3 | 12 High | IT Service Owner |
| R2 | Document archive; unauthorised disclosure | Listing and direct dummy file retrieval both HTTP 200 (`baseline-listing.txt`, `baseline-file.txt`) | In a real analogue, disclosure of internal records | 4 | 4 | 16 High | Application Owner |
| R3 | Internal HTTP service; unauthorised clients reach portal | UFW inactive and approved test client could reach TCP/80; absence of a source-specific firewall rule (`baseline-ports.txt`, Ubuntu UFW screenshot) | Unnecessary client exposure and broader opportunity for misuse | 3 | 4 | 12 High | Infrastructure/Security Owner |
| R4 | Portal content; accidental deletion or system failure | Live portal file with no restoration evidence at baseline; recovery control established only later | Service interruption and integrity/availability impacts | 3 | 4 | 12 High | Service Continuity Owner |

**Evidence limitation:** R4's likelihood is a planning estimate, not a measured failure rate; R3 demonstrates insufficient network restriction, not that a malicious actor actually connected.

## 4. Change and rollback: risk avoidance

**Change ID:** CHG-GRC103-001. **Proposal:** Retire the unnecessary `grc-legacy.service` while retaining Nginx TCP/80. **Approval role:** Northbridge IT Service Owner — **SIMULATED**, not real management approval. **Expected business impact:** Loss of obsolete training endpoint only; approved portal remains accessible. **Test:** `systemctl is-active`, `ss -lntp`, Kali Nmap and HTTP checks. **Rollback:** `sudo systemctl enable --now grc-legacy`; verify HTTP 200. **Reapply:** `sudo systemctl disable --now grc-legacy` and rerun Nmap.

| State | TCP/80 | TCP/8080 | Evidence |
|---|---|---|---|
| Baseline | Open, portal HTTP 200 | Open, legacy HTTP 200 | `baseline-ports.txt`, `baseline-legacy.txt` |
| Retired | Open; `/public/` HTTP 200 | Closed; curl connection failed | `avoidance-ports.txt`, `avoidance-legacy.txt`, `avoidance-portal.txt` |
| Simulated rollback | Portal remained available | Legacy HTTP 200 | `rollback-legacy.txt` |
| Final re-treatment | Open | Closed | `avoidance-final-ports.txt` |

This avoids the exposure of the retired endpoint; **it does not eliminate risk to the remaining Nginx service**.

## 5. Preventive controls: archive and network

**Archive:** The dummy archive was moved from `/var/www/grc-lab/archive` to `/srv/grc-private/archive`, with group/other permissions removed. Nginx `autoindex off` was configured and `location /archive/ { deny all; }` explicitly blocked the old path.

| Path | Baseline | After hardening | Evidence |
|---|---|---|---|
| `/` | HTTP 200, lists directories | HTTP 403 | `baseline-web.txt`, `hardening-root.txt` |
| `/archive/` | HTTP 200, lists dummy file | HTTP 403 | `baseline-listing.txt`, `hardening-archive.txt` |
| `/archive/dummy-records.txt` | HTTP 200, full dummy file | HTTP 403 | `baseline-file.txt`, `hardening-file.txt` |
| `/public/` | HTTP 200 | HTTP 200 | `avoidance-portal.txt`, `hardening-public.txt` |

Turning off directory listings alone would **not** prevent direct requests for a known file. Moving it outside the served root, filesystem restriction and explicit denial provide independent safeguards.

**Network:** Ubuntu UFW configured with default deny incoming, default allow outgoing, logging enabled, and only `192.168.128.4 -> TCP/80` explicitly permitted. Console operation was used, avoiding an SSH lockout dependency. `sudo ufw status numbered` displayed a single source-restricted rule. The approved client obtained HTTP 200. A secondary Kali IP `192.168.128.11/24` was temporarily added after a duplicate-address check; bound-source curl timed out after approximately five seconds; the alias was removed.

## 6. Detective controls and correlation

| Test ID | Timestamp (UTC) | Source | Request/service | Expected / actual | Evidence / log |
|---|---|---|---|---|---|
| LOG-01 | 19:21:19 | 192.168.128.4 | GET `/public/` TCP/80 | 200 / 200 | `firewall-allowed.txt`; Nginx `grc_access.log` |
| LOG-02 | 19:18:45 | 192.168.128.4 | GET `/archive/` TCP/80 | 403 / 403 | `hardening-archive.txt`; Nginx `grc_access.log` |
| LOG-03 | 19:18:50 | 192.168.128.4 | GET `/archive/dummy-records.txt` | 403 / 403 | `hardening-file.txt`; Nginx `grc_access.log` |
| LOG-04 | 19:24:09–13 | 192.168.128.11 | TCP SYN to 192.168.128.5:80 | Timeout / timeout; block log present | `firewall-blocked.txt`, `firewall-blocked-time.txt`; kernel `UFW BLOCK` entries |

UFW events contain `IN=enp0s1`, `SRC=192.168.128.11`, `DST=192.168.128.5`, `PROTO=TCP` and `DPT=80`. The screenshots show these events both in kernel journal and `/var/log/ufw.log`. A dropped connection cannot complete an HTTP request and should not reach the Nginx request log. The displayed Nginx entries contain approved-source traffic and no completed request from the blocked alias.

## 7. Corrective control: backed-up restore

**Backup:** `/srv/grc-backups/public-before-test.tgz`, protected directory mode 700. Original `/var/www/grc-lab/public/index.html` SHA-256 was recorded in `~/portal-before.sha256`. The first restoration demonstrated hash verification and HTTP 200 but did not preserve a definitive failed-response test, so a final controlled run was performed.

| Event | UTC timestamp | Verified evidence |
|---|---|---|
| Final exercise started | 19:57:27 | `recovery-final-start.txt` |
| Dummy portal file absent | Before failure request | Ubuntu `ls`: No such file or directory |
| Failed external request | 19:57:53 | Kali `recovery-failed.txt` HTTP 403 |
| Archive restored; hash verified | 19:58:17 | Ubuntu SHA-256 check: `index.html: OK`; `recovery-final-end.txt` |
| External service restored | 19:58:23 | Kali `recovery-final-restored.txt` HTTP 200, original content |

**Observed measurement:** 50 seconds from exercise start to the timestamp recorded after restore/hash verification; 56 seconds to successful HTTP verification. These intervals include manual operator delays; they are not a service-level commitment or representative recovery guarantee. Same-host backup protects against some accidental deletions but **not** total server loss, destructive compromise or backup corruption.

## 8. Four-strategy governance record

| Strategy | Decision | Accountable role | Status and conditions |
|---|---|---|---|
| Avoidance | Retire legacy service, retain approved portal | IT Service Owner | Implemented and tested; simulated change approval |
| Mitigation | Archive isolation, source allowlisting, logging, verified restore | Application / Infrastructure / Continuity Owners | Implemented and tested within scope |
| Transfer | Consider third-party managed backup | Procurement + Service Continuity Owner | Proposal only; no vendor or insurance contract |
| Acceptance | Plain HTTP for dummy-data-only isolated lab | Fictional Risk Owner | **SIMULATED conditional approval only**; expires 22 Nov 2026 if adopted on 8 Nov 2026 |

**Acceptance condition:** Proposed 14-day expiry, review by 22 Nov 2026, isolate to host-only VMs and dummy records, no bridged/public network and no production use. Immediate reconsideration and escalation if any real data, broader use, changed network connectivity, elevated exposure, lost controls or new security finding occurs. If organisational risk appetite does not allow HTTP, stop the workflow and deploy TLS instead. Plain HTTP presents confidentiality/integrity and interception risks even on a private lab segment.

### Hypothetical managed-backup service clause

> The provider shall maintain encrypted managed copies of designated portal backups, protect backup access using least privilege, produce job-status and exception evidence, retain recovery records for a period agreed by the customer, and support an agreed restoration test at least quarterly. The customer shall classify the data, approve retention, restrict credentials, monitor provider reports, independently validate restorability, and operate the recovered application. Service availability, recovery objectives, data-centre/site failure scope, exclusions, breach notification, subcontracting and deletion must be specified in the final agreement. Neither this clause nor an insurance arrangement eliminates the underlying technical risk. No agreement is executed in this classroom exercise.

**Proposed evidence retention:** 12 months for test results and backup job records as a fictional working requirement, subject to actual legal, contractual and organisational retention policies; raw dummy backup retention is to be separately approved.

## 9. First-year cost and benefit analysis

All amounts below are **fictional classroom assumptions**; not invoices, quotations or measured financial savings.

| Option | Setup | Labour | Annual recurring | First-year total |
|---|---:|---:|---:|---:|
| A — Hardening | $0 | 4 h × $25 = $100 | $50 | **$150** |
| B — Managed backup | $120 | $0 specified | $20 × 12 = $240 | **$360** |
| C — TLS | $0 | 3 h × $25 = $75 | $25 | **$100** |
| A + B | $120 | $100 | $290 | **$510** |
| A + B + C | $120 | $175 | $315 | **$610** |

**Recommended combination for a real analogue:** A + B + C where business need and risk appetite justify the spend: hardening mitigates current access exposures; managed backup addresses some host-loss exposure not covered by local-only copies; TLS protects transport in broader/real-data use. The current isolated dummy-data exercise implements A's technical measures in the lab and does **not** purchase B or implement C. This recommendation is contingent on a validated backup service scope, appropriate off-host isolation and further risk review.

**Separate illustrative annualised loss expectancy (ALE) scenario for Option B only:**

- Assumed annual occurrence rate (ARO): 0.2 incidents/year.
- Assumed baseline single-loss expectancy (SLE): $5,000/event.
- Assumed residual SLE after tested recovery capability: $1,000/event.
- **Baseline ALE:** 0.2 × $5,000 = **$1,000/year**.
- **Residual ALE:** 0.2 × $1,000 = **$200/year**.
- **Illustrative annual benefit:** $800/year.
- **Option B first-year cost:** $360.
- **Illustrative first-year net benefit:** $800 − $360 = **$440**.

These financial assumptions are **not established by the local recovery test**. Exclusions: downtime while migrating, storage/egress growth, staff management overhead, service taxes, validation labour, vendor due diligence, security incidents, business interruptions beyond the model, and overlapping benefits. Do not add risk score values to currency or sum benefits across overlapping controls.

## 10. Residual risk review

| ID | Tested treatment outcome | Residual L | Residual I | Score / band | Owner | Review trigger |
|---|---|---:|---:|---|---|---|
| R1 | Legacy TCP/8080 closed; controlled rollback and re-retirement verified | 1 | 3 | 3 Low | IT Service Owner | Port 8080 reopens; service enabled; change or inventory drift |
| R2 | Archive relocated/restricted; old path and known file return 403 | 1 | 4 | 4 Low | Application Owner | Web root/config changes; new archive URL; new content |
| R3 | Approved source gets 200; unapproved source times out and UFW BLOCK corroborates | 2 | 4 | 8 Medium | Infrastructure/Security Owner | UFW rule drift; new client; host-network change; logging gap |
| R4 | Local backup restores file with SHA-256 OK and externally verified HTTP 200; host-loss gap remains | 3 | 4 | 12 High | Continuity Owner | Failed restore; host compromise/loss; backup failure; managed backup validation |

Residual scores are **illustrative analyst assessments**, not proof of risk elimination. In particular, no hosted managed-backup service has been tested or implemented; R4 therefore retains its host-loss residual. The four rows are not a substitute for a fresh threat assessment after a changed use case.

## 11. Monitoring and operational handover

The following are **proposed ongoing checks, not deployed continuous monitoring**.

| Metric/control | Owner | Frequency | Threshold | Escalation/action |
|---|---|---|---|---|
| Approved portal availability | Service Operations | Every 5 minutes | Any 2 consecutive failed /public/ checks or unexpected non-200 | Notify Application Owner; investigate HTTP/service and initiate incident process |
| Unexpected open ports | Infrastructure/Security | Daily and after change | Any TCP/8080 reopening or any unapproved listener | Alert Infrastructure Owner; disable unexpected service, investigate drift |
| Recovery-test success | Service Continuity | Quarterly and after backup changes | Any failed SHA-256 check, missing backup, or unsuccessful HTTP 200 restoration | Escalate to Continuity Owner; remediate and retest |
| Retired service configuration drift | Infrastructure/Security | Daily and after patch/deployment | `grc-legacy` active/enabled or TCP/8080 listening | Change exception review; re-disable after incident evaluation |

**Handover:** Service Operations maintains portal checks; Security reviews firewall events and configuration drift; the Application Owner approves Nginx changes; the Continuity Owner maintains backup/restore procedures. Keep evidence with UTC timestamps, host/interface references and appropriately redacted log excerpts. Route exceptions to fictional risk owners for simulated classroom approval and review.

## 12. Limitations and next actions

- No production network or real records were involved; findings demonstrate lab behaviour, not enterprise exploitability.
- The temporary alias tests network-source filtering; it does not establish cryptographic user authentication.
- Default UFW route information displayed a self-referential gateway; the observed direct host-only link worked, but this should not be extrapolated to complex routing scenarios.
- Nginx remained on HTTP; TLS deployment is priced as a fictional option but not implemented.
- Monitoring thresholds, supplier responsibilities and acceptance are **proposals**; actual organisational endorsement has not occurred.
- Source files, screenshot exports, configuration captures and redacted logs still need collection from the VMs for the required evidence ZIP.

**Conclusion:** The lab verified avoidance, preventive, detective and corrective treatment controls. It also showed that successful technical treatment of one exposure does not remove other residual risks, particularly complete-host-loss recovery and plaintext HTTP use beyond the restricted classroom boundary.
