from pkg.parse import parse_risk_tolerance, parse_environment_tolerance, parse_social_tolerance, \
    parse_governance_tolerance


class Respondent:
    def __init__(self, d):
        self.risk_tolerance = parse_risk_tolerance(d.risk)
        self.environment = parse_environment_tolerance(d.short, d.long)
        self.social = parse_social_tolerance(d. short, d.long)
        self.governance = parse_governance_tolerance(d.short, d.long)
