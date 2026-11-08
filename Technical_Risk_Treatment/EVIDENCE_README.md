# Evidence inventory and reproduction guide

All files below are **expected artefacts from the local VMs**, not files automatically uploaded to GitHub. Baseline, avoidance, hardening and recovery HTTP files were visibly created on Kali during testing; the Ubuntu source-side files still need to be copied out. Record paths exactly and note missing exports explicitly rather than inventing them.

## 1. Evidence map

| Assessment step | Evidence | Source |
|---|---|---|
| Environment and isolation | UTM Host Only screenshots, checkpoint screenshot, `network-time.txt`, `kali-network.txt`, `kali-routes.txt`, Ubuntu `ip -br addr`/`ip route` | Kali, Ubuntu, Mac |
| Baseline services | `baseline-time.txt`, `baseline-ports.txt`, `baseline-web.txt`, `baseline-listing.txt`, `baseline-file.txt`, `baseline-legacy.txt` | Kali |
| Avoidance | `avoidance-ports.txt`, `avoidance-legacy.txt`, `avoidance-portal.txt`, `rollback-legacy.txt`, `avoidance-final-ports.txt`, `systemctl` outputs | Kali, Ubuntu |
| Archive hardening | `hardening-public.txt`, `hardening-archive.txt`, `hardening-file.txt`, `hardening-root.txt`, updated Nginx site config, private-directory permissions | Kali, Ubuntu |
| UFW permit/deny | `firewall-allowed.txt`, `firewall-blocked.txt`, `firewall-blocked-time.txt`, `ufw status numbered` | Kali, Ubuntu |
| Detective controls | `grc_access.log` relevant extracts, `UFW BLOCK` log excerpts | Ubuntu |
| Recovery | `recovery-failed.txt`, `recovery-final-restored.txt`, `portal-before.sha256`, `recovery-final-start.txt`, `recovery-final-end.txt`, hash check result | Kali, Ubuntu |
| Governance | `REPORT.md`, management summary, risk treatment register | Repository/documentation |
| Financial | Calculation workbook and first-year/ALE formulas | Submission package |

## 2. Expected ZIP layout

```text
GRC103_Technical_Risk_Treatment_Evidence.zip
├── README.md
├── kali/
│   ├── baseline-*.txt
│   ├── avoidance-*.txt
│   ├── rollback-legacy.txt
│   ├── hardening-*.txt
│   ├── firewall-*.txt
│   └── recovery-*.txt
├── ubuntu/
│   ├── configs/grc-lab.nginx.conf
│   ├── configs/grc-legacy.service
│   ├── configs/ufw-status.txt
│   ├── logs/grc-access-redacted.log
│   ├── logs/ufw-block-redacted.log
│   └── recovery/
│       ├── portal-before.sha256
│       ├── recovery-final-start.txt
│       ├── recovery-final-end.txt
│       └── sha256-verify.txt
├── screenshots/
└── calculations/
    └── treatment-costs.xlsx
```

The ZIP should contain the *actual* outputs, not recreated example values. Redact personal identities, secrets, irrelevant MACs and non-lab addresses as necessary while preserving the source/destination lab IP, timestamps, protocol, destination port and outcome fields needed for correlation.

## 3. Useful export commands (Ubuntu console)

```bash
mkdir -p ~/grc-ubuntu-evidence/{configs,logs,recovery}
sudo cp /etc/nginx/sites-available/grc-lab ~/grc-ubuntu-evidence/configs/grc-lab.nginx.conf
sudo cp /etc/systemd/system/grc-legacy.service ~/grc-ubuntu-evidence/configs/grc-legacy.service
sudo ufw status numbered > ~/grc-ubuntu-evidence/configs/ufw-status.txt
sudo grep 'UFW BLOCK' /var/log/ufw.log | tail -n 20 > ~/grc-ubuntu-evidence/logs/ufw-block-redacted.log
sudo tail -n 30 /var/log/nginx/grc_access.log > ~/grc-ubuntu-evidence/logs/grc-access-redacted.log
cp ~/portal-before.sha256 ~/recovery-final-start.txt ~/recovery-final-end.txt ~/grc-ubuntu-evidence/recovery/
sha256sum -c ~/portal-before.sha256 > ~/grc-ubuntu-evidence/recovery/sha256-verify.txt
```

**Note:** Review and redact the exported logs before publication. The output of `sudo cp` into a user-owned directory may be root-owned; use `sudo chown -R "$USER:$USER" ~/grc-ubuntu-evidence` after exporting when appropriate.

## 4. Submission checklist

- [ ] PDF report containing one-page management summary, risk register, treatment changes/rollback, timing, financials, residual risk and monitoring.
- [ ] ZIP containing actual command outputs, configs, redacted logs, screenshots, calculation workbook and this mapping.
- [ ] Baseline and post-treatment comparisons are intelligible from file contents.
- [ ] All tests clearly show expected versus actual outcomes and timestamps.
- [ ] No passwords, private keys, real records or VM images.
- [ ] Simulated approvals are explicitly labelled.
- [ ] Local-only backup limitation and unimplemented transfer/TLS decisions remain clear.
