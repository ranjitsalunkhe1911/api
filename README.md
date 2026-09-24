# 🗺️ AI Travel Planner

An AI-powered travel planning web application built with **Python, FastAPI, and Google Gemini**. The application generates personalized multi-day travel itineraries based on the user's destination, number of days, interests, and budget.

The project also includes a **Demo Mode**, which allows users to generate a sample itinerary without providing a Gemini API key.

---

## 📌 Project Overview

The **AI Travel Planner** is designed to help travelers create customized travel plans quickly and conveniently.

Users can provide:

* 📍 Travel destination
* 📅 Number of days
* ❤️ Interests and travel preferences
* 💰 Budget level
* 🔑 Optional Gemini API key
* 🧪 Demo mode selection

The application processes these inputs and generates a structured travel itinerary containing daily activities, food recommendations, practical travel tips, and estimated expenses.

The backend is implemented using **FastAPI**, while **Google Gemini** is used to generate AI-powered travel recommendations when a valid API key is available.

---

# ✨ Features

## 1. 🤖 AI-Powered Itinerary Generation

The application uses Google Gemini to generate personalized travel plans.

The AI receives information such as:

* Destination
* Trip duration
* Interests
* Budget tier

It then generates a detailed Markdown-formatted itinerary.

The application attempts multiple Gemini models if necessary:

* `gemini-1.5-flash`
* `gemini-2.0-flash`
* `gemini-1.5-pro`
* `gemini-pro`

---

## 2. 🧪 Demo Mode

The application can operate without a Gemini API key through its built-in demo itinerary generator.

Demo Mode is useful for:

* Testing the application
* Demonstrating the interface
* Running the project without an API key
* Developing the frontend/backend locally

When Demo Mode is enabled, the application generates a predefined smart itinerary instead of calling Gemini.

---

## 3. 🎯 Personalized Travel Preferences

The application accepts the following travel preferences:

| Input       | Description                               |
| ----------- | ----------------------------------------- |
| Destination | City, country, or travel location         |
| Days        | Number of travel days                     |
| Interests   | User's preferred activities               |
| Budget      | Low, medium, or high                      |
| API Key     | Optional Gemini API key                   |
| Demo Mode   | Enables offline/demo itinerary generation |

These inputs are represented by the `TravelRequest` Pydantic model.

---

# 💰 Budget Categories

The demo itinerary supports three budget levels.

### 🟢 Low

Approximately:

**$40 – $70/day**

Designed around:

* Backpacker-friendly travel
* Public transportation
* Street food

### 🟡 Medium

Approximately:

**$100 – $180/day**

Designed around:

* Comfortable boutique hotels
* Guided highlights
* Mixed dining options

### 🔵 High

Approximately:

**$300 – $600+/day**

Designed around:

* Luxury accommodation
* Private transfers
* Fine dining
* Exclusive experiences

These estimates are part of the built-in demo itinerary generator.

---

# 🏗️ Project Architecture

The application follows a simple client-server architecture.

```text
                ┌──────────────────────┐
                │      User / UI       │
                │     index.html       │
                └──────────┬───────────┘
                           │
                           │ HTTP Request
                           ▼
                ┌──────────────────────┐
                │      FastAPI         │
                │      main.py         │
                └──────────┬───────────┘
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
       ┌─────────────────┐   ┌──────────────────┐
       │   Demo Mode     │   │   Google Gemini  │
       │ Itinerary       │   │   AI Generation  │
       │ Generator       │   │                  │
       └────────┬────────┘   └─────────┬────────┘
                │                      │
                └──────────┬───────────┘
                           ▼
                ┌──────────────────────┐
                │ Generated Travel     │
                │ Itinerary / JSON     │
                └──────────────────────┘
```

---

# 🛠️ Technologies Used

## Backend

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn**

## AI

* **Google Gemini API**
* `google.generativeai`

## Configuration

* **python-dotenv**
* `.env` environment variables

