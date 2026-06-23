"""
KrishiMitra — AI Farm Advisory Agent
=====================================
Track: Agents for Good
Competition: Kaggle 5-Day AI Agents Intensive Capstone 2026

Problem: Smallholder farmers in Karnataka lack quick access to expert
advice on crop diseases, weather-based decisions, fertilizer dosing,
and government schemes.

Solution: KrishiMitra is a conversational AI agent built with Google ADK
and Gemini 2.5 Flash that gives farmers personalized, actionable advice
in English, Kannada, Hindi, and Telugu.

Key concepts demonstrated:
1. ADK Agent with multi-tool architecture (6 specialized tools)
2. Security features (input sanitization, prompt injection prevention)
3. Antigravity IDE for vibe coding the agent
4. Agent CLI (adk web) for local development and testing

Author: [Write your name here]
Date: June 2026
"""

import re
import requests
from google.adk.agents import Agent


# ─── SECURITY LAYER ─────────────────────────────────────────────
# Protects the agent from prompt injection and misuse.
# All user inputs pass through sanitize_input() before tool use.

MAX_INPUT_LENGTH = 500

BLOCKED_PATTERNS = [
    r"<script.*?>",
    r"DROP TABLE",
    r"ignore previous",
    r"system:",
    r"jailbreak",
]

def sanitize_input(text: str) -> str:
    """Removes dangerous patterns and enforces length limits.
    This is a security function — do not remove it.

    Args:
        text: Raw input string from user or agent
    Returns:
        Cleaned, safe string
    """
    if not text or not isinstance(text, str):
        return ""
    text = text[:MAX_INPUT_LENGTH]
    for pattern in BLOCKED_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text.strip()


# ─── TOOL 1: WEATHER ────────────────────────────────────────────
# Uses Open-Meteo free API — no key required.
# Called when farmer asks about rain, irrigation, or spraying.

def get_weather(location: str) -> dict:
    """Fetches real-time weather data for a given location.
    Used to advise farmers on irrigation and spraying timing.

    Args:
        location: City or district name e.g. Mangalore, Davangere
    Returns:
        dict with temperature, precipitation, wind speed
    """
    # Sanitize input before making API call
    location = sanitize_input(location)
    if not location:
        return {"status": "error", "message": "Please provide a valid location."}

    try:
        # Step 1: Convert location name to coordinates
        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": location, "count": 1},
            timeout=10
        ).json()

        if not geo.get("results"):
            return {"status": "error", "message": f"Location not found: {location}"}

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        # Step 2: Get current weather using coordinates
        weather = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,precipitation,wind_speed_10m"
            },
            timeout=10
        ).json()

        c = weather.get("current", {})
        return {
            "status": "success",
            "location": location,
            "temperature_c": c.get("temperature_2m"),
            "precipitation_mm": c.get("precipitation"),
            "wind_speed_kmh": c.get("wind_speed_10m")
        }

    except requests.exceptions.Timeout:
        return {"status": "error", "message": "Weather service timed out. Please try again."}
    except Exception as e:
        return {"status": "error", "message": f"Weather lookup failed: {str(e)}"}


# ─── TOOL 2: FERTILIZER CALCULATOR ──────────────────────────────
# Pure logic tool — no external API needed, always reliable.
# NPK values are general estimates for Karnataka conditions.

def estimate_fertilizer(crop: str, area_acres: float) -> dict:
    """Calculates approximate NPK fertilizer requirements.
    Based on general agronomic guidelines for Karnataka crops.

    Args:
        crop: Crop name e.g. tomato, ragi, paddy, maize
        area_acres: Farm area in acres (e.g. 2.5)
    Returns:
        dict with N, P, K amounts in kg and a safety note
    """
    # Sanitize crop name input
    crop = sanitize_input(crop)

    # NPK requirements per acre for common Karnataka crops
    # Source: General Karnataka agriculture department guidelines
    per_acre = {
        "tomato":    {"N": 40, "P": 25, "K": 25},
        "ragi":      {"N": 16, "P": 8,  "K": 8},
        "paddy":     {"N": 48, "P": 20, "K": 20},
        "maize":     {"N": 30, "P": 15, "K": 15},
        "groundnut": {"N": 10, "P": 20, "K": 20},
        "cotton":    {"N": 32, "P": 16, "K": 16},
        "jowar":     {"N": 20, "P": 10, "K": 10},
    }

    rates = per_acre.get(crop.lower())
    if not rates:
        return {
            "status": "error",
            "message": f"No data for crop: {crop}. Available: {', '.join(per_acre.keys())}"
        }

    return {
        "status": "success",
        "crop": crop,
        "area_acres": area_acres,
        "estimated_kg": {k: round(v * area_acres, 1) for k, v in rates.items()},
        "note": "General estimate only. Always confirm with a local soil test before applying."
    }


