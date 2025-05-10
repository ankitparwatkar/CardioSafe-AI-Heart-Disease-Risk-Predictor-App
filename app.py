# CardioSafe AI Streamlit App
import streamlit as st
import joblib
import numpy as np
from streamlit.components.v1 import html

# Custom CSS and JavaScript
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def particle_js():
    return """
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <div id="particles-js" style="position:fixed;top:0;left:0;right:0;bottom:0;z-index:-1;"></div>
    <script>
    particlesJS('particles-js',
        {
            "particles": {
                "number": {"value": 80},
                "color": {"value": "#ffffff"},
                "shape": {"type": "circle"},
                "opacity": {"value": 0.5},
                "size": {"value": 3},
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#ffffff",
                    "opacity": 0.4,
                    "width": 1
                },
                "move": {
                    "enable": true,
                    "speed": 6,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {"enable": true, "mode": "repulse"},
                    "onclick": {"enable": true, "mode": "push"},
                    "resize": true
                }
            },
            "retina_detect": true
        }
    );
    </script>
    """

# Load custom CSS
local_css("style.css")

# Initialize particles
html(particle_js(), height=0, width=0)

# Load model
model = joblib.load('heart_disease.pkl')

# App Header
st.markdown("""
<div class="main-header">
    <h1>❤️ CardioSafe AI</h1>
    <p>Heart Disease Risk Prediction System</p>
</div>
""", unsafe_allow_html=True)

# Developer Info
with st.expander("Developer Profile", expanded=False):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("profile_image.jpeg", width=150)  # Replace with your image URL
    with col2:
        st.markdown("""
        **Developed by Ankit Parwatkar**  
        📍 Machine Learning Engineer | Healthcare AI Specialist  
        [![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/ankitparwatkar)  
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://linkedin.com/in/ankitparwatkar)
        """)

# Input Section
with st.form("prediction_form"):
    st.markdown("### 🩺 Patient Information")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Age", 20, 100, 40,
                       help="Select the patient's age")
        sex = st.selectbox("Gender", ["Male", "Female"],
                          help="Select biological gender")
        cp = st.selectbox("Chest Pain Type", [
            "Typical Angina", 
            "Atypical Angina", 
            "Non-anginal Pain", 
            "Asymptomatic"
        ], help="Type of chest pain experienced")
        
    with col2:
        trestbps = st.slider("Resting Blood Pressure (mm Hg)", 90, 200, 120,
                            help="Resting blood pressure measurement")
        chol = st.slider("Serum Cholesterol (mg/dl)", 100, 600, 200,
                        help="Cholesterol level in mg/dl")
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"],
                          help="Fasting blood sugar level")
    
    st.markdown("### 🏥 Medical Metrics")
    col3, col4 = st.columns(2)
    
    with col3:
        thalach = st.slider("Max Heart Rate Achieved", 70, 220, 150,
                           help="Maximum heart rate during exercise")
        exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"],
                            help="Chest pain during exercise?")
        
    with col4:
        oldpeak = st.slider("ST Depression Induced", 0.0, 6.2, 1.0,
                           help="ST depression measurement")
        slope = st.selectbox("ST Slope", [
            "Upsloping", 
            "Flat", 
            "Downsloping"
        ], help="Slope of peak exercise ST segment")

    # Convert inputs
    sex = 1 if sex == "Male" else 0
    cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp) + 1
    fbs = 1 if fbs == "Yes" else 0
    restecg = 0  # Placeholder based on your model's needs
    exang = 1 if exang == "Yes" else 0
    slope = ["Upsloping", "Flat", "Downsloping"].index(slope) + 1

    submit_button = st.form_submit_button("🚀 Analyze Risk")

# Prediction and Results
if submit_button:
    input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope]).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    
    st.markdown(f"""
    <div class="result-card {'high-risk' if prediction == 1 else 'low-risk'}">
        <h3>{"⚠️ High Risk Detected" if prediction == 1 else "✅ Low Risk"}</h3>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {probability*100}%"></div>
        </div>
        <p>Risk Probability: {probability*100:.1f}%</p>
    </div>
    """, unsafe_allow_html=True)
    
    if prediction == 1:
        st.error("""
        **Immediate Action Recommended:**
        - Consult a cardiologist immediately
        - Emergency contact: 112
        - Download [Heart Health Guide](https://github.com/ankitparwatkar/CardioSafe-AI-Heart-Disease-Risk-Predictor-App/blob/main/heart_health_guide.txt)
        """)
        st.session_state.balloons = False
    else:
        st.success("""
        **Maintenance Recommendations:**
        - Continue regular checkups
        - Download [Prevention Checklist](https://github.com/ankitparwatkar/CardioSafe-AI-Heart-Disease-Risk-Predictor-App/blob/main/prevention_checklist.txt)
        - Subscribe to health newsletter
        """)
        st.balloons()

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>© 2024 CardioSafe AI | Developed with ❤️ by Ankit Parwatkar</p>
    <div class="social-links">
        <a href="https://github.com/ankitparwatkar" target="_blank"><i class="fab fa-github"></i></a>
        <a href="https://linkedin.com/in/ankitparwatkar" target="_blank"><i class="fab fa-linkedin"></i></a>
        <a href="mailto:ankitparwatkar35@gmail.com"><i class="fas fa-envelope"></i></a>
    </div>
</div>
""", unsafe_allow_html=True)