The project loads environment variables from a `.env` file located in the same directory as `main.py`.

---

# 📁 Project Structure

A typical project structure is:

```text
AI-Travel-Planner/
│
├── main.py
├── index.html
├── .env
├── requirements.txt
└── README.md
```

### `main.py`

Contains the FastAPI backend, request model, Gemini integration, demo itinerary generator, API endpoints, and server configuration.

### `index.html`

Contains the frontend interface used to interact with the travel planner.

The backend looks for this file in the same directory as `main.py`. If it cannot find it, the application returns an `index.html not found` error.

### `.env`

Stores the Gemini API key as an environment variable.

### `requirements.txt`

Contains the Python packages required to run the application.

### `README.md`

Contains project documentation and setup instructions.

---

# 🔑 Environment Configuration

Create a `.env` file in the project directory.

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

The application reads the key using:

```python
os.getenv("GEMINI_API_KEY", "")
```

It also checks for placeholder values and treats them as an unavailable API key.

### ⚠️ Security

Do not upload your actual Gemini API key to GitHub or other public repositories.

Add `.env` to `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
```

---

# 📦 Installation

## Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Step 2: Clone or Download the Project

Place all project files inside the same folder.

Example:

```text
AI-Travel-Planner/
```

---

## Step 3: Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📥 Install Dependencies

Install the required packages:

```bash
pip install fastapi uvicorn pydantic python-dotenv google-generativeai
```

Alternatively, if a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

The application runs by default on:

```text
http://127.0.0.1:8000
```

The Python file also contains a direct server startup configuration using Uvicorn with host `127.0.0.1` and port `8000`.

Open the address in a web browser.

---

# 🌐 API Endpoints

## 1. Home Page

### Endpoint

```http
GET /
```

### Purpose

Loads the `index.html` frontend.

If the file is missing, the API returns:

```text
index.html not found
```

with HTTP status code `404`.

---

# 2. API Status

### Endpoint

```http
GET /api/status
```

### Purpose

Checks whether the backend is online and whether a server-side Gemini API key is configured.

Example response:

```json
{
  "status": "online",
  "has_server_key": true,
  "models_available": [
    "gemini-1.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-pro"
  ]
}
```

The endpoint is implemented in `get_status()`.

---

# 3. Generate Travel Plan

### Endpoint

```http
POST /plan
```

This is the main endpoint of the application.

It receives a `TravelRequest` containing:

```json
{
  "destination": "Paris",
  "days": 5,
  "interests": "history, food, museums",
  "budget": "medium",
  "api_key": null,
  "demo_mode": false
}
```

---

# 🧾 Request Parameters

| Parameter     | Type    | Default                          | Description             |
| ------------- | ------- | -------------------------------- | ----------------------- |
| `destination` | String  | Required                         | Travel destination      |
| `days`        | Integer | Required                         | Number of days          |
| `interests`   | String  | sightseeing, local food, culture | Travel interests        |
| `budget`      | String  | medium                           | low / medium / high     |
| `api_key`     | String  | None                             | Optional Gemini API key |
| `demo_mode`   | Boolean | False                            | Enables demo itinerary  |

---

# 🔄 Travel Plan Processing Flow

When a request is sent to `/plan`, the application follows this process:

```text
User submits travel preferences
             ↓
FastAPI receives POST /plan
             ↓
Check for Gemini API key
             ↓
       ┌─────┴─────┐
       │           │
     No Key      Key Found
       │           │
       ▼           ▼
 Demo Mode      Configure
 Itinerary      Gemini API
       │           │
       │           ▼
       │      Generate AI Plan
       │           │
       └─────┬─────┘
             ▼
       Return itinerary
```

The application first determines whether an API key was supplied in the request or configured on the server.

---

# 🤖 Gemini AI Generation

When a valid API key is available, the application configures Gemini:

```python
genai.configure(api_key=active_key)
```

It then constructs a detailed travel-planning prompt containing:

