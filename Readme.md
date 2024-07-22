Create a Virtual Environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

pip install -r requirements.txt
pip install fastapi uvicorn transformers torch
Run the FastAPI Server:


uvicorn main:app --reload
API Endpoints
1. Root Endpoint
URL: /

Method: GET

Description: Returns a welcome message to confirm that the API is running.

Response:

json
Copy code
{
  "message": "Welcome to the BERT Language Model API"
}
2. Text Generation Endpoint
URL: /generate_text

Method: POST

Description: Takes an input text containing a [MASK] token and returns possible completions for the masked token.

Request Body:

json
Copy code
{
  "text": "string"
}
text: A string containing the [MASK] token.
Response:

json
Copy code
{
  "filled_texts": [
    "string1",
    "string2",
    ...
  ]
}
filled_texts: A list of strings with possible completions for the masked token.
Example Request:

bash
Copy code
curl -X 'POST' \
  'http://127.0.0.1:8000/generate_text' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "The capital of Pakistan is [MASK]."
}'
Example Response:

json
Copy code
{
  "filled_texts": [
    "the capital of pakistan is islamabad.",
    "the capital of pakistan is karachi.",
    "the capital of pakistan is lahore.",
    "the capital of pakistan is peshawar.",
    "the capital of pakistan is sindh."
  ]
}
Error Handling
The API includes error handling for the following scenarios:

Missing Mask Token:

Status Code: 400 Bad Request
Response:
json
Copy code
{
  "detail": "The input text must contain the [MASK] token."
}
Internal Server Error:

Status Code: 500 Internal Server Error
Response:
json
Copy code
{
  "detail": "Error generating text: <error message>"
}