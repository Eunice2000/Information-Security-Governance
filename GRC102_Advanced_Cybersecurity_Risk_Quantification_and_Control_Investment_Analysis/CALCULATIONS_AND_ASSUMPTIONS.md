# Calculation methodology and worked solutions

## 1. Input figures supplied in the brief

The brief provides a mobile banking system with 500,000 active customers, 50,000 daily transactions and a $2,500 average transaction. These contextual metrics are **not** used to extrapolate incident frequency, because the brief does not provide a relationship between transaction volume and incident occurrence.

- API authentication bypass: 15% exploit probability; maximum single-incident loss **$5,000,000**; estimated detection time **48 hours**.
- Database injection: 25% exploit probability; **500,000 records** at **$250/record** = **$125,000,000** maximum exposure.
- Session hijacking: 40% exploit probability; **5,000 accounts** at **$1,500/account** = **$7,500,000** maximum exposure.
- API gateway: **$350,000** initial, **$50,000/year** maintenance, **90%** effectiveness against API vulnerabilities.
- WAF: **$150,000** initial, **$25,000/year** maintenance, **75%** effectiveness against web vulnerabilities.
- Enhanced MFA: **$200,000** initial, **$30,000/year** maintenance, **95%** effectiveness against account takeover.

## 2. ARO and ALE: explicit assumption

The brief gives exploit probabilities **without a time period**. We adopt the following illustrative interpretation: each supplied probability is the chance of **at most one loss event during a one-year evaluation period**. Therefore, for this Bernoulli scenario only:

`Assumed ARO = P(one event in the year) × 1 event/year`.

This is **not** an empirical annual incident frequency and does not cover multiple events in one year. The maximum incident loss is used as the base-case SLE, not because it is known to be the mean severity but to model the maximum-loss scenario.

`SLE = max incident loss (or exposed records/accounts × loss per unit)`  
`ALE = SLE × assumed ARO`

| Risk | SLE calculation | Assumed ARO | ALE calculation |
|---|---|---:|---|
| API bypass | $5,000,000 | 0.15 | $5,000,000 × 0.15 = **$750,000** |
| DB injection | 500,000 × $250 = $125,000,000 | 0.25 | $125,000,000 × 0.25 = **$31,250,000** |
| Session hijacking | 5,000 × $1,500 = $7,500,000 | 0.40 | $7,500,000 × 0.40 = **$3,000,000** |

**Total modelled baseline ALE = $35,000,000/year.**

Financial priority cutoffs are **analyst assumptions**: Critical ≥ $10m/year; High ≥ $1m/year; Moderate below $1m/year. Thus DB injection is Critical, session hijacking High, API bypass Moderate by **ALE**, despite API bypass being labelled a "Critical Finding" in the vulnerability assessment. A vulnerability's technical severity is not the same as its financial ALE priority.

## 3. Control mapping and risk reduction

To avoid double counting, each control is mapped to one distinct risk for this simplified model:

- API gateway → API authentication bypass; model applies **90%** reduction to API bypass ALE.
- WAF → database injection; model applies **75%** reduction to database-injection ALE.
- Enhanced MFA → session hijacking; model applies **95%** reduction to session-hijacking ALE.

**These are applicability assumptions, not evidence that the controls will eliminate those specific weaknesses.** In practice, a gateway does not fix every authentication/authorisation flaw, a WAF cannot substitute for parameterised queries, and MFA may not prevent replay of a stolen session.

`Annual avoided ALE = baseline ALE × assumed effectiveness`  
`Residual ALE = baseline ALE − annual avoided ALE`

| Control | Baseline ALE | Assumed reduction | Avoided ALE | Residual ALE |
|---|---:|---:|---:|---:|
| API gateway | $750,000 | 90% | $675,000 | $75,000 |
| WAF | $31,250,000 | 75% | $23,437,500 | $7,812,500 |
| MFA | $3,000,000 | 95% | $2,850,000 | $150,000 |
| **Total** | **$35,000,000** | | **$26,962,500** | **$8,037,500** |