* Destination
* Duration
* Interests
* Budget
* Daily activities
* Food recommendations
* Travel tips
* Estimated costs

The application tries multiple Gemini models until one successfully generates a response.

---

# 🧪 Demo Mode Processing

If Demo Mode is selected, the application does not call Gemini.

Instead, it calls:

```python
generate_demo_itinerary()
```

The generated itinerary contains:

* Destination overview
* Day-by-day schedule
* Morning activities
* Afternoon activities
* Evening activities
* Local food suggestions
* Practical travel tips
* Estimated daily budget

---

# 📋 Generated Itinerary Format

The generated AI itinerary is requested in Markdown format.

It contains sections such as:

```text
# Complete X-Day Itinerary

## Day-by-Day Detailed Plan

### Day 1
Morning
Afternoon
Evening

## Top 3 Must-Try Local Delicacies

## Practical Travel Tips

## Estimated Daily Budget Breakdown
```

The AI prompt explicitly requests daily activities, local food, practical tips, and budget information.

---

# 🍲 Food Recommendations

The itinerary includes three local food or drink recommendations.

The demo version categorizes them as:

1. Signature heritage dish
2. Street market food
3. Traditional sweet and beverage

---

# 💡 Travel Tips

The generated itinerary provides practical travel information such as:

* Transportation
* Attraction reservations
* Local etiquette
* Payment methods
* Walking considerations

The AI prompt specifically requests transportation, advance booking, safety/etiquette, and payment-method tips.

---

# 💵 Budget Estimation

The application divides daily travel expenditure into:

```text
Accommodation     ~45%
Dining & Drinks   ~30%
Activities/Transit ~25%
```

These percentages are used by the demo itinerary generator.

The AI-generated version is asked to provide estimated costs for:

* Accommodation
* Food & Drinks
* Sightseeing & Transport

---

# ⚠️ Error Handling

The application handles several possible errors.

## Missing API Key

If no API key is available and Demo Mode was not selected, the application returns:

```json
{
  "error": "NO_API_KEY",
  "message": "...",
  "can_demo": true
}
```

This allows the frontend to tell the user that they can either provide an API key or use Demo Mode.

---

## Gemini Configuration Error

If Gemini cannot be configured, the application returns:

```json
{
  "error": "CONFIG_ERROR",
  "message": "Failed to configure Gemini..."
}
```

with HTTP status `400`.

---

## Gemini Generation Error

If all configured Gemini models fail, the application returns:

```json
{
  "error": "API_ERROR",
  "message": "Gemini API returned an error...",
  "can_demo": true
}
```

with HTTP status `500`.

---

# 🔐 API Key Handling

The application supports two API-key sources.

### 1. Server-side API Key

The key can be stored in:

```env
GEMINI_API_KEY=your_key
```

### 2. Request API Key

A key can also be supplied through the `api_key` field of a travel request.

The application gives the request key priority when one is supplied; otherwise, it uses the server-side key.

---

# 🧩 Main Python Components

## FastAPI Application

```python
app = FastAPI(
    title="AI Travel Planner",
    version="2.0.0"
)
```

This creates the main FastAPI application.

---

## TravelRequest Model

The `TravelRequest` class validates incoming travel-planning data.

```python
class TravelRequest(BaseModel):
    destination: str
    days: int
    interests: Optional[str]
    budget: Optional[str]
    api_key: Optional[str]
    demo_mode: Optional[bool]
```

---

## Demo Generator

```python
generate_demo_itinerary()
```

Creates an itinerary without using an external AI service.

---

## Main Planning Endpoint

```python
generate_plan()
```

Handles the complete travel-plan generation process.

---

# 🔁 Complete Application Workflow

