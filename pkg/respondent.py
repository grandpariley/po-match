from pkg.parse import parse_risk_tolerance, parse_environment_tolerance, parse_social_tolerance, \
    parse_governance_tolerance


def parse(d):
    return Respondent(parse_risk_tolerance(d['risk']),
                      parse_environment_tolerance(d['short'], d['long']),
                      parse_social_tolerance(d['short'], d['long']),
                      parse_governance_tolerance(d['short'], d['long']))


class Respondent:
    def __init__(self, risk_tolerance, environment, social, governance):
        self.risk_tolerance = risk_tolerance
        self.environment = environment
        self.social = social
        self.governance = governance
