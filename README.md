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

---

## Features

- **RESTful API Endpoint:** `/stop-and-search/outcome`
- **Query Parameters:**
  - `force` (required): The name of the police force (e.g., `metropolitan`).
  - `date` (required): Date in `YYYY-MM` format.
- **Rate Limiting:** Limits API usage to 5 requests per minute per client.
- **Error Handling:** Provides descriptive error messages for invalid inputs, external API failures, and rate-limit breaches.
- **Mocked Tests:** Comprehensive test suite using `pytest` and `pytest-mock`.

---

## Technologies Used

- **Flask:** For building the REST API.
- **Flask-Limiter:** For rate-limiting requests.
- **Requests:** For interacting with the external UK Police API.
- **Pytest:** For writing unit tests.
- **Python 3.8+:** Programming language.

---

## API Specification

### Endpoint: `/stop-and-search/outcome`

#### Request

**Method:** `GET`  
**Query Parameters:**

- `force` (required): The name of the police force.
- `date` (required): Date in `YYYY-MM` format.

#### Response

- **Success (200):**

  ```json
  {
    "total": 8,
    "breakdown": {
      "Arrest": 5,
      "A no further action disposal": 3
    }
  }
  ```

- **Error (400):** Missing or invalid parameters:

  ```json
  {
    "error": "Both 'force' and 'date' parameters are required."
  }
  ```

- **Error (500):** External API failure:

  ```json
  {
    "error": "Failed to fetch data from the Police API.",
    "details": "Timeout exceeded"
  }
  ```

- **Error (429):** Rate limit exceeded:
  ```json
  {
    "error": "Rate limit exceeded. Try again later."
  }
  ```

---

## Installation

### Prerequisites

- Python 3.8+ installed
- `pip` package manager installed

### Setup Steps

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd uk_police_api
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   python run.py
   ```

5. **Access the API:**
   Open your browser or API testing tool (like Postman) and navigate to:
   ```
   http://localhost:8080/stop-and-search/outcome?force=metropolitan&date=2022-08
   ```

---

## Project Structure

```plaintext
uk_police_api/
├── app/
│   ├── __init__.py           # Initializes the Flask app and extensions
│   ├── routes.py             # Defines the API endpoints
│   ├── services.py           # External API interaction logic
│   ├── utils.py              # Helper functions like date validation
│   ├── config.py             # Application configuration (e.g., rate limits, API URL)
│   ├── tests/                # Test suite for the application
│       ├── __init__.py       # Initializes the test suite
│       ├── test_routes.py    # Tests for the API endpoints
│       ├── test_services.py  # Tests for service functions
│       └── test_utils.py     # Tests for utility functions
├── run.py                    # Entry point to run the application
├── requirements.txt          # Project dependencies
├── README.md                 # Documentation (this file)
└── .env                      # Environment variables (e.g., API keys) [optional]
```

---

## Running Tests

### Install Testing Dependencies

Ensure `pytest` and `pytest-mock` are installed:

```bash
pip install pytest pytest-mock
```

### Run the Test Suite

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest app/tests/test_routes.py
```

---

## Key Design Decisions

1. **Modular Code Structure:**

   - Separated functionality into `routes`, `services`, and `utils` to maintain clean and maintainable code.

2. **Mocking External API Calls:**

   - Used `pytest-mock` to simulate the behavior of external APIs during testing, avoiding dependency on live systems.

3. **Error Handling:**

   - Comprehensive error handling for input validation, external API failures, and rate-limit violations.

4. **Rate-Limiting:**
   - Used `Flask-Limiter` to prevent API abuse by limiting requests to **5 per minute per client**.

---

## Example Usage

### Valid Request

```bash
curl "http://localhost:8080/stop-and-search/outcome?force=metropolitan&date=2022-08"
```

Response:

```json
{
  "total": 8,
  "breakdown": {
    "Arrest": 5,
    "A no further action disposal": 3
  }
}
```

### Invalid Request

```bash
curl "http://localhost:8080/stop-and-search/outcome?force=metropolitan&date=2022-13"
```

Response:

```json
{
  "error": "Invalid date format. Use YYYY-MM."
}
```

---

## Future Improvements

- **Pagination Support:** Handle large datasets by introducing pagination for API responses.
- **Caching:** Use a caching mechanism (e.g., Redis) to reduce redundant API calls for frequently requested data.
- **Database Integration:** Store historical data for improved performance and offline functionality.
- **Authentication:** Add API key-based authentication for secure access.

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/my-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add my feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/my-feature
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
