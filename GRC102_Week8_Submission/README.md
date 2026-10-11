# GRC102 Week 8 Practical Lab

## Student Information

- **Student:** Adediran Eunice Adebukola
- **Registration number:** C11-26-CGRCE-17595
- **Course:** GRC102 Information Security Governance
- **Assessment:** Linux Security Governance Practical Laboratory

## Submission Overview

This folder contains the report and supporting evidence for the Week 8 practical laboratory. The work follows the four-part structure in the assessment brief:

1. Setting up a simulated Docker environment
2. Analyzing security governance failures
3. Implementing and verifying governance controls
4. Developing governance metrics and reporting

## Folder Structure

- `01_Environment` - Docker Compose configuration, database initialization and environment evidence
- `02_Vulnerability_and_Patch_Management` - vulnerability scanner, patch-management script and scan reports
- `03_Governance_Failure_Analysis` - governance tracker, controlled attack simulation, analysis results and Equifax comparison
- `04_Control_Implementation` - control implementation script, control reports and verification evidence
- `05_Metrics_and_Reporting` - metrics script, executive dashboard, board report, charts and user guidance
- `06_Final_Report` - final PDF submission and editable Word version
- `Evidence_Screenshots` - selected screenshots from the practical work

## Main Submission File

The submission-ready report is:

`06_Final_Report/GRC102_Week8_Practical_Lab_Adediran_Eunice_Adebukola_C11-26-CGRCE-17595.pdf`

## Environment Note

The original laboratory VM could not reach Docker Hub. The environment was therefore completed using Docker Desktop's Linux virtual machine on macOS. The unavailable `vulhub/struts2:s2-045` tag was replaced with `vulhub/struts2:2.3.30`, and host-executed scripts used `127.0.0.1:8080` instead of the internal Docker hostname.

## Verification Note

The supplied control scripts record simulated remediation rather than replacing or reconfiguring the vulnerable containers. The post-control scan and attack retest therefore remained successful. This result is retained as evidence and discussed as a control-effectiveness limitation in the final report.
