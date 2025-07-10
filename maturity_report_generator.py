import matplotlib.pyplot as plt

def generate_maturity_radar(results: dict, company_name: str = "Saillent"):
    domains = list(results['domain_breakdown'].keys())
    scores = [v['score'] for v in results['domain_breakdown'].values()]

    angles = [n / float(len(domains)) * 2 * 3.1415926 for n in range(len(domains))]
    scores += scores[:1]  # close the radar loop
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, scores, linewidth=2)
    ax.fill(angles, scores, alpha=0.25)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(domains)
    ax.set_title(f"{company_name} Compliance Maturity Radar", size=14)
    ax.set_yticklabels(['0', '20', '40', '60', '80', '100'])

    fig.savefig("maturity_radar.png")
    print("✅ Radar chart saved as maturity_radar.png")

if __name__ == "__main__":
    # Example from previous results
    sample_results = {
        "overall_score": 71.88,
        "domain_breakdown": {
            "Policy & Governance": {"score": 62.5, "weight": 25.0},
            "Technical Controls": {"score": 87.5, "weight": 40.0},
            "Monitoring & Evidence": {"score": 75.0, "weight": 25.0},
            "Organization & Process": {"score": 25.0, "weight": 10.0}
        }
    }

    generate_maturity_radar(sample_results, company_name="Saillent")
