# Cloud Compliance Maturity Assessment Framework

## Overview
This project provides a strategic framework and scoring engine to assess cloud compliance maturity for organizations. It helps security leaders understand their current compliance posture and guides them on prioritized improvements.

## What We Built
- **Assessment Framework**: Defined maturity levels across four domains: Policy & Governance, Technical Controls, Monitoring & Evidence, and Organization & Process.
- **Automated Scoring Engine**: Python script (maturity_scorer.py) that calculates weighted compliance scores based on client input.
- **Executive Reports**: Generates visual radar charts and PDF reports summarizing maturity scores and actionable recommendations.
- **Roadmap Generator**: Suggests prioritized next steps for improving compliance maturity.

## How to Use
1. Clone this repo.
2. Create and activate a Python virtual environment:
   \`\`\`
   python3 -m venv venv
   source venv/bin/activate
   \`\`\`
3. Install dependencies:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`
4. Run the scorer with your assessment data:
   \`\`\`
   python3 maturity_scorer.py
   \`\`\`
5. Generate reports:
   \`\`\`
   python3 maturity_report_generator.py
   python3 maturity_report_pdf.py
   \`\`\`
6. View outputs: radar chart (maturity_radar.png) and PDF report (compliance_maturity_report.pdf).

## Why It Matters
- Provides a **business-focused view** of cloud compliance posture.
- Helps CISOs answer the key question: *"Where do we stand, and what’s next?"*
- Serves as a **foundation for consulting engagements**, audits, and compliance roadmaps.

## Next Steps (optional)
- Integrate automated data collectors for live scanning.
- Enhance PDF report styling.
- Build a web UI for interactive assessments.
- Add multi-framework support (SOC 2, ISO 27001, HIPAA, etc.)

## Maintainer
Al Bochi — Cloud Security Compliance Auditor

---
