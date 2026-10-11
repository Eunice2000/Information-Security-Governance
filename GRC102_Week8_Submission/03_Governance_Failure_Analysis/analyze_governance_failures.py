#!/usr/bin/env python3

import os
import sys
import json
import datetime

def load_vulnerability_report():
    """Load the latest vulnerability report"""
    report_files = [f for f in os.listdir(".") if f.startswith("vulnerability_report_") and f.endswith(".json")]
    
    if not report_files:
        print("No vulnerability reports found")
        return None
    
    latest_report = max(report_files)
    
    with open(latest_report, "r") as f:
        return json.load(f)

def load_attack_log():
    """Load the attack log"""
    if not os.path.exists("attack_log.json"):
        print("No attack log found")
        return None
    
    with open("attack_log.json", "r") as f:
        return json.load(f)

def load_governance_data():
    """Load governance data"""
    if not os.path.exists("governance_data.json"):
        print("No governance data found")
        return None
    
    with open("governance_data.json", "r") as f:
        return json.load(f)

def load_patch_status():
    """Load patch status"""
    if not os.path.exists("patch_status.json"):
        return {"struts_patched": False, "mysql_secured": False, "network_segmented": False}
    
    with open("patch_status.json", "r") as f:
        return json.load(f)

def analyze_governance_failures():
    """Analyze security governance failures"""
    vulnerability_report = load_vulnerability_report()
    attack_log = load_attack_log()
    governance_data = load_governance_data()
    patch_status = load_patch_status()
    
    failures = []
    
    # Check for patch management failures
    if vulnerability_report:
        for vuln in vulnerability_report["vulnerabilities"]:
            if vuln.get("vulnerable", False) and vuln.get("severity") in ["Critical", "High"]:
                failures.append({
                    "category": "Patch Management",
                    "description": f"Unpatched {vuln['vulnerability']} with {vuln['severity']} severity",
                    "impact": "System vulnerable to exploitation",
                    "recommendation": vuln["remediation"]
                })
    
    # Check for attack success
    if attack_log and attack_log.get("success", False):
        failures.append({
            "category": "Incident Detection",
            "description": f"Successful {attack_log['attack_type']} attack not detected",
            "impact": f"Unauthorized access to {attack_log['data_accessed']}",
            "recommendation": "Implement real-time security monitoring and alerting"
        })
    
    # Check for governance process failures
    if governance_data:
        # Check patch policy implementation
        patch_policies = [p for p in governance_data["policies"] if "patch" in p["name"].lower()]
        if patch_policies and not patch_status.get("struts_patched", False):
            failures.append({
                "category": "Policy Implementation",
                "description": "Patch Management Policy not effectively implemented",
                "impact": "Critical vulnerabilities remain unpatched despite policy",
                "recommendation": "Improve patch management process and oversight"
            })
        
        # Check vulnerability management
        vuln_policies = [p for p in governance_data["policies"] if "vulnerabilit" in p["name"].lower()]
        if vuln_policies and vulnerability_report and vulnerability_report["summary"]["critical"] > 0:
            failures.append({
                "category": "Vulnerability Management",
                "description": "Vulnerability Management Policy not effectively implemented",
                "impact": "Critical vulnerabilities not remediated in a timely manner",
                "recommendation": "Improve vulnerability management process and oversight"
            })
        
        # Check metrics effectiveness
        metrics = governance_data.get("metrics", [])
        patch_metrics = [m for m in metrics if "patch" in m["name"].lower()]
        if patch_metrics and not patch_status.get("struts_patched", False):
            failures.append({
                "category": "Metrics and Measurement",
                "description": "Security metrics not driving effective remediation",
                "impact": "Metrics not leading to security improvements",
                "recommendation": "Implement actionable metrics with clear ownership and accountability"
            })
    
    # Check for network segmentation failures
    if not patch_status.get("network_segmented", False):
        failures.append({
            "category": "Security Architecture",
            "description": "Insufficient network segmentation",
            "impact": "Potential for lateral movement and expanded compromise",
            "recommendation": "Implement network segmentation according to least privilege principle"
        })
    
    # Check for authentication failures
    if not patch_status.get("mysql_secured", False):
        failures.append({
            "category": "Authentication and Access Control",
            "description": "Weak database authentication",
            "impact": "Potential for unauthorized database access",
            "recommendation": "Implement strong authentication and access controls for databases"
        })
    
    return failures

def generate_report(failures):
    """Generate a governance failure analysis report"""
    report = {
        "timestamp": datetime.datetime.now().isoformat(),
        "failures": failures,
        "summary": {
            "total_failures": len(failures),
            "categories": {}
        }
    }
    
    # Count failures by category
    for failure in failures:
        category = failure["category"]
        if category in report["summary"]["categories"]:
            report["summary"]["categories"][category] += 1
        else:
            report["summary"]["categories"][category] = 1
    
    return report

def main():
    failures = analyze_governance_failures()
    report = generate_report(failures)
    
    report_file = f"governance_failure_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"Governance failure analysis completed. Report saved to {report_file}")
    print(f"Summary: {report['summary']['total_failures']} governance failures identified")
    
    for category, count in report["summary"]["categories"].items():
        print(f"  {category}: {count}")

if __name__ == "__main__":
    main()
