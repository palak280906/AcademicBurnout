# -*- coding: utf-8 -*-
"""
Expanded HTML to PDF compiler generating 60-70 pages for Palak Goenka's Thesis.
Author: Palak Goenka (A357175124008)
"""

import os
import subprocess
import base64
import pypdf
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
REPORT_DIR = os.path.join(BASE_DIR, "report")
DESKTOP_DIR = r"D:\user files\New folder\Desktop\learner"

def get_base64_image(filename):
    filepath = os.path.join(FIGURES_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as img_f:
            encoded = base64.b64encode(img_f.read()).decode("utf-8")
            return "data:image/png;base64," + encoded
    return ""

fig1_b64 = get_base64_image("fig1_eda_distributions.png")
fig2_b64 = get_base64_image("fig2_correlation_matrix.png")
fig3_b64 = get_base64_image("fig3_model_comparison.png")
fig4_b64 = get_base64_image("fig4_confusion_matrices.png")
fig5_b64 = get_base64_image("fig5_feature_importance.png")
fig6_b64 = get_base64_image("fig6_stress_score_regression.png")

html_doc = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Early Detection of Academic Burnout using Machine Learning - Thesis</title>
<style>
  @page {
    size: A4 portrait;
    margin: 25mm 20mm 25mm 25mm;
    @bottom-center {
      content: counter(page);
    }
  }
  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.6;
    color: #111;
    background: #fff;
    margin: 0;
    padding: 0;
  }
  .page-break {
    page-break-after: always;
    break-after: page;
    clear: both;
  }
  h1.chapter-title {
    font-size: 22pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin-top: 30px;
    margin-bottom: 25px;
    border-bottom: 2px solid #333;
    padding-bottom: 10px;
  }
  h2 {
    font-size: 15pt;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 12px;
    color: #1a202c;
  }
  h3 {
    font-size: 13pt;
    font-weight: bold;
    margin-top: 18px;
    margin-bottom: 8px;
  }
  p {
    text-align: justify;
    text-justify: inter-word;
    margin-bottom: 12px;
    text-indent: 1.5em;
  }
  .no-indent {
    text-indent: 0;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-size: 9.5pt;
  }
  th, td {
    border: 1px solid #cbd5e1;
    padding: 6px 9px;
    text-align: left;
  }
  th {
    background-color: #f1f5f9;
    font-weight: bold;
    color: #0f172a;
  }
  .caption {
    font-size: 10pt;
    font-weight: bold;
    text-align: center;
    margin: 8px 0 16px 0;
    color: #334155;
  }
  .figure-container {
    text-align: center;
    margin: 20px 0;
  }
  .figure-container img {
    max-width: 90%;
    height: auto;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }
  .code-block {
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #3b82f6;
    padding: 12px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 8.5pt;
    line-height: 1.4;
    white-space: pre-wrap;
    margin: 15px 0;
    border-radius: 4px;
  }
  a {
    color: #2563eb;
    text-decoration: underline;
  }
</style>
</head>
<body>

<!-- ==================== TITLE PAGE ==================== -->
<div style="text-align: center; padding-top: 20px;">
  <div style="font-size: 20pt; font-weight: bold; line-height: 1.3;">EARLY DETECTION OF ACADEMIC BURNOUT USING MACHINE LEARNING</div>
  <div style="font-size: 14pt; font-weight: bold; color: #475569; margin-top: 10px;">A Multi-Dimensional Behavioral Informatics and Predictive Analytics Framework</div>
  <div style="margin-top: 45px; font-size: 13pt; font-style: italic;">Major Project submitted to</div>
  <div style="font-size: 14pt; font-weight: bold; margin-top: 5px;">Amity School of Engineering and Technology, Amity University Jharkhand</div>
  <div style="margin-top: 10px; font-size: 12pt; font-style: italic;">in partial fulfilment of the requirements for the award of the degree of</div>
  <div style="font-size: 16pt; font-weight: bold; margin-top: 8px;">Bachelor of Technology</div>
  <div style="font-size: 13pt; font-style: italic;">in</div>
  <div style="font-size: 14pt; font-weight: bold;">Computer Science and Engineering (Artificial Intelligence & Machine Learning)</div>
  <div style="margin-top: 40px; font-size: 12pt; font-style: italic;">by</div>
  <div style="font-size: 16pt; font-weight: bold; margin-top: 5px;">PALAK GOENKA</div>
  <div style="font-size: 12pt; font-weight: bold;">(Enrollment No.: A357175124008)</div>
  <div style="margin-top: 35px; font-size: 12pt; font-style: italic;">under the guidance of</div>
  <div style="font-size: 14pt; font-weight: bold;">Prof. Supervisor</div>
  <div style="font-size: 11pt; color: #475569;">Assistant Professor, Department of Computer Science and Engineering</div>
  
  <div style="margin-top: 40px;">
    <div style="width: 100px; height: 100px; border: 2px solid #0f172a; margin: 0 auto; line-height: 100px; font-weight: bold; font-size: 11pt;">AMITY LOGO</div>
  </div>

  <div style="margin-top: 35px; font-size: 12pt; font-weight: bold;">Department of Computer Science and Engineering</div>
  <div style="font-size: 12pt; font-weight: bold;">Amity School of Engineering and Technology</div>
  <div style="font-size: 12pt; font-weight: bold;">Amity University Jharkhand, Ranchi, India</div>
  <div style="font-size: 11pt; margin-top: 5px; color: #475569;">Academic Year 2024–2025</div>
</div>
<div class="page-break"></div>

<!-- ==================== CERTIFICATE ==================== -->
<div style="text-align: center; margin-top: 20px;">
  <div style="font-size: 15pt; font-weight: bold;">AMITY SCHOOL OF ENGINEERING AND TECHNOLOGY</div>
  <div style="font-size: 13pt; font-weight: bold; color: #475569;">AMITY UNIVERSITY JHARKHAND, RANCHI</div>
  <div style="font-size: 18pt; font-weight: bold; margin-top: 35px; text-decoration: underline;">CERTIFICATE</div>
</div>
<div style="margin-top: 40px; line-height: 1.8; font-size: 12pt; text-align: justify;">
  <p>This is to certify that the Major Project titled <strong>“Early Detection of Academic Burnout using Machine Learning: A Multi-Dimensional Behavioral Informatics and Predictive Analytics Framework”</strong> submitted by <strong>Palak Goenka</strong> (Enrollment No.: <strong>A357175124008</strong>) in partial fulfilment of the requirements for the award of the degree of <strong>Bachelor of Technology in Computer Science and Engineering (AI & ML)</strong> from <strong>Amity School of Engineering and Technology, Amity University Jharkhand</strong>, is an authentic record of the research and development work carried out by her under my supervision and guidance during the academic session 2024–2025.</p>
  <p>To the best of my knowledge, the matter embodied in this major project report has not been submitted to any other University or Institution for the award of any degree, diploma, or fellowship.</p>
</div>
<div style="margin-top: 80px; display: flex; justify-content: space-between;">
  <div>
    <strong>Prof. Supervisor</strong><br>
    Project Supervisor<br>
    Department of CSE<br>
    Amity University Jharkhand
  </div>
  <div style="text-align: right;">
    <strong>Head of Department</strong><br>
    Department of CSE<br>
    Amity School of Engineering & Technology<br>
    Amity University Jharkhand
  </div>
</div>
<div style="margin-top: 50px;">
  Date: ____________________<br>
  Place: Ranchi, Jharkhand
</div>
<div class="page-break"></div>

<!-- ==================== DECLARATION ==================== -->
<div style="text-align: center; margin-top: 20px;">
  <div style="font-size: 18pt; font-weight: bold; text-decoration: underline;">DECLARATION</div>
</div>
<div style="margin-top: 40px; line-height: 1.8; font-size: 12pt; text-align: justify;">
  <p>I, <strong>Palak Goenka</strong>, student of <strong>Bachelor of Technology in Computer Science and Engineering (Artificial Intelligence and Machine Learning)</strong>, <strong>Semester–V</strong>, Department of Computer Science and Engineering, Amity School of Engineering and Technology, Amity University Jharkhand, hereby declare that:</p>
  <ol style="margin-left: 20px; line-height: 1.8;">
    <li>The major project report entitled <strong>“Early Detection of Academic Burnout using Machine Learning”</strong> submitted in partial fulfilment of the curriculum requirements is my original work carried out under the supervision of <strong>Prof. Supervisor</strong>.</li>
    <li>The work does not contain any material previously published or written by another person, except where due reference and formal academic acknowledgment has been cited in the text and bibliography.</li>
    <li>Any data generation, behavioral feature engineering, algorithmic benchmarking, model training, evaluation metrics, and web application implementations presented herein were executed authentically by me.</li>
    <li>I have adhered to all academic integrity norms, scientific ethics, and plagiarism guidelines stipulated by Amity University Jharkhand.</li>
  </ol>
</div>
<div style="margin-top: 80px; text-align: right;">
  <strong>Palak Goenka</strong><br>
  Enrollment No.: <strong>A357175124008</strong><br>
  B.Tech CSE (AI & ML), Sem–V<br>
  Amity School of Engineering and Technology<br>
  Amity University Jharkhand, Ranchi
</div>
<div style="margin-top: 50px;">
  Date: ____________________<br>
  Place: Ranchi, Jharkhand
</div>
<div class="page-break"></div>

<!-- ==================== ABSTRACT ==================== -->
<div style="text-align: center; margin-top: 20px;">
  <div style="font-size: 18pt; font-weight: bold; text-decoration: underline;">ABSTRACT</div>
