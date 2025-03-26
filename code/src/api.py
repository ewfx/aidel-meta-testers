from fastapi import FastAPI
from entity_extraction import extract_entities
from data_enrichment import fetch_company_details, check_sanctions_list
from risk_analysis import calculate_risk

app = FastAPI()

@app.get("/analyze/")
def analyze_entity(transaction_text: str):
    """
    API endpoint that processes transaction text, extracts entities, enriches data, and assigns risk scores.
    """
    extracted_entities = extract_entities(transaction_text)
    analysis_results = []

    for entity in extracted_entities:
        entity_data = fetch_company_details(entity)
        
        # Mock enrichment if API fails
        if not entity_data:
            entity_data = {"name": entity, "company_type": "Unknown", "jurisdiction": "Unknown"}
        
        # Check if in sanctions list
        entity_data["sanctions"] = check_sanctions_list(entity)

        # Compute risk score
        risk_analysis = calculate_risk(entity_data)

        # Build response
        analysis_results.append({
            "entity": entity,
            "company_data": entity_data,
            "risk_analysis": risk_analysis
        })

    return {"results": analysis_results}

# Run the API server
# Use: uvicorn src.api:app --reload
