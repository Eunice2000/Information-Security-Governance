# Lab 3A — Calculation Walkthrough and Assumption Register

## Source and scope

Source: *Lab 3A.docx*, “Lab 3: Advanced GRC Phishing Simulation & Quantitative Risk Analysis,” pp. 1–8. All source inputs are reproduced on the `Inputs` and `Campaign Metrics` sheets of the Excel workbook. USD values are nominal; the brief supplies no inflation, discount rate, annual maintenance, deployment start date or empirical annual breach frequency.

## 1. Phishing metrics

For each campaign, open/click/credential/PII rates = stage event count / emails sent. Stage conversions: open-to-click = clicks / opens; click-to-credential = credentials / clicks.

| Campaign | Open | Click | Credential | PII | Open-to-click | Click-to-credential |
|---|---:|---:|---:|---:|---:|---:|
| A | 82.00% | 47.00% | 18.00% | 5.00% | 57.32% | 38.30% |
| B | 80.00% | 60.00% | 30.00% | 10.00% | 75.00% | 50.00% |
| C | 90.00% | 75.00% | 15.00% | 10.00% | 83.33% | 20.00% |
| Weighted | 82.33% | 59.77% | 24.42% | 8.84% | 72.60% | 40.86% |

Overall rate = 105 credential submissions / 430 emails = 24.4186%, **not** the brief's 22.1%.

## 2. Exposure model (exercise method)

`projected stolen = 2,000 × (credential submissions / emails sent)`  
`expected major breach events = projected stolen × 25%`  
`scenario exposure = expected events × $4,350,000`

- Campaign A: 2,000 × 18% = 360; ×25% = 90; ×$4.35M = **$391.50M**, not the brief's $156.60M.
- Campaign B: 2,000 × 30% = 600; ×25% = 150; ×$4.35M = **$652.50M**.
- Campaign C: 2,000 × 15% = 300; ×25% = 75; ×$4.35M = **$326.25M**, not the brief's $104.40M.

**Crucial limitation:** The supplied 25% probability is conditional on stolen credentials; it is not an annual frequency. The brief assumes that every compromised account can generate an independent $4.35M “major breach”, risking severe double-counting of correlated incidents. The scenarios also extrapolate a small sample (including a distinct executive cohort) to the entire 2,000-person workforce. The figures must not be represented as validated annual loss forecasts or summed as independent events.

## 3. Confidence intervals

The brief specifies the approximate 95% Wald interval: `p ± 1.96 × SQRT[p × (1-p) / n]`.

- A: p=.18, n=100, margin=.07530; **10.47%–25.53%**.
- B: p=.30, n=250, margin=.05680; **24.32%–35.68%**.
- C: p=.15, n=80, margin=.07824; **7.18%–22.82%**.

These intervals assume approximately independent, representative observations; they are not causal tests and do not adjust for employee overlap, cohort differences or nonrandom sampling.

## 4. Standalone controls and ROI

`Risk reduction = baseline × effectiveness`  
`Residual risk = baseline × (1 − effectiveness)`  
`1-year ROI = (risk reduction − initial cost) / initial cost × 100`  
`Simple payback (years) = initial cost / annual avoided loss`

| Control | Cost | Efficacy | Avoided scenario exposure | ROI |
|---|---:|---:|---:|---:|
| MFA | $90,000 | 99.9% | $651,847,500 | 724,175% |
| Training | $100,000 | 60% | $391,500,000 | 391,400% |
| Email filtering | $50,000 | 20% (assumption) | $130,500,000 | 260,900% |

The brief incorrectly calls 30% Campaign B's click rate. The true click rate is 150/250=60%. Training reduces this to 60% × (1−60%)=24%. If the post-click credential conversion remains 75/150=50%, the new credential rate is 12%, or 240 projected compromised accounts; the classroom exposure becomes $261M. The final result agrees with the brief, but its intermediate labelling is wrong.

Email filtering's 20% reduction is an **analyst assumption inferred** from the brief's $130.5M reduction illustration, not a supplied effectiveness input. The source ROI of 260,800% is inconsistent with the formula; the result is 260,900%.

## 5. Combined portfolio and budget

Avoid double-counting overlapping standalone savings. Sequential exposure:

- Baseline: $652,500,000.
- After training (×40%): $261,000,000.
- After MFA (×0.1%): $261,000.
- After assumed email filtering (×80%): **$208,800**.

Three quantified controls cost $240,000. The brief's full programme cost is $490,000 = MFA $90K + training $100K + filtering $50K + simulations $25K + monitoring $150K + analytics $75K. Do not invent effectiveness for the three unquantified activities. Full programme scenario ROI = `(($652,500,000−$208,800)−$490,000)/$490,000 × 100` = **133,020.65%**. This very high ROI is a mathematical output of extreme baseline and efficacy assumptions, not a procurement forecast.

**Bonus break-even:** $490,000 / $4,350,000 = **0.1126** of one major breach of stated severity; preventing one such discrete event would exceed programme cost, conditional on the assumed severity.

## 6. Critical reconciliation of the source brief

The brief's 93.75% breach probability is not derivable from “150 expected breaches”; a count is not a probability. The final stated $65M post-control ALE / 90% reduction is inconsistent with 99.9% MFA impact reduction when applied to the same baseline. The supplied “industry averages” have no citations and are not independently validated. Risk labels are taken from the brief and separated from corrected financial ranking.

## 7. What the CFO should request before funding decisions

Actual annual major-breach frequency; incident clustering and severity distribution; customer and workforce population segmentation; verified MFA coverage and efficacy; recurring maintenance; rollout time; costs of operations; realistic training effectiveness; observed control impacts; risk appetite and risk acceptance authority. Until those are available, treat all dollar savings as *illustrative scenario outputs*.
