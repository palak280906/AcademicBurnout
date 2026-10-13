"""
Inference & Early Intervention Recommendation Engine for Academic Burnout
Author: B.Tech (Artificial Intelligence), Amity University
"""

import os
import argparse
import joblib
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
CLF_PATH = os.path.join(MODELS_DIR, "best_burnout_classifier.joblib")
REG_PATH = os.path.join(MODELS_DIR, "best_burnout_regressor.joblib")


def engineer_features_single(student_dict):
    df = pd.DataFrame([student_dict])
    # 1. Academic Pressure Index
    df['Academic_Pressure_Index'] = df['Assignment_Load'] * df['Exam_Frequency']
    # 2. Screen-to-Sleep Ratio
    df['Screen_Sleep_Ratio'] = df['Screen_Time'] / (df['Sleep_Hours'] + 0.5)
    # 3. Social Support Deficit
    df['Social_Support_Deficit'] = df['Peer_Pressure'] - df['Family_Support']
    # 4. Lifestyle Balance Score
    exercise_bonus = (df['Physical_Exercise'].str.lower() == 'yes').astype(float) * 2.0
    df['Lifestyle_Balance_Score'] = (df['Sleep_Hours'] + exercise_bonus) - ((df['Social_Media_Use'] + df['Screen_Time']) / 2.0)
    return df


def generate_recommendations(profile, risk_level, stress_score):
    recs = []
    if risk_level == "High" or stress_score > 20:
        recs.append("[CRITICAL ACTION] High burnout risk detected. Connect student with academic counseling.")
    elif risk_level == "Medium" or stress_score > 10:
        recs.append("[EARLY WARNING] Moderate stress accumulating. Implement proactive workload rebalancing.")
    else:
        recs.append("[HEALTHY STATUS] Student maintains resilient study-life balance.")

    if profile.get('Sleep_Hours', 7) < 6:
        recs.append(f"- Sleep Hygiene: Nightly sleep is only {profile['Sleep_Hours']}h. Target at least 7-8 hours to prevent cognitive exhaustion.")
    if profile.get('Screen_Time', 4) > 8:
        recs.append(f"- Digital Detox: High screen time ({profile['Screen_Time']}h/day). Enforce scheduled screen breaks during exam cycles.")
    if profile.get('Assignment_Load', 4) >= 7 and profile.get('Exam_Frequency', 4) >= 7:
        recs.append(f"- Academic Pacing: High concurrent assignment load ({profile['Assignment_Load']}/9) and exam frequency ({profile['Exam_Frequency']}/9). Spread deadlines.")
    if profile.get('Physical_Exercise', 'No').lower() == 'no':
        recs.append("- Physical Activity: Zero exercise reported. Recommend at least 30 minutes of aerobic activity 3 times/week to regulate cortisol.")
    if profile.get('Anxiety_Level', 3) >= 7:
        recs.append(f"- Anxiety Management: Self-reported anxiety is elevated ({profile['Anxiety_Level']}/9). Offer mindfulness and stress-reduction workshops.")
    if profile.get('Peer_Pressure', 3) > profile.get('Family_Support', 5) + 2:
        recs.append("- Psychosocial Support: Severe peer pressure outweighs family support. Foster peer mentorship networks.")

    return recs


def predict_student(student_data):
    if not os.path.exists(CLF_PATH) or not os.path.exists(REG_PATH):
        raise FileNotFoundError("Trained models not found. Run pipeline.py first.")

    clf_pipe = joblib.load(CLF_PATH)
    reg_pipe = joblib.load(REG_PATH)

    df_feats = engineer_features_single(student_data)
    
    # Classification prediction
    risk_pred = clf_pipe.predict(df_feats)[0]
    risk_probs = clf_pipe.predict_proba(df_feats)[0]
    classes = clf_pipe.classes_
    prob_dict = {cls: float(prob) for cls, prob in zip(classes, risk_probs)}

    # Regression prediction
    score_pred = float(reg_pipe.predict(df_feats)[0])

    recommendations = generate_recommendations(student_data, risk_pred, score_pred)

    return {
        'Predicted_Burnout_Level': risk_pred,
        'Risk_Probabilities': prob_dict,
        'Predicted_Stress_Score': round(score_pred, 2),
        'Recommendations': recommendations
    }


def main():
    parser = argparse.ArgumentParser(description="Predict student academic burnout risk level")
    parser.add_argument("--sample", action="store_true", help="Run benchmark predictions on sample profiles")
    args = parser.parse_args()

    sample_students = [
        {
            "name": "Student A (High Risk Profile)",
            "data": {
                "Age": 22, "Gender": "Female", "Study_Hours": 8, "Class_Attendance": 45,
                "Tuition": "Yes", "Exam_Frequency": 9, "Assignment_Load": 9, "Sleep_Hours": 4,
                "Physical_Exercise": "No", "Social_Media_Use": 6, "Screen_Time": 11,
                "Family_Income_Level": "Low", "Peer_Pressure": 9, "Family_Support": 2,
                "Anxiety_Level": 9, "University_Type": "National University"
            }
        },
        {
            "name": "Student B (Balanced / Low Risk Profile)",
            "data": {
                "Age": 20, "Gender": "Male", "Study_Hours": 6, "Class_Attendance": 92,
                "Tuition": "No", "Exam_Frequency": 3, "Assignment_Load": 2, "Sleep_Hours": 8,
                "Physical_Exercise": "Yes", "Social_Media_Use": 2, "Screen_Time": 3,
                "Family_Income_Level": "Medium", "Peer_Pressure": 2, "Family_Support": 8,
                "Anxiety_Level": 2, "University_Type": "Public University"
            }
        }
    ]

    print("\n" + "="*70)
    print("EARLY DETECTION OF ACADEMIC BURNOUT: INFERENCE ENGINE")
    print("="*70)

    for s in sample_students:
        print(f"\nEvaluating: {s['name']}")
        res = predict_student(s['data'])
        print(f"  > Predicted Burnout Category: {res['Predicted_Burnout_Level']}")
        print(f"  > Predicted Burnout Stress Score: {res['Predicted_Stress_Score']}")
        print("  > Category Confidence:")
        for k, v in res['Risk_Probabilities'].items():
            print(f"      - {k:<8}: {v*100:.2f}%")
        print("  > Tailored Institutional Recommendations:")
        for r in res['Recommendations']:
            print(f"    {r}")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
