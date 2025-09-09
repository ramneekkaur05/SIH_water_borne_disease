# app.py
import streamlit as st
import google.generativeai as genai

# -----------------------------
# Configure Gemini API
# -----------------------------
genai.configure(api_key="AIzaSyChb_aU84pPZda0Z4nnnrQPOVR-qmdP-JU")  # 🔑 Replace with your actual key
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Smart Health Surveillance", page_icon="💧", layout="centered")

st.title("💧 Smart Health Surveillance & Early Warning System")
st.markdown("### AI-based Prediction of Water-borne Diseases")

with st.form("prediction_form"):
    st.subheader("Enter Water Quality Details")

    source = st.selectbox("Water Source", ["Well", "River", "Tap", "Borewell", "Tank", "Pond"])
    ph = st.number_input("pH Level (5.0 - 9.5)", min_value=5.0, max_value=9.5, value=7.0, step=0.1)
    turbidity = st.number_input("Turbidity (0 - 20 NTU)", min_value=0.0, max_value=20.0, value=2.5, step=0.1)
    ecoli = st.selectbox("E.coli Presence", ["Yes", "No"])
    chlorine = st.number_input("Chlorine Residual (0 - 2 mg/L)", min_value=0.0, max_value=2.0, value=0.5, step=0.1)
    test_method = st.selectbox("Test Method", ["Chemical Kit", "IoT Sensor", "Lab Test", "Strip Test"])

    submitted = st.form_submit_button("🔮 Predict Disease with AI")

# -----------------------------
# AI Prediction
# -----------------------------
if submitted:
    prompt = f"""
    You are a health AI assistant.
    Based on the following water quality parameters:
    - Source: {source}
    - pH: {ph}
    - Turbidity: {turbidity} NTU
    - E.coli Presence: {ecoli}
    - Chlorine Residual: {chlorine} mg/L
    - Test Method: {test_method}

    Predict the most likely water-borne disease (choose from: Cholera, Typhoid, Diarrhea, Hepatitis A, or Safe).
    Also provide:
    1. Reason for this prediction (based on given values) in just 2-3 lines.
    """

    with st.spinner("🤖 AI is analyzing water quality... Please wait..."):
        try:
            response = gemini_model.generate_content(prompt)
            result = response.text if hasattr(response, "text") else "⚠️ No response generated."
        except Exception as e:
            result = f"❌ Error: {e}"

    st.success("### 🦠 AI Model Prediction")
    st.write(result)