# ─── TOOL 3: GOVERNMENT SCHEMES ─────────────────────────────────
# Curated database of central and Karnataka state schemes.
# Updated for 2025-26 farming season.

def find_schemes(crop: str = "") -> dict:
    """Returns relevant government agriculture schemes for
    Karnataka farmers. Covers central and state schemes.

    Args:
        crop: Optional crop name to tailor suggestions
    Returns:
        dict with list of applicable schemes and how to apply
    """
    schemes = [
        {
            "name": "PM-KISAN",
            "desc": "Direct income support of Rs.6000/year to landholding farmers.",
            "how_to_apply": "Register at pmkisan.gov.in or visit your nearest CSC center."
        },
        {
            "name": "PMFBY (Fasal Bima Yojana)",
            "desc": "Crop insurance against drought, flood, and pest loss.",
            "how_to_apply": "Apply at your nearest bank branch or CSC before sowing."
        },
        {
            "name": "Soil Health Card Scheme",
            "desc": "Free soil testing with crop-wise nutrient recommendations.",
            "how_to_apply": "Contact your local agriculture office or Raitha Samparka Kendra."
        },
        {
            "name": "Kisan Credit Card",
            "desc": "Low-interest credit for seeds, fertilizer, and equipment.",
            "how_to_apply": "Apply at any nationalized bank with land ownership documents."
        },
        {
            "name": "Raitha Samparka Kendra (RSK)",
            "desc": "Karnataka state schemes, subsidies, and farm support services.",
            "how_to_apply": "Visit your nearest RSK office for current Karnataka schemes."
        },
        {
            "name": "PM Krishi Sinchai Yojana",
            "desc": "Subsidy for drip and sprinkler irrigation systems.",
            "how_to_apply": "Apply at district agriculture office with farm documents."
        },
    ]
    return {"status": "success", "schemes": schemes}


# ─── TOOL 4: PEST & DISEASE DIAGNOSIS ───────────────────────────
# Knowledge-based diagnosis using symptom keyword matching.
# Covers most common diseases in Karnataka conditions.
# Always includes safety disclaimer — never gives unsafe advice.

