README: UK Police Crime Data API

## Task Description

The goal of this project is to create an API that fetches and summarizes stop-and-search outcome data from the UK Police API for a specific police force and date. The resulting API endpoint provides a summary of the outcomes and their respective counts, along with a total count of all outcomes.

### Requirements

1. **Endpoint:** Create a `GET` endpoint `/stop-and-search/outcome` that accepts `force` and `date` parameters.
2. **Validation:** Ensure all input parameters are validated.
3. **Data Aggregation:** Aggregate the outcomes returned by the external UK Police API and present them in a summary format.
4. **Rate Limiting:** Implement rate limiting to protect the server from abuse.
5. **Error Handling:** Handle errors gracefully, including input validation errors, external API failures, and timeout issues.
6. **Documentation:** The script is documented for clarity and maintainability.