## 4. One-year control economics

Evaluation period: **one year**.  
`First-year cost = initial investment + one year of annual maintenance`  
`First-year net benefit = annual avoided ALE − first-year cost`  
`First-year ROI = first-year net benefit / first-year cost × 100%`  
`Simple payback in years = initial investment / (annual avoided ALE − annual maintenance)`  
`Simple payback in months = years × 12`

| Control | First-year cost | Net benefit | First-year ROI | Simple payback |
|---|---:|---:|---:|---:|
| API gateway | $400,000 | $275,000 | **68.75%** | **6.72 months** |
| WAF | $175,000 | $23,262,500 | **13,292.86%** | **0.08 months** |
| MFA | $230,000 | $2,620,000 | **1,139.13%** | **0.85 months** |
| **Portfolio** | **$805,000** | **$26,157,500** | **3,249.38%** | **0.31 months (pooled model)** |

The WAF's very short mathematical payback reflects the maximum-loss model and **must not** be presented as a realistic deployment-to-savings guarantee. Payback ignores implementation lag, ongoing losses before go-live, discounted cash flow, uncertainty and other costs.

## 5. Severity sensitivity

The base case assumes 100% of the maximum incident loss is incurred if the event occurs. To illustrate the sensitivity to this aggressive severity assumption, hold annual probabilities, control efficacy and costs fixed and multiply all incident severities by a common factor.

| Severity realised | Baseline ALE | Avoided ALE | Residual ALE | First-year ROI |
|---|---:|---:|---:|---:|
| 10% of maximum | $3,500,000 | $2,696,250 | $803,750 | 234.94% |
| 25% of maximum | $8,750,000 | $6,740,625 | $2,009,375 | 737.34% |
| 50% of maximum | $17,500,000 | $13,481,250 | $4,018,750 | 1,574.07% |
| 100% of maximum | $35,000,000 | $26,962,500 | $8,037,500 | 3,249.38% |

These are deterministic scenarios, not estimated percentiles or evidence-based loss distributions.

## 6. Risk heat map

Probability bands (analyst assumptions): Low <20%; Medium 20% to <35%; High ≥35%.  
Impact bands (analyst assumptions): Low <$1m; Medium $1m to <$10m; High ≥$10m.

- R1 API bypass: **Low probability, Medium impact**.
- R2 DB injection: **Medium probability, High impact**.
- R3 session hijacking: **High probability, Medium impact**.

Heat-map classifications and financial ALE priority serve different purposes and need not match.

## 7. Risk treatment and monitoring

**First 30 days:** Immediately contain API authentication bypass; validate affected assets and transaction limits; deploy and independently test WAF controls for the injection pathway; verify database access monitoring and incident readiness.

**Within 90 days:** Deploy enhanced MFA and session controls; centralise audit/security telemetry; tune SIEM alerting; independently retest WAF and MFA effectiveness.

**Within one year:** Complete API gateway deployment; independently retest authentication and authorisation; quarterly risk-model updates and governance reporting.

**Schedule assumption:** WAF day 30, MFA day 90, gateway day 180. The risk reduction line shows the **annualised ALE run-rate after hypothetical control go-live**, not actual accumulated savings or observed historical risk.

## 8. Bonus budget analysis

The official brief supplies **no budget limit**. For an explicitly hypothetical **$400,000 first-year budget**, the workbook evaluates all eight possible combinations of the three controls. Under the modelled one-to-one benefits, **WAF alone** maximises avoided annual ALE among affordable combinations ($175,000 cost; $23,437,500 avoided ALE). This financial optimum does **not** waive the need to contain and remediate the API authentication bypass.

## 9. Evidence limitations and decision discipline

No annual event history, empirical severity distribution, loss recovery, control coverage tests, regulatory fine schedule, deployment timeline, or approved risk appetite was supplied. The model therefore must not be interpreted as an actuarial forecast or a confirmed security posture. Technical remediation, compensating controls, independent retesting and periodic recalibration are required.
