import streamlit as st 
import numpy as np
import joblib
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mental Stress Assessment",
    page_icon="🧠",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("stress_model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------- FIXED CSS ----------------
st.markdown("""
<style>
/* Global */
.stApp {
    background-color: #F5F7FB;
    color: #1F2937;   
    font-family: 'Segoe UI', sans-serif;
}

/* Cards */
.card {
    background-color: #1E3A8A;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    color: #1F2937;
}

/* KPI Boxes */
.kpi-box {
    background: #F3F4F6;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-weight: 600;
}

/* Titles */
.section-title {
    font-size: 22px;
    font-weight: 600;
    color: #111827;
    margin-bottom: 15px;
}

.sub-title {
    font-size: 15px;
    color: #4B5563;
    margin-bottom: 20px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #4F46E5, #6366F1);
    color: white !important;
    font-size: 17px;
    font-weight: 600;
    height: 3.2em;
    border-radius: 12px;
    border: none;
}

/* Slider numbers */
.css-1qg05tj, .css-1y4p8pa {
    color: #1F2937 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="card">
    <h1 style="text-align:center; color:white;">🧠 Mental Stress Assessment</h1>
    <p style="text-align:center; color:white;">
    A machine learning-based system to evaluate stress levels in students
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- KPI BOXES BELOW HEADER (Professional Design) ----------------
st.markdown("<br>", unsafe_allow_html=True)

kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)

# Box 1: Total Factors
with kpi_col1:
    st.markdown("""
    <div style="
        background:#BE185D; 
        color:white; 
        padding:25px; 
        border-radius:16px; 
        text-align:center;
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
        <div style='font-size:20px; font-weight:600;'>📊 Total Factors</div>
        <div style='font-size:28px; font-weight:700; margin-top:5px;'>20</div>
    </div>
    """, unsafe_allow_html=True)

# Box 2: Psychological Factors
with kpi_col2:
    st.markdown("""
    <div style="
        background:#0D9488; 
        color:white; 
        padding:25px; 
        border-radius:16px; 
        text-align:center;
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
        <div style='font-size:20px; font-weight:600;'>🧠 Psychological</div>
        <div style='font-size:28px; font-weight:700; margin-top:5px;'>10</div>
    </div>
    """, unsafe_allow_html=True)

# Box 3: Academic & Environmental Factors
with kpi_col3:
    st.markdown("""
    <div style="
        background:#D97706; 
        color:white; 
        padding:25px; 
        border-radius:16px; 
        text-align:center;
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
        <div style='font-size:20px; font-weight:600;'>🎓 Academic & Env.</div>
        <div style='font-size:28px; font-weight:700; margin-top:5px;'>10</div>
    </div>
    """, unsafe_allow_html=True)

# Box 4: Prediction Classes
with kpi_col4:
    st.markdown("""
    <div style="
        background:#DC2626; 
        color:white; 
        padding:25px; 
        border-radius:16px; 
        text-align:center;
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);">
        <div style='font-size:20px; font-weight:600;'>🔮 Prediction Classes</div>
        <div style='font-size:28px; font-weight:700; margin-top:5px;'>3</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ---------------- LAYOUT ----------------
form_col, side_col = st.columns([3.2, 1.2])

# ---------------- FORM CARD ----------------
with form_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Stress Evaluation Form</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Rate each factor from 0 (Very Low) to 30 (Very High)</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    c1.markdown("### 🧠 Psychological Factors")
    c2.markdown("### 🎓 Academic & Environmental Factors")

    left_fields = [
        "Anxiety Level", "Self Esteem", "Mental Health History",
        "Depression", "Headache", "Blood Pressure",
        "Sleep Quality", "Breathing Problem",
        "Social Support", "Peer Pressure"
    ]

    right_fields = [
        "Noise Level", "Living Conditions", "Safety",
        "Basic Needs", "Academic Performance",
        "Study Load", "Teacher Student Relationship",
        "Future Career Concerns", "Extracurricular Activities",
        "Bullying"
    ]

    inputs = []

    col1, col2 = st.columns(2)
    with col1:
        for field in left_fields:
            st.markdown(f"<div style='font-weight:500; margin-bottom:3px;'>{field}</div>", unsafe_allow_html=True)
            inputs.append(st.slider(field, 0, 30, 5))
    with col2:
        for field in right_fields:
            st.markdown(f"<div style='font-weight:500; margin-bottom:3px;'>{field}</div>", unsafe_allow_html=True)
            inputs.append(st.slider(field, 0, 30, 5))

# ---------------- LEFT-ALIGNED PREDICTION BUTTON ----------------
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔍 Predict Stress Level"):
    input_array = np.array([inputs])
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]

    st.markdown('<div class="section-title">📊 Assessment Result</div>', unsafe_allow_html=True)

    if prediction == 0:
        st.markdown("""
        <div style="
            background-color:#D1FAE5; 
            color:#065F46; 
            padding:15px; 
            border-radius:12px; 
            font-size:18px;
            font-weight:600;
        ">
        Low Stress 😌 — You appear mentally balanced.You are currently experiencing a low level of stress. This indicates good emotional balance and healthy coping habits. Keep maintaining a positive lifestyle, regular physical activity, and proper rest to stay well.
        </div>
        """, unsafe_allow_html=True)

    elif prediction == 1:
        st.markdown("""
        <div style="
            background-color:#FEF3C7; 
            color:#78350F; 
            padding:15px; 
            border-radius:12px; 
            font-size:18px;
            font-weight:600;
        ">
        Moderate Stress 😐 — You may be experiencing a moderate level of stress. This is common and manageable, but it’s important to pay attention to your mental well-being. Consider taking short breaks, practicing relaxation techniques, and maintaining a balanced routine.Consider improving stress management.
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div style="
            background-color:#FECACA; 
            color:#991B1B; 
            padding:15px; 
            border-radius:12px; 
            font-size:18px;
            font-weight:600;
        ">
        High Stress 😟 — You are experiencing a high level of stress, which may affect your mental and physical health. It is strongly recommended to seek support, reduce workload where possible, practice stress-relief activities, and consider consulting a mental health professional..Professional support is recommended.
        </div>
        """, unsafe_allow_html=True)


# ---------------- SIDE CARD ----------------
with side_col:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💡 Wellness Tips</div>', unsafe_allow_html=True)

    # Removed useless yellow box above image
    image_path = "C:/Users/Muhammad Afraz Khan/Desktop/Mental-Stress-App/mentalwellness.jpg"
    if os.path.exists(image_path):
        st.image(image_path, width=300)
    else:
        st.image("https://i.imgur.com/0Z8iF4V.png", width=300)

    st.markdown("""
    🛌 Maintain a consistent sleep schedule  
    🧘 Practice breathing or meditation exercises  
    📚 Manage academic workload effectively  
    🏃‍♂️ Exercise regularly  
    🍎 Eat a balanced and healthy diet  
    💧 Stay hydrated  
    🧑‍🤝‍🧑 Stay socially connected with friends/family  
    🎨 Engage in hobbies or creative activities  
    🎓 Take breaks during study sessions  
    📅 Plan and prioritize tasks  
    🗣️ Speak to a counselor/mentor when needed  
    🖥️ Limit excessive screen time  
    🌳 Spend time outdoors in nature  
    🎶 Listen to calming music  
    📝 Keep a journal to track thoughts & feelings  
    🤝 Participate in group activities or clubs  
    🛑 Avoid procrastination, last-minute stress  
    😌 Practice positive self-talk & mindfulness  

    """)
    st.markdown('</div>', unsafe_allow_html=True)
