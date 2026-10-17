from typing import List, Dict, Any
from app.services.decision_engine import check_eligibility


def compute_suitability(student: Dict[str, Any], opportunity: Dict[str, Any]) -> Dict[str, Any]:
    score = 0.5  # baseline
    explanations = ["Baseline suitability based on available data"]

    student_interests = set((student.get("interests") or []))
    student_skills = set(s.get("skill") if isinstance(s, dict) else s for s in (student.get("skills") or []))
    req_skills = set(opportunity.get("required_skills") or [])
    pref_skills = set(opportunity.get("preferred_skills") or [])
    cat = (opportunity.get("category") or "").lower()

    if student_interests and cat and any(i.lower() in cat for i in student_interests if isinstance(i, str)):
        score += 0.15
        explanations.append("Category aligns with stated interests")

    overlap_req = len(student_skills & req_skills)
    if req_skills and overlap_req > 0:
        score += min(0.2, 0.05 * overlap_req)
        explanations.append(f"Matches {overlap_req} required skill(s)")

    overlap_pref = len(student_skills & pref_skills)
    if pref_skills and overlap_pref > 0:
        score += min(0.1, 0.03 * overlap_pref)
        explanations.append(f"Matches {overlap_pref} preferred skill(s)")

    # Learning accessibility boost
    if opportunity.get("mode") == "offline" or opportunity.get("cost_or_stipend") == "Free":
        score += 0.05
        explanations.append("Accessible format/cost")

    score = min(1.0, max(0.0, round(score, 2)))

    # Skill gaps
    gaps = sorted(list(req_skills - student_skills))
    has = sorted(list(student_skills & (req_skills | pref_skills)))

    return {
        "suitability_score": score,
        "explanations": explanations,
        "matching_skills": has,
        "skill_gaps": gaps,
    }


def recommend(student: Dict[str, Any], opportunities: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    results = []
    for opp in opportunities:
        elig = check_eligibility(student, opp)
        suit = compute_suitability(student, opp)
        results.append({
            "opportunity_id": opp.get("id") or opp.get("external_id"),
            "title": opp.get("title"),
            "category": opp.get("category"),
            "eligibility_state": elig.state,
            "eligibility_reasons": elig.reasons,
            "eligibility_unknowns": elig.unknowns,
            "suitability_score": suit["suitability_score"],
            "explanation": "; ".join(suit["explanations"]),
            "matching_interests": [],
            "matching_skills": suit["matching_skills"],
            "skill_gaps": suit["skill_gaps"],
            "known_constraints": [],
            "official_source_url": opp.get("official_source_url"),
            "application_url": opp.get("application_url"),
            "deadline": opp.get("application_deadline"),
            "verification_status": opp.get("verification_status"),
            "last_verified": opp.get("last_verified"),
        })
    results.sort(key=lambda x: (x["eligibility_state"] != "eligible", -x["suitability_score"]))
    return results
