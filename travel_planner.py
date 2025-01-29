import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBRxOT6lcgk3EkhRAFxYGLx_eL3tq7q1J4")  # Replace with your Google API key

# Initializing the Gemini model gemini-pro
model = genai.GenerativeModel('gemini-pro')

# setting up the App Title
st.title("AI-Powered Travel Itinerary Planner")

# Step 1: Gathering User Inputs through interface
st.header("Step 1: Tell Us About Your Trip")
user_input = st.text_input("What kind of trip are you looking for? (e.g., relaxing, adventurous, cultural)")
budget = st.selectbox("What is your budget?", ["Low", "Moderate", "High"])
trip_duration = st.number_input("How many days will your trip be?", min_value=1, max_value=30)
destination = st.text_input("Where are you traveling to?")
purpose = st.selectbox("What is the purpose of your trip?", ["Leisure", "Business", "Family Visit", "Other"])
preferences = st.text_input("Any specific preferences? (e.g., food, activities, accommodation)")

# Step 2: Refining User Inputs (Optional)
st.header("Step 2: Refine Your Preferences")
dietary_preferences = st.text_input("Any dietary preferences? (e.g., vegetarian, vegan, gluten-free)")
interests = st.text_input("Specific interests? (e.g., museums, hiking, nightlife)")
walking_tolerance = st.selectbox("How much walking can you tolerate?", ["Low", "Moderate", "High"])
accommodation = st.selectbox("Preferred accommodation type?", ["Budget", "Mid-range", "Luxury"])

# Step 3: Generating Itinerary
if st.button("Generate Itinerary"):
    if not destination:
        st.error("Please enter a destination.")
    else:
        try:
            # Creating a prompt for Gemini to process and produce required itinerary
            prompt = f"""
            Create a detailed {trip_duration}-day travel itinerary for a trip to {destination} with a {budget} budget. 
            The purpose of the trip is {purpose}, and the traveler prefers {preferences}. 
            Dietary preferences: {dietary_preferences}. 
            Interests: {interests}. 
            Walking tolerance: {walking_tolerance}. 
            Accommodation: {accommodation}.

            The itinerary should include:
            1. Top-rated attractions or activities.
            2. Suggestions aligned with the user's preferences.
            3. Timing and grouping of activities for each day.
            4. Recommendations for meals and accommodations.

            Itinerary:
            """
            response = model.generate_content(prompt)
            itinerary = response.text

            # Display Itinerary
            st.header("Your Personalized Travel Itinerary")
            st.write(itinerary)

        except Exception as e:
            st.error(f"An error occurred: {e}")

# Hosting Instructions at the sidebar
st.sidebar.header("How to Use")
st.sidebar.write("1. Fill in your trip details in Step 1.")
st.sidebar.write("2. Refine your preferences in Step 2 (optional).")
st.sidebar.write("3. Click 'Generate Itinerary' to get your personalized travel plan.")