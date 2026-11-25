# Threat Intel Feed Aggregator

A Python script designed to automatically fetch, aggregate, and export the latest cybersecurity threat intelligence (like CVEs) into a structured format for consumption by SIEMs or firewalls.

## 📖 Complete Brief
Threat Intel is crucial for preemptively blocking attacks. This project acts as an automated pipeline that pulls the latest vulnerabilities (Common Vulnerabilities and Exposures - CVEs) from public databases. Instead of security analysts manually checking for new threats, this script mimics the process of querying an upstream API, aggregating the data, and standardizing it into a simplified STIX-like (Structured Threat Information Expression) JSON format. This standardized `.json` export can then be automatically ingested by defensive tools (like the Network Anomaly IDS from this portfolio) to update blocklists dynamically.

## ✨ Features
- **Automated Aggregation:** Script can be set on a cron-job to continually pull the latest threat data.
- **STIX-Like Formatting:** Converts raw vulnerability data into a structured bundle recognized across the cybersecurity industry.
- **Self-Contained MVP:** Uses an internal mock dataset to demonstrate functionality without requiring the user to register for third-party API keys right out of the box.

## 🛠 Prerequisites
- Python 3.x
- `requests`

## 🚀 How to Run

1. **Navigate to the feed directory:**
   ```bash
   cd ./threat-intel-feed/
   ```

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```
   *(Alternatively: `pip install requests`)*

3. **Run the feed aggregator:**
   ```bash
   python3 feed.py
   ```

4. **Expected Output:**
   The script will simulate fetching the latest high and critical severity CVEs, parse them, and generate a new `intel_feed.json` file in the same directory:
   ```text
   [*] Fetching latest threat intel...
   [+] Successfully exported 3 indicators to intel_feed.json
   ```
   You can cat the generated file to see the STIX-formatted output.
