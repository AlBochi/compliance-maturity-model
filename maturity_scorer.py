import yaml
import json

class ComplianceMaturityScorer:
    def __init__(self, framework_file):
        with open(framework_file) as f:
            self.framework = yaml.safe_load(f)

    def calculate_score(self, assessment_data):
        domain_scores = {}
        total_score = 0

        for domain in self.framework['domains']:
            domain_score = 0
            max_domain_score = len(domain['criteria']) * 4

            for criterion in domain['criteria']:
                user_level = assessment_data.get(criterion['control'], 1)
                domain_score += min(user_level, 4)

            domain_pct = domain_score / max_domain_score * 100
            weight_pct = float(domain['weight'].strip('%'))
            weighted_score = domain_pct * (weight_pct / 100)

            domain_scores[domain['name']] = {
                'score': domain_pct,
                'weight': weight_pct
            }

            total_score += weighted_score

        return {
            'overall_score': round(total_score, 2),
            'domain_breakdown': domain_scores
        }

# Sample run
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

    result = scorer.calculate_score(client_data)
    print(json.dumps(result, indent=2))