```text
                START
                  │
                  ▼
          Open Travel Planner
                  │
                  ▼
       Enter destination & days
                  │
                  ▼
       Select interests & budget
                  │
                  ▼
        Submit travel request
                  │
                  ▼
       FastAPI receives request
                  │
                  ▼
          Check API Key
             /        \
           No          Yes
           │            │
           ▼            ▼
      Demo Mode     Configure
      available?    Gemini API
        /    \          │
      Yes     No        ▼
       │       │    Generate AI
       ▼       ▼      itinerary
     Demo    Return       │
    Plan     API Error    │
       │                    │
       └─────────┬──────────┘
                 ▼
          Return Travel Plan
                 │
                 ▼
                END
```

---

# 🧪 Testing the API

You can test the status endpoint:

```bash
curl http://127.0.0.1:8000/api/status
```

You can test the planning endpoint using a POST request:

```bash
curl -X POST http://127.0.0.1:8000/plan \
-H "Content-Type: application/json" \
-d "{\"destination\":\"Paris\",\"days\":3,\"interests\":\"food, culture\",\"budget\":\"medium\",\"demo_mode\":true}"
```

---

# 📊 Example Input

```json
{
  "destination": "Mumbai",
  "days": 3,
  "interests": "food, culture, sightseeing",
  "budget": "medium",
  "demo_mode": true
}
```

---

# 📄 Example Output Structure

```text
Complete 3-Day Travel Guide to Mumbai

Destination Overview

Day 1
Morning
Afternoon
Evening

Day 2
Morning
Afternoon
Evening

Day 3
Morning
Afternoon
Evening

Top 3 Must-Try Local Foods & Drinks

Practical Travel Tips

Estimated Daily Budget Breakdown
```

---

# 🚨 Important Notes

### 1. Internet Connection

AI itinerary generation using Gemini requires access to the Gemini service.

### 2. API Key

A valid Gemini API key is required for actual AI-generated itineraries unless Demo Mode is used.

### 3. Demo Mode

Demo Mode does not require a Gemini API key.

### 4. `index.html`

The backend expects `index.html` to be located in the same directory as `main.py`.

### 5. AI-Generated Information

Travel recommendations generated by an AI model should be verified before making actual bookings or travel arrangements.

---

# 🔮 Future Improvements

Possible future improvements include:

* 🌍 Real-time destination information
* 🗺️ Interactive maps
* 🏨 Hotel recommendations
* ✈️ Flight information
* 🚆 Public transportation integration
* 🌦️ Weather information
* 📍 Google Maps integration
* 💾 Saving and downloading itineraries
* 👤 User accounts
* 🗓️ Calendar integration
* 💱 Automatic currency conversion
* 📱 Improved mobile interface
* 🌐 Multi-language support

These are potential enhancements and are **not currently implemented in the provided `main.py`**.

---

# 📝 Project Information

**Project Name:** AI Travel Planner

**Application Type:** AI-powered Web Application

**Backend:** FastAPI

**Programming Language:** Python

**AI Service:** Google Gemini

**API:** REST-style HTTP endpoints

**Default Server:** `127.0.0.1:8000`

**Version:** 2.0.0

---

# 👩‍💻 Development

The application is designed with a lightweight backend structure so that the frontend and AI travel-generation logic can be developed independently.

The backend is responsible for:

* Receiving travel preferences
* Validating request data
* Managing API keys
* Generating demo itineraries
* Calling Gemini
* Handling AI errors
* Returning generated travel plans

---

# 📜 License

Add your preferred license here before publishing the project publicly.

For example:

```text
This project is developed for educational and demonstration purposes.
```

---

# 🙌 Acknowledgement

This project uses:

* FastAPI for backend API development
* Pydantic for request validation
* Google Gemini for AI-powered itinerary generation
* Uvicorn as the ASGI server
* Python-dotenv for environment configuration

---

## ⭐ Summary

**AI Travel Planner** is a FastAPI-based application that combines user travel preferences with Google Gemini to generate personalized travel itineraries. It supports destination, duration, interests, and budget-based planning, while its built-in Demo Mode allows the application to be tested without an API key.

The application provides a simple foundation that can be extended with maps, real-time travel information, hotel and flight services, weather APIs, and itinerary storage.
