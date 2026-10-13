# Early Detection of Academic Burnout: End-to-End Machine Learning System

> **Major Project / B.Tech (Artificial Intelligence) Thesis**  
> **Department of Computer Science and Engineering**  
> **Amity School of Engineering and Technology, Amity University Jharkhand, Ranchi**  
> **Enrollment No:** A910119819008 | **Date:** October 2026  

---

## 📌 Project Overview
Academic burnout is an insidious syndrome characterized by **emotional exhaustion, cynicism/depersonalization toward studies, and perceived loss of academic competence**. Left unaddressed, it leads to cognitive fatigue, course failure, and student dropouts.

Traditional university mental health screening relies on periodic, retrospective self-assessment surveys (e.g., MBI-SS) that detect issues only after acute damage has occurred. 

This project delivers an **end-to-end Machine Learning and Clinical Decision-Support System** that proactively identifies early burnout risks using non-invasive lifestyle, pedagogical, and psychosocial parameters.

---

## 🚀 Key Results & Highlights
- **Dataset:** 3,000 verified university student records across National, Public, and Private tertiary institutions.
- **Novel Feature Engineering:** Formulated domain interaction terms:
  - $\text{Academic Pressure Index} = \text{Assignment Load} \times \text{Exam Frequency}$
  - $\text{Screen-to-Sleep Ratio} = \frac{\text{Screen Time}}{\text{Sleep Hours} + 0.5}$
  - $\text{Social Support Deficit} = \text{Peer Pressure} - \text{Family Support}$
  - $\text{Lifestyle Balance Score} = (\text{Sleep} + 2 \cdot \mathbb{I}_{\text{Exercise}}) - \frac{\text{Social Media} + \text{Screen}}{2}$
- **Classification Performance:** **Multinomial Logistic Regression** achieves **99.50% Cross-Validated Accuracy** (Macro F1: **0.9909**), beating Neural Nets (MLP: 97.53%), SVMs (94.73%), and Gradient Boosting (90.23%).
- **Continuous Score Regression:** Ridge Regression achieves an **$R^2 = 1.0000$** ($\text{MAE} = 0.00$, $\text{RMSE} = 0.01$) for granular burnout severity mapping.
- **Prescriptive Interventions:** Translates risk scores into actionable lifestyle and counseling recommendations (sleep hygiene, digital detox, deadline spacing, peer mentorship).
- **Official Thesis PDF:** Generated 17-page formal academic thesis matching the Amity University Jharkhand project template.

---

## 📁 Repository Structure
```
academic_burnout_ml/
├── data/
│   └── academic_burnout_dataset.csv          # 3,000 verified student records
├── figures/                                  # 300 DPI publication plots
│   ├── fig1_eda_distributions.png           # Feature distributions by burnout tier
│   ├── fig2_correlation_matrix.png          # Correlation matrix heatmap
│   ├── fig3_model_comparison.png             # 7-Model benchmark bar chart
│   ├── fig4_confusion_matrices.png           # Confusion matrices (counts & normalized)
│   ├── fig5_feature_importance.png           # Top 14 predictive features
│   └── fig6_stress_score_regression.png      # Continuous stress regression parity plot
├── models/
│   ├── best_burnout_classifier.joblib        # Serialized classification pipeline
│   ├── best_burnout_regressor.joblib         # Serialized continuous regressor
│   └── metrics_summary.json                  # All cross-validation and test metrics
├── report/
│   ├── Thesis_Early_Detection_Academic_Burnout.pdf   # 17-page compiled official thesis PDF
│   ├── Thesis_Early_Detection_Academic_Burnout.html  # Clean web thesis report
│   ├── Thesis_Early_Detection_Academic_Burnout.md    # Markdown thesis source
│   └── build_html_report.py                          # Report compilation script
├── src/
│   ├── pipeline.py                           # Full ML training, CV & plot generator
│   └── predict.py                            # CLI inference & recommendation engine
├── tests/
│   └── test_model.py                         # Automated unit & integration test suite
├── web/
│   ├── templates/index.html                  # Interactive Glassmorphic Web Dashboard
│   └── static/figures/                       # Static figures for dashboard
├── app.py                                    # Flask web application server
└── requirements.txt                          # Python package dependencies
run_project.py                                # Master orchestrator CLI script
```

---

## ⚡ Quickstart Guide

### 1. Installation
Ensure Python 3.10+ is installed:
```powershell
pip install -r academic_burnout_ml/requirements.txt
```

### 2. Run the Interactive Web Dashboard
```powershell
python run_project.py --web
```
Open your browser at: **`http://127.0.0.1:5000`**
- **Single Student Assessment:** Real-time sliders for live risk diagnosis.
- **Batch CSV Predictor:** Upload cohort CSV files and view/download predictions.
- **Model Analytics:** Embedded 300 DPI publication figures & benchmark tables.
- **Thesis Download:** Direct link to download the 17-page Thesis PDF.

### 3. Run Automated Tests
```powershell
python run_project.py --test
```

### 4. Run Terminal Inference Demo
```powershell
python run_project.py --predict
```

### 5. Re-train Pipeline & Re-compile PDF
```powershell
python run_project.py --all
```

---

## 📊 Cross-Validation Performance Benchmark

Evaluated across 3,000 students using 5-Fold Stratified Cross-Validation:

| Model Architecture | Accuracy (%) | Std Dev | Macro F1 | Macro Precision | Macro Recall |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Multinomial Logistic Regression** | **99.50%** | **±0.11%** | **0.9909** | **0.9933** | **0.9886** |
| **Multi-Layer Perceptron (MLP)** | 97.53% | ±0.34% | 0.9594 | 0.9618 | 0.9571 |
| **Support Vector Machine (RBF)** | 94.73% | ±0.89% | 0.9377 | 0.9536 | 0.9246 |
| **Gradient Boosting (GBM)** | 90.23% | ±0.83% | 0.8724 | 0.9131 | 0.8466 |
| **Extra Trees Classifier** | 85.40% | ±1.31% | 0.7801 | 0.9021 | 0.7426 |
| **Random Forest Classifier** | 85.17% | ±0.78% | 0.7945 | 0.8909 | 0.7565 |
| **K-Nearest Neighbors (KNN)** | 83.67% | ±1.74% | 0.7816 | 0.8531 | 0.7495 |

---

## 🌐 REST API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves the interactive web dashboard. |
| `POST` | `/api/predict` | JSON endpoint for single-student prediction and recommendations. |
| `POST` | `/api/batch-predict` | Multipart form endpoint for uploading a cohort CSV file. |
| `GET` | `/api/metrics` | Returns full cross-validation and model metrics JSON. |
| `GET` | `/download-pdf` | Downloads the compiled 17-page Thesis PDF. |
| `GET` | `/report-html` | Opens the styled web publication version of the thesis. |

---

## 🎓 Academic Thesis Details
- **Title:** Early Detection of Academic Burnout
- **Degree:** Bachelor of Technology in Artificial Intelligence — B.Tech (AI)
- **Institution:** Amity School of Engineering and Technology, Amity University Jharkhand
- **Structure:** Title Page, Certificate, Declaration, Abstract (Enrollment No. `A910119819008`), Acknowledgements, Table of Contents, Lists of Figures & Tables, Abbreviations, Chapters 1 to 6, Appendix A, and IEEE Bibliography.
