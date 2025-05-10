# CardioSafe-AI-Heart-Disease-Risk-Predictor-App
```markdown
# ❤️ CardioSafe AI - Heart Disease Risk Prediction System

![Streamlit App](https://cardiosafe-ai-heart-disease-risk-predictor-app-ankit-parwatkar.streamlit.app/)
![GitHub last commit](https://github.com/ankitparwatkar/CardioSafe-AI-Heart-Disease-Risk-Predictor-App)

An intelligent web application that predicts cardiovascular disease risk using machine learning. Designed for both patients and healthcare professionals with an interactive clinical interface.

<div align="center">
  <img src="Screenshot 2025-05-10 211208.png" width="800" alt="App Interface">
</div>

## 🌟 Features

- **Patient Risk Assessment**  
  Input 11 clinical parameters including age, cholesterol levels, and ECG metrics
- **Real-Time Prediction**  
  Instant risk classification with probability percentage
- **Clinical Guidance**  
  Actionable recommendations based on risk level
- **Interactive Visualization**  
  Dynamic progress bars and particle effects
- **Responsive Design**  
  Mobile-friendly interface with clinical-grade UI

## 🚀 Try the Live Demo

[![Open in Streamlit](https://cardiosafe-ai-heart-disease-risk-predictor-app-ankit-parwatkar.streamlit.app/)]

## 📥 Installation

1. Clone repository:
   ```bash
   git clone https://github.com/ankitparwatkar/CardioSafe-AI-Heart-Disease-Risk-Predictor-App.git
   cd CardioSafe-AI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📊 Dataset Overview

| Parameter | Description | Range |
|-----------|-------------|-------|
| Age | Patient's age in years | 20-100 |
| Resting BP | Blood pressure (mm Hg) | 90-200 |
| Cholesterol | Serum level (mg/dl) | 100-600 |
| ST Depression | Exercise-induced measurement | 0-6.2 |
| Max Heart Rate | Achieved during test | 70-220 |

**Target Variable**: Risk Percentage %

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Classifier (Pre-trained)
- **Accuracy**: 92.4% on test set
- **Features**: 11 clinical parameters
- **Output**: Risk probability with interpretable results

## 📸 Application Highlights

<div align="center">
  <img src="Screenshot 2025-05-10 211314.png" width="400" alt="Input Section">
  <img src="Screenshot 2025-05-10 211346.png" width="400" alt="Results View">
</div>

## 🛠️ Technical Stack

- **Frontend**: Streamlit + Custom CSS
- **Backend**: Python 3.9+
- **ML Framework**: Scikit-learn + XGBoost
- **Visualization**: Particles.js + Animated CSS

## 👨💻 Developer Profile

**Ankit Parwatkar**  
📍 Machine Learning Engineer | Healthcare AI Specialist

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/ankitparwatkar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://linkedin.com/in/ankitparwatkar)
[![Email](https://img.shields.io/badge/Contact-Email-red?logo=gmail)](mailto:ankitparwatkar35@gmail.com)


---

**⚠️ Clinical Disclaimer**: This tool provides risk estimations and should not replace professional medical advice. Always consult a qualified healthcare provider for diagnosis and treatment.
```
