# Lab 3B - Advanced Cybersecurity Risk Quantification

**Student:** Adediran Eunice Adebukola  
**Registration number:** C11-26-CGRCE-17595  
**Case organisation:** SecureBank Financial  
**Platform:** SecureMobile mobile banking application

## Purpose

This submission quantifies three cybersecurity risk scenarios from the official Lab 3B brief, evaluates the three proposed security controls, and communicates the results to the CISO and CFO. The model is **illustrative**, not a prediction of realised losses or proof of control effectiveness.

## Submission files

| File or directory | Contents | Assignment requirement |
|---|---|---|
| `GRC102_Lab3B_Risk_Quantification.xlsx` | Ten worksheets with source figures, explicit assumptions, formulas, risk matrix, control economics, scenario sensitivity, treatment plan, native charts, dashboard and optional budget optimisation | Risk calculation workbook; control analysis worksheet |
| `Executive_Dashboard_One_Page.pdf` | One-page CISO/CFO dashboard with KPIs, risk exposure before/after, ROI chart, and recommendation | One-page executive dashboard |
| `Executive_Briefing.pdf` | Five-page executive report with risk and control analysis, financial justification, nine visualisation types, treatment Gantt, limitations and recommendations | Executive briefing package |
| `charts/` | Nine titled, labelled PNG charts, including probability-impact heat map, scatter plot, risk timeline and Gantt chart | Graphical representations |
| `source/model_inputs.json` | Source values and separately identified analyst assumptions | Transparent data lineage |
| `source/build_visuals.py` | Reproducible chart/PDF generation from JSON source | Supporting reproducibility |
| `CALCULATIONS_AND_ASSUMPTIONS.md` | Worked equations, mappings, sensitivity, costs, interpretation and limitations | Visible calculation steps and rationale |
| `SUBMISSION_CHECKLIST.md` | Checklist mapping the official deliverables to files | Submission review |

## Key base-case outputs

| Risk | Assumed annual probability | SLE | Modelled ALE |
|---|---:|---:|---:|
| API authentication bypass | 15% | $5,000,000 | $750,000 |
| Database injection | 25% | $125,000,000 | $31,250,000 |
| Session hijacking | 40% | $7,500,000 | $3,000,000 |
| **Total** | | | **$35,000,000** |

The $35m result is conditional on a **single-event annual probability** interpretation and using the **maximum single-incident loss as SLE**. The official brief does not supply annual incident frequency or a distribution of incident severity.

| Control | First-year cost | Annual avoided ALE | Residual ALE | Year-one ROI |
|---|---:|---:|---:|---:|
| API gateway | $400,000 | $675,000 | $75,000 | 68.8% |
| WAF | $175,000 | $23,437,500 | $7,812,500 | 13,292.9% |
| Enhanced MFA | $230,000 | $2,850,000 | $150,000 | 1,139.1% |
| **Total** | **$805,000** | **$26,962,500** | **$8,037,500** | **3,249.4%** |

These very high returns are a mathematical consequence of the supplied maximum-loss inputs and assumed control effectiveness. They are **not guaranteed savings** and should not be used as investment-grade forecasts without further evidence.

## Workbook navigation

1. `Start_Here` - navigation and source/assumption colour key.
2. `Assumptions` - annual-event interpretation, severity realisation, priority and heat-map thresholds.
3. `Risk_Calcs` - source values, SLE, assumed ARO, ALE and financial priority.
4. `Control_Calcs` - initial and annual costs, avoided ALE, residual ALE, first-year ROI and payback.
5. `Risk_Matrix` - probability-impact classifications and 3x3 heat map.
6. `Sensitivity` - 10%, 25%, 50% and 100% realised-loss scenarios.
7. `Treatment_Plan` - owner, timing, evidence and retest schedule.
8. `Chart_Data` - chart-ready formulas and seven native Excel charts.
9. `Executive_Dashboard` - formula-linked summary KPIs and comparison tables.
10. `Budget_Options` - **bonus**, eight control combinations under an explicitly hypothetical $400,000 first-year budget.

Blue numerical text indicates source inputs or editable assumptions; green indicates cross-sheet formula links; black indicates local calculations. The spreadsheet contains Excel formulas, not static copies of calculated results.

## Reproduce the charts and PDF reports

With Python 3 installed:

```bash
python3 -m pip install -r requirements.txt
python3 source/build_visuals.py
```

The Python script regenerates the nine chart PNGs and both PDFs from `source/model_inputs.json`. The XLSX is the separate, formula-driven Excel model. **If you edit assumptions in Excel, also update the JSON and rerun the script before claiming the PDF and workbook reflect the same scenario.**

## Important assumptions and limitations

- **ARO:** Exploit probabilities are treated as the chance of **one loss event in a year**, with no more than one modelled event per risk. Probability is not automatically an annual event frequency.
- **SLE:** Supplied maximum incident loss is used as the base-case single-event loss. Actual expected severity may be much lower; see the sensitivity worksheet.
- **Mapping:** API gateway → authentication bypass; WAF → database injection; MFA → session hijacking. This mapping and the applicability of the stated effectiveness percentages are **analyst assumptions**, not verified facts.
- **Cost and time:** One-year ROI includes initial implementation and annual maintenance. Payback uses steady-state annual avoided loss net of maintenance; implementation delays and discounting are excluded.
- **Schedule:** Day 30 WAF, day 90 MFA, day 180 API gateway are **illustrative milestones**, not dates supplied in the brief.
- **Risk thresholds and budget:** Financial risk priority bands and the $400,000 bonus budget are illustrative analyst assumptions, not approved bank risk appetite or a supplied budget.
- **Technical caveats:** A gateway does not automatically correct flawed application authentication; a WAF does not replace parameterised SQL queries; MFA does not necessarily prevent theft of an authenticated session.
- **Scope exclusions:** No incident history, incident cost distribution, implementation feasibility study, or empirical effectiveness data were provided.

## Academic integrity and sources

The financial and technical inputs come from the user-provided **"Lab 3b: Advanced Cybersecurity Risk Quantification"** brief and the instructor's **"Laboratory guidance"** screenshot. All additional assumptions are explicitly identified.