def diagnose_pest_disease(crop: str, symptoms: str) -> dict:
    """Diagnoses likely pest or disease from crop and symptoms.
    Uses keyword matching against a curated Karnataka crop database.

    Security: Both inputs are sanitized before processing.

    Args:
        crop: Crop name e.g. tomato, ragi, paddy
        symptoms: Farmer's description e.g. yellow leaves, white powder
    Returns:
        dict with diagnosis, recommended action, severity,
        and mandatory safety disclaimer
    """
    # Sanitize both inputs — security requirement
    crop = sanitize_input(crop)
    symptoms = sanitize_input(symptoms)

    if not crop or not symptoms:
        return {"status": "error", "message": "Please provide both crop name and symptoms."}

    # Symptom-to-diagnosis mapping for Karnataka crops
    diagnoses = {
        "tomato": {
            "yellow leaves": {
                "diagnosis": "Likely Nitrogen deficiency or Early Blight fungal infection.",
                "action": "Check soil nitrogen levels. If fungal spots visible, apply copper-based fungicide. Ensure proper drainage.",
                "severity": "Medium"
            },
            "white powder": {
                "diagnosis": "Powdery Mildew fungal disease.",
                "action": "Apply sulfur-based fungicide early morning. Improve air circulation between plants.",
                "severity": "Medium"
            },
            "holes in leaves": {
                "diagnosis": "Caterpillar or fruit borer attack.",
                "action": "Check undersides of leaves for eggs. Use neem oil spray as first step.",
                "severity": "High"
            },
            "wilting": {
                "diagnosis": "Possible Fusarium Wilt or water stress.",
                "action": "Check soil moisture. If moist and wilting, likely fungal — remove affected plants.",
                "severity": "High"
            },
            "brown spots": {
                "diagnosis": "Early Blight or Septoria Leaf Spot.",
                "action": "Remove affected leaves. Apply mancozeb fungicide. Avoid overhead watering.",
                "severity": "Medium"
            },
        },
        "ragi": {
            "yellow leaves": {
                "diagnosis": "Iron/nitrogen deficiency or Blast disease.",
                "action": "Apply ferrous sulfate spray. Check for blast spots on leaves.",
                "severity": "Medium"
            },
            "spots on leaves": {
                "diagnosis": "Ragi Blast disease — very common in Karnataka.",
                "action": "Apply Tricyclazole fungicide. Avoid excess nitrogen.",
                "severity": "High"
            },
            "holes in leaves": {
                "diagnosis": "Aphid or grasshopper damage.",
                "action": "Spray neem oil solution 5ml per litre water.",
                "severity": "Medium"
            },
        },
        "paddy": {
            "yellow leaves": {
                "diagnosis": "Yellow Stem Borer or nutrient deficiency.",
                "action": "Check stem for borer holes. Apply Chlorpyrifos if confirmed.",
                "severity": "High"
            },
            "brown spots": {
                "diagnosis": "Brown Plant Hopper or Brown Leaf Spot.",
                "action": "Drain field for a few days. Apply neem-based pesticide.",
                "severity": "Medium"
            },
            "wilting": {
                "diagnosis": "Bacterial Leaf Blight or water deficit.",
                "action": "Ensure adequate water. Apply copper fungicide if bacterial.",
                "severity": "High"
            },
        },
        "maize": {
            "yellow leaves": {
                "diagnosis": "Nitrogen deficiency or Maize Streak Virus.",
                "action": "Apply urea top dressing. Remove infected plants if streaks visible.",
                "severity": "Medium"
            },
            "holes in leaves": {
                "diagnosis": "Fall Armyworm — serious pest in Karnataka.",
                "action": "Apply Emamectin Benzoate or neem oil into the whorl.",
                "severity": "High"
            },
        },
    }

    crop_data = diagnoses.get(crop.lower())
    if not crop_data:
        return {
            "status": "partial",
            "message": f"No specific data for {crop}. Please consult your local Krishi Vigyan Kendra.",
        }

    # Match symptoms using keyword search
    for keyword, result in crop_data.items():
        if keyword in symptoms.lower():
            return {
                "status": "success",
                "crop": crop,
                "symptoms": symptoms,
                "diagnosis": result["diagnosis"],
                "recommended_action": result["action"],
                "severity": result["severity"],
                "disclaimer": "WARNING: This is a preliminary diagnosis only. Always confirm with your local agriculture officer before applying any chemical treatment."
            }

    return {
        "status": "partial",
        "message": f"Symptoms not matched for {crop}. Visit your nearest Raitha Samparka Kendra for accurate diagnosis.",
    }


# ─── TOOL 5: CROP CALENDAR ──────────────────────────────────────
# Provides sowing, watering, and harvest schedule.
# Tailored for Karnataka's Kharif and Rabi seasons.

