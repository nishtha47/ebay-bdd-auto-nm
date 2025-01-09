import requests
import pytest

# Function to fetch the data from the endpoint
def fetch_bpi_data():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    return response.json()

# Test function to verify the requirements
def test_bpi_data():
    # Fetch the response
    data = fetch_bpi_data()
    
    # Ensure the BPI section exists
    assert "bpi" in data, "BPI section is missing from the response"

    # Ensure there are exactly 3 currencies
    bpi = data["bpi"]
    assert len(bpi) == 3, f"Expected 3 BPIs, but found {len(bpi)}"
    
    # Ensure the required currencies exist
    assert "USD" in bpi, "USD currency is missing"
    assert "GBP" in bpi, "GBP currency is missing"
    assert "EUR" in bpi, "EUR currency is missing"

    # Verify GBP description
    gbp_description = bpi["GBP"]["description"]
    assert gbp_description == "British Pound Sterling", f"GBP description mismatch: {gbp_description}"

if __name__ == "__main__":
    # Running the test manually
    try:
        test_bpi_data()
        print("All tests passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")
