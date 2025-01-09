Explanation of the Code:
Fetching Data:

The fetch_bpi_data function sends a GET request to the endpoint and returns the parsed JSON response.
Tests:

The test_bpi_data function:
Validates that the bpi field exists in the response.
Verifies that there are exactly 3 BPIs (currencies).
Ensures USD, GBP, and EUR are present.
Checks that the description for GBP is 'British Pound Sterling'.
Execution:

The script will print "All tests passed successfully!" if all conditions are met or the assertion error message if any test fails.
