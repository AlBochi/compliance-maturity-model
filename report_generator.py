import matplotlib.pyplot as plt
import yaml
from maturity_scorer import ComplianceMaturityScorer

def generate_maturity_report(assessment_results, company_name):
    # Radar chart
    domains = list(assessment_results['domain_breakdown'].keys())
    scores = [v['score'] for v in assessment_results['domain_breakdown'].values()]
    
    # Complete the loop for radar chart
    domains += [domains[0]]
    scores += [scores[0]]
    
    angles = [n / float(len(domains)) * 2 * 3.14159 for n in range(len(domains))]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.plot(angles, scores, linewidth=2)
    ax.fill(angles, scores, 'skyblue', alpha=0.4)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(domains[:-1])
    ax.set_title(f"{company_name} Compliance Maturity Radar", size=16)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20%", "40%", "60%", "80%", "100%"])

    plt.savefig(f"{company_name}_maturity_radar.png")
    print(f"Radar chart saved: {company_name}_maturity_radar.png")

# Usage
if __name__ == "__main__":
    scorer = ComplianceMaturityScorer("framework.yaml")
    client_data = {
        "Compliance policy documented": 3,
        "Risk assessment process": 2,
        "Infrastructure as Code": 4,
        "Data Protection": 3,
        "Compliance monitoring": 2,
        "Audit readiness": 4,
        "Training & Awareness": 1
    }
    results = scorer.calculate_score(client_data)
    generate_maturity_report(results, "AcmeCorp")
