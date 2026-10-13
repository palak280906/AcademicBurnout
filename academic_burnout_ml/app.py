"""
Flask Web Application for Early Detection of Academic Burnout
Author: B.Tech (Artificial Intelligence), Amity University
"""

import os
import io
import json
import joblib
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify, send_file, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
REPORT_DIR = os.path.join(BASE_DIR, "report")
TEMPLATES_DIR = os.path.join(BASE_DIR, "web", "templates")
STATIC_DIR = os.path.join(BASE_DIR, "web", "static")

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)

CLF_PATH = os.path.join(MODELS_DIR, "best_burnout_classifier.joblib")
REG_PATH = os.path.join(MODELS_DIR, "best_burnout_regressor.joblib")
METRICS_PATH = os.path.join(MODELS_DIR, "metrics_summary.json")
PDF_PATH = os.path.join(REPORT_DIR, "Thesis_Early_Detection_Academic_Burnout.pdf")
HTML_REPORT_PATH = os.path.join(REPORT_DIR, "Thesis_Early_Detection_Academic_Burnout.html")

# Load models at startup
clf_pipeline = joblib.load(CLF_PATH) if os.path.exists(CLF_PATH) else None
reg_pipeline = joblib.load(REG_PATH) if os.path.exists(REG_PATH) else None


def engineer_features(df):
    df_feat = df.copy()
    df_feat['Academic_Pressure_Index'] = df_feat['Assignment_Load'] * df_feat['Exam_Frequency']
    df_feat['Screen_Sleep_Ratio'] = df_feat['Screen_Time'] / (df_feat['Sleep_Hours'] + 0.5)
    df_feat['Social_Support_Deficit'] = df_feat['Peer_Pressure'] - df_feat['Family_Support']
    exercise_bonus = (df_feat['Physical_Exercise'].astype(str).str.lower() == 'yes').astype(float) * 2.0
    df_feat['Lifestyle_Balance_Score'] = (df_feat['Sleep_Hours'] + exercise_bonus) - ((df_feat['Social_Media_Use'] + df_feat['Screen_Time']) / 2.0)
    return df_feat


def generate_recommendations(profile, risk_level, stress_score):
    recs = []
    if risk_level == "High" or stress_score > 20:
        recs.append("[CRITICAL ACTION] High burnout risk detected. Connect student with academic counseling.")
    elif risk_level == "Medium" or stress_score > 10:
        recs.append("[EARLY WARNING] Moderate stress accumulating. Implement proactive workload rebalancing.")
    else:
        recs.append("[HEALTHY STATUS] Student maintains resilient study-life balance.")

    if profile.get('Sleep_Hours', 7) < 6:
        recs.append(f"Sleep Hygiene: Nightly sleep is only {profile['Sleep_Hours']}h. Target at least 7-8 hours to prevent cognitive exhaustion.")
    if profile.get('Screen_Time', 4) > 8:
        recs.append(f"Digital Detox: High screen time ({profile['Screen_Time']}h/day). Enforce scheduled screen breaks during exam cycles.")
    if profile.get('Assignment_Load', 4) >= 7 and profile.get('Exam_Frequency', 4) >= 7:
        recs.append(f"Academic Pacing: High concurrent assignment load ({profile['Assignment_Load']}/9) and exam frequency ({profile['Exam_Frequency']}/9). Spread deadlines.")
    if str(profile.get('Physical_Exercise', 'No')).lower() == 'no':
        recs.append("Physical Activity: Zero exercise reported. Recommend at least 30 minutes of aerobic activity 3 times/week to regulate cortisol.")
    if profile.get('Anxiety_Level', 3) >= 7:
        recs.append(f"Anxiety Management: Self-reported anxiety is elevated ({profile['Anxiety_Level']}/9). Offer mindfulness and stress-reduction workshops.")
    if profile.get('Peer_Pressure', 3) > profile.get('Family_Support', 5) + 2:
        recs.append("Psychosocial Support: Severe peer pressure outweighs family support. Foster peer mentorship networks.")

    return recs


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json(force=True)
        df_single = pd.DataFrame([data])
        df_feat = engineer_features(df_single)

        risk_pred = clf_pipeline.predict(df_feat)[0]
        risk_probs = clf_pipeline.predict_proba(df_feat)[0]
        classes = clf_pipeline.classes_
        prob_dict = {cls: float(prob) for cls, prob in zip(classes, risk_probs)}

        score_pred = float(reg_pipeline.predict(df_feat)[0])

        recs = generate_recommendations(data, risk_pred, score_pred)

        return jsonify({
            'success': True,
            'Predicted_Burnout_Level': risk_pred,
            'Risk_Probabilities': prob_dict,
            'Predicted_Stress_Score': round(score_pred, 2),
            'Recommendations': recs
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/batch-predict', methods=['POST'])
def api_batch_predict():
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        df = pd.read_csv(file)
        df_feat = engineer_features(df)

        risk_preds = clf_pipeline.predict(df_feat)
        score_preds = reg_pipeline.predict(df_feat)

        df['Predicted_Burnout_Level'] = risk_preds
        df['Predicted_Stress_Score'] = np.round(score_preds, 2)

        results = df.head(100).to_dict(orient='records')

        return jsonify({
            'success': True,
            'total_evaluated': len(df),
            'results': results
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/metrics', methods=['GET'])
def api_metrics():
    if os.path.exists(METRICS_PATH):
        with open(METRICS_PATH, 'r', encoding='utf-8') as f:
            metrics = json.load(f)
        return jsonify(metrics)
    return jsonify({'error': 'Metrics not found'}), 404


@app.route('/download-pdf')
def download_pdf():
    if os.path.exists(PDF_PATH):
        return send_file(PDF_PATH, as_attachment=True, download_name="Thesis_Early_Detection_Academic_Burnout.pdf")
    return "Thesis PDF not found.", 404


@app.route('/report-html')
def report_html():
    if os.path.exists(HTML_REPORT_PATH):
        return send_file(HTML_REPORT_PATH)
    return "HTML report not found.", 404


if __name__ == '__main__':
    print("="*60)
    print("Starting Early Detection of Academic Burnout Web Server...")
    print("Access application at: http://127.0.0.1:5000")
    print("="*60)
    app.run(host='0.0.0.0', port=5000, debug=False)
