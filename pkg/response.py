from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict


class RiskSurvey(BaseModel):
    r1: Optional[str] = None
    r10: Optional[str] = None
    r2: Optional[str] = None
    r3: Optional[str] = None
    r4: Optional[str] = None
    r5: Optional[str] = None
    r6: Optional[str] = None
    r7: Optional[str] = None
    r8: Optional[str] = None
    r9: Optional[str] = None
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class ShortSurvey(BaseModel):
    q1: Optional[str] = None
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class LongSurvey(BaseModel):
    q2: Optional[str] = None
    q3: List[Optional[int]] = None
    q4a: Optional[int] = None
    q4b: Optional[int] = None
    q4c: Optional[int] = None
    q5: Optional[str] = None
    q6: List[Optional[int]] = None
    q7: List[Optional[int]] = None
    q8: List[Optional[int]] = None
    q9: Optional[str] = None
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class Response(BaseModel):
    id: Optional[str] = Field(alias="_id", default=None)
    risk: Optional[RiskSurvey] = None
    short: Optional[ShortSurvey] = None
    long: Optional[LongSurvey] = None
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


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
    return -2


def parse_risk_tolerance(risk):
    if not risk:
        return None
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
    if not short:
        return None
    if short['q1'] != "A" or not long:
        return 0
    score = 0
    score += sum([1.00 if i is not None else 0 for i in long['q3']]) / float(len(long['q3']))
    if long['q4a']:
        score += long['q4a'] / 100.00
    if long['q5'] != 'A':
        return score
    score += sum([1.00 if i is not None else 0 for i in long['q6']]) / float(len(long['q6']))
    return score


def parse_social_tolerance(short, long):
    if not short:
        return None
    if short['q1'] != "A" or not long:
        return 0
    score = 0
    score += sum([1.00 if i is not None else 0 for i in long['q3']]) / float(len(long['q3']))
    if long['q4b']:
        score += long['q4b'] / 100.00
    if long['q5'] != 'A':
        return score
    score += sum([1.00 if i is not None else 0 for i in long['q7']]) / float(len(long['q7']))
    return score


def parse_governance_tolerance(short, long):
    if not short:
        return None
    if short['q1'] != "A" or not long:
        return 0
    score = 0
    score += sum([1 if i is not None else 0 for i in long['q3']]) / float(len(long['q3']))
    if long['q4c']:
        score += long['q4c'] / 100.00
    if long['q5'] != 'A':
        return score
    score += sum([1 if i is not None else 0 for i in long['q8']]) / float(len(long['q8']))
    return score


def parse(d):
    return {
        "portfolio_id": str(d['_id']),
        "risk_tolerance": parse_risk_tolerance(d['risk']),
        "environment": parse_environment_tolerance(d['short'], d['long']),
        "social": parse_social_tolerance(d['short'], d['long']),
        "governance": parse_governance_tolerance(d['short'], d['long'])
    }