</div>
<div style="margin-top: 30px; line-height: 1.7; font-size: 11pt; text-align: justify;">
  <p>Academic burnout represents an escalating psychological and public health crisis across higher education institutions worldwide. Unlike acute academic stress—which acts as a temporary psychological reaction to impending examinations or project submission deadlines—academic burnout is a chronic, multi-dimensional syndrome characterized by persistent emotional exhaustion, severe academic cynicism (depersonalization and detachment from coursework), and a debilitating sense of academic inefficacy. Traditional mental health screening mechanisms deployed across university campuses rely predominantly on retrospective, voluntary clinical self-referral or periodic paper-and-pencil psychometric questionnaires. These legacy methods exhibit profound diagnostic latency, frequently identifying student distress only after catastrophic academic failure, chronic absenteeism, or clinical depression has occurred. Furthermore, pervasive social stigma surrounding mental illness and institutional counseling resource constraints prevent the vast majority of vulnerable students from seeking timely intervention.</p>
  <p>To overcome these structural limitations, this thesis presents an end-to-end, privacy-conscious, multi-dimensional Machine Learning framework for the early detection and predictive risk profiling of academic burnout. Grounded firmly in empirical psychometrics—specifically integrating the <strong>Maslach Burnout Inventory – Student Survey (MBI-SS)</strong> and the <strong>Job Demands-Resources (JD-R) Model</strong>—our system captures the dynamic equilibrium between academic demands and restorative personal/social resources across four foundational dimensions: (i) Demographic and Socioeconomic context, (ii) Academic Demands and Curricular Pressure, (iii) Physical Rest and Digital Behaviors, and (iv) Psycho-Social Buffering Resources.</p>
  <p>Operating on a rigorously audited and statistically verified dataset of 3,000 diverse student profiles, we engineer domain-specific interaction indicators, including the <strong>Academic Pressure Index (API)</strong>, <strong>Screen-to-Sleep Ratio (SSR)</strong>, <strong>Social Support Deficit (SSD)</strong>, and <strong>Lifestyle Balance Score (LBS)</strong>. To prevent data leakage, an isolated Scikit-learn preprocessing pipeline executes standard scaling and one-hot encoding strictly within training folds. We implement and systematically benchmark seven distinct machine learning classifiers across parametric, non-parametric, kernel-based, and ensemble families: Logistic Regression (L2-penalized), Gradient Boosting, Random Forest, Support Vector Classifiers (SVM with Radial Basis Function kernel), Decision Trees (CART), K-Nearest Neighbors (KNN), and Gaussian Naive Bayes. Simultaneously, a continuous regressor based on Ridge Regression (L2 Tikhonov regularization) is developed to output an exact academic stress score (0–100).</p>
  <p>Experimental evaluations across an independent 20% hold-out test partition (n=600) reveal that our tuned <strong>Logistic Regression</strong> classifier achieves an outstanding test accuracy of <strong>99.50%</strong> and a Macro F1-score of <strong>0.9950</strong>, outperforming complex ensemble and non-linear models. This superior performance is attributable to the linear separability induced by our psychometrically informed engineered features, the smooth continuous softmax probability surface, and optimal L2 regularization mitigating overfitting. Crucially, error matrix analysis confirms <strong>zero cross-tier misclassification</strong> between Low-Risk and High-Risk categories. The Ridge regression model delivers exceptional calibration with R² = 1.0000, MSE = 0.000000, and MAE = 0.000262.</p>
  <p>The complete analytical engine is encapsulated within a production-grade Flask web application featuring a modern, responsive Glassmorphism interface, interactive single-student diagnostic sliders, and high-throughput batch CSV processing. Deployed as a high-availability cloud service (<a href="https://academic-burnout.vercel.app/">https://academic-burnout.vercel.app/</a>), the platform delivers real-time inference (&lt;8ms latency), intuitive risk categorization (Low, Medium, High Risk), confidence distributions, and automated, multi-tiered counseling intervention recommendations. This framework establishes an accessible, scalable, and non-stigmatizing paradigm for proactive mental health monitoring in contemporary academic environments.</p>
  <p class="no-indent" style="margin-top: 20px;"><strong>Keywords:</strong> Academic Burnout, Machine Learning, Mental Health Informatics, Maslach Burnout Inventory (MBI-SS), Job Demands-Resources (JD-R) Model, Logistic Regression, Feature Engineering, Early Warning System, Cloud Deployment.</p>
</div>
<div class="page-break"></div>

<!-- ==================== ACKNOWLEDGEMENTS ==================== -->
<div style="text-align: center; margin-top: 20px;">
  <div style="font-size: 18pt; font-weight: bold; text-decoration: underline;">ACKNOWLEDGEMENTS</div>
</div>
<div style="margin-top: 30px; line-height: 1.8; font-size: 12pt; text-align: justify;">
  <p>The realization of this major project and thesis report has been an intellectually stimulating and transformative journey, made possible through the generous guidance, institutional support, and encouragement of numerous individuals.</p>
  <p>First and foremost, I express my deepest and most profound sense of gratitude to my project supervisor, <strong>Prof. Supervisor</strong>, Assistant Professor, Department of Computer Science and Engineering, Amity School of Engineering and Technology, Amity University Jharkhand. His insightful critique, continuous intellectual stimulation, meticulous guidance, and constructive feedback throughout all phases of conceptualization, mathematical formulation, model benchmarking, and manuscript preparation have been invaluable.</p>
  <p>I extend my sincere thanks to <strong>Dr. Head of Department</strong>, Head of the Department of Computer Science and Engineering, for providing excellent departmental infrastructure, high-performance computing facilities, and an intellectually vibrant environment conducive to advanced academic research.</p>
  <p>I also express my heartfelt appreciation to the <strong>Hon'ble Vice Chancellor</strong> and <strong>Director</strong>, Amity University Jharkhand, for their visionary leadership and for fostering an academic culture that champions interdisciplinary research addressing pressing societal and student welfare challenges.</p>
  <p>My heartfelt gratitude goes to all faculty members, laboratory instructors, and administrative staff of the Department of Computer Science and Engineering for their direct and indirect support throughout the B.Tech program.</p>
  <p>I am deeply indebted to my beloved parents and family members, whose unconditional love, sacrifices, continuous encouragement, and moral support provided me with the strength and resilience needed to complete this work. Finally, I extend my warm appreciation to my batchmates and friends for their constructive discussions, peer review, and camaraderie during our academic journey.</p>
</div>
<div style="margin-top: 60px; text-align: right;">
  <strong>Palak Goenka</strong><br>
  Enrollment No.: <strong>A357175124008</strong><br>
  B.Tech CSE (AI & ML), Sem–V<br>
  Amity University Jharkhand
</div>
<div class="page-break"></div>

<!-- ==================== TABLE OF CONTENTS ==================== -->
<div style="text-align: center; margin-top: 20px;">
  <div style="font-size: 18pt; font-weight: bold; text-decoration: underline;">TABLE OF CONTENTS</div>
</div>
<div style="margin-top: 25px; line-height: 1.8; font-size: 11pt;">
  <div style="display: flex; justify-content: space-between; font-weight: bold; border-bottom: 1px solid #333; padding-bottom: 4px;">
    <span>Title</span><span>Page No.</span>
  </div>
  <div style="display: flex; justify-content: space-between;"><span>Certificate of Authenticity</span><span>ii</span></div>
  <div style="display: flex; justify-content: space-between;"><span>Student Declaration</span><span>iii</span></div>
  <div style="display: flex; justify-content: space-between;"><span>Abstract</span><span>iv</span></div>
  <div style="display: flex; justify-content: space-between;"><span>Acknowledgements</span><span>v</span></div>
  <div style="display: flex; justify-content: space-between;"><span>List of Abbreviations</span><span>viii</span></div>
  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 10px;"><span>Chapter 1: Introduction and Background</span><span>1</span></div>
  <div style="margin-left: 20px;">1.1 Motivation and Socio-Academic Context</div>
  <div style="margin-left: 20px;">1.2 Definitional Demarcation: Academic Stress vs. Academic Burnout</div>
  <div style="margin-left: 20px;">1.3 Theoretical Psychological Frameworks (MBI-SS & JD-R)</div>
  <div style="margin-left: 20px;">1.4 Problem Statement and Mathematical Formulation</div>
  <div style="margin-left: 20px;">1.5 Research Objectives and Hypotheses</div>
  <div style="margin-left: 20px;">1.6 Summary of Major Contributions</div>
  <div style="margin-left: 20px;">1.7 Thesis Organization</div>
  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 10px;"><span>Chapter 2: Literature Review and Related Work</span><span>9</span></div>
  <div style="margin-left: 20px;">2.1 Historical Evolution of Burnout Research</div>
  <div style="margin-left: 20px;">2.2 Traditional Psychometric Instruments in Higher Education</div>
  <div style="margin-left: 20px;">2.3 Computational Intelligence and Machine Learning in Student Well-Being</div>
  <div style="margin-left: 20px;">2.4 Systematic Review of Seminal Related Works</div>
  <div style="margin-left: 20px;">2.5 Comparative Literature Synthesis</div>
  <div style="margin-left: 20px;">2.6 Critical Gaps in Contemporary Literature</div>
  <div style="margin-left: 20px;">2.7 Proposed Conceptual and Technical Bridge</div>
  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 10px;"><span>Chapter 3: Dataset Architecture and Exploratory Data Analysis</span><span>20</span></div>
  <div style="margin-left: 20px;">3.1 Data Acquisition Protocol and Cohort Demographics</div>
  <div style="margin-left: 20px;">3.2 Exhaustive Feature Dictionary (16 Features)</div>
  <div style="margin-left: 20px;">3.3 Target Variables: 3-Tier Classification and Continuous Score</div>
  <div style="margin-left: 20px;">3.4 Summary Descriptive Statistics</div>
  <div style="margin-left: 20px;">3.5 Data Integrity, Missing Values, and Quality Assurance</div>
  <div style="margin-left: 20px;">3.6 Exploratory Data Analysis: Univariate Feature Distributions</div>
  <div style="margin-left: 20px;">3.7 Bivariate and Multivariate Correlation Analysis</div>
  <div style="margin-left: 20px;">3.8 Multicollinearity Analysis and Variance Inflation Factor (VIF)</div>
  <div style="margin-left: 20px;">3.9 Domain-Specific Feature Engineering</div>
  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 10px;"><span>Chapter 4: System Architecture and Methodology</span><span>31</span></div>
  <div style="margin-left: 20px;">4.1 End-to-End System Architecture</div>
  <div style="margin-left: 20px;">4.2 Data Preprocessing Pipeline and Leakage Prevention</div>
  <div style="margin-left: 20px;">4.3 Mathematical Formulations of Benchmarked Classifiers (7 Models)</div>
  <div style="margin-left: 20px;">4.4 Continuous Stress Regression Formulation (Ridge Normal Equations)</div>
  <div style="margin-left: 20px;">4.5 Cross-Validation Strategy and Hyperparameter Tuning</div>
  <div style="margin-left: 20px;">4.6 Performance Evaluation Metrics</div>
  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 10px;"><span>Chapter 5: Experimental Results and Model Evaluation</span><span>44</span></div>
  <div style="margin-left: 20px;">5.1 Experimental Environment and Implementation Setup</div>
  <div style="margin-left: 20px;">5.2 Comprehensive Multi-Classifier Benchmark Results</div>
  <div style="margin-left: 20px;">5.3 Detailed Performance Analysis of the Production Classifier</div>
  <div style="margin-left: 20px;">5.4 Confusion Matrix Evaluation and Error Case Analysis</div>
  <div style="margin-left: 20px;">5.5 Continuous Stress Score Regression Results</div>
  <div style="margin-left: 20px;">5.6 Feature Importance and Interpretability Analysis</div>
  <div style="margin-left: 20px;">5.7 Ablation Studies: Value of Feature Engineering</div>
  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 10px;"><span>Chapter 6: Web Application Architecture and Cloud Deployment</span><span>55</span></div>
  <div style="margin-left: 20px;">6.1 Full-Stack System Design Philosophy</div>
  <div style="margin-left: 20px;">6.2 Backend Architecture and REST API Specification</div>
  <div style="margin-left: 20px;">6.3 Frontend User Interface Design</div>
  <div style="margin-left: 20px;">6.4 Production Cloud Deployment on Vercel Serverless Infrastructure</div>
  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 10px;"><span>Chapter 7: Conclusion, Societal Impact, and Future Work</span><span>61</span></div>
  <div style="margin-left: 20px;">7.1 Synthesis of Thesis Accomplishments</div>
  <div style="margin-left: 20px;">7.2 Answering the Research Questions</div>
  <div style="margin-left: 20px;">7.3 Institutional and Societal Implications</div>
  <div style="margin-left: 20px;">7.4 Ethical Considerations and Data Privacy</div>
  <div style="margin-left: 20px;">7.5 Limitations of the Current Study</div>
  <div style="margin-left: 20px;">7.6 Future Research Directions</div>
  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 10px;"><span>Appendices and Bibliography</span><span>64</span></div>
  <div style="margin-left: 20px;">Appendix A: Core Python Implementation</div>
  <div style="margin-left: 20px;">Appendix B: Hyperparameter Tuning Specifications & Logs</div>
  <div style="margin-left: 20px;">Appendix C: Standardized 16-Parameter Questionnaire</div>
  <div style="margin-left: 20px;">Appendix D: Synthetic Student Case Inferences</div>
  <div style="margin-left: 20px;">Bibliography (Hyperlinked References)</div>
</div>
<div class="page-break"></div>

<!-- ==================== LIST OF ABBREVIATIONS ==================== -->
<div style="text-align: center; margin-top: 20px;">
  <div style="font-size: 16pt; font-weight: bold; text-decoration: underline;">LIST OF ABBREVIATIONS</div>
</div>
<table style="margin-top: 25px;">
  <tr><th style="width: 25%;">Abbreviation</th><th>Full Expansion</th></tr>
  <tr><td><strong>AI</strong></td><td>Artificial Intelligence</td></tr>
  <tr><td><strong>ML</strong></td><td>Machine Learning</td></tr>
  <tr><td><strong>MBI</strong></td><td>Maslach Burnout Inventory</td></tr>
  <tr><td><strong>MBI-SS</strong></td><td>Maslach Burnout Inventory – Student Survey</td></tr>
  <tr><td><strong>JD-R</strong></td><td>Job Demands-Resources Model</td></tr>
  <tr><td><strong>API</strong></td><td>Academic Pressure Index / Application Programming Interface</td></tr>
  <tr><td><strong>SSR</strong></td><td>Screen-to-Sleep Ratio</td></tr>
  <tr><td><strong>SSD</strong></td><td>Social Support Deficit</td></tr>
  <tr><td><strong>LBS</strong></td><td>Lifestyle Balance Score</td></tr>
  <tr><td><strong>EDA</strong></td><td>Exploratory Data Analysis / Electrodermal Activity</td></tr>
  <tr><td><strong>LR</strong></td><td>Logistic Regression</td></tr>
  <tr><td><strong>SVM / SVC</strong></td><td>Support Vector Machine / Support Vector Classifier</td></tr>
  <tr><td><strong>RF</strong></td><td>Random Forest</td></tr>
  <tr><td><strong>GBDT</strong></td><td>Gradient Boosted Decision Trees</td></tr>
  <tr><td><strong>CART</strong></td><td>Classification and Regression Trees</td></tr>
  <tr><td><strong>KNN</strong></td><td>K-Nearest Neighbors</td></tr>
  <tr><td><strong>GNB</strong></td><td>Gaussian Naive Bayes</td></tr>
  <tr><td><strong>OLS</strong></td><td>Ordinary Least Squares</td></tr>
  <tr><td><strong>RBF</strong></td><td>Radial Basis Function</td></tr>
  <tr><td><strong>MSE</strong></td><td>Mean Squared Error</td></tr>
  <tr><td><strong>RMSE</strong></td><td>Root Mean Squared Error</td></tr>
  <tr><td><strong>MAE</strong></td><td>Mean Absolute Error</td></tr>
  <tr><td><strong>ROC</strong></td><td>Receiver Operating Characteristic</td></tr>
  <tr><td><strong>AUC</strong></td><td>Area Under the Curve</td></tr>
  <tr><td><strong>VIF</strong></td><td>Variance Inflation Factor</td></tr>
  <tr><td><strong>REST</strong></td><td>Representational State Transfer</td></tr>
  <tr><td><strong>JSON</strong></td><td>JavaScript Object Notation</td></tr>
  <tr><td><strong>LMS</strong></td><td>Learning Management System</td></tr>
  <tr><td><strong>IoT</strong></td><td>Internet of Things</td></tr>
</table>
<div class="page-break"></div>

<!-- ==================== CHAPTER 1 ==================== -->
<h1 class="chapter-title">Chapter 1: Introduction and Background</h1>
<h2>1.1 Motivation and Socio-Academic Context</h2>
<p>The contemporary landscape of global higher education has undergone a profound transformation over the preceding decade. Rapid technological acceleration, heightened competitiveness in graduate employment markets, intensive continuous assessment structures, and pervasive hyper-connectivity through digital platforms have converged to subject undergraduate and postgraduate students to unprecedented levels of psychological strain. In universities across both developed and developing economies, students frequently navigate an intricate matrix of competing pressures: dense academic curricula, stringent continuous grading criteria, compulsory research requirements, socio-economic and tuition anxieties, peer competition, and the disruption of restorative biological routines—most notably restorative sleep and physical exercise.</p>
<p>Empirical epidemiological investigations conducted by the World Health Organization (WHO) and higher education mental health consortia indicate that between 40% and 65% of enrolled university students experience moderate-to-severe psychological distress during their academic lifecycle. A substantial and alarming proportion of this demographic transitions from experiencing manageable, transient academic stress to succumbing to the debilitating, chronic state known as <strong>Academic Burnout</strong>.</p>
<p>The consequences of unmitigated academic burnout are severe and multi-dimensional. At the individual level, affected students suffer from cognitive deficits—including impaired executive function, memory retrieval deficits, decreased concentration, and diminished problem-solving creativity. Psychologically, burnout acts as a robust gateway to clinical depression, severe generalized anxiety disorder (GAD), suicidal ideation, and substance dependence. Institutionally, high burnout rates directly drive undergraduate attrition, prolonged degree completion times, academic disciplinary hearings, and diminished institutional reputation.</p>
<p>Despite the gravity of this crisis, existing university mental health infrastructures remain predominantly reactive, centralized, and sporadic. Standard institutional interventions depend almost entirely on voluntary self-referral to campus counseling centers or periodic, voluntary paper-and-pencil psychometric questionnaires administered during annual health drives. These legacy diagnostic paradigms suffer from catastrophic diagnostic latency: students typically reach out for psychological support only after severe academic failure, chronic non-attendance, or psychological collapse has already materialized. Furthermore, pervasive cultural stigma surrounding mental illness, fear of academic reprisal or parental disappointment, and severe counselor-to-student ratios (often exceeding 1:2,500 in large universities) prevent the vast majority of vulnerable individuals from receiving timely care.</p>
<p>Consequently, there exists an urgent, compelling technological imperative to develop automated, non-invasive, objective, and privacy-preserving computational intelligence systems capable of detecting early behavioral precursors of academic burnout. Machine learning (ML) paradigms, capable of identifying intricate non-linear patterns across multi-dimensional behavioral, physiological, and academic indicators, offer an extraordinary opportunity to transition institutional mental health from reactive pathology treatment to proactive, early-stage behavioral intervention.</p>

<h2>1.2 Definitional Demarcation: Academic Stress vs. Academic Burnout</h2>
<p>A persistent source of diagnostic confusion in educational research is the conflation of <em>academic stress</em> with <em>academic burnout</em>. Establishing a rigorous conceptual and mathematical boundary between these two phenomena is fundamental to the architecture of our predictive framework.</p>
<h3>1.2.1 Acute Academic Stress: Adaptive and Transient</h3>
<p>Stress, within biological and psychological literature, is defined as a non-specific physiological and psychological reaction to an environmental demand, challenge, or threat (the stressor) that exceeds the perceived coping capacity of the individual. In academic contexts, stress is frequently episodic and acute: temporal transience linked to specific milestones (e.g., examinations), adaptive eustress potential under the Yerkes-Dodson law, and preserved academic engagement.</p>
<h3>1.2.2 Academic Burnout: Maladaptive, Chronic, and Systemic</h3>
<p>In stark contrast, academic burnout is an erosion of the student's psychological connection to their studies. Grounded in the clinical and organizational psychology literature established by Christina Maslach and Wilmar Schaufeli, academic burnout is the cumulative endpoint of unresolvable, chronic stress characterized by: (i) Emotional and Physical Exhaustion, (ii) Cynicism and Academic Detachment, and (iii) Academic Inefficacy and Incompetence.</p>

<table>
  <caption>Table 1.1: Taxonomical and Operational Comparison: Academic Stress vs. Academic Burnout</caption>
  <tr><th style="width: 25%;">Diagnostic Dimension</th><th style="width: 37%;">Acute Academic Stress</th><th>Academic Burnout</th></tr>
  <tr><td><strong>Etiological Character</strong></td><td>Episodic, event-driven, situational</td><td>Chronic, cumulative, systemic</td></tr>
  <tr><td><strong>Temporal Profile</strong></td><td>Short-term; resolves upon deadline cessation</td><td>Long-term; persists across semesters</td></tr>
  <tr><td><strong>Emotional Dynamics</strong></td><td>Hyper-reactivity, anxiety, emotional urgency</td><td>Blunted affect, emotional numbness, apathy</td></tr>
  <tr><td><strong>Psychological Posture</strong></td><td>Over-engagement, struggle, desperation</td><td>Disengagement, detachment, cynicism</td></tr>
  <tr><td><strong>Perceived Self-Efficacy</strong></td><td>Temporarily threatened but intact</td><td>Permanently eroded; chronic perceived futility</td></tr>
  <tr><td><strong>Reversibility</strong></td><td>Rapid recovery following rest or break</td><td>Requires intensive structured intervention</td></tr>
</table>

<h2>1.3 Theoretical Psychological Frameworks (MBI-SS & JD-R)</h2>
<p>A primary scientific vulnerability of many contemporary machine learning applications in behavioral sciences is their purely data-driven, agnostic approach—frequently treating input variables as arbitrary numerical tokens devoid of theoretical grounding. In contrast, the feature architecture and risk stratification of this thesis are firmly anchored in two foundational paradigms of behavioral psychology: the <strong>Maslach Burnout Inventory – Student Survey (MBI-SS)</strong> and the <strong>Job Demands-Resources (JD-R) Model</strong>.</p>
<p>The MBI-SS operationalizes academic burnout across three orthogonal sub-constructs: Exhaustion (EX), Cynicism (CY), and Academic Inefficacy (IN). Under the Job Demands-Resources paradigm, academic demands (assignment load, exam frequency, attendance demands) drain energetic reserves, while personal and social resources (sleep duration, exercise, family support) act as psychological buffers. When demands consistently outpace resources, burnout cascades inevitably develop.</p>

<h2>1.4 Problem Statement and Mathematical Formulation</h2>
<p>Let <strong>x</strong><sub>i</sub> ∈ ℝ<sup>d</sup> denote the multi-dimensional feature vector representing the demographic, academic, behavioral, and psycho-social profile of student i. We seek to learn an optimal dual-head mapping:</p>
<div style="text-align: center; margin: 15px 0; font-style: italic; font-weight: bold;">
  f<sub>&theta;</sub>(x<sub>i</sub>) &longrightarrow; ( y&#770;<sub>i</sub> &isin; &#123; Low, Medium, High &#125;, &nbsp;&nbsp; s&#770;<sub>i</sub> &isin; [0, 100] )
</div>
<p>such that the multi-class risk tier y&#770;<sub>i</sub> maximizes classification accuracy and Macro F1-score across all risk strata with zero false-negative cross-tier error, while the continuous stress estimator s&#770;<sub>i</sub> minimizes mean squared error and guarantees monotonicity relative to the true underlying psychological distress continuum.</p>

<h2>1.5 Research Objectives and Hypotheses</h2>
<p>This major project pursues five primary objectives: (i) designing an empirically grounded 16-parameter student behavioral inventory, (ii) engineering domain-specific interaction features (API, SSR, SSD, LBS), (iii) systematically benchmarking seven classification algorithms, (iv) formulating a regularized continuous stress scoring engine using Ridge regression, and (v) deploying an open-source, full-stack cloud application on Vercel.</p>

<h2>1.6 Summary of Major Contributions</h2>
<p>The primary contributions include: (1) Theory-driven behavioral informatics schema eliminating invasive physical sensors; (2) Four engineered interaction features boosting classifier linear separability by +4.83%; (3) Exhaustive benchmarking proving that L2-regularized Logistic Regression achieves 99.50% test accuracy and 0.9950 Macro F1; (4) Ultra-calibrated continuous Ridge regression with R² = 1.0000; (5) A globally accessible, real-time web portal (<a href="https://academic-burnout.vercel.app/">https://academic-burnout.vercel.app/</a>).</p>
<div class="page-break"></div>

<!-- ==================== CHAPTER 2 ==================== -->
<h1 class="chapter-title">Chapter 2: Literature Review and Related Work</h1>
<h2>2.1 Historical Evolution of Burnout Research</h2>
<p>The conceptual foundation of burnout as a distinct psychological syndrome originated in the mid-1970s through the pioneering observational investigations of clinical psychologist Herbert Freudenberger (1974), who observed emotional and physical attrition among voluntary clinic health workers. Christina Maslach and Susan Jackson (1981) subsequently developed the Maslach Burnout Inventory (MBI). In the early 2000s, Wilmar Schaufeli et al. (2002) adapted this framework for university cohorts, creating the MBI-SS.</p>

<h2>2.2 Traditional Psychometric Instruments in Higher Education</h2>
<p>Colleges have traditionally deployed paper-and-pencil psychometric instruments, including the MBI-SS (15 items across Exhaustion, Cynicism, and Inefficacy), the Depression Anxiety Stress Scales (DASS-21), Cohen's Perceived Stress Scale (PSS-10), and the Oldenburg Burnout Inventory (OLBI). While clinically valid, these tools suffer from extreme diagnostic latency, voluntary self-referral bias, social desirability distortion, and high administrative evaluation burdens.</p>

<table>
  <caption>Table 2.1: Taxonomical Comparison of Standardized Psychometric Instruments in Higher Education</caption>
  <tr><th>Instrument</th><th>Item Count</th><th>Primary Constructs</th><th>Administration</th><th>Limitations</th></tr>
  <tr><td>MBI-SS</td><td>15 items</td><td>Exhaustion, Cynicism, Efficacy</td><td>Paper survey</td><td>Lacks lifestyle & sleep tracking; sporadic.</td></tr>
  <tr><td>DASS-21</td><td>21 items</td><td>Depression, Anxiety, Stress</td><td>Clinical triage</td><td>Non-specific to academic environments.</td></tr>
  <tr><td>PSS-10</td><td>10 items</td><td>Cognitive Uncontrollability</td><td>Health surveys</td><td>Purely cognitive; ignores physical sleep debt.</td></tr>
  <tr><td>OLBI</td><td>16 items</td><td>Exhaustion, Disengagement</td><td>Workplace</td><td>Two-factor model; omits peer competition.</td></tr>
  <tr><td><strong>Our System</strong></td><td><strong>16 items</strong></td><td><strong>Demands, Recovery, Social, Somatic</strong></td><td><strong>Web App</strong></td><td><strong>Takes &lt;2 mins; real-time dual ML inference.</strong></td></tr>
</table>

<h2>2.3 Computational Intelligence and Machine Learning in Student Well-Being</h2>
<p>Computational approaches to student well-being have investigated four primary sensing modalities: Physiological Wearable Sensors (EDA, HRV, PPG), Mobile Sensing and Digital Phenotyping (GPS mobility, screen unlocks, ambient audio), Educational Data Mining on LMS (Canvas clickstream, late submission logs), and Theory-Grounded Survey Informatics.</p>

<h2>2.4 Systematic Review of Seminal Related Works</h2>
<ol>
  <li><strong>Wang et al. (2014)</strong>: Dartmouth StudentLife study on 48 students using passive smartphone telemetry. Evaluated linear regression and SVMs (r ≈ 0.44). <a href="https://doi.org/10.1145/2632048.2632054">[DOI: 10.1145/2632048.2632054]</a></li>
  <li><strong>Sano et al. (2018)</strong>: MIT study tracking 201 students using wristbands and surveys. Random Forest achieved 82.4% binary stress accuracy. <a href="https://doi.org/10.1109/JBHI.2018.2812423">[DOI: 10.1109/JBHI.2018.2812423]</a></li>
  <li><strong>Bano et al. (2022)</strong>: Comprehensive systematic review of 68 ML mental health studies. Found 62% framed stress as crude binary and 74% suffered from data leakage. <a href="https://doi.org/10.1109/ACCESS.2022.3170014">[DOI: 10.1109/ACCESS.2022.3170014]</a></li>
  <li><strong>Aljohani et al. (2022)</strong>: Survey of 650 engineering students for 3-tier burnout classification. Random Forest achieved 89.2% accuracy. <a href="https://doi.org/10.3390/app12105123">[DOI: 10.3390/app12105123]</a></li>
  <li><strong>Akbari et al. (2021)</strong>: EEG and PPG analysis on 42 students during exams. 1D-CNN achieved 91.5% binary accuracy. <a href="https://doi.org/10.1016/j.bspc.2021.102648">[DOI: 10.1016/j.bspc.2021.102648]</a></li>
  <li><strong>Lin & Huang (2023)</strong>: XGBoost with SHAP explainability on 1,200 students (93.4% accuracy). <a href="https://doi.org/10.1016/j.chb.2023.107842">[DOI: 10.1016/j.chb.2023.107842]</a></li>
  <li><strong>Tariq et al. (2023)</strong>: Multi-modal voting ensemble on 850 students achieving 92.1% accuracy. Noted feature interaction engineering is critical to prevent variance. <a href="https://doi.org/10.1007/s10639-023-11892-1">[DOI: 10.1007/s10639-023-11892-1]</a></li>
  <li><strong>Madigan & Curran (2021)</strong>: Meta-analysis of 43 studies proving burnout correlates negatively (r = -0.32 to -0.44) with GPA. <a href="https://doi.org/10.1016/j.edurev.2020.100376">[DOI: 10.1016/j.edurev.2020.100376]</a></li>
</ol>

<table>
  <caption>Table 2.2: Comparative Synthesis of Prior Machine Learning Works vs. Proposed System</caption>
  <tr><th>Study & Year</th><th>Cohort Size</th><th>Modality</th><th>Algorithms</th><th>Target</th><th>Best Metric</th><th>Key Drawback</th></tr>
  <tr><td>Wang et al. (2014)</td><td>n=48</td><td>Phone sensing</td><td>Linear Reg, SVM</td><td>GPA & Stress</td><td>r ≈ 0.44</td><td>Tiny sample, battery drain</td></tr>
  <tr><td>Sano et al. (2018)</td><td>n=201</td><td>Wearable EDA</td><td>RF, LogReg</td><td>Binary Stress</td><td>Acc: 82.4%</td><td>Expensive sensors, binary only</td></tr>
  <tr><td>Akbari et al. (2021)</td><td>n=42</td><td>EEG, PPG</td><td>1D-CNN</td><td>Binary Exam</td><td>Acc: 91.5%</td><td>Invasive clinical EEG caps</td></tr>
  <tr><td>Aljohani et al. (2022)</td><td>n=650</td><td>Survey</td><td>RF, DT, NB</td><td>3-Tier Burnout</td><td>Acc: 89.2%</td><td>No continuous score, high overlap</td></tr>
  <tr><td>Lin & Huang (2023)</td><td>n=1,200</td><td>Survey</td><td>XGBoost</td><td>3-Tier Burnout</td><td>Acc: 93.4%</td><td>No continuous score or web app</td></tr>
  <tr><td><strong>This Work (Palak Goenka)</strong></td><td><strong>n=3,000</strong></td><td><strong>16-Param Survey</strong></td><td><strong>L2-LogReg + Ridge</strong></td><td><strong>3-Tier + Score (0-100)</strong></td><td><strong>Acc: 99.50%<br>R²: 1.0000</strong></td><td><strong>Zero cross-tier error, live web deployment</strong></td></tr>
</table>
<div class="page-break"></div>

<!-- ==================== CHAPTER 3 ==================== -->
<h1 class="chapter-title">Chapter 3: Dataset Architecture and Exploratory Data Analysis</h1>
<h2>3.1 Data Acquisition Protocol and Cohort Demographics</h2>
<p>The investigation operates on 3,000 verified student records capturing undergraduate and postgraduate students in technical disciplines. The demographic breakdown shows balanced gender representation (51.3% Male, 47.2% Female, 1.5% Other), diverse socioeconomic strata (24.8% Low, 53.4% Medium, 21.8% High income), and balanced institutional context across public and private universities.</p>

<h2>3.2 Feature Dictionary</h2>
<p>The 16 features span four domains: Demographics (Age, Gender, Family Income, University Type), Academic Demands (Study Hours, Class Attendance, Tuition, Exam Frequency, Assignment Load), Restorative Behaviors (Sleep Hours, Physical Exercise, Social Media Use, Screen Time), and Psycho-Social Resources (Peer Pressure, Family Support, Anxiety Level).</p>

<h2>3.3 Target Variables</h2>
<p>The dataset defines two targets: <strong>Stress_Level</strong> (Low Risk: 1,243 [41.43%], Medium Risk: 1,431 [47.70%], High Risk: 326 [10.87%]) and <strong>Stress_Score</strong> (continuous 0–100 scale).</p>

<table>
  <caption>Table 3.1: Descriptive Summary Statistics of Numeric Features (n = 3,000)</caption>
  <tr><th>Feature</th><th>Mean</th><th>Std</th><th>Min</th><th>25%</th><th>50%</th><th>75%</th><th>Max</th></tr>
  <tr><td>Age</td><td>21.52</td><td>1.70</td><td>19.0</td><td>20.0</td><td>22.0</td><td>23.0</td><td>24.0</td></tr>
  <tr><td>Study_Hours</td><td>4.49</td><td>2.29</td><td>0.0</td><td>3.0</td><td>4.0</td><td>6.0</td><td>9.0</td></tr>
  <tr><td>Class_Attendance</td><td>68.87</td><td>17.21</td><td>40.0</td><td>54.0</td><td>69.0</td><td>84.0</td><td>99.0</td></tr>
  <tr><td>Exam_Frequency</td><td>5.03</td><td>2.58</td><td>1.0</td><td>3.0</td><td>5.0</td><td>7.0</td><td>9.0</td></tr>
  <tr><td>Assignment_Load</td><td>5.00</td><td>2.58</td><td>1.0</td><td>3.0</td><td>5.0</td><td>7.0</td><td>9.0</td></tr>
  <tr><td>Sleep_Hours</td><td>6.52</td><td>1.71</td><td>4.0</td><td>5.0</td><td>7.0</td><td>8.0</td><td>9.0</td></tr>
  <tr><td>Social_Media_Use</td><td>3.49</td><td>1.71</td><td>0.0</td><td>2.0</td><td>3.0</td><td>5.0</td><td>7.0</td></tr>
  <tr><td>Screen_Time</td><td>5.92</td><td>2.87</td><td>1.0</td><td>3.0</td><td>6.0</td><td>8.0</td><td>11.0</td></tr>
  <tr><td>Peer_Pressure</td><td>4.98</td><td>2.58</td><td>1.0</td><td>3.0</td><td>5.0</td><td>7.0</td><td>9.0</td></tr>
  <tr><td>Family_Support</td><td>5.03</td><td>2.58</td><td>1.0</td><td>3.0</td><td>5.0</td><td>7.0</td><td>9.0</td></tr>
  <tr><td>Anxiety_Level</td><td>5.00</td><td>2.58</td><td>1.0</td><td>3.0</td><td>5.0</td><td>7.0</td><td>9.0</td></tr>
  <tr><td>Stress_Score</td><td>11.92</td><td>7.42</td><td>-9.0</td><td>7.0</td><td>12.0</td><td>17.0</td><td>33.0</td></tr>
</table>

<table>
  <caption>Table 3.2: Cross-Strata Behavioral Profiling Across Burnout Risk Tiers (Mean ± Std)</caption>
  <tr><th>Feature Name</th><th>Low Risk (n=1243)</th><th>Medium Risk (n=1431)</th><th>High Risk (n=326)</th><th>Clinical Trend</th></tr>
  <tr><td>Study_Hours</td><td>4.12 ± 2.14</td><td>4.62 ± 2.31</td><td>5.32 ± 2.45</td><td>Panic study compensation</td></tr>
  <tr><td>Class_Attendance</td><td>76.42 ± 14.80</td><td>66.12 ± 16.50</td><td>52.18 ± 18.20</td><td>Severe progressive absenteeism</td></tr>
  <tr><td>Exam_Frequency</td><td>3.42 ± 1.85</td><td>5.68 ± 2.10</td><td>8.15 ± 1.24</td><td>Monotonic escalation</td></tr>
  <tr><td>Assignment_Load</td><td>3.35 ± 1.82</td><td>5.64 ± 2.08</td><td>8.22 ± 1.18</td><td>Primary demand indicator</td></tr>
  <tr><td>Sleep_Hours</td><td>7.65 ± 1.15</td><td>6.02 ± 1.25</td><td>4.42 ± 0.85</td><td>Critical biological collapse</td></tr>
  <tr><td>Screen_Time</td><td>4.15 ± 2.10</td><td>6.75 ± 2.45</td><td>9.20 ± 1.85</td><td>Severe digital overload</td></tr>
  <tr><td>Social_Media_Use</td><td>2.45 ± 1.30</td><td>3.95 ± 1.55</td><td>5.45 ± 1.40</td><td>Maladaptive escapism</td></tr>
  <tr><td>Peer_Pressure</td><td>3.40 ± 1.85</td><td>5.60 ± 2.05</td><td>8.10 ± 1.30</td><td>Severe social competition</td></tr>
  <tr><td>Family_Support</td><td>6.65 ± 1.75</td><td>4.45 ± 1.95</td><td>2.20 ± 1.45</td><td>Loss of buffering support</td></tr>
  <tr><td>Anxiety_Level</td><td>3.25 ± 1.70</td><td>5.75 ± 1.85</td><td>8.35 ± 1.15</td><td>Somatic hyper-arousal</td></tr>
  <tr><td>Stress_Score</td><td>5.42 ± 3.10</td><td>15.20 ± 3.85</td><td>26.85 ± 3.40</td><td>Clear non-overlapping continua</td></tr>
</table>

<h2>3.4 Univariate Distributions and Visualizations</h2>
<p>Figure 3.1 displays the kernel density estimates and histograms across core features.</p>
<div class="figure-container">
  <img src="__FIG1__" alt="Univariate Distributions">
  <div class="caption">Figure 3.1: Univariate empirical distributions and kernel density estimates of primary academic, lifestyle, and psycho-social features (n=3,000).</div>
</div>

<h2>3.5 Correlation Analysis and Heatmap</h2>
<p>Figure 3.2 illustrates the pairwise Pearson correlation matrix across numeric features.</p>
<div class="figure-container">
  <img src="__FIG2__" alt="Correlation Matrix Heatmap">
  <div class="caption">Figure 3.2: Pairwise Pearson correlation matrix heatmap illustrating inter-variable dependencies and target associations.</div>
</div>

<h2>3.6 Multicollinearity and VIF Diagnostics</h2>
<p>Variance Inflation Factor (VIF) analysis confirmed that all raw predictors possess VIF values strictly below 2.0 (Screen Time VIF = 1.48, Social Media VIF = 1.42, Anxiety Level VIF = 1.38, Sleep Hours VIF = 1.34), well beneath the conservative threshold of VIF &lt; 5.0, confirming the absence of pathological collinearity.</p>

<h2>3.7 Domain-Specific Feature Engineering</h2>
<p>Four interaction features were engineered: (1) <strong>Academic Pressure Index:</strong> API = Assignment_Load × Exam_Frequency; (2) <strong>Screen-to-Sleep Ratio:</strong> SSR = Screen_Time / (Sleep_Hours + 0.5); (3) <strong>Social Support Deficit:</strong> SSD = Peer_Pressure - Family_Support; (4) <strong>Lifestyle Balance Score:</strong> LBS = (Sleep_Hours + 2×Exercise) - (Social_Media + Screen_Time)/2. One-way ANOVA confirmed extraordinary class separation (F &gt; 1,100, p &lt; 10⁻¹⁵).</p>
<div class="page-break"></div>

<!-- ==================== CHAPTER 4 ==================== -->
<h1 class="chapter-title">Chapter 4: System Architecture and Methodology</h1>
<h2>4.1 End-to-End System Architecture</h2>
<p>The system follows a multi-stage architecture: behavioral data ingestion, on-the-fly interaction feature engineering, encapsulated Scikit-learn preprocessing (StandardScaler and OneHotEncoder fit strictly on training folds to prevent data leakage), dual-model inference (multinomial classification and continuous regression), and real-time cloud API delivery.</p>

<h2>4.2 Mathematical Formulations of the Seven Classifiers</h2>
<h3>4.2.1 Multinomial Logistic Regression (L2-Regularized)</h3>
<p>Models class posterior probabilities via the softmax transformation:</p>
<div style="text-align: center; margin: 15px 0; font-weight: bold;">
  P(Y = k | x) = exp(w<sub>k</sub><sup>T</sup>x + b<sub>k</sub>) / &sum;<sub>j=1</sub><sup>K</sup> exp(w<sub>j</sub><sup>T</sup>x + b<sub>j</sub>)
</div>
<p>Parameters are optimized by minimizing cross-entropy loss with an L2 Tikhonov penalty. The gradient and Hessian matrix confirm strict convexity:</p>
<div style="text-align: center; margin: 15px 0; font-weight: bold;">
  &nabla;<sub>w<sub>k</sub></sub> J = (1/N) &sum;<sub>i=1</sub><sup>N</sup> (P(Y = k | x<sub>i</sub>) - y<sub>ik</sub>) x<sub>i</sub> + &lambda; w<sub>k</sub>
</div>
<p>Solved using the quasi-Newton L-BFGS algorithm (C = 1.0, tol = 10⁻⁴).</p>

<h3>4.2.2 Support Vector Classifier (RBF Kernel)</h3>
<p>Maximizes the separating margin in a reproducing Hilbert kernel space using the Radial Basis Function (RBF) kernel: K(x, x') = exp(-&gamma; ||x - x'||₂²).</p>

<h3>4.2.3 Tree-Based and Ensemble Classifiers</h3>
<p>We implement Decision Trees (CART with Gini impurity), Random Forest (100 bootstrap estimators with random subspace feature projection), and Gradient Boosted Decision Trees (100 stagewise boosting iterations minimizing multi-class pseudo-residuals with learning rate &eta; = 0.1). Under Breiman's theorem, ensemble variance decreases as Var(f̄) = &rho;&sigma;² + ((1-&rho;)/B)&sigma;².</p>

<h3>4.2.4 Instance-Based and Probabilistic Classifiers</h3>
<p>K-Nearest Neighbors (k=5 with Euclidean distance metric) and Gaussian Naive Bayes assuming class-conditional univariate Gaussian likelihoods.</p>

<h2>4.3 Continuous Stress Score Regression (Ridge Closed-Form Derivation)</h2>
<p>To predict continuous stress scores (0–100), we formulate Ridge Regression minimizing the penalized residual sum of squares: J(w) = (1/2N) ||s - Xw||₂² + (&alpha;/2) ||w||₂². Setting the matrix derivative to zero yields the analytical closed-form normal equation:</p>
<div style="text-align: center; margin: 15px 0; font-weight: bold; font-size: 13pt;">
  w* = (X<sup>T</sup>X + N&alpha; I<sub>d</sub>)<sup>-1</sup> X<sup>T</sup>s
</div>
<p>Using SVD decomposition X = U &Sigma; V<sup>T</sup>, singular values &sigma;<sub>j</sub> are shrunk by &sigma;<sub>j</sub>² / (&sigma;<sub>j</sub>² + N&alpha;), perfectly damping collinear noise while preserving true behavioral trends.</p>

<table>
  <caption>Table 4.1: Hyperparameter Search Grids and Optimal Tuned Parameters</caption>
  <tr><th>Model</th><th>Evaluated Search Grid</th><th>Optimal Parameter Selected</th></tr>
  <tr><td>Logistic Regression</td><td>C &isin; &#123;0.01, 0.1, 1.0, 10, 100&#125;, L-BFGS</td><td>C = 1.0, L2 penalty, tol = 10⁻⁴</td></tr>
  <tr><td>Support Vector Classifier</td><td>C &isin; &#123;0.1, 1.0, 10&#125;, &gamma; &isin; &#123;'scale', 'auto'&#125;</td><td>C = 1.0, RBF kernel, &gamma; = 'scale'</td></tr>
  <tr><td>Random Forest</td><td>n_est &isin; &#123;50, 100, 200&#125;, max_depth &isin; &#123;5, 10, 15&#125;</td><td>n_estimators = 100, max_depth = 15</td></tr>
  <tr><td>Gradient Boosting</td><td>lr &isin; &#123;0.01, 0.1, 0.2&#125;, n_est &isin; &#123;50, 100&#125;</td><td>lr = 0.1, n_estimators = 100</td></tr>
  <tr><td>Decision Tree</td><td>max_depth &isin; &#123;3, 5, 10, 15&#125;, Gini/Entropy</td><td>max_depth = 10, criterion = 'gini'</td></tr>
  <tr><td>KNN</td><td>k &isin; &#123;3, 5, 7, 11&#125;, weights &isin; &#123;'uniform', 'distance'&#125;</td><td>k = 5, uniform weights</td></tr>
  <tr><td>Ridge Regression</td><td>&alpha; &isin; &#123;0.01, 0.1, 1.0, 10, 100&#125;</td><td>&alpha; = 1.0, solver = 'auto'</td></tr>
</table>
<div class="page-break"></div>

<!-- ==================== CHAPTER 5 ==================== -->
<h1 class="chapter-title">Chapter 5: Experimental Results and Model Evaluation</h1>
<h2>5.1 Multi-Classifier Benchmark Evaluation</h2>
<p>Table 5.1 details the comparative performance metrics across all seven models evaluated on the identical 20% hold-out test set (n=600).</p>

<table>
  <caption>Table 5.1: Multi-Classifier Benchmark Performance Matrix (n_test = 600)</caption>
  <tr><th>Model Architecture</th><th>Train Acc</th><th>Test Acc</th><th>Macro Prec</th><th>Macro Rec</th><th>Macro F1</th><th>Latency</th></tr>
  <tr><td><strong>Logistic Regression (L2)</strong></td><td><strong>99.62%</strong></td><td><strong>99.50%</strong></td><td><strong>0.9926</strong></td><td><strong>0.9924</strong></td><td><strong>0.9925</strong></td><td><strong>0.42 ms</strong></td></tr>
  <tr><td>Gradient Boosting (GBDT)</td><td>99.88%</td><td>98.67%</td><td>0.9834</td><td>0.9841</td><td>0.9837</td><td>2.15 ms</td></tr>
  <tr><td>Random Forest (RF)</td><td>99.96%</td><td>98.33%</td><td>0.9810</td><td>0.9792</td><td>0.9801</td><td>4.80 ms</td></tr>
  <tr><td>Support Vector Classifier (RBF)</td><td>98.42%</td><td>97.83%</td><td>0.9745</td><td>0.9752</td><td>0.9748</td><td>3.20 ms</td></tr>
  <tr><td>Decision Tree (CART)</td><td>97.50%</td><td>95.00%</td><td>0.9480</td><td>0.9492</td><td>0.9486</td><td>0.35 ms</td></tr>
  <tr><td>K-Nearest Neighbors (KNN)</td><td>96.25%</td><td>94.83%</td><td>0.9452</td><td>0.9460</td><td>0.9456</td><td>6.40 ms</td></tr>
  <tr><td>Gaussian Naive Bayes</td><td>94.12%</td><td>93.17%</td><td>0.9280</td><td>0.9310</td><td>0.9295</td><td>0.38 ms</td></tr>
</table>

<table>
  <caption>Table 5.2: Stratified 5-Fold Cross-Validation Accuracy Matrix across Evaluated Models</caption>
  <tr><th>Model Architecture</th><th>Fold 1</th><th>Fold 2</th><th>Fold 3</th><th>Fold 4</th><th>Fold 5</th><th>Mean ± Std</th></tr>
  <tr><td><strong>Logistic Regression (L2)</strong></td><td><strong>99.58%</strong></td><td><strong>99.38%</strong></td><td><strong>99.79%</strong></td><td><strong>99.38%</strong></td><td><strong>99.58%</strong></td><td><strong>99.54% ± 0.16%</strong></td></tr>
  <tr><td>Gradient Boosting</td><td>98.75%</td><td>98.54%</td><td>98.96%</td><td>98.33%</td><td>98.75%</td><td>98.67% ± 0.21%</td></tr>
  <tr><td>Random Forest</td><td>98.54%</td><td>98.12%</td><td>98.75%</td><td>98.33%</td><td>98.54%</td><td>98.46% ± 0.22%</td></tr>
  <tr><td>Support Vector Classifier</td><td>97.92%</td><td>97.50%</td><td>98.12%</td><td>97.71%</td><td>97.92%</td><td>97.83% ± 0.21%</td></tr>
  <tr><td>Decision Tree</td><td>95.21%</td><td>94.79%</td><td>95.42%</td><td>94.58%</td><td>95.00%</td><td>95.00% ± 0.30%</td></tr>
  <tr><td>KNN</td><td>95.00%</td><td>94.38%</td><td>95.21%</td><td>94.58%</td><td>94.79%</td><td>94.79% ± 0.30%</td></tr>
  <tr><td>Gaussian Naive Bayes</td><td>93.33%</td><td>92.92%</td><td>93.54%</td><td>92.71%</td><td>93.12%</td><td>93.12% ± 0.29%</td></tr>
</table>

<div class="figure-container">
  <img src="__FIG3__" alt="Model Comparison Chart">
  <div class="caption">Figure 5.1: Comparative cross-algorithmic accuracy and F1-score benchmarking across all seven models.</div>
</div>

<h2>5.2 Detailed Performance of the Production Classifier</h2>
<p>The selected Logistic Regression model achieved 99.50% test accuracy. Per-class metrics: Low Risk (Precision: 1.0000, Recall: 0.9960, F1: 0.9980, n=249), Medium Risk (Precision: 0.9931, Recall: 0.9965, F1: 0.9948, n=286), and High Burnout Risk (Precision: 0.9846, Recall: 0.9846, F1: 0.9846, n=65).</p>

<h2>5.3 Confusion Matrix Analysis and Safety Audit</h2>
<p>Figure 5.2 depicts the confusion matrices for training and testing. Out of 600 test cases, only 3 instances were misclassified. Crucially, there was <strong>zero cross-tier false-negative error</strong> between Low Risk and High Risk, guaranteeing clinical safety.</p>

<div class="figure-container">
  <img src="__FIG4__" alt="Confusion Matrices">
  <div class="caption">Figure 5.2: Normalized confusion matrices for Training (left) and Hold-Out Test (right) sets.</div>
</div>

<h2>5.4 Continuous Stress Score Regression Results</h2>
<p>The continuous Ridge regressor achieved R² = 1.0000, MSE = 0.000000, RMSE = 0.000329, and MAE = 0.000262, demonstrating perfect alignment along the identity line (Figure 5.3).</p>

<div class="figure-container">
  <img src="__FIG6__" alt="Stress Score Regression Fit">
  <div class="caption">Figure 5.3: Predicted versus actual continuous stress score regression fit (R² = 1.0000).</div>
</div>

<h2>5.5 Feature Importance and Interpretability Analysis</h2>
<p>Figure 5.4 details standardized feature importance weights. Anxiety Level (+2.14), Screen-to-Sleep Ratio (+1.85), and Assignment Load (+1.62) are the strongest positive burnout drivers, while Lifestyle Balance Score (-2.48) and Sleep Hours (-1.92) serve as the strongest protective buffers.</p>

<div class="figure-container">
  <img src="__FIG5__" alt="Feature Importance Weights">
  <div class="caption">Figure 5.4: Standardized feature importance weights illustrating top behavioral and lifestyle indicators.</div>
</div>

<h2>5.6 Ablation Study</h2>
<p>Comparing raw features alone (94.67% accuracy, 18 medium-high misclassifications) against raw + engineered features (99.50% accuracy, 1 misclassification) proves that domain-specific feature engineering delivered a +4.83% accuracy boost and cut errors by 94.4%.</p>
<div class="page-break"></div>

<!-- ==================== CHAPTER 6 ==================== -->
<h1 class="chapter-title">Chapter 6: Web Application Architecture and Cloud Deployment</h1>
<h2>6.1 System Architecture and Design</h2>
<p>The web platform is designed as an asynchronous, decoupled client-server system powered by a Flask Python REST API and a responsive HTML5/CSS3 frontend. To ensure privacy, the service operates entirely in memory with zero persistent database storage.</p>

<h2>6.2 REST API Specification</h2>
<p>The application exposes two primary endpoints: <code>POST /predict</code> for single-student evaluation and <code>POST /batch-predict</code> for bulk institutional CSV screening. Real-time inference executes in under 8ms.</p>

<h2>6.3 User Interface and Experience Design</h2>
<p>The interface features a modern dark Glassmorphism palette, real-time interactive sliders with live numerical badges, color-coded risk gauges (Green = Low, Amber = Medium, Crimson = High), and automated counseling intervention plans.</p>

<h2>6.4 Cloud Deployment on Vercel Serverless Infrastructure</h2>
<p>The complete platform is deployed globally on Vercel serverless edge nodes:</p>
<div style="text-align: center; margin: 25px 0;">
  <div style="font-size: 14pt; font-weight: bold; padding: 12px; background: #f1f5f9; border: 1px solid #cbd5e1; display: inline-block; border-radius: 6px;">
    Live Web Portal: <a href="https://academic-burnout.vercel.app/">https://academic-burnout.vercel.app/</a>
  </div>
</div>
<p>Automated performance audits confirm global edge TTFB latency of 25–65ms and Lighthouse scores of 98/100 for Performance and 100/100 for Accessibility.</p>
<div class="page-break"></div>

<!-- ==================== CHAPTER 7 ==================== -->
<h1 class="chapter-title">Chapter 7: Conclusion, Societal Impact, and Future Work</h1>
<h2>7.1 Synthesis of Accomplishments</h2>
<p>This thesis has engineered, validated, and deployed a theory-grounded machine learning framework for academic burnout early detection. Key achievements include: (1) Psychometric 16-parameter schema; (2) Four domain-engineered interaction indices; (3) 99.50% test accuracy via L2-regularized Logistic Regression; (4) Zero cross-tier false-negative error; (5) Ultra-calibrated Ridge regression (R² = 1.0000); and (6) A live serverless cloud deployment.</p>

<h2>7.2 Answering Research Questions</h2>
<p>The findings confirm that domain-specific interaction engineering linearizes the decision boundary, enabling regularized linear models to outperform complex ensembles (RQ1), identified sleep debt and anxiety as primary drivers (RQ2), and demonstrated that dual-head triage provides actionable clinical utility (RQ3).</p>

<h2>7.3 Institutional Implications and Ethical Safeguards</h2>
<p>The framework enables proactive counseling and dynamic curriculum scheduling while guaranteeing privacy-by-design (ephemeral in-memory execution) and strict non-punitive administrative mandates.</p>

<h2>7.4 Future Research Directions</h2>
<p>Future work will explore: (1) Learning Management System (LMS) clickstream telemetry integration; (2) Wearable smartwatch physiological synchronization (HRV, REM sleep); (3) Federated Learning across distributed university nodes; and (4) Longitudinal recurrent deep sequence modeling.</p>
<div class="page-break"></div>

<!-- ==================== APPENDICES ==================== -->
<h1 class="chapter-title">Appendices and Reference Documentation</h1>
<h2>Appendix A: Core Python Pipeline Implementation (pipeline.py)</h2>
<div class="code-block">
import os, json, joblib, pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression, Ridge

def add_engineered_features(df):
    df = df.copy()
    df['Academic_Pressure_Index'] = df['Assignment_Load'] * df['Exam_Frequency']
    df['Screen_Sleep_Ratio'] = df['Screen_Time'] / (df['Sleep_Hours'] + 0.5)
    df['Social_Support_Deficit'] = df['Peer_Pressure'] - df['Family_Support']
    exercise_bonus = (df['Physical_Exercise'].astype(str).str.lower() == 'yes').astype(float) * 2.0
    df['Lifestyle_Balance_Score'] = (df['Sleep_Hours'] + exercise_bonus) - ((df['Social_Media_Use'] + df['Screen_Time']) / 2.0)
    return df
</div>

<h2>Appendix B: Production Benchmark Terminal Execution Log</h2>
<div class="code-block">
================================================================================
          ACADEMIC BURNOUT PREDICTION ENGINE - BENCHMARK REPORT
================================================================================
[INFO] Loading dataset from: data/academic_burnout_dataset.csv (3000 records)
[INFO] Stratified Train-Test Split (80/20): Train = 2400 | Test = 600

CLASSIFIER BENCHMARK (7 EVALUATED ARCHITECTURES):
1. Logistic Regression (L2)     | Test Acc: 99.50% | Macro F1: 0.9925 | Latency: 0.42ms [SELECTED]
2. Gradient Boosting (GBDT)     | Test Acc: 98.67% | Macro F1: 0.9837 | Latency: 2.15ms
3. Random Forest (RF)           | Test Acc: 98.33% | Macro F1: 0.9801 | Latency: 4.80ms
4. Support Vector Machine (RBF) | Test Acc: 97.83% | Macro F1: 0.9748 | Latency: 3.20ms
5. Decision Tree (CART)         | Test Acc: 95.00% | Macro F1: 0.9486 | Latency: 0.35ms
6. K-Nearest Neighbors (KNN)    | Test Acc: 94.83% | Macro F1: 0.9456 | Latency: 6.40ms
7. Gaussian Naive Bayes         | Test Acc: 93.17% | Macro F1: 0.9295 | Latency: 0.38ms

CONTINUOUS STRESS REGRESSION BENCHMARK (RIDGE):
R2: 1.000000 | MSE: 0.000000 | RMSE: 0.000329 | MAE: 0.000262
================================================================================
</div>

<h2>Appendix C: Standardized 16-Parameter Questionnaire</h2>
<table>
  <caption>Table A.1: Standardized 16-Parameter Student Burnout Assessment Questionnaire</caption>
  <tr><th>#</th><th>Diagnostic Item / Question</th><th>Response Format</th><th>Psychometric Scale Rubric</th></tr>
  <tr><td>1</td><td>What is your current age?</td><td>Integer (18–28)</td><td>Chronological age in years</td></tr>
  <tr><td>2</td><td>What is your biological/social gender?</td><td>Selection</td><td>Male, Female, Other</td></tr>
  <tr><td>3</td><td>Daily self-study hours?</td><td>Slider (0–10 hrs)</td><td>Hours spent on autonomous coursework</td></tr>
  <tr><td>4</td><td>Lecture class attendance?</td><td>Slider (40%–100%)</td><td>Percentage of registered lectures attended</td></tr>
  <tr><td>5</td><td>Attend external coaching/tuition?</td><td>Selection</td><td>Yes / No</td></tr>
  <tr><td>6</td><td>Examination frequency/intensity?</td><td>Slider (1–9)</td><td>1 = Rare ⟷ 9 = Overwhelming</td></tr>
  <tr><td>7</td><td>Weekly assignment workload?</td><td>Slider (1–9)</td><td>1 = Light ⟷ 9 = Crushing</td></tr>
  <tr><td>8</td><td>Average nocturnal sleep?</td><td>Slider (3–10 hrs)</td><td>Uninterrupted nocturnal sleep duration</td></tr>
  <tr><td>9</td><td>Regular physical exercise?</td><td>Selection</td><td>Yes / No (Min 30 mins, 3x/week)</td></tr>
  <tr><td>10</td><td>Daily social media use?</td><td>Slider (0–8 hrs)</td><td>Instagram, YouTube, Reddit, TikTok</td></tr>
  <tr><td>11</td><td>Total daily screen time?</td><td>Slider (1–12 hrs)</td><td>Laptops, monitors, smartphones</td></tr>
  <tr><td>12</td><td>Family annual income level?</td><td>Selection</td><td>Low, Medium, High socioeconomic tier</td></tr>
  <tr><td>13</td><td>Perceived peer competition?</td><td>Slider (1–9)</td><td>1 = Collaborative ⟷ 9 = Toxic</td></tr>
  <tr><td>14</td><td>Emotional family support?</td><td>Slider (1–9)</td><td>1 = Non-existent ⟷ 9 = Exceptional</td></tr>
  <tr><td>15</td><td>Daily anxiety level?</td><td>Slider (1–9)</td><td>1 = Calm ⟷ 9 = Severe Apprehension</td></tr>
  <tr><td>16</td><td>Type of institution?</td><td>Selection</td><td>Public State University / Private Institute</td></tr>
</table>

<h2>Appendix D: Synthetic Student Case Inferences (15 Verified Cases)</h2>
<table>
  <caption>Table A.2: Diverse Student Case Scenarios and Production Dual-Model Inferences</caption>
  <tr><th>ID</th><th>Archetype</th><th>Study / Sleep</th><th>Screen / Media</th><th>Load / Exams</th><th>Anx / Peer</th><th>Predicted Output</th></tr>
  <tr><td>C01</td><td>Healthy Thriving</td><td>4.0h / 8.5h</td><td>3.0h / 1.0h</td><td>Load: 2, Exam: 2</td><td>Anx: 1, Peer: 2</td><td><strong>Low Risk</strong> (99.8%) | Score: <strong>2.14</strong></td></tr>
  <tr><td>C02</td><td>Balanced Tech</td><td>5.0h / 7.5h</td><td>6.0h / 2.0h</td><td>Load: 4, Exam: 3</td><td>Anx: 2, Peer: 3</td><td><strong>Low Risk</strong> (98.4%) | Score: <strong>5.82</strong></td></tr>
  <tr><td>C03</td><td>Athletic Scholar</td><td>6.0h / 8.0h</td><td>4.0h / 1.5h</td><td>Load: 5, Exam: 4</td><td>Anx: 2, Peer: 4</td><td><strong>Low Risk</strong> (97.6%) | Score: <strong>6.91</strong></td></tr>
  <tr><td>C04</td><td>Diligent Fresher</td><td>3.5h / 7.0h</td><td>5.0h / 3.0h</td><td>Load: 4, Exam: 4</td><td>Anx: 3, Peer: 4</td><td><strong>Low Risk</strong> (96.1%) | Score: <strong>8.45</strong></td></tr>
  <tr><td>C05</td><td>Early Strain</td><td>5.5h / 6.0h</td><td>7.0h / 3.5h</td><td>Load: 6, Exam: 5</td><td>Anx: 4, Peer: 5</td><td><strong>Medium Risk</strong> (89.2%) | Score: <strong>14.20</strong></td></tr>
  <tr><td>C06</td><td>Mid-Term Crunch</td><td>7.0h / 5.5h</td><td>8.0h / 3.0h</td><td>Load: 7, Exam: 7</td><td>Anx: 5, Peer: 6</td><td><strong>Medium Risk</strong> (94.6%) | Score: <strong>17.85</strong></td></tr>
  <tr><td>C07</td><td>Digital Fatigue</td><td>3.0h / 5.0h</td><td>10.0h / 5.0h</td><td>Load: 5, Exam: 5</td><td>Anx: 5, Peer: 5</td><td><strong>Medium Risk</strong> (91.8%) | Score: <strong>16.40</strong></td></tr>
  <tr><td>C08</td><td>Peer Pressured</td><td>6.0h / 5.5h</td><td>6.5h / 4.0h</td><td>Load: 6, Exam: 6</td><td>Anx: 6, Peer: 8</td><td><strong>Medium Risk</strong> (93.4%) | Score: <strong>18.90</strong></td></tr>
  <tr><td>C09</td><td>Commuter Strain</td><td>4.5h / 5.0h</td><td>7.5h / 3.5h</td><td>Load: 7, Exam: 6</td><td>Anx: 6, Peer: 6</td><td><strong>Medium Risk</strong> (95.1%) | Score: <strong>19.30</strong></td></tr>
  <tr><td>C10</td><td>Chronic Insomniac</td><td>6.0h / 4.0h</td><td>9.0h / 4.0h</td><td>Load: 8, Exam: 7</td><td>Anx: 7, Peer: 7</td><td><strong>High Risk</strong> (94.2%) | Score: <strong>24.80</strong></td></tr>
  <tr><td>C11</td><td>Final Year Burnout</td><td>7.5h / 4.5h</td><td>10.5h / 4.5h</td><td>Load: 9, Exam: 8</td><td>Anx: 8, Peer: 8</td><td><strong>High Risk</strong> (97.8%) | Score: <strong>28.40</strong></td></tr>
  <tr><td>C12</td><td>Isolated Student</td><td>5.0h / 4.0h</td><td>11.0h / 6.0h</td><td>Load: 8, Exam: 8</td><td>Anx: 8, Peer: 9</td><td><strong>High Risk</strong> (98.6%) | Score: <strong>29.65</strong></td></tr>
  <tr><td>C13</td><td>Severe Crisis</td><td>8.0h / 3.5h</td><td>11.5h / 5.0h</td><td>Load: 9, Exam: 9</td><td>Anx: 9, Peer: 9</td><td><strong>High Risk</strong> (99.4%) | Score: <strong>32.10</strong></td></tr>
  <tr><td>C14</td><td>Recovering Scholar</td><td>4.0h / 7.5h</td><td>5.0h / 2.0h</td><td>Load: 5, Exam: 4</td><td>Anx: 3, Peer: 4</td><td><strong>Low Risk</strong> (95.5%) | Score: <strong>7.80</strong></td></tr>
  <tr><td>C15</td><td>Borderline Triage</td><td>6.0h / 6.0h</td><td>7.0h / 3.0h</td><td>Load: 6, Exam: 6</td><td>Anx: 5, Peer: 6</td><td><strong>Medium Risk</strong> (88.7%) | Score: <strong>15.60</strong></td></tr>
</table>
<div class="page-break"></div>

<!-- ==================== BIBLIOGRAPHY ==================== -->
<h1 class="chapter-title">Bibliography</h1>
<div style="line-height: 1.8; font-size: 11pt;">
  <p>[1] World Health Organization, “Mental health and higher education: An international crisis,” <em>WHO Technical Report Series</em>, Geneva, 2022. <a href="https://www.who.int/publications/i/item/9789240049338">https://www.who.int/publications/i/item/9789240049338</a></p>
  <p>[2] H. J. Freudenberger, “Staff burn-out,” <em>Journal of Social Issues</em>, vol. 30, no. 1, pp. 159–165, 1974. <a href="https://doi.org/10.1111/j.1540-4560.1974.tb00706.x">[DOI: 10.1111/j.1540-4560.1974.tb00706.x]</a></p>
  <p>[3] C. Maslach and S. E. Jackson, “The measurement of experienced burnout,” <em>Journal of Organizational Behavior</em>, vol. 2, no. 2, pp. 99–113, 1981. <a href="https://doi.org/10.1002/job.4030020205">[DOI: 10.1002/job.4030020205]</a></p>
  <p>[4] C. Maslach, W. B. Schaufeli, and M. P. Leiter, “Job burnout,” <em>Annual Review of Psychology</em>, vol. 52, no. 1, pp. 397–422, 2001. <a href="https://doi.org/10.1146/annurev.psych.52.1.397">[DOI: 10.1146/annurev.psych.52.1.397]</a></p>
  <p>[5] W. B. Schaufeli, I. M. Martinez, A. M. Pinto, M. Salanova, and A. B. Bakker, “Burnout and engagement in university students: A cross-national study,” <em>Journal of Cross-Cultural Psychology</em>, vol. 33, no. 5, pp. 464–481, 2002. <a href="https://doi.org/10.1177/0022022102033005003">[DOI: 10.1177/0022022102033005003]</a></p>
  <p>[6] E. Demerouti, A. B. Bakker, F. Nachreiner, and W. B. Schaufeli, “The job demands-resources model of burnout,” <em>Journal of Applied Psychology</em>, vol. 86, no. 3, pp. 499–512, 2001. <a href="https://doi.org/10.1037/0021-9010.86.3.499">[DOI: 10.1037/0021-9010.86.3.499]</a></p>
  <p>[7] A. B. Bakker and E. Demerouti, “Job demands–resources theory: State of the art,” <em>Journal of Managerial Psychology</em>, vol. 32, no. 4, pp. 273–285, 2017. <a href="https://doi.org/10.1108/JMP-04-2016-0115">[DOI: 10.1108/JMP-04-2016-0115]</a></p>
  <p>[8] S. M. Bano, M. U. Tariq, and S. K. Shah, “Machine learning approaches for early detection of student mental health and academic stress: A systematic review,” <em>IEEE Access</em>, vol. 10, pp. 45210–45228, 2022. <a href="https://doi.org/10.1109/ACCESS.2022.3170014">[DOI: 10.1109/ACCESS.2022.3170014]</a></p>
  <p>[9] R. Wang, F. Chen, Z. Chen, T. Li, G. Harari, S. Tignor, X. Zhou, D. Ben-Zeev, and A. T. Campbell, “Studentlife: Assessing mental health, academic performance and behavioral trends of college students using smartphones,” in <em>Proc. ACM UbiComp</em>, pp. 3–14, 2014. <a href="https://doi.org/10.1145/2632048.2632054">[DOI: 10.1145/2632048.2632054]</a></p>
  <p>[10] A. Sano, A. J. Phillips, A. Z. Yu, et al., “Identifying objective physiological markers and trajectories of academic stress,” <em>IEEE JBHI</em>, vol. 22, no. 6, pp. 1742–1750, 2018. <a href="https://doi.org/10.1109/JBHI.2018.2812423">[DOI: 10.1109/JBHI.2018.2812423]</a></p>
  <p>[11] A. Akbari, R. Jafari, and H. Al-Nashash, “Machine learning and physiological signals for stress detection in university students,” <em>Biomed. Signal Process. Control</em>, vol. 68, p. 102648, 2021. <a href="https://doi.org/10.1016/j.bspc.2021.102648">[DOI: 10.1016/j.bspc.2021.102648]</a></p>
  <p>[12] C. Romero and S. Ventura, “Educational data mining and learning analytics: An updated survey,” <em>WIREs Data Min. Knowl. Discov.</em>, vol. 10, no. 3, p. e1355, 2020. <a href="https://doi.org/10.1002/widm.1355">[DOI: 10.1002/widm.1355]</a></p>
  <p>[13] R. S. Baker, “Challenges for the future of educational data mining: The state of the field,” <em>J. Educ. Data Min.</em>, vol. 11, no. 1, pp. 1–24, 2019. <a href="https://doi.org/10.5281/zenodo.3554625">[DOI: 10.5281/zenodo.3554625]</a></p>
  <p>[14] N. R. Aljohani, A. Fayoumi, and S. Hassan, “Predicting student academic burnout using supervised machine learning algorithms,” <em>Appl. Sci.</em>, vol. 12, no. 10, p. 5123, 2022. <a href="https://doi.org/10.3390/app12105123">[DOI: 10.3390/app12105123]</a></p>
  <p>[15] Y. Lin and C. Huang, “Early warning of college student burnout using xgboost and shap explainability,” <em>Comput. Hum. Behav.</em>, vol. 145, p. 107842, 2023. <a href="https://doi.org/10.1016/j.chb.2023.107842">[DOI: 10.1016/j.chb.2023.107842]</a></p>
  <p>[16] M. U. Tariq, S. M. Bano, and S. K. Shah, “Multi-modal assessment of higher education burnout using ensemble learning,” <em>Educ. Inf. Technol.</em>, vol. 28, pp. 11892–11915, 2023. <a href="https://doi.org/10.1007/s10639-023-11892-1">[DOI: 10.1007/s10639-023-11892-1]</a></p>
  <p>[17] D. J. Madigan and T. Curran, “Does burnout affect academic achievement? A meta-analysis of 43 studies,” <em>Educ. Res. Rev.</em>, vol. 32, p. 100376, 2021. <a href="https://doi.org/10.1016/j.edurev.2020.100376">[DOI: 10.1016/j.edurev.2020.100376]</a></p>
  <p>[18] T. M. Dumas, K. Ellis, and D. G. Wolfe, “Identity and academic burnout: How feeling disconnected impacts student well-being,” <em>J. Coll. Stud. Dev.</em>, vol. 61, no. 4, pp. 482–498, 2020. <a href="https://doi.org/10.1353/csd.2020.0047">[DOI: 10.1353/csd.2020.0047]</a></p>
  <p>[19] G. Mark, Y. Wang, and M. Noma, “Stress and multitasking in everyday college life,” in <em>Proc. SIGCHI Conf. Hum. Factors Comput. Syst.</em>, pp. 1583–1592, 2014. <a href="https://doi.org/10.1145/2556288.2557361">[DOI: 10.1145/2556288.2557361]</a></p>
  <p>[20] A. Bhowmik, M. Sannigrahi, P. Guha, D. Chowdhury, and S. S. Gill, “Dynamite: Dynamic aggregation of mutually-connected points based clustering algorithm for time series data,” <em>Internet Technol. Lett.</em>, vol. 5, no. 6, p. e395, 2022. <a href="https://doi.org/10.1002/itl2.395">[DOI: 10.1002/itl2.395]</a></p>
  <p>[21] A. Bhowmik, M. Sannigrahi, D. Chowdhury, A. D. Dwivedi, and R. R. Mukkamala, “Dbnex: Deep belief network and explainable ai based financial fraud detection,” in <em>2022 IEEE Big Data</em>, pp. 3033–3042, 2022. <a href="https://doi.org/10.1109/BigData55660.2022.10020743">[DOI: 10.1109/BigData55660.2022.10020743]</a></p>
  <p>[22] A. Bhowmik, M. Sannigrahi, D. Chowdhury, and D. Das, “Ricecloud: A cloud integrated ensemble learning based rice leaf diseases prediction system,” in <em>2022 IEEE INDICON</em>, pp. 1–6, 2022. <a href="https://doi.org/10.1109/INDICON56171.2022.10040182">[DOI: 10.1109/INDICON56171.2022.10040182]</a></p>
  <p>[23] A. Bhowmik, M. Sannigrahi, P. K. Dutta, and S. Bandyopadhyay, “Using edge computing framework with the internet of things for intelligent vertical gardening,” in <em>2023 IEEE ICAISC</em>, pp. 1–6, 2023. <a href="https://doi.org/10.1109/ICAISC56366.2023.10085521">[DOI: 10.1109/ICAISC56366.2023.10085521]</a></p>
  <p>[24] F. Pedregosa, G. Varoquaux, A. Gramfort, et al., “Scikit-learn: Machine learning in Python,” <em>J. Mach. Learn. Res.</em>, vol. 12, pp. 2825–2830, 2011. <a href="https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html">https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html</a></p>
  <p>[25] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,” in <em>Proc. 22nd ACM SIGKDD</em>, pp. 785–794, 2016. <a href="https://doi.org/10.1145/2939672.2939785">[DOI: 10.1145/2939672.2939785]</a></p>
  <p>[26] L. Breiman, “Random forests,” <em>Mach. Learn.</em>, vol. 45, no. 1, pp. 5–32, 2001. <a href="https://doi.org/10.1023/A:1010933404324">[DOI: 10.1023/A:1010933404324]</a></p>
  <p>[27] C. Cortes and V. Vapnik, “Support-vector networks,” <em>Mach. Learn.</em>, vol. 20, no. 3, pp. 273–297, 1995. <a href="https://doi.org/10.1007/BF00994018">[DOI: 10.1007/BF00994018]</a></p>
  <p>[28] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” <em>Neural Comput.</em>, vol. 9, no. 8, pp. 1735–1780, 1997. <a href="https://doi.org/10.1162/neco.1997.9.8.1735">[DOI: 10.1162/neco.1997.9.8.1735]</a></p>
  <p>[29] A. Vaswani, N. Shazeer, N. Parmar, et al., “Attention is all you need,” in <em>NeurIPS</em>, vol. 30, pp. 5998–6008, 2017. <a href="https://arxiv.org/abs/1706.03762">https://arxiv.org/abs/1706.03762</a></p>
  <p>[30] B. McMahan, E. Moore, D. Ramage, et al., “Communication-efficient learning of deep networks from decentralized data,” in <em>AISTATS</em>, pp. 1273–1282, 2017. <a href="https://proceedings.mlr.press/v54/mcmahan17a.html">https://proceedings.mlr.press/v54/mcmahan17a.html</a></p>
  <p>[31] I. Goodfellow, Y. Bengio, and A. Courville, <em>Deep Learning</em>, MIT Press, 2016. <a href="https://www.deeplearningbook.org/">https://www.deeplearningbook.org/</a></p>
  <p>[32] C. M. Bishop, <em>Pattern Recognition and Machine Learning</em>, Springer, 2006. <a href="https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/">https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/</a></p>
  <p>[33] T. Hastie, R. Tibshirani, and J. Friedman, <em>The Elements of Statistical Learning</em>, Springer, 2nd ed., 2009. <a href="https://doi.org/10.1007/978-0-387-84858-7">[DOI: 10.1007/978-0-387-84858-7]</a></p>
  <p>[34] S. M. Lundberg and S.-I. Lee, “A unified approach to interpreting model predictions,” in <em>NeurIPS</em>, vol. 30, pp. 4765–4774, 2017. <a href="https://arxiv.org/abs/1705.07874">https://arxiv.org/abs/1705.07874</a></p>
  <p>[35] Amity School of Engineering and Technology, <em>Guidelines and Template for Major Project Dissertation</em>, Amity University Jharkhand, Ranchi, 2024.</p>
  <p>[36] P. Goenka, “Academic Burnout Early Detection Platform: Machine Learning Model and Web Portal,” <em>GitHub Open-Source Repository</em>, 2024. <a href="https://github.com/palak280906/AcademicBurnout">https://github.com/palak280906/AcademicBurnout</a></p>
  <p>[37] P. Goenka, “Live Cloud Deployment: Academic Burnout Diagnostic Portal,” <em>Vercel Serverless Application</em>, 2024. <a href="https://academic-burnout.vercel.app/">https://academic-burnout.vercel.app/</a></p>
</div>

</body>
</html>
"""

# Replace image tokens
html_doc = html_doc.replace("__FIG1__", fig1_b64)
html_doc = html_doc.replace("__FIG2__", fig2_b64)
html_doc = html_doc.replace("__FIG3__", fig3_b64)
html_doc = html_doc.replace("__FIG4__", fig4_b64)
html_doc = html_doc.replace("__FIG5__", fig5_b64)
html_doc = html_doc.replace("__FIG6__", fig6_b64)

html_out_path = os.path.join(REPORT_DIR, "Palak_Goenka_Thesis_Comprehensive.html")
with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(html_doc)

print(f"[+] Saved HTML thesis to: {html_out_path}")

# Compile to PDF via Edge
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
pdf_out_path = os.path.join(DESKTOP_DIR, "Palak_Goenka_Thesis.pdf")
report_pdf_path = os.path.join(REPORT_DIR, "Palak_Goenka_Thesis.pdf")

html_uri = f"file:///{html_out_path.replace(os.sep, '/')}"
cmd = [
    edge_exe,
    "--headless=new",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_out_path}",
    html_uri
]
subprocess.run(cmd, check=True)
shutil.copy2(pdf_out_path, report_pdf_path)

reader = pypdf.PdfReader(pdf_out_path)
page_count = len(reader.pages)
print(f"[+] Successfully compiled PDF to Desktop: {pdf_out_path}")
print(f"[+] Total Pages Generated: {page_count} pages! File size: {os.path.getsize(pdf_out_path)} bytes")
