# KrishiMitra 🌾
### AI Farm Advisory Agent for Karnataka's Smallholder Farmers

> **Kaggle 5-Day AI Agents Intensive Capstone 2026 — Agents for Good Track**

---

## The Problem

Karnataka has over 5 million smallholder farmers. Most have no quick 
access to expert advice when their crop gets diseased, when they need 
to know how much fertilizer to use, or which government schemes they 
qualify for.

By the time they visit a Krishi Vigyan Kendra or agriculture officer, 
crop damage has already spread. The language barrier makes it worse — 
most digital tools work only in English, but Karnataka farmers speak 
Kannada, Hindi, or Telugu.

KrishiMitra solves this directly.

---

## The Solution

KrishiMitra (meaning Friend of the Farmer) is a conversational AI 
agent that farmers can talk to in their own language and get immediate, 
personalized, actionable advice.

It is not just a chatbot. It is a true AI agent — it calls real tools, 
fetches live weather data, calculates fertilizer doses, diagnoses pests 
from symptom descriptions, and finds government schemes relevant to the 
farmer's specific crop and location.

---

## Key Features

- Pest and disease diagnosis from symptom description
- Real-time weather advice for irrigation and spraying timing
- NPK fertilizer calculator per acre
- Government scheme finder — PM-KISAN, PMFBY, RSK, Soil Health Card
- Crop calendar for Karnataka Kharif and Rabi seasons
- Soil type advisor — red, black, laterite, sandy, loamy
- Multi-language support — English, Kannada, Hindi, Telugu
- Security layer — input sanitization and prompt injection prevention

---

## Architecture

| Component | Details |
|---|---|
| Framework | Google ADK (Agent Development Kit) |
| Model | Gemini 2.5 Flash |
| IDE | Antigravity (vibe coding) |
| Weather API | Open-Meteo (free, no key needed) |
| Security | Input sanitization on all tool inputs |

### Tools

| Tool | What it does |
|---|---|
| get_weather | Fetches live weather for a location |
| estimate_fertilizer | Calculates NPK kg needed per acre |
| find_schemes | Lists government schemes and how to apply |
| diagnose_pest_disease | Diagnoses disease from farmer's symptoms |
| get_crop_calendar | Gives sowing and harvest schedule |
| get_soil_advice | Advises based on Karnataka soil type |

---

## Key Course Concepts Demonstrated

1. **ADK Agent with multi-tool architecture** — 6 FunctionTools
   called intelligently by the agent based on farmer queries

2. **Security features** — input sanitization, blocked pattern 
   filtering, prompt injection prevention, API keys in environment 
   variables only

3. **Antigravity IDE** — entire project built using vibe coding 
   with natural language descriptions

4. **Agent CLI** — adk web used throughout development and testing 
   with Events and Traces panel to verify tool invocations

---

## Setup Instructions

### Step 1 — Requirements

- Python 3.9 or higher
- Free Gemini API key from https://aistudio.google.com/apikey

### Step 2 — Clone the repository

Open your terminal and run:

git clone https://github.com/Rajugudta/krishimitra.git
cd krishimitra

### Step 3 — Create virtual environment

On Windows:
python -m venv venv
venv\Scripts\activate

On Mac or Linux:
python -m venv venv
source venv/bin/activate

### Step 4 — Install packages

pip install google-adk requests python-dotenv

### Step 5 — Add your API key

Create a file named .env in the project root folder.
Add this inside it:

GOOGLE_API_KEY=your_gemini_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE

Get your free key at: https://aistudio.google.com/apikey

Your key will start with AIzaSy...

### Step 6 — Run the agent

adk web

Open your browser and go to: http://localhost:8000
Select KrishiMitra from the dropdown and start chatting.

### Step 7 — Run the full Streamlit app (optional)

pip install streamlit google-generativeai
streamlit run app.py

Open your browser and go to: http://localhost:8501

---

## How to Use KrishiMitra

Once running, try these example messages:

- My tomato leaves have white powder on them
- I have 2 acres of ragi near Davangere, how much fertilizer do I need?
- Will it rain in Mangalore this week?
- What government schemes can I apply for as a farmer?
- I have red soil, which crops are best?
- When should I sow paddy? It is June now.

You can also type in Kannada, Hindi, or Telugu and KrishiMitra 
will reply in the same language.

---

## Security Notes

- API keys are stored as environment variables only
- The .env file is listed in .gitignore and never pushed to GitHub
- All user inputs are sanitized before passing to any tool
- Prompt injection patterns are filtered and blocked
- Input length is limited to 500 characters per tool call

---

## Demo Video

[YOUR YOUTUBE LINK HERE]

---

## Project by

RAJU
Kaggle 5-Day AI Agents Intensive Capstone — June 2026
Track: Agents for Good