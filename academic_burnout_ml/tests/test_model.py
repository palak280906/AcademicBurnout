"""
Comprehensive Unit & Integration Test Suite for Academic Burnout ML System
"""

import os
import unittest
import json
import joblib
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "academic_burnout_dataset.csv")
MODELS_DIR = os.path.join(BASE_DIR, "models")
CLF_PATH = os.path.join(MODELS_DIR, "best_burnout_classifier.joblib")
REG_PATH = os.path.join(MODELS_DIR, "best_burnout_regressor.joblib")
PDF_PATH = os.path.join(BASE_DIR, "report", "Thesis_Early_Detection_Academic_Burnout.pdf")

from academic_burnout_ml.app import app, engineer_features, generate_recommendations


class TestAcademicBurnoutML(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        self.sample_high_risk = {
            "Age": 22, "Gender": "Female", "Study_Hours": 8, "Class_Attendance": 45,
            "Tuition": "Yes", "Exam_Frequency": 9, "Assignment_Load": 9, "Sleep_Hours": 4,
            "Physical_Exercise": "No", "Social_Media_Use": 6, "Screen_Time": 11,
            "Family_Income_Level": "Low", "Peer_Pressure": 9, "Family_Support": 2,
            "Anxiety_Level": 9, "University_Type": "National University"
        }

        self.sample_low_risk = {
            "Age": 20, "Gender": "Male", "Study_Hours": 6, "Class_Attendance": 92,
            "Tuition": "No", "Exam_Frequency": 3, "Assignment_Load": 2, "Sleep_Hours": 8,
            "Physical_Exercise": "Yes", "Social_Media_Use": 2, "Screen_Time": 3,
            "Family_Income_Level": "Medium", "Peer_Pressure": 2, "Family_Support": 8,
            "Anxiety_Level": 2, "University_Type": "Public University"
        }

    def test_01_dataset_integrity(self):
        """Verify dataset exists, has 3,000 rows and 18 attributes"""
        self.assertTrue(os.path.exists(DATA_PATH), "Dataset file missing!")
        df = pd.read_csv(DATA_PATH)
        self.assertEqual(df.shape, (3000, 18), f"Unexpected dataset shape: {df.shape}")
        expected_cols = [
            'Age', 'Gender', 'Study_Hours', 'Class_Attendance', 'Tuition',
            'Exam_Frequency', 'Assignment_Load', 'Sleep_Hours', 'Physical_Exercise',
            'Social_Media_Use', 'Screen_Time', 'Family_Income_Level', 'Peer_Pressure',
            'Family_Support', 'Anxiety_Level', 'University_Type', 'Stress_Score', 'Stress_Level'
        ]
        self.assertListEqual(list(df.columns), expected_cols)

    def test_02_feature_engineering(self):
        """Verify engineered features are calculated accurately"""
        df_raw = pd.DataFrame([self.sample_high_risk])
        df_feat = engineer_features(df_raw)

        self.assertIn('Academic_Pressure_Index', df_feat.columns)
        self.assertIn('Screen_Sleep_Ratio', df_feat.columns)
        self.assertIn('Social_Support_Deficit', df_feat.columns)
        self.assertIn('Lifestyle_Balance_Score', df_feat.columns)

        # Check values
        self.assertEqual(df_feat['Academic_Pressure_Index'].iloc[0], 9 * 9)
        self.assertAlmostEqual(df_feat['Screen_Sleep_Ratio'].iloc[0], 11 / (4 + 0.5), places=2)
        self.assertEqual(df_feat['Social_Support_Deficit'].iloc[0], 9 - 2)

    def test_03_classifier_inference(self):
        """Verify classifier model loads and predicts proper classes"""
        self.assertTrue(os.path.exists(CLF_PATH), "Classifier model file missing!")
        clf = joblib.load(CLF_PATH)

        df_high = engineer_features(pd.DataFrame([self.sample_high_risk]))
        pred_high = clf.predict(df_high)[0]
        self.assertEqual(pred_high, "High", f"Expected High, got {pred_high}")

        df_low = engineer_features(pd.DataFrame([self.sample_low_risk]))
        pred_low = clf.predict(df_low)[0]
        self.assertEqual(pred_low, "Low", f"Expected Low, got {pred_low}")

    def test_04_regressor_inference(self):
        """Verify regressor model loads and predicts continuous stress score"""
        self.assertTrue(os.path.exists(REG_PATH), "Regressor model file missing!")
        reg = joblib.load(REG_PATH)

        df_high = engineer_features(pd.DataFrame([self.sample_high_risk]))
        score_high = float(reg.predict(df_high)[0])
        self.assertGreater(score_high, 20.0, "High risk student should have score > 20")

        df_low = engineer_features(pd.DataFrame([self.sample_low_risk]))
        score_low = float(reg.predict(df_low)[0])
        self.assertLess(score_low, 10.0, "Low risk student should have score < 10")

    def test_05_recommendations_generation(self):
        """Verify prescriptive recommendations are generated based on risk"""
        recs_high = generate_recommendations(self.sample_high_risk, "High", 38.0)
        self.assertTrue(any("CRITICAL ACTION" in r for r in recs_high))
        self.assertTrue(any("Sleep Hygiene" in r for r in recs_high))

        recs_low = generate_recommendations(self.sample_low_risk, "Low", 5.0)
        self.assertTrue(any("HEALTHY STATUS" in r for r in recs_low))

    def test_06_flask_api_predict(self):
        """Verify Flask API POST /api/predict returns valid JSON response"""
        response = self.app.post('/api/predict', json=self.sample_high_risk)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['Predicted_Burnout_Level'], 'High')
        self.assertIn('Risk_Probabilities', data)
        self.assertIn('Predicted_Stress_Score', data)
        self.assertIsInstance(data['Recommendations'], list)

    def test_07_pdf_compiled_report_exists(self):
        """Verify Thesis PDF exists and has valid non-zero size"""
        self.assertTrue(os.path.exists(PDF_PATH), "Compiled Thesis PDF missing!")
        size = os.path.getsize(PDF_PATH)
        self.assertGreater(size, 1000000, "Thesis PDF is smaller than expected (<1MB)")


if __name__ == '__main__':
    unittest.main()
