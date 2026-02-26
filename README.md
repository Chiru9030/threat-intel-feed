# Decentralized Threat Intel Feed

A proactive Blue Team utility that aggregates Common Vulnerabilities and Exposures (CVEs) and packages them into structured JSON (STIX-like format) for ingestion by SIEMs like Splunk or Elastic Security.

## Features
- **Data Aggregation**: Mocks fetching daily zero-day intel.
- **SIEM Ready**: Outputs data in a standardized JSON wrapper for immediate pipeline ingestion.

## Setup
```bash
pip install -r requirements.txt
python feed.py
```
