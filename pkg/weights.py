OBJECTIVES = ['risk_tolerance', 'environment', 'social', 'governance']


def response_to_weight(response, extremes):
    risk_tolerance = (response['risk_tolerance'] - extremes['risk_tolerance']['min']) / (
            extremes['risk_tolerance']['max'] - extremes['risk_tolerance']['min']) / 4
    environment = (response['environment'] - extremes['environment']['min']) / (
            extremes['environment']['max'] - extremes['environment']['min']) / 4
    social = (response['social'] - extremes['social']['min']) / (
            extremes['social']['max'] - extremes['social']['min']) / 4
    governance = (response['governance'] - extremes['governance']['min']) / (
            extremes['governance']['max'] - extremes['governance']['min']) / 4
    ret = 1 - (risk_tolerance + environment + social + governance)
    return {
        "portfolio_id": response['portfolio_id'],
        "var": risk_tolerance / 2,
        "cvar": risk_tolerance / 2,
        "return": ret,
        "environment": environment,
        "social": social,
        "governance": governance
    }


def get_weights(responses):
    extremes = dict()
    for o in OBJECTIVES:
        extremes[o] = {
            'max': None,
            'min': None
        }
        extremes[o]['max'] = max([response[o] for response in responses])
        extremes[o]['min'] = min([response[o] for response in responses])
    weights = [response_to_weight(response, extremes) for response in responses]
    return weights
