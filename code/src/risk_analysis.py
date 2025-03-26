def calculate_risk(entity_data):
    """
    Calculates risk score based on company attributes.
    """
    risk_score = 0
    risk_reasons = []

    if "sanctions" in entity_data and entity_data["sanctions"]:
        risk_score += 50
        risk_reasons.append("Entity is in a sanctions list")

    if entity_data.get("company_type", "").lower() in ["shell", "offshore"]:
        risk_score += 30
        risk_reasons.append("Possible shell company")

    if entity_data.get("jurisdiction", "").lower() in ["cayman islands", "panama"]:
        risk_score += 20
        risk_reasons.append("Registered in a high-risk jurisdiction")

    return {
        "risk_score": risk_score,
        "risk_reasons": risk_reasons
    }

# Example usage
if __name__ == "__main__":
    sample_entity = {"sanctions": True, "company_type": "Shell", "jurisdiction": "Cayman Islands"}
    print(calculate_risk(sample_entity))