def get_crop_calendar(crop: str, month: int = None) -> dict:
    """Returns sowing, watering, and harvest schedule for
    Karnataka crops. Provides month-specific advice if month given.

    Args:
        crop: Crop name e.g. tomato, ragi, paddy, maize
        month: Current month as number 1-12 (optional)
    Returns:
        dict with full calendar and current month advice
    """
    crop = sanitize_input(crop)

    # Crop calendars for Karnataka's two main seasons
    # Kharif: June-November | Rabi: November-April
    calendars = {
        "ragi": {
            "sowing_months": [6, 7],
            "sowing_advice": "Sow in June-July with onset of monsoon.",
            "watering": "Every 10-12 days. Critical at flowering (day 45-60).",
            "fertilizer_timing": "Basal dose at sowing. Top dress nitrogen at 30 days.",
            "harvest_months": [10, 11],
            "harvest_advice": "Harvest when ears turn brown. Dry for 5-7 days.",
            "total_days": 120,
            "tips": "Drought tolerant — avoid overwatering. Best for red soil areas.",
        },
        "tomato": {
            "sowing_months": [6, 7, 11, 12],
            "sowing_advice": "Two seasons: Kharif (June-July) and Rabi (Nov-Dec).",
            "watering": "Every 5-7 days. Drip irrigation is best.",
            "fertilizer_timing": "Every 15 days after transplanting.",
            "harvest_months": [9, 10, 2, 3],
            "harvest_advice": "Pick when fruits turn light red. Harvest every 3-4 days.",
            "total_days": 90,
            "tips": "Stake plants at 30 days. Watch for fruit borer after flowering.",
        },
        "paddy": {
            "sowing_months": [6, 7],
            "sowing_advice": "Transplant 25-day seedlings in June-July.",
            "watering": "Keep field flooded 5cm during vegetative stage.",
            "fertilizer_timing": "Basal at transplanting. Top dress at 30 and 55 days.",
            "harvest_months": [10, 11],
            "harvest_advice": "Harvest when 80% of grains turn golden yellow.",
            "total_days": 135,
            "tips": "Drain field 10 days before harvest for easy cutting.",
        },
        "maize": {
            "sowing_months": [6, 7, 10],
            "sowing_advice": "Kharif: June-July. Rabi: October.",
            "watering": "Every 7-10 days. Critical at tasseling stage.",
            "fertilizer_timing": "Basal at sowing. Top dress at 25 and 45 days.",
            "harvest_months": [9, 10, 1],
            "harvest_advice": "Harvest when husks turn dry and brown.",
            "total_days": 100,
            "tips": "Earth up soil at 30 days to support the stem.",
        },
        "groundnut": {
            "sowing_months": [6, 7],
            "sowing_advice": "Sow at start of monsoon in June-July.",
            "watering": "Every 10 days. Stop watering 2 weeks before harvest.",
            "fertilizer_timing": "Apply gypsum at flowering — critical for pod filling.",
            "harvest_months": [10, 11],
            "harvest_advice": "Harvest when leaves yellow and pods have dark veins.",
            "total_days": 120,
            "tips": "Good for red soil in Karnataka. Needs well-drained conditions.",
        },
    }

    calendar = calendars.get(crop.lower())
    if not calendar:
        return {
            "status": "error",
            "message": f"No data for {crop}. Available: {', '.join(calendars.keys())}"
        }

    result = {"status": "success", "crop": crop, "calendar": calendar}

    # Add month-specific advice if month was provided
    if month:
        if month in calendar["sowing_months"]:
            result["current_advice"] = f"This is a good month to SOW {crop}! {calendar['sowing_advice']}"
        elif month in calendar["harvest_months"]:
            result["current_advice"] = f"This is harvest time for {crop}! {calendar['harvest_advice']}"
        else:
            result["current_advice"] = f"Growing period for {crop}. Focus on: {calendar['watering']}"

    return result


# ─── TOOL 6: SOIL ADVISOR ────────────────────────────────────────
# Karnataka has 5 major soil types. Each needs different management.
# Covers the most common soil types found across the state.

