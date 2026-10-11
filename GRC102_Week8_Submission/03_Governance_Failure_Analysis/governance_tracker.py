#!/usr/bin/env python3

import os
import sys
import json
import datetime
import argparse

class GovernanceTracker:
    def __init__(self, data_file="governance_data.json"):
        self.data_file = data_file
        self.load_data()
    
    def load_data(self):
        """Load governance data from file"""
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                self.data = json.load(f)
        else:
            # Initialize with default data
            self.data = {
                "policies": [],
                "controls": [],
                "risks": [],
                "incidents": [],
                "metrics": [],
                "audits": []
            }
    
    def save_data(self):
        """Save governance data to file"""
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=2)
    
    def add_policy(self, name, description, owner, approval_date, review_date):
        """Add a security policy"""
        policy = {
            "id": f"POL-{len(self.data['policies']) + 1:03d}",
            "name": name,
            "description": description,
            "owner": owner,
            "approval_date": approval_date,
            "review_date": review_date,
            "status": "Active"
        }
        
        self.data["policies"].append(policy)
        self.save_data()
        return policy["id"]
    
    def add_control(self, name, description, policy_id, owner, implementation_date):
        """Add a security control"""
        control = {
            "id": f"CTL-{len(self.data['controls']) + 1:03d}",
            "name": name,
            "description": description,
            "policy_id": policy_id,
            "owner": owner,
            "implementation_date": implementation_date,
            "status": "Implemented"
        }
        
        self.data["controls"].append(control)
        self.save_data()
        return control["id"]
    
    def add_risk(self, name, description, likelihood, impact, owner, mitigation_plan):
        """Add a security risk"""
        risk_level = self.calculate_risk_level(likelihood, impact)
        
        risk = {
            "id": f"RISK-{len(self.data['risks']) + 1:03d}",
            "name": name,
            "description": description,
            "likelihood": likelihood,
            "impact": impact,
            "risk_level": risk_level,
            "owner": owner,
            "mitigation_plan": mitigation_plan,
            "status": "Open"
        }
        
        self.data["risks"].append(risk)
        self.save_data()
        return risk["id"]
    
    def add_incident(self, name, description, date, severity, affected_systems, root_cause, resolution):
        """Add a security incident"""
        incident = {
            "id": f"INC-{len(self.data['incidents']) + 1:03d}",
            "name": name,
            "description": description,
            "date": date,
            "severity": severity,
            "affected_systems": affected_systems,
            "root_cause": root_cause,
            "resolution": resolution,
            "status": "Closed"
        }
        
        self.data["incidents"].append(incident)
        self.save_data()
        return incident["id"]
    
    def add_metric(self, name, description, target, actual, period, trend):
        """Add a security metric"""
        metric = {
            "id": f"MET-{len(self.data['metrics']) + 1:03d}",
            "name": name,
            "description": description,
            "target": target,
            "actual": actual,
            "period": period,
            "trend": trend,
            "status": "Active"
        }
        
        self.data["metrics"].append(metric)
        self.save_data()
        return metric["id"]
    
    def add_audit(self, name, description, date, auditor, findings, recommendations):
        """Add a security audit"""
        audit = {
            "id": f"AUD-{len(self.data['audits']) + 1:03d}",
            "name": name,
            "description": description,
            "date": date,
            "auditor": auditor,
            "findings": findings,
            "recommendations": recommendations,
            "status": "Completed"
        }
        
        self.data["audits"].append(audit)
        self.save_data()
        return audit["id"]
    
    def calculate_risk_level(self, likelihood, impact):
        """Calculate risk level based on likelihood and impact"""
        risk_matrix = {
            "High": {"High": "Critical", "Medium": "High", "Low": "Medium"},
            "Medium": {"High": "High", "Medium": "Medium", "Low": "Low"},
            "Low": {"High": "Medium", "Medium": "Low", "Low": "Very Low"}
        }
        
        return risk_matrix.get(likelihood, {}).get(impact, "Unknown")
    
    def list_policies(self):
        """List all policies"""
        return self.data["policies"]
    
    def list_controls(self):
        """List all controls"""
        return self.data["controls"]
    
    def list_risks(self):
        """List all risks"""
        return self.data["risks"]
    
    def list_incidents(self):
        """List all incidents"""
        return self.data["incidents"]
    
    def list_metrics(self):
        """List all metrics"""
        return self.data["metrics"]
    
    def list_audits(self):
        """List all audits"""
        return self.data["audits"]
    
    def generate_dashboard(self):
        """Generate a security governance dashboard"""
        dashboard = {
            "generated_date": datetime.datetime.now().isoformat(),
            "summary": {
                "policies": len(self.data["policies"]),
                "controls": len(self.data["controls"]),
                "risks": len(self.data["risks"]),
                "incidents": len(self.data["incidents"]),
                "metrics": len(self.data["metrics"]),
                "audits": len(self.data["audits"])
            },
            "risk_summary": {
                "critical": sum(1 for r in self.data["risks"] if r["risk_level"] == "Critical"),
                "high": sum(1 for r in self.data["risks"] if r["risk_level"] == "High"),
                "medium": sum(1 for r in self.data["risks"] if r["risk_level"] == "Medium"),
                "low": sum(1 for r in self.data["risks"] if r["risk_level"] == "Low"),
                "very_low": sum(1 for r in self.data["risks"] if r["risk_level"] == "Very Low")
            },
            "incident_summary": {
                "critical": sum(1 for i in self.data["incidents"] if i["severity"] == "Critical"),
                "high": sum(1 for i in self.data["incidents"] if i["severity"] == "High"),
                "medium": sum(1 for i in self.data["incidents"] if i["severity"] == "Medium"),
                "low": sum(1 for i in self.data["incidents"] if i["severity"] == "Low")
            },
            "metrics_summary": [
                {
                    "name": m["name"],
                    "target": m["target"],
                    "actual": m["actual"],
                    "status": "Green" if m["actual"] >= m["target"] else "Red"
                }
                for m in self.data["metrics"]
            ]
        }
        
        return dashboard

