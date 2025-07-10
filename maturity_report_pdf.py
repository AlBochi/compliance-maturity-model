from fpdf import FPDF
import json
from datetime import datetime

class MaturityPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Compliance Maturity Assessment - Saillent', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Report generated on {datetime.today().strftime("%Y-%m-%d")}', 0, 0, 'C')

    def add_overview(self, score):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, f"Overall Compliance Maturity Score: {score:.2f}%\n")

    def add_domain_breakdown(self, breakdown):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Domain Breakdown:', ln=True)
        self.set_font('Arial', '', 12)
        for domain, data in breakdown.items():
            self.cell(0, 10, f"{domain}: {data['score']:.1f}% (Weight: {data['weight']}%)", ln=True)

    def add_chart(self, chart_path):
        self.image(chart_path, x=30, w=150)
        self.ln(10)

    def add_recommendation(self, score):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Recommendations:', ln=True)
        self.set_font('Arial', '', 12)
        if score < 40:
            self.multi_cell(0, 10, " Critical: Implement foundational compliance controls.")
        elif score < 70:
            self.multi_cell(0, 10, " Moderate: Strengthen control automation and monitoring.")
        else:
            self.multi_cell(0, 10, " Strong: Focus on continuous optimization and threat modeling.")

def generate_pdf_report(results_file='maturity_radar.png', output='compliance_maturity_report.pdf'):
    results = {
        "overall_score": 71.88,
        "domain_breakdown": {
            "Policy & Governance": {"score": 62.5, "weight": 25.0},
            "Technical Controls": {"score": 87.5, "weight": 40.0},
            "Monitoring & Evidence": {"score": 75.0, "weight": 25.0},
            "Organization & Process": {"score": 25.0, "weight": 10.0}
        }
    }

    pdf = MaturityPDF()
    pdf.add_page()
    pdf.add_overview(results['overall_score'])
    pdf.add_domain_breakdown(results['domain_breakdown'])
    pdf.add_chart(results_file)
    pdf.add_recommendation(results['overall_score'])
    pdf.output(output)
    print(f" PDF report generated: {output}")

if __name__ == "__main__":
    generate_pdf_report()