def get_soil_advice(soil_type: str, crop: str = "") -> dict:
    """Gives farming advice based on Karnataka soil types.
    Covers red, black, laterite, sandy, and loamy soils.

    Args:
        soil_type: Soil type e.g. red, black, laterite, sandy, loamy
        crop: Optional crop to check soil suitability
    Returns:
        dict with characteristics, improvement tips, crop suitability
    """
    soil_type = sanitize_input(soil_type)
    crop = sanitize_input(crop)

    # Soil profiles for Karnataka's 5 major soil types
    soil_data = {
        "red": {
            "local_name": "Red Soil (Kempu Manu) — very common across Karnataka",
            "suitable_crops": ["ragi", "groundnut", "maize", "pulses", "vegetables"],
            "characteristics": "Low fertility, good drainage, iron-rich but low nitrogen.",
            "improvement_tips": [
                "Add farmyard manure (FYM) 5 tonnes per acre before sowing.",
                "Apply lime if pH below 6.0 to reduce acidity.",
                "Use green manure crops like Dhaincha before main crop.",
                "Mulching helps retain moisture in dry periods.",
            ],
            "water_retention": "Low — needs more frequent irrigation.",
            "ph_range": "pH 6.0 to 7.0 — slightly acidic",
        },
        "black": {
            "local_name": "Black Cotton Soil (Regur) — common in North Karnataka",
            "suitable_crops": ["cotton", "jowar", "wheat", "sunflower", "chickpea"],
            "characteristics": "High fertility, holds water well, swells when wet.",
            "improvement_tips": [
                "Never till when wet — wait until slightly dry.",
                "Add gypsum to improve structure if waterlogged.",
                "Deep ploughing once a year breaks the hardpan.",
                "Excellent for dryland farming.",
            ],
            "water_retention": "Very High — risk of waterlogging.",
            "ph_range": "pH 7.0 to 8.5 — neutral to slightly alkaline",
        },
        "laterite": {
            "local_name": "Laterite Soil — common in Coastal Karnataka and Malnad",
            "suitable_crops": ["cashew", "rubber", "arecanut", "coconut", "banana"],
            "characteristics": "Hard when dry, iron-rich, low organic matter, acidic.",
            "improvement_tips": [
                "Apply 8-10 tonnes of compost per acre every season.",
                "Lime application essential before monsoon.",
                "Mulching with dry leaves retains moisture.",
                "Terracing on slopes prevents erosion.",
            ],
            "water_retention": "Medium — good for plantation crops.",
            "ph_range": "pH 5.0 to 6.5 — acidic",
        },
        "sandy": {
            "local_name": "Sandy Soil — found in river bank areas",
            "suitable_crops": ["groundnut", "watermelon", "vegetables", "sweet potato"],
            "characteristics": "Very low water retention, drains fast, low nutrients.",
            "improvement_tips": [
                "Add large amounts of compost and FYM every season.",
                "Use drip irrigation — water is lost very quickly.",
                "Apply fertilizer in small doses frequently.",
                "Mulching is essential to reduce evaporation.",
            ],
            "water_retention": "Very Low — needs drip irrigation.",
            "ph_range": "pH 6.0 to 7.0",
        },
        "loamy": {
            "local_name": "Loamy Soil — ideal farming soil",
            "suitable_crops": ["most crops", "vegetables", "fruits", "cereals", "pulses"],
            "characteristics": "Best mix of sand, silt and clay. High fertility.",
            "improvement_tips": [
                "Maintain organic matter with compost every season.",
                "Practice crop rotation to keep soil healthy.",
                "Avoid heavy machinery that compacts the soil.",
                "This is the best soil — focus on maintaining it.",
            ],
            "water_retention": "Good — best natural balance.",
            "ph_range": "pH 6.5 to 7.0 — neutral",
        },
    }

    soil = soil_data.get(soil_type.lower())
    if not soil:
        return {
            "status": "error",
            "message": f"Soil type not recognized. Try: red, black, laterite, sandy, or loamy."
        }

    result = {"status": "success", "soil_type": soil_type, "details": soil}

    # Check if the crop suits this soil type
    if crop:
        suitable = [c.lower() for c in soil["suitable_crops"]]
        if crop.lower() in suitable or "most crops" in suitable:
            result["crop_match"] = f"Good news — {crop} grows well in {soil_type} soil."
        else:
            result["crop_match"] = f"{crop} may not be ideal for {soil_type} soil. Better options: {', '.join(soil['suitable_crops'][:3])}."

    return result


# ─── ROOT AGENT ──────────────────────────────────────────────────
# This is the main ADK agent. It receives farmer messages,
# decides which tools to call, and synthesizes the final response.
# The instruction defines the agent's persona, behavior, and
# explicit tool usage rules.

root_agent = Agent(
    name="KrishiMitra",
    model="gemini-2.5-flash",
    description="AI farm advisory agent for Karnataka smallholder farmers.",
    instruction="""You are KrishiMitra, a friendly and knowledgeable farm
advisor for smallholder farmers in Karnataka, India. You give clear,
practical, locally-relevant advice in simple language.

Always greet with Namaste on the first message.
Reply in the same language the farmer uses:
- If they write in Kannada, reply in Kannada
- If they write in Hindi, reply in Hindi
- If they write in Telugu, reply in Telugu
- Default to English if unclear

Always:
- Ask for crop, location, and land size if not known
- Keep responses short and actionable
- Add a safety note before any chemical recommendation
- Be warm and encouraging — farming is hard work

You have 6 tools. Always use them instead of guessing:
- get_weather: when farmer asks about rain, irrigation, or spraying timing
- estimate_fertilizer: when farmer asks about fertilizer amounts or dosage
- find_schemes: when farmer asks about government support or subsidies
- diagnose_pest_disease: when farmer describes symptoms like yellow leaves,
  white powder, holes, wilting, or brown spots
- get_crop_calendar: when farmer asks about sowing, watering, or harvest timing
- get_soil_advice: when farmer mentions their soil type or asks about soil

Real data from tools is always better than guessing.
Never make up fertilizer amounts or disease diagnoses without tools.
""",
    tools=[
        get_weather,
        estimate_fertilizer,
        find_schemes,
        diagnose_pest_disease,
        get_crop_calendar,
        get_soil_advice,
    ],
)