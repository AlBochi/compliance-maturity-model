# report_generator.py
import matplotlib.pyplot as plt
import numpy as np

def generate_maturity_radar(assessment_results, company_name):
    domains = list(assessment_results['domain_breakdown'].keys())
    scores = [v['score'] for v in assessment_results['domain_breakdown'].values()]

    # Radar chart setup
    angles = np.linspace(0, 2 * np.pi, len(domains), endpoint=False).tolist()
    scores += scores[:1]  # close the radar chart
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.plot(angles, scores, linewidth=2)
    ax.fill(angles, scores, alpha=0.25)

    ax.set_thetagrids(np.degrees(angles[:-1]), domains)
    ax.set_title(f"{company_name} - Compliance Maturity Radar", size=16)
    ax.set_ylim(0, 100)

    plt.savefig("maturity_radar.png")
    print("✅ Saved radar chart as maturity_radar.png")

if __name__ == "__main__":
    # Example data from maturity_scorer.py
    sample_results = {
        "overall_score": 71.88,
        "domain_breakdown": {
            "Policy & Governance": {"score": 62.5, "weight": 25.0},
            "Technical Controls": {"score": 87.5, "weight": 40.0},
            "Monitoring & Evidence": {"score": 75.0, "weight": 25.0},
            "Organization & Process": {"score": 25.0, "weight": 10.0}
        }
    }

    generate_maturity_radar(sample_results, "Saillent")
