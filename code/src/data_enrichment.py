import requests

def fetch_company_details(entity_name):
    """
    Fetches company details from OpenCorporates API.
    """
    url = f"https://api.opencorporates.com/v0.4/companies/search?q={entity_name}"
    try:
        response = requests.get(url)
        data = response.json()
        if data['results']['companies']:
            return data['results']['companies'][0]['company']
    except Exception as e:
        print(f"Error fetching data for {entity_name}: {e}")
    return None

def check_sanctions_list(entity_name):
    """
    Checks if the entity is in the OFAC sanctions list.
    """
    # Mock implementation (replace with actual API calls)
    sanctions_list = ["XYZ Holdings", "ABC Shell Ltd"]
    return entity_name in sanctions_list

# Example usage
if __name__ == "__main__":
    company = fetch_company_details("ABC Corp")
    print(company)