def main():
    parser = argparse.ArgumentParser(description="Security Governance Tracker")
    parser.add_argument("--add-policy", action="store_true", help="Add a security policy")
    parser.add_argument("--add-control", action="store_true", help="Add a security control")
    parser.add_argument("--add-risk", action="store_true", help="Add a security risk")
    parser.add_argument("--add-incident", action="store_true", help="Add a security incident")
    parser.add_argument("--add-metric", action="store_true", help="Add a security metric")
    parser.add_argument("--add-audit", action="store_true", help="Add a security audit")
    parser.add_argument("--list-policies", action="store_true", help="List all policies")
    parser.add_argument("--list-controls", action="store_true", help="List all controls")
    parser.add_argument("--list-risks", action="store_true", help="List all risks")
    parser.add_argument("--list-incidents", action="store_true", help="List all incidents")
    parser.add_argument("--list-metrics", action="store_true", help="List all metrics")
    parser.add_argument("--list-audits", action="store_true", help="List all audits")
    parser.add_argument("--dashboard", action="store_true", help="Generate a security governance dashboard")
    
    args = parser.parse_args()
    
    tracker = GovernanceTracker()
    
    if args.add_policy:
        name = input("Policy Name: ")
        description = input("Description: ")
        owner = input("Owner: ")
        approval_date = input("Approval Date (YYYY-MM-DD): ")
        review_date = input("Review Date (YYYY-MM-DD): ")
        
        policy_id = tracker.add_policy(name, description, owner, approval_date, review_date)
        print(f"Policy added with ID: {policy_id}")
    
    elif args.add_control:
        name = input("Control Name: ")
        description = input("Description: ")
        policy_id = input("Policy ID: ")
        owner = input("Owner: ")
        implementation_date = input("Implementation Date (YYYY-MM-DD): ")
        
        control_id = tracker.add_control(name, description, policy_id, owner, implementation_date)
        print(f"Control added with ID: {control_id}")
    
    elif args.add_risk:
        name = input("Risk Name: ")
        description = input("Description: ")
        likelihood = input("Likelihood (High/Medium/Low): ")
        impact = input("Impact (High/Medium/Low): ")
        owner = input("Owner: ")
        mitigation_plan = input("Mitigation Plan: ")
        
        risk_id = tracker.add_risk(name, description, likelihood, impact, owner, mitigation_plan)
        print(f"Risk added with ID: {risk_id}")
    
    elif args.add_incident:
        name = input("Incident Name: ")
        description = input("Description: ")
        date = input("Date (YYYY-MM-DD): ")
        severity = input("Severity (Critical/High/Medium/Low): ")
        affected_systems = input("Affected Systems: ")
        root_cause = input("Root Cause: ")
        resolution = input("Resolution: ")
        
        incident_id = tracker.add_incident(name, description, date, severity, affected_systems, root_cause, resolution)
        print(f"Incident added with ID: {incident_id}")
    
    elif args.add_metric:
        name = input("Metric Name: ")
        description = input("Description: ")
        target = float(input("Target Value: "))
        actual = float(input("Actual Value: "))
        period = input("Period (e.g., 'May 2023'): ")
        trend = input("Trend (Improving/Stable/Declining): ")
        
        metric_id = tracker.add_metric(name, description, target, actual, period, trend)
        print(f"Metric added with ID: {metric_id}")
    
    elif args.add_audit:
        name = input("Audit Name: ")
        description = input("Description: ")
        date = input("Date (YYYY-MM-DD): ")
        auditor = input("Auditor: ")
        findings = input("Findings: ")
        recommendations = input("Recommendations: ")
        
        audit_id = tracker.add_audit(name, description, date, auditor, findings, recommendations)
        print(f"Audit added with ID: {audit_id}")
    
    elif args.list_policies:
        policies = tracker.list_policies()
        print(json.dumps(policies, indent=2))
    
    elif args.list_controls:
        controls = tracker.list_controls()
        print(json.dumps(controls, indent=2))
    
    elif args.list_risks:
        risks = tracker.list_risks()
        print(json.dumps(risks, indent=2))
    
    elif args.list_incidents:
        incidents = tracker.list_incidents()
        print(json.dumps(incidents, indent=2))
    
    elif args.list_metrics:
        metrics = tracker.list_metrics()
        print(json.dumps(metrics, indent=2))
    
    elif args.list_audits:
        audits = tracker.list_audits()
        print(json.dumps(audits, indent=2))
    
    elif args.dashboard:
        dashboard = tracker.generate_dashboard()
        print(json.dumps(dashboard, indent=2))
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
