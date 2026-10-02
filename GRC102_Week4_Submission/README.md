# GRC102 Week 4 Practical Laboratory

**Student:** Adediran Eunice Adebukola  
**Registration Number:** C11-26-CGRCE-17595  
**Course:** GRC102 Information Security Governance  
**Organisation:** Meridian Digital Services  
**Submission Date:** 2 October 2026

## Laboratory Scope

This repository contains evidence produced during the GRC102 Week 4 Linux security auditing practical. The assessment covered Linux auditing with auditd, system and authentication log analysis, Lynis security assessment, governance/control monitoring, and SIEM/continuous-monitoring mapping.

## Evidence Bundle 1 — Auditd Configuration and Events

Located in `01_Auditd_Evidence/`.

Evidence includes:

- auditd service status
- active audit rules
- ausearch event evidence
- aureport summaries
- supporting raw command output
- four screenshot exhibits

## Evidence Bundle 2 — Linux Log Analysis

Located in `02_Log_Analysis/`.

Evidence includes:

- journalctl review
- warning/error analysis
- SSH authentication activity
- sudo/privileged activity
- failed-login review
- security-event review table
- three screenshot exhibits

## Evidence Bundle 3 — Lynis Security Assessment

Located in `03_Lynis_Assessment/`.

Evidence includes:

- Lynis scan results
- Lynis report data
- Lynis log
- prioritised findings
- hardening index evidence
- two screenshot exhibits

Key findings identified during the assessment included:

1. Security repository configuration requiring validation.
2. One or more vulnerable packages requiring remediation.
3. Loaded iptables modules without an active ruleset, requiring validation of the effective host firewall architecture.

## Evidence Bundle 4 — Control Monitoring and Governance

Located in `04_Control_Monitoring/`.

Contains the control-monitoring table and governance escalation assessment covering control objective, evidence source, ownership, status, risk, remediation and retesting.

## Evidence Bundle 5 — SIEM and Automation Mapping

Located in `05_SIEM_Automation/`.

Contains the mapping of Linux audit, authentication, system and Lynis evidence to SIEM monitoring, operational alerting, governance escalation and continuous control monitoring.

## Evidence Bundle 6 — Final Audit Report

Located in `06_Final_Report/`.

The final report consolidates the scope, methodology, evidence-backed findings, risk priorities, recommendations, control monitoring, SIEM mapping, remediation ownership and retest approach.

## Evidence Authenticity

Raw command outputs and logs in this repository were collected from the authorised GRC102 Week 4 lab environment. Screenshot exhibits display retained evidence generated during the practical.

AI assistance was used for report structuring and language refinement. Lab activities, commands, evidence collection, technical verification and review of findings were performed by the student.
