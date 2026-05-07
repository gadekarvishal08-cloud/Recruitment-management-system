# AI Job Description Generator

A FastAPI-based service that generates comprehensive, inclusive job descriptions using the Groq API and Llama 3 model.

## Features

- Generate complete job descriptions from role title and 5 bullet points
- Structured output with responsibilities and qualifications
- Built-in bias detection for inclusive language
- RESTful API with proper error handling
- Clean, modular architecture

## Tech Stack

- Python 3.8+
- FastAPI
- Groq API (Llama 3 70B)
- Pydantic
- Uvicorn

## Project Structure

```
ai-jd-generator/
│
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── routes.py        # API route definitions
│   ├── service.py       # Groq API integration service
│   ├── prompts.py       # Prompt templates
│   ├── utils.py         # Utility functions (bias detection)
│   └── config.py        # Configuration management
│
├── .env                 # Environment variables (API key)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Installation

1. Clone or download the project

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Groq API key:
   - Get your API key from [https://console.groq.com/](https://console.groq.com/)
   - Create a `.env` file in the project root
   - Add your API key:
     ```
     GROQ_API_KEY=your_actual_api_key_here
     ```

## Running the Application

Start the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoint

### POST /api/generate-jd

Generate a job description from role and bullet points.

**Request Body:**
```json
{
  "role": "Backend Developer",
  "points": [
    "Build REST APIs",
    "Work with databases",
    "Use Spring Boot",
    "Handle scalability",
    "Collaborate with frontend"
  ]
}
```

**Response:**
```json
{
  "job_title": "Backend Software Engineer",
  "summary": "We are seeking a skilled Backend Software Engineer to design and implement robust REST APIs...",
  "responsibilities": [
    "Design, develop, and maintain scalable REST APIs...",
    "Collaborate with database teams to optimize data models...",
    "Implement backend services using Spring Boot framework...",
    "Ensure system scalability and performance optimization...",
    "Work closely with frontend teams to integrate APIs..."
  ],
  "required_qualifications": [
    "Bachelor's degree in Computer Science or related field",
    "3+ years of experience in backend development",
    "Proficiency in Java and Spring Boot"
  ],
  "preferred_qualifications": [
    "Experience with cloud platforms (AWS, GCP)",
    "Knowledge of microservices architecture"
  ],
  "bias_check": {
    "bias_found": false,
    "suggestions": []
  }
}
```

## Sample cURL Request

```bash
curl -X POST "http://localhost:8000/api/generate-jd" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "Backend Developer",
    "points": [
      "Build REST APIs",
      "Work with databases",
      "Use Spring Boot",
      "Handle scalability",
      "Collaborate with frontend"
    ]
  }'
```

## Error Handling

- **400 Bad Request**: Missing fields, invalid input, or incorrect number of bullet points
- **500 Internal Server Error**: Groq API failure or unexpected errors

## Bias Detection

The system includes built-in bias detection that identifies potentially biased language such as:
- "rockstar", "ninja", "guru", "wizard"
- "dominant", "aggressive", "competitive"
- "young", "fresh", "digital native"

When bias is detected, the API returns suggestions for more inclusive alternatives.

## Development

The codebase follows clean architecture principles:
- **config.py**: Environment configuration
- **prompts.py**: LLM prompt templates
- **utils.py**: Helper functions (bias detection, validation)
- **service.py**: Business logic and API integration
- **routes.py**: API endpoint definitions
- **main.py**: Application setup and middleware

## License

MIT License
