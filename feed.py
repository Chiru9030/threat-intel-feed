import requests
import json
import time
from datetime import datetime

class ThreatIntelFeed:
    def __init__(self):
        # We use a public summary of NVD or similar mock endpoint for the MVP
        self.api_url = "https://cveawg.mitre.org/api/cve/"
        self.feed_data = []

    def fetch_latest_cves(self, limit=5):
        print(f"[*] Fetching latest threat intel...")
        # Mocking the fetch process for the MVP to ensure it runs without API keys
        mock_cves = [
            {"id": "CVE-2024-1234", "severity": "HIGH", "description": "RCE in popular web framework"},
            {"id": "CVE-2024-5678", "severity": "CRITICAL", "description": "Auth bypass in Zero-Trust Proxy"},
            {"id": "CVE-2024-9012", "severity": "MEDIUM", "description": "XSS in Dashboard UI"}
        ]
        
        for cve in mock_cves:
            cve['timestamp'] = datetime.utcnow().isoformat()
            self.feed_data.append(cve)
            
    def export_stix_format(self, filename="intel_feed.json"):
        # Exporting in a simplified STIX-like format
        stix_wrapper = {
            "type": "bundle",
            "id": f"bundle--{int(time.time())}",
            "objects": self.feed_data
        }
        with open(filename, 'w') as f:
            json.dump(stix_wrapper, f, indent=4)
        print(f"[+] Successfully exported {len(self.feed_data)} indicators to {filename}")

if __name__ == "__main__":
    feed = ThreatIntelFeed()
    feed.fetch_latest_cves()
    feed.export_stix_format()
