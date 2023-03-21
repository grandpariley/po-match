def get_numeric_risk(r, num_answers):
    if r == 'A':
        return -2
    if r == 'B':
        return -1
    if num_answers % 2 == 0:
        if r == 'C':
            return 1
        if r == 'D':
            return 2
    else:
        if r == 'C':
            return 0
        if r == 'D':
            return 1
        if r == 'E':
            return 2


def parse_risk_tolerance(risk):
    score = 0
    score += get_numeric_risk(risk['r1'], 5)
    score += get_numeric_risk(risk['r2'], 4)
    score += get_numeric_risk(risk['r3'], 5)
    score += get_numeric_risk(risk['r4'], 5)
    score += get_numeric_risk(risk['r5'], 4)
    score += get_numeric_risk(risk['r6'], 5)
    score += get_numeric_risk(risk['r7'], 4)
    score += get_numeric_risk(risk['r8'], 5)
    score += get_numeric_risk(risk['r9'], 5)
    score += get_numeric_risk(risk['r10'], 5)
    return score


def parse_environment_tolerance(short, long):
    if short['q1'] != "A" or long is None:
        return 0
    score = 0
    score += sum([1.00 if i is not None else 0 for i in long['q3']]) / float(len(long['q3']))
    score += long['q4a'] / 100.00
    if long['q5'] != 'A':
        return score
    score += sum([1.00 if i is not None else 0 for i in long['q6']]) / float(len(long['q6']))
    return score


def parse_social_tolerance(short, long):
    if short['q1'] != "A" or long is None:
        return 0
    score = 0
    score += sum([1.00 if i is not None else 0 for i in long['q3']]) / float(len(long['q3']))
    score += long['q4b'] / 100.00
    if long['q5'] != 'A':
        return score
    score += sum([1.00 if i is not None else 0 for i in long['q7']]) / float(len(long['q7']))
    return score


def parse_governance_tolerance(short, long):
    if short['q1'] != "A" or long is None:
        return 0
    score = 0
    score += sum([1 if i is not None else 0 for i in long['q3']]) / float(len(long['q3']))
    score += long['q4c'] / 100.00
    if long['q5'] != 'A':
        return score
    score += sum([1 if i is not None else 0 for i in long['q8']]) / float(len(long['q8']))
    return score
