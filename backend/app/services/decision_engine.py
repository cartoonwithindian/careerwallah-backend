from typing import List, Dict, Any
from datetime import date


class EligibilityResult:
    def __init__(self, state: str, reasons: List[str] = None, unknowns: List[str] = None):
        self.state = state  # eligible|potentially_eligible|not_eligible
        self.reasons = reasons or []
        self.unknowns = unknowns or []


def check_eligibility(student: Dict[str, Any], opportunity: Dict[str, Any]) -> EligibilityResult:
    reasons = []
    unknowns = []
    blockers = []

    # Education
    if opportunity.get("education_requirements"):
        if not student.get("education_level"):
            unknowns.append("education_level not specified by student")
        else:
            reasons.append(f"Education level provided: {student.get('education_level')}")

    # Budget
    student_budget = student.get("budget")
    cost = opportunity.get("cost_or_stipend", "")
    if cost and any(k in cost.lower() for k in ["fee", "paid", "cost"]):
        if student_budget is None:
            unknowns.append("budget constraints unknown")
        elif student_budget >= 0:  # be conservative
            reasons.append("Budget info available for consideration")

    # Device/internet
    if opportunity.get("device_requirements") and opportunity.get("device_requirements") != "Provided at center":
        if not student.get("device_access"):
            unknowns.append("device access unknown")
        else:
            reasons.append(f"Device access: {student.get('device_access')}")

    if opportunity.get("internet_requirements") and opportunity.get("internet_requirements") != "Provided at center":
        if not student.get("internet_access"):
            unknowns.append("internet access unknown")
        else:
            reasons.append(f"Internet access: {student.get('internet_access')}")

    # Deadline
    if opportunity.get("application_deadline"):
        try:
            dl = opportunity["application_deadline"]
            if isinstance(dl, str):
                dl = date.fromisoformat(dl)
            if dl < date.today():
                blockers.append("Application deadline has passed")
        except Exception:
            unknowns.append("deadline could not be parsed")

    if blockers:
        return EligibilityResult(state="not_eligible", reasons=reasons, unknowns=unknowns)

    if unknowns:
        return EligibilityResult(state="potentially_eligible", reasons=reasons, unknowns=unknowns)

    return EligibilityResult(state="eligible", reasons=reasons + ["No known blockers based on available data"], unknowns=[])
