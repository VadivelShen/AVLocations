from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
import streamlit as st
import os

# Set up API key for Google's Generative AI
os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Prompt template for generating location recommendations
location_template = "Provide the top 5 recommended places to visit in {location}"
Provide the top 5 recommended places to visit in {location}. 
Include a brief description of why each place is popular and must-visit for travelers.


location_prompt = PromptTemplate(template=location_template, input_variables=["location"])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Create the LLM chain for generating location recommendations
recommendation_chain = location_prompt | gemini_model

# Streamlit App Setup
st.header("Top Travel Location Recommendations")

# User Input: Location
location = st.text_input("Enter a location (city, state, or country):")

# Generate Recommendations Button
if st.button("Generate Recommendations"):
    if location.strip():
        # Invoke the chain with user input
        recommendations = recommendation_chain.invoke({"location": location})
        st.subheader("Top 5 Places to Visit in {location}")
        st.write(recommendations.content)
    else:
        st.warning("Please enter a valid location.")
