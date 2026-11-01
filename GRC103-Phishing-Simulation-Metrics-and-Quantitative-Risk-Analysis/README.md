# GRC102 Lab 3A — Advanced GRC Phishing Simulation & Quantitative Risk Analysis

**Student:** Adediran Eunice Adebukola  
**Registration number:** C11-26-CGRCE-17595  
**Scenario:** GlobalTech Inc.  
**Prepared:** 1 November 2026

## Repository contents

- `GRC102_Lab3A_Phishing_Risk_Model.xlsx` — formula-driven workbook: source inputs, campaign metrics, risk exposure, confidence intervals, control economics, sequential portfolio, sensitivity, risk matrix, treatment plan, dashboard, source reconciliation.
- `Executive_Briefing.pdf` — executive report with complete calculations, risk recommendations and treatment timeline.
- `Executive_Dashboard_One_Page.pdf` — concise one-page executive dashboard.
- `charts/` — nine exportable, labelled charts, including campaign funnel, risk exposure, uncertainty, ROI, heat-map proxy, sequential reduction, budget and Gantt.
- `CALCULATIONS_AND_ASSUMPTIONS.md` — formulas, calculation walkthrough, caveats and source corrections.
- `SUBMISSION_CHECKLIST.md` — deliverable-to-file crosswalk.

## Key results (scenario estimates, not forecasts)

| Campaign | Credential submission rate | Corrected financial scenario |
|---|---:|---:|
| A: HR Bonus | 18% | $391,500,000 |
| B: IT Reset | 30% | $652,500,000 |
| C: CEO Review | 15% | $326,250,000 |

Overall credential submissions: **105/430 = 24.42%**. The three campaigns targeted different populations; their hypothetical exposures must not be added together as a single organisational annual loss forecast.

## Modelling limitations

The original brief does not supply an annual occurrence rate for major breaches. Its 25% breach probability is conditional on credentials being stolen and does not specify a time period. The large “ALE” results follow the classroom scenario formula but are not calibrated annual forecasts. The original brief also contains arithmetic inconsistencies for Campaigns A/C and an incorrect overall credential rate; the workbook reconciles these rather than silently repeating them.

ROI calculations assume a **one-year evaluation horizon**, initial implementation cost only, uniform annual avoided losses and no quantified maintenance or deployment delays (these were not supplied). The assumed **20% email-filter effectiveness** is inferred from a worked example, not a stated efficacy rate. Standalone control savings overlap; the portfolio uses sequential residual risk.

## How to review

1. Open `Inputs` in the Excel workbook and read the blue source values and yellow analyst assumptions.
2. Review formula cells on `Campaign Metrics`, `Risk Exposure`, `Confidence Intervals` and `Control Analysis`.
3. Review `Source Reconciliation` before interpreting the executive dashboard.
4. Read the PDF briefing and inspect the nine `charts/` figures.

## Academic integrity

The numerical source data comes from the supplied Lab 3A assignment, not an actual live phishing campaign. Calculations and financial projections are modelled classroom scenarios. AI assistance was used to structure the analysis, create formulas, charts and draft the reports; the student should independently verify and be able to explain every calculation before submission.
