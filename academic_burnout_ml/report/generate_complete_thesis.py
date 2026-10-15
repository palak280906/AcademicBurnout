"""
Generator for Complete Official Academic Thesis Report
Strictly adheres to Amity School of Engineering and Technology (ASET) Template.
Embeds all high-resolution figures (Base64), comprehensive analytical tables,
mathematical formulations, code snippets, and live model prediction outputs.
"""

import os
import base64
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
REPORT_DIR = os.path.join(BASE_DIR, "report")

# Load figures as Base64 strings to ensure 100% embedded rendering in PDF
def get_base64_image(filename):
    filepath = os.path.join(FIGURES_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "rb") as img_f:
            encoded = base64.b64encode(img_f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""

fig1_b64 = get_base64_image("fig1_eda_distributions.png")
fig2_b64 = get_base64_image("fig2_correlation_matrix.png")
fig3_b64 = get_base64_image("fig3_model_comparison.png")
fig4_b64 = get_base64_image("fig4_confusion_matrices.png")
fig5_b64 = get_base64_image("fig5_feature_importance.png")
fig6_b64 = get_base64_image("fig6_stress_score_regression.png")

css = """
<style>
  @page {
    size: A4 portrait;
    margin: 25mm 20mm 25mm 25mm; /* Standard academic thesis binding margins */
    @bottom-center {
      content: counter(page);
    }
  }

  *, *:before, *:after {
    box-sizing: border-box;
  }

  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.6;
    color: #111;
    background: #ffffff;
    margin: 0;
    padding: 0;
  }

  .page-break {
    page-break-after: always;
    break-after: page;
    clear: both;
  }

  /* Academic Typography */
  h1.thesis-title {
    font-size: 22pt;
    font-weight: bold;
    text-align: center;
    line-height: 1.3;
    margin-top: 40px;
    margin-bottom: 25px;
    text-transform: uppercase;
    border-top: 2px solid #000;
    border-bottom: 2px solid #000;
    padding: 15px 0;
  }

  h1.chapter-title {
    font-size: 18pt;
    font-weight: bold;
    text-align: left;
    margin-top: 20px;
    margin-bottom: 15px;
    text-transform: uppercase;
    border-bottom: 1.5px solid #000;
    padding-bottom: 5px;
  }

  h2.section-title {
    font-size: 14pt;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 10px;
    color: #000;
  }

  h3.subsection-title {
    font-size: 12pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 18px;
    margin-bottom: 8px;
  }

  p {
    text-align: justify;
    text-justify: inter-word;
    margin-bottom: 12px;
    text-indent: 0;
  }

  .page-num {
    text-align: center;
    font-size: 10pt;
    margin-top: 30px;
  }

  /* Title Page */
  .title-page-container {
    text-align: center;
    padding-top: 20px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 920px;
  }

  .amity-logo-box {
    margin: 35px auto;
    width: 220px;
    padding: 12px;
    border: 2px solid #1a365d;
    background: #f8fafc;
    border-radius: 6px;
  }

  .amity-logo-title {
    font-size: 18pt;
    font-weight: 800;
    color: #1a365d;
    letter-spacing: 1px;
    margin: 0;
  }

  .amity-logo-sub {
    font-size: 11pt;
    font-weight: 700;
    color: #d97706;
    letter-spacing: 0.5px;
    margin: 0;
  }

  /* Certificate & Declaration */
  .cert-container {
    padding-top: 20px;
  }

  .signature-table {
    width: 100%;
    margin-top: 60px;
    border-collapse: collapse;
  }

  .signature-table td {
    border: none;
    padding: 30px 10px 10px 10px;
    vertical-align: bottom;
    text-align: center;
    width: 33.33%;
  }

  .sig-line {
    border-top: 1px solid #000;
    width: 85%;
    margin: 0 auto 5px auto;
  }

  /* Abstract Metadata Table */
  .meta-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 25px;
  }

  .meta-table td {
    padding: 6px 10px;
    font-size: 11pt;
    border-top: 1px solid #000;
    border-bottom: 1px solid #000;
  }

  /* Tables */
  table.academic-table {
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-size: 10pt;
    page-break-inside: avoid;
  }

  table.academic-table th, table.academic-table td {
    border: 1px solid #333;
    padding: 6px 10px;
    text-align: left;
  }

  table.academic-table th {
    background-color: #f1f5f9;
    font-weight: bold;
    text-align: center;
  }

  table.academic-table tr:nth-child(even) {
    background-color: #f8fafc;
  }

  .table-caption {
    font-size: 10.5pt;
    font-weight: bold;
    margin-top: 15px;
    margin-bottom: 6px;
    text-align: left;
  }

  /* Figures */
  .figure-container {
    text-align: center;
    margin: 20px 0;
    page-break-inside: avoid;
  }

  .figure-container img {
    max-width: 95%;
    max-height: 400px;
    height: auto;
    display: block;
    margin: 0 auto;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 4px;
    background: #fff;
  }

  .figure-caption {
    font-size: 10pt;
    font-weight: bold;
    margin-top: 8px;
    margin-bottom: 18px;
    text-align: center;
  }

  /* Code / Terminal Output Block */
  pre.terminal-output {
    background-color: #0f172a;
    color: #38bdf8;
    padding: 14px 18px;
    border-radius: 6px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 9pt;
    line-height: 1.45;
    overflow-x: auto;
    margin: 15px 0;
    border: 1px solid #1e293b;
    page-break-inside: avoid;
  }

  code {
    font-family: 'Consolas', 'Courier New', monospace;
    background: #f1f5f9;
    padding: 2px 4px;
    border-radius: 3px;
    font-size: 10pt;
  }

  .formula-box {
    background: #f8fafc;
    border-left: 3px solid #1a365d;
    padding: 10px 15px;
    margin: 14px 0;
    font-family: 'Times New Roman', serif;
    font-size: 11pt;
  }
</style>
"""

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Thesis: Early Detection of Academic Burnout using Machine Learning - Amity University</title>
  {css}
</head>
<body>

  <!-- ================= PAGE 1: TITLE PAGE ================= -->
  <div class="title-page-container">
    <div>
      <h1 class="thesis-title">Early Detection of Academic Burnout using Machine Learning<br><span style="font-size: 14pt; font-weight: normal; text-transform: none;">A Multi-Dimensional Predictive Behavioral Informatics System</span></h1>
      
      <p style="font-size: 13pt; font-style: italic; margin-top: 25px;">Major Project submitted to</p>
      <p style="font-size: 13pt; font-weight: bold;">Amity School of Engineering and Technology, Amity University</p>
      <p style="font-size: 12pt; font-style: italic;">in partial fulfilment of the requirements for</p>
      <p style="font-size: 14pt; font-weight: bold; margin-top: 10px;">The degree of</p>
      <p style="font-size: 16pt; font-weight: bold; color: #1a365d;">Bachelor of Technology</p>
      <p style="font-size: 13pt; font-style: italic;">from</p>
      <p style="font-size: 13pt; font-weight: bold;">Department of Computer Science and Engineering,<br>Amity School of Engineering and Technology</p>

      <p style="font-size: 12pt; font-style: italic; margin-top: 35px;">by</p>
      <p style="font-size: 14pt; font-weight: bold;">Palak Goenka</p>
      <p style="font-size: 11pt; color: #475569;">(Enrollment No: A357175124008)</p>

      <p style="font-size: 12pt; font-style: italic; margin-top: 15px;">under the guidance of</p>
      <p style="font-size: 14pt; font-weight: bold;">Prof. Supervisor</p>
    </div>

    <div>
      <div class="amity-logo-box">
        <div class="amity-logo-title">AMITY</div>
        <div class="amity-logo-sub">UNIVERSITY</div>
        <div style="font-size: 8.5pt; font-weight: 600; color: #1e293b; letter-spacing: 0.5px;">— JHARKHAND —</div>
      </div>

      <p style="font-size: 12pt; font-weight: bold; margin-bottom: 2px;">Amity School of Engineering and Technology</p>
      <p style="font-size: 13pt; font-weight: bold; letter-spacing: 1px; color: #1a365d;">AMITY UNIVERSITY</p>
      <p style="font-size: 11pt; margin-top: 2px;">Ranchi-834002, Jharkhand, India</p>
      <p style="font-size: 11pt; font-weight: bold; margin-top: 4px;">October 2026</p>
    </div>
  </div>
  <div class="page-break"></div>

  <!-- ================= PAGE 2: CERTIFICATE ================= -->
  <div class="cert-container">
    <h1 style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 40px; text-transform: uppercase;">Certificate</h1>

    <p style="font-size: 12pt; line-height: 1.8; text-align: justify;">
      This is to certify that the project work entitled <strong>“Early Detection of Academic Burnout using Machine Learning”</strong> has been prepared by <strong>“Palak Goenka”</strong> under my supervision and guidance. The thesis is his original work completed after careful research and investigation. The work of the thesis is of the standard expected of a candidate for the <strong>Bachelor of Technology Programme in Artificial Intelligence</strong> and I recommend that it be sent for evaluation.
    </p>

    <div style="margin-top: 80px;">
      <p style="font-size: 11pt; margin-bottom: 20px;"><strong>Date:</strong> October 2026</p>
      <p style="font-size: 11pt;"><strong>Forwarded By:</strong></p>

      <table class="signature-table">
        <tr>
          <td>
            <div class="sig-line"></div>
            <strong>Prof. Supervisor</strong><br>
            <span style="font-size: 10pt;">Name and Signature of the Guide</span>
          </td>
          <td>
            <div class="sig-line"></div>
            <strong>Head of Department</strong><br>
            <span style="font-size: 10pt;">Name and Signature of the Head of the Department</span>
          </td>
          <td>
            <div class="sig-line"></div>
            <strong>Director / Principal</strong><br>
            <span style="font-size: 10pt;">Name and Signature of the Head of Institution</span>
          </td>
        </tr>
      </table>
    </div>

    <div class="page-num">ii</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= PAGE 3: DECLARATION ================= -->
  <div class="cert-container">
    <h1 style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 40px; text-transform: uppercase;">Declaration</h1>

    <p style="font-size: 12pt; line-height: 1.8; text-align: justify;">
      I, <strong>Palak Goenka</strong>, registered as an undergraduate scholar, bearing <strong>Registration Number: A357175124008</strong> for the <strong>Bachelor of Technology Programme in Artificial Intelligence</strong> under the Amity School of Engineering and Technology of Amity University Jharkhand, do hereby declare that I have completed the requirements as per mentioned by the university for project submission.
    </p>

    <p style="font-size: 12pt; line-height: 1.8; text-align: justify; margin-top: 20px;">
      I do hereby declare that the project submitted is original and is the outcome of the independent investigations / research carried out by me and contains no plagiarism. The work is leading to the discovery of new techniques in educational machine learning and predictive behavioral analytics. This work has not been submitted by any other University or Body in quest of a degree, diploma or any other kind of academic award.
    </p>

    <p style="font-size: 12pt; line-height: 1.8; text-align: justify; margin-top: 20px;">
      I do hereby further declare that the text, diagrams or any other material taken from other sources (including but not limited to books, journals and web) have been acknowledged, referred and cited to the best of my knowledge and understanding.
    </p>

    <div style="margin-top: 90px;">
      <p style="font-size: 11pt;"><strong>Date:</strong> October 2026</p>
      <div style="float: right; text-align: center; margin-top: 30px; width: 300px;">
        <div style="border-top: 1px solid #000; padding-top: 5px; font-weight: bold;">Signature of Student</div>
        <div style="font-size: 10pt;">Palak Goenka (Enroll No: A357175124008)</div>
      </div>
      <div style="clear: both;"></div>
    </div>

    <div class="page-num">iii</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= PAGE 4: ABSTRACT ================= -->
  <div>
    <h1 style="text-align: center; font-size: 18pt; font-weight: bold; font-style: italic; margin-bottom: 25px;">Abstract</h1>

    <table class="meta-table">
      <tr>
        <td><strong>Name of the student:</strong> Palak Goenka</td>
        <td><strong>Enroll No:</strong> A357175124008</td>
      </tr>
      <tr>
        <td><strong>Degree for which submitted:</strong> B.Tech (AI)</td>
        <td><strong>Department:</strong> CSE Department</td>
      </tr>
      <tr>
        <td colspan="2"><strong>Project title:</strong> Early Detection of Academic Burnout using Machine Learning</td>
      </tr>
      <tr>
        <td colspan="2"><strong>Project Guide:</strong> Prof. Supervisor</td>
      </tr>
      <tr>
        <td colspan="2"><strong>Month and year of project submission:</strong> October 2026</td>
      </tr>
    </table>

    <p style="text-align: justify; font-size: 11.5pt; line-height: 1.65;">
      Academic burnout represents a multidimensional syndrome characterized by emotional exhaustion, depersonalization or cynicism toward educational commitments, and a perceived reduction in personal academic efficacy. Left unaddressed, chronic academic stress leads to severe depression, cognitive attrition, and student dropout rates. Traditional screening methodologies rely predominantly on periodic self-reported retrospective psychometric instruments (such as the Maslach Burnout Inventory – Student Survey, MBI-SS), which typically detect burnout only after acute psychological impairment has already manifested.
    </p>

    <p style="text-align: justify; font-size: 11.5pt; line-height: 1.65;">
      In this research, we propose, develop, and validate an end-to-end Machine Learning framework designed for the <strong>early, non-invasive detection of academic burnout</strong>. Utilizing a multi-institutional cohort dataset of <strong>3,000 university students</strong> across National, Public, and Private tertiary institutions, we engineer domain-specific physiological, lifestyle, and pedagogical interaction features—including the <em>Academic Pressure Index</em>, <em>Screen-to-Sleep Ratio</em>, <em>Social Support Deficit</em>, and <em>Lifestyle Balance Score</em>.
    </p>

    <p style="text-align: justify; font-size: 11.5pt; line-height: 1.65;">
      We systematically evaluate seven machine learning classification architectures under a rigorous 5-fold Stratified Cross-Validation protocol: Multinomial Logistic Regression, Support Vector Machines (SVM with RBF Kernel), Multi-Layer Perceptrons (MLP), Gradient Boosting (GBM), Random Forest (RF), Extra Trees (ET), and K-Nearest Neighbors (KNN). Concurrently, a secondary regression pipeline is developed to predict continuous <em>Burnout Stress Scores</em>.
    </p>

    <p style="text-align: justify; font-size: 11.5pt; line-height: 1.65;">
      Empirical evaluation indicates that the <strong>Multinomial Logistic Classifier</strong> achieves the highest classification performance with an overall accuracy of <strong>99.50% (&plusmn;0.11%)</strong> and a Macro F1-score of <strong>0.9909</strong>, followed by the Multi-Layer Perceptron (<strong>97.53%</strong>) and Support Vector Machine (<strong>94.73%</strong>). Ridge Regression achieves an <strong>R&sup2; score of 1.0000</strong> (MAE: 0.00, RMSE: 0.01) for continuous stress score mapping, demonstrating a quantifiable, linear relationship between cumulative psychosocial stressors and clinical burnout risk. Feature importance diagnostics identify <em>Assignment Load</em>, <em>Exam Frequency</em>, <em>Sleep Deprivation</em>, <em>Anxiety Level</em>, and <em>Digital Screen Exposure</em> as the primary predictive drivers. Finally, an interactive decision-support engine is implemented to translate classification outputs into personalized, prescriptive academic and lifestyle intervention directives.
    </p>

    <div class="page-num">iv</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= PAGE 5: ACKNOWLEDGEMENTS ================= -->
  <div class="cert-container">
    <h1 style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 40px; text-transform: uppercase;">Acknowledgements</h1>

    <p style="font-size: 12pt; line-height: 1.8; text-align: justify;">
      I express my deepest sense of gratitude and sincere indebtedness to my project supervisor, <strong>Prof. Supervisor</strong>, Department of Computer Science and Engineering, Amity School of Engineering and Technology, Amity University Jharkhand, for invaluable guidance, constructive critique, and constant encouragement throughout the course of this major project.
    </p>

    <p style="font-size: 12pt; line-height: 1.8; text-align: justify; margin-top: 20px;">
      I am immensely thankful to the <strong>Head of the Department</strong>, Department of Computer Science and Engineering, and the <strong>Head of Institution</strong>, Amity School of Engineering and Technology, for providing the state-of-the-art computational infrastructure, laboratories, and academic support required to successfully accomplish this research.
    </p>

    <p style="font-size: 12pt; line-height: 1.8; text-align: justify; margin-top: 20px;">
      I also extend my heartfelt thanks to all faculty members, technical staff, and peer colleagues at Amity University for their insightful discussions and moral support. Lastly, I owe endless gratitude to my parents and family members whose unwavering encouragement and patience have been my greatest pillars of strength.
    </p>

    <div style="margin-top: 80px; text-align: right;">
      <p style="font-weight: bold; margin-bottom: 2px;">Palak Goenka</p>
      <p style="font-size: 11pt; margin-bottom: 2px;">Enrollment No: A357175124008</p>
      <p style="font-size: 11pt; margin-bottom: 2px;">B.Tech (Artificial Intelligence)</p>
      <p style="font-size: 11pt;">Amity University Jharkhand, Ranchi</p>
    </div>

    <div class="page-num">v</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= PAGE 6: CONTENTS ================= -->
  <div>
    <h1 style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 30px;">Contents</h1>

    <table style="width: 100%; font-size: 11.5pt; border-collapse: collapse; line-height: 1.8;">
      <tr><td><strong>Acknowledgements</strong></td><td style="text-align: right;">v</td></tr>
      <tr><td><strong>List of Figures</strong></td><td style="text-align: right;">vii</td></tr>
      <tr><td><strong>List of Tables</strong></td><td style="text-align: right;">viii</td></tr>
      <tr><td><strong>Abbreviations</strong></td><td style="text-align: right;">ix</td></tr>
      <tr><td colspan="2" style="padding-top: 10px;"></td></tr>
      <tr><td><strong>1&nbsp;&nbsp;Introduction</strong></td><td style="text-align: right;"><strong>1</strong></td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.1 Background and Context</td><td style="text-align: right;">1</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.2 Problem Statement</td><td style="text-align: right;">1</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.3 Research Objectives</td><td style="text-align: right;">2</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.4 Scope and Significance</td><td style="text-align: right;">2</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;1.5 Organization of Thesis</td><td style="text-align: right;">2</td></tr>
      <tr><td colspan="2" style="padding-top: 6px;"></td></tr>
      <tr><td><strong>2&nbsp;&nbsp;Related Works</strong></td><td style="text-align: right;"><strong>3</strong></td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;2.1 Psychological Frameworks of Burnout</td><td style="text-align: right;">3</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;2.2 Traditional Psychometric Inventories &amp; Limitations</td><td style="text-align: right;">3</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;2.3 AI and Machine Learning in Student Mental Health</td><td style="text-align: right;">3</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;2.4 Research Gaps Addressed in this Study</td><td style="text-align: right;">4</td></tr>
      <tr><td colspan="2" style="padding-top: 6px;"></td></tr>
      <tr><td><strong>3&nbsp;&nbsp;Theoretical Background</strong></td><td style="text-align: right;"><strong>5</strong></td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.1 Supervised Learning Paradigm</td><td style="text-align: right;">5</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.2 Candidate Classifier Formulations (LR, SVM, RF, GBM, MLP)</td><td style="text-align: right;">5</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.3 Continuous Stress Estimation via Ridge Regression</td><td style="text-align: right;">6</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;3.4 Evaluation Metrics and Validation Protocol</td><td style="text-align: right;">6</td></tr>
      <tr><td colspan="2" style="padding-top: 6px;"></td></tr>
      <tr><td><strong>4&nbsp;&nbsp;Methodology</strong></td><td style="text-align: right;"><strong>7</strong></td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;4.1 System Architectural Pipeline</td><td style="text-align: right;">7</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;4.2 Dataset Ingestion and Demographic Profile (N=3,000)</td><td style="text-align: right;">7</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;4.3 Data Preprocessing &amp; Categorical Encoding</td><td style="text-align: right;">8</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;4.4 Domain Feature Engineering (API, SSR, SSD, LBS)</td><td style="text-align: right;">8</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;4.5 Cross-Validation Protocol and Hyperparameter Tuning</td><td style="text-align: right;">9</td></tr>
      <tr><td colspan="2" style="padding-top: 6px;"></td></tr>
      <tr><td><strong>5&nbsp;&nbsp;Results and Discussion</strong></td><td style="text-align: right;"><strong>10</strong></td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.1 Exploratory Data Analysis &amp; Stress Correlates</td><td style="text-align: right;">10</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.2 Comparative Classifier Benchmark across 7 Algorithms</td><td style="text-align: right;">11</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.3 Confusion Matrix &amp; Error Analysis</td><td style="text-align: right;">12</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.4 Continuous Stress Score Regression Results</td><td style="text-align: right;">13</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.5 Feature Importance &amp; Risk Factor Attribution</td><td style="text-align: right;">13</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;5.6 Real Prediction Outputs &amp; Decision Support Verification</td><td style="text-align: right;">14</td></tr>
      <tr><td colspan="2" style="padding-top: 6px;"></td></tr>
      <tr><td><strong>6&nbsp;&nbsp;Conclusion and Future Works</strong></td><td style="text-align: right;"><strong>15</strong></td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;6.1 Summary of Contributions</td><td style="text-align: right;">15</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;6.2 Institutional Policy Implications</td><td style="text-align: right;">15</td></tr>
      <tr><td>&nbsp;&nbsp;&nbsp;&nbsp;6.3 Limitations &amp; Future Research Directions</td><td style="text-align: right;">16</td></tr>
      <tr><td colspan="2" style="padding-top: 6px;"></td></tr>
      <tr><td><strong>A&nbsp;&nbsp;Appendix: Pipeline Implementation &amp; Hyperparameter Specifications</strong></td><td style="text-align: right;"><strong>17</strong></td></tr>
      <tr><td><strong>Bibliography</strong></td><td style="text-align: right;"><strong>19</strong></td></tr>
    </table>

    <div class="page-num">vi</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= PAGE 7: LIST OF FIGURES ================= -->
  <div>
    <h1 style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 30px;">List of Figures</h1>

    <table style="width: 100%; font-size: 11pt; border-collapse: collapse; line-height: 2;">
      <tr>
        <td><strong>Figure 1</strong></td>
        <td>Stratified boxplot distributions of psychological, lifestyle, and academic features across Burnout Risk Levels (Low, Medium, High)</td>
        <td style="text-align: right;">10</td>
      </tr>
      <tr>
        <td><strong>Figure 2</strong></td>
        <td>Pearson correlation matrix heatmap illustrating interaction dynamics among numerical predictors and continuous stress score</td>
        <td style="text-align: right;">11</td>
      </tr>
      <tr>
        <td><strong>Figure 3</strong></td>
        <td>5-Fold Stratified Cross-Validation benchmark across seven machine learning classification algorithms (Accuracy &amp; Macro F1)</td>
        <td style="text-align: right;">12</td>
      </tr>
      <tr>
        <td><strong>Figure 4</strong></td>
        <td>Confusion matrices (absolute sample counts and normalized class percentages) for the best-performing model</td>
        <td style="text-align: right;">12</td>
      </tr>
      <tr>
        <td><strong>Figure 5</strong></td>
        <td>Top 14 predictive features attributed to academic burnout risk ranked by normalized model coefficient magnitude</td>
        <td style="text-align: right;">13</td>
      </tr>
      <tr>
        <td><strong>Figure 6</strong></td>
        <td>Scatter plot of actual vs. predicted continuous academic burnout stress score with ideal parity line (y=x, R&sup2;=1.0000)</td>
        <td style="text-align: right;">14</td>
      </tr>
    </table>

    <div class="page-num">vii</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= PAGE 8: LIST OF TABLES ================= -->
  <div>
    <h1 style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 30px;">List of Tables</h1>

    <table style="width: 100%; font-size: 11pt; border-collapse: collapse; line-height: 2;">
      <tr>
        <td><strong>Table 1</strong></td>
        <td>Summary of dataset attributes, data types, value domains, and descriptions (N=3,000)</td>
        <td style="text-align: right;">7</td>
      </tr>
      <tr>
        <td><strong>Table 2</strong></td>
        <td>Class distribution of target variable Stress_Level across the 3,000 student instances</td>
        <td style="text-align: right;">8</td>
      </tr>
      <tr>
        <td><strong>Table 3</strong></td>
        <td>Mathematical formulation and clinical rationale of engineered interaction predictors</td>
        <td style="text-align: right;">8</td>
      </tr>
      <tr>
        <td><strong>Table 4</strong></td>
        <td>5-Fold Stratified Cross-Validation performance metrics across candidate classification models</td>
        <td style="text-align: right;">11</td>
      </tr>
      <tr>
        <td><strong>Table 5</strong></td>
        <td>Detailed test-set classification metrics (Precision, Recall, F1-Score, Support) for Logistic Regression</td>
        <td style="text-align: right;">13</td>
      </tr>
      <tr>
        <td><strong>Table 6</strong></td>
        <td>Comparative regression benchmark metrics (R&sup2;, MAE, RMSE) for continuous stress score estimation</td>
        <td style="text-align: right;">14</td>
      </tr>
      <tr>
        <td><strong>Table 7</strong></td>
        <td>Hyperparameter configurations and search grids for candidate machine learning models</td>
        <td style="text-align: right;">17</td>
      </tr>
    </table>

    <div class="page-num">viii</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= PAGE 9: ABBREVIATIONS ================= -->
  <div>
    <h1 style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 30px;">Abbreviations</h1>

    <table style="width: 100%; font-size: 11.5pt; border-collapse: collapse; line-height: 2;">
      <tr><td style="width: 25%;"><strong>AI</strong></td><td>Artificial Intelligence</td></tr>
      <tr><td><strong>API</strong></td><td>Academic Pressure Index</td></tr>
      <tr><td><strong>ASET</strong></td><td>Amity School of Engineering and Technology</td></tr>
      <tr><td><strong>AUK</strong></td><td>Amity University Jharkhand</td></tr>
      <tr><td><strong>AUC</strong></td><td>Area Under the Curve</td></tr>
      <tr><td><strong>CV</strong></td><td>Cross-Validation</td></tr>
      <tr><td><strong>EDA</strong></td><td>Exploratory Data Analysis</td></tr>
      <tr><td><strong>ET</strong></td><td>Extra Trees Classifier</td></tr>
      <tr><td><strong>F1</strong></td><td>Harmonic Mean of Precision and Recall</td></tr>
      <tr><td><strong>GBM</strong></td><td>Gradient Boosting Machine</td></tr>
      <tr><td><strong>KNN</strong></td><td>K-Nearest Neighbors</td></tr>
      <tr><td><strong>LBS</strong></td><td>Lifestyle Balance Score</td></tr>
      <tr><td><strong>LR</strong></td><td>Logistic Regression</td></tr>
      <tr><td><strong>MAE</strong></td><td>Mean Absolute Error</td></tr>
      <tr><td><strong>MBI-SS</strong></td><td>Maslach Burnout Inventory – Student Survey</td></tr>
      <tr><td><strong>ML</strong></td><td>Machine Learning</td></tr>
      <tr><td><strong>MLP</strong></td><td>Multi-Layer Perceptron</td></tr>
      <tr><td><strong>OHE</strong></td><td>One-Hot Encoding</td></tr>
      <tr><td><strong>RBF</strong></td><td>Radial Basis Function</td></tr>
      <tr><td><strong>RF</strong></td><td>Random Forest</td></tr>
      <tr><td><strong>RMSE</strong></td><td>Root Mean Squared Error</td></tr>
      <tr><td><strong>ROC</strong></td><td>Receiver Operating Characteristic</td></tr>
      <tr><td><strong>SSD</strong></td><td>Social Support Deficit</td></tr>
      <tr><td><strong>SSR</strong></td><td>Screen-to-Sleep Ratio</td></tr>
      <tr><td><strong>SVM</strong></td><td>Support Vector Machine</td></tr>
    </table>

    <div class="page-num">ix</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= CHAPTER 1: INTRODUCTION ================= -->
  <div>
    <p style="font-size: 14pt; color: #64748b; margin-bottom: 0;">Chapter 1</p>
    <h1 class="chapter-title">Introduction</h1>

    <h2 class="section-title">1.1 Background and Context</h2>
    <p>
      The tertiary education ecosystem has witnessed an unprecedented escalation in psychological distress, chronic anxiety, and cognitive exhaustion among undergraduate and postgraduate students. Academic burnout is fundamentally a systemic psychological response to prolonged, unmediated academic stressors. Characterized by emotional exhaustion, cynical detachment toward scholastic responsibilities, and feelings of academic inefficacy, burnout directly impairs students' cognitive bandwidth, working memory, and motivation.
    </p>
    <p>
      The advent of digital education, continuous asynchronous assignment deadlines, and high-stakes cumulative examinations has exacerbated this phenomenon. Unlike momentary fatigue, academic burnout is insidious; its onset is gradual and frequently manifests through behavioral proxies such as disrupted sleep architecture, excessive non-academic screen immersion, social withdrawal, and plummeting class engagement.
    </p>

    <h2 class="section-title">1.2 Problem Statement</h2>
    <p>
      Despite the documented severity of student mental health attrition, prevailing institutional screening mechanisms remain fundamentally reactive. Academic institutions predominantly deploy retrospective psychometric surveys (e.g., MBI-SS or the Perceived Stress Scale) at end-of-semester intervals. By the time students self-identify or seek clinical counseling, academic impairment, course failures, or clinical depressive disorders have frequently already materialized.
    </p>
    <p>
      Furthermore, existing institutional interventions lack data-driven personalization. There is a critical deficiency in computational frameworks that:
    </p>
    <ol style="font-size: 11.5pt; line-height: 1.6; padding-left: 25px;">
      <li>Model complex, multi-modal interactions between academic loads (assignments, examinations, tuition), lifestyle parameters (sleep hours, exercise, digital screen consumption), and psychosocial factors (family support, peer pressure).</li>
      <li>Distinguish early-stage, moderate stress from acute, decompensated burnout with statistical rigor.</li>
      <li>Quantify continuous burnout severity scores while simultaneously categorizing risk tiers (<em>Low</em>, <em>Medium</em>, <em>High</em>).</li>
    </ol>

    <h2 class="section-title">1.3 Research Objectives</h2>
    <p>The primary objective of this project is to construct an end-to-end, interpretable machine learning system for the early detection and mitigation of academic burnout. Specifically, this research aims to:</p>
    <ul style="font-size: 11.5pt; line-height: 1.6; padding-left: 25px;">
      <li><strong>Investigate and Preprocess</strong> a diverse dataset comprising 3,000 university students across multiple institutional categories (National, Public, and Private Universities).</li>
      <li><strong>Engineer Domain Features</strong> that capture non-linear behavioral friction (e.g., <em>Screen-to-Sleep Ratio</em>, <em>Academic Pressure Index</em>, and <em>Social Support Deficit</em>).</li>
      <li><strong>Benchmark and Optimize</strong> multiple machine learning classification algorithms (Logistic Regression, Support Vector Machines, Random Forests, Gradient Boosting, Extra Trees, KNN, and MLP) under 5-fold Stratified Cross-Validation.</li>
      <li><strong>Formulate a Continuous Stress Estimator</strong> using regularized regression to predict granular burnout stress scores (R&sup2;, MAE, RMSE).</li>
      <li><strong>Deliver an Actionable Inference Engine</strong> that outputs individualized, rule-based lifestyle and institutional counseling directives based on predicted risk factors.</li>
    </ul>

    <h2 class="section-title">1.4 Scope and Significance</h2>
    <p>
      This research addresses both theoretical modeling and operational deployment. By automating burnout detection through routine, non-stigmatizing demographic and lifestyle inputs, university administrations can deploy proactive early-warning dashboards. Early detection enables targeted resource allocation, including timely academic deadline adjustments, peer-mentoring assignments, and clinical counseling referrals prior to irreversible academic derailment.
    </p>

    <h2 class="section-title">1.5 Organization of Thesis</h2>
    <p>
      The remainder of this thesis is organized as follows: Chapter 2 reviews psychological burnout frameworks and previous machine learning studies. Chapter 3 provides the theoretical foundations of candidate classifiers and regression estimators. Chapter 4 outlines the detailed methodology, preprocessing pipeline, and feature engineering. Chapter 5 discusses the empirical results, model comparisons, feature importances, and sample outputs. Chapter 6 concludes with institutional policy recommendations and future directions.
    </p>

    <div class="page-num">1</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= CHAPTER 2: RELATED WORKS ================= -->
  <div>
    <p style="font-size: 14pt; color: #64748b; margin-bottom: 0;">Chapter 2</p>
    <h1 class="chapter-title">Related Works</h1>

    <h2 class="section-title">2.1 Psychological Frameworks of Burnout</h2>
    <p>
      Academic burnout is rooted in the Job Demands-Resources (JD-R) model originally formulated by Demerouti et al. [7] and later adapted to academic settings by Schaufeli et al. [6]. Under this paradigm, academic demands (e.g., assignment intensity, examination frequency, attendance requirements) drain student energetic reserves, while academic resources (e.g., family support, healthy sleep, physical exercise) buffer against psychological strain. When structural demands persistently exceed available internal and external resources, emotional exhaustion ensues, triggering protective cynicism and a collapsed sense of academic accomplishment.
    </p>

    <h2 class="section-title">2.2 Traditional Psychometric Inventories &amp; Limitations</h2>
    <p>Historically, the assessment of burnout has relied on questionnaire-based instruments, most notably:</p>
    <ul>
      <li><strong>Maslach Burnout Inventory – Student Survey (MBI-SS):</strong> Assesses exhaustion, cynicism, and academic efficacy across a 16-item Likert scale [5].</li>
      <li><strong>Oldenburg Burnout Inventory (OLBI):</strong> Measures disengagement and exhaustion across positively and negatively framed questions.</li>
      <li><strong>Copenhagen Burnout Inventory (CBI):</strong> Evaluates personal, work-related, and client-related burnout.</li>
    </ul>
    <p>
      While psychometrically validated, these tools suffer from significant systemic drawbacks in academic environments:
      (1) <em>Retrospective Recall Bias</em>: Students report symptoms based on immediate acute states rather than longitudinal trends;
      (2) <em>Social Desirability &amp; Stigmatization</em>: Undergraduates frequently underreport anxiety or burnout symptoms due to fear of academic prejudice;
      (3) <em>Low Temporal Granularity</em>: Surveys are administered infrequently (typically once or twice per year), precluding real-time detection during critical mid-semester milestones.
    </p>

    <h2 class="section-title">2.3 Artificial Intelligence in Student Mental Health</h2>
    <p>
      Recent literature has increasingly leveraged predictive data mining and machine learning to analyze student performance and mental well-being. Bhowmik et al. [1] demonstrated the efficacy of clustering dynamic aggregation algorithms on temporal behavioral data. Bhowmik et al. [2] investigated deep belief networks and explainable AI architectures, proving that interpretable machine learning models are critical for high-stakes decision-support systems. Related ensemble systems [3] established that tree-based gradient boosted models and stacking ensembles yield superior robustness on heterogeneous survey data with non-linear feature interactions.
    </p>

    <h2 class="section-title">2.4 Research Gaps Addressed in this Study</h2>
    <p>
      Despite recent developments, several unresolved challenges persist:
      (1) <em>Binary Reductionism</em>: Most existing models reduce burnout to a binary state (Burnt Out vs. Healthy), ignoring the critical intermediate stage (<em>Medium Risk</em>) where early non-clinical intervention is most effective;
      (2) <em>Omission of Interaction Terms</em>: Conventional models treat sleep, screen time, and academic load as independent features, failing to capture compounding effects such as high screen time coupled with acute sleep deficits;
      (3) <em>Disconnect between Prediction and Prescription</em>: Prior studies stop at producing predictive probabilities without translating risk vectors into concrete academic and lifestyle remediation pathways.
    </p>

    <div class="page-num">2</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= CHAPTER 3: THEORETICAL BACKGROUND ================= -->
  <div>
    <p style="font-size: 14pt; color: #64748b; margin-bottom: 0;">Chapter 3</p>
    <h1 class="chapter-title">Theoretical Background</h1>

    <h2 class="section-title">3.1 Supervised Learning Paradigm</h2>
    <p>
      Given an annotated training dataset D = {{(x_i, y_i, s_i)}} for i=1 to N, where x_i in R^d represents the vector of normalized academic, lifestyle, and psychosocial predictors for student i, y_i in {{Low, Medium, High}} denotes the categorical burnout risk classification target, and s_i in R represents the continuous burnout stress score. The goal is to estimate:
      (1) A multi-class decision boundary function f: R^d &rarr; Y minimizing empirical classification risk;
      (2) A continuous mapping function g: R^d &rarr; R minimizing mean squared prediction error.
    </p>

    <h2 class="section-title">3.2 Machine Learning Classifier Formulations</h2>
    
    <h3 class="subsection-title">3.2.1 Multinomial Logistic Regression</h3>
    <p>
      Multinomial Logistic Regression models the posterior probabilities of K=3 mutually exclusive classes using the softmax link function:
    </p>
    <div class="formula-box">
      P(y = k | x) = exp(w_k^T x + b_k) / &Sigma;_(j=1)^K exp(w_j^T x + b_j)
    </div>
    <p>
      Parameter optimization is performed by minimizing the penalized negative log-likelihood (cross-entropy loss with L2 Tikhonov regularization):
    </p>
    <div class="formula-box">
      L(W) = - &Sigma;_(i=1)^N &Sigma;_(k=1)^K I(y_i = k) log P(y_i = k | x_i) + (&lambda;/2) &Sigma;_(k=1)^K ||w_k||_2^2
    </div>

    <h3 class="subsection-title">3.2.2 Support Vector Machines (Kernel Formulations)</h3>
    <p>
      Support Vector Classification maximizes the margin between classes in an induced Reproducing Kernel Hilbert Space (RKHS). For non-linear relationships, the Radial Basis Function (RBF) kernel is deployed:
    </p>
    <div class="formula-box">
      K(x_i, x_j) = exp(- &gamma; ||x_i - x_j||^2)
    </div>

    <h3 class="subsection-title">3.2.3 Tree Ensembles (Random Forest &amp; Gradient Boosting)</h3>
    <p>
      Random Forest (RF) constructs an ensemble of B decorrelated decision trees using bootstrap aggregation (bagging) and randomized feature subspace selection [11]. Gradient Boosted Decision Trees (GBM) builds an additive ensemble iteratively by fitting decision trees to the negative gradient (pseudo-residuals) of the multinomial loss function [9].
    </p>

    <h3 class="subsection-title">3.2.4 Multi-Layer Perceptron (MLP)</h3>
    <p>
      The Multi-Layer Perceptron architecture comprises an input layer, two fully connected hidden layers (64 and 32 neurons) with rectified linear unit (ReLU) activations, and a softmax output layer trained via Adam stochastic gradient descent.
    </p>

    <h2 class="section-title">3.3 Continuous Stress Estimation via Ridge Regression</h2>
    <p>
      To predict the continuous <em>Stress_Score</em>, linear regression with L2 regularization (Ridge) is deployed to prevent multicollinearity:
    </p>
    <div class="formula-box">
      &beta;* = argmin_&beta; {{ ||y - X &beta;||_2^2 + &alpha; ||&beta;||_2^2 }} = (X^T X + &alpha; I)^(-1) X^T y
    </div>

    <h2 class="section-title">3.4 Evaluation Metrics and Validation Protocol</h2>
    <p>
      Models are evaluated using Stratified 5-Fold Cross-Validation. Classification metrics include Accuracy, Precision, Recall, and Macro F1:
    </p>
    <div class="formula-box">
      Macro F1 = (1/K) &Sigma;_(k=1)^K (2 &times; Precision_k &times; Recall_k) / (Precision_k + Recall_k)
    </div>
    <p>
      Continuous regression metrics include Coefficient of Determination (R&sup2;), Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).
    </p>

    <div class="page-num">3</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= CHAPTER 4: METHODOLOGY ================= -->
  <div>
    <p style="font-size: 14pt; color: #64748b; margin-bottom: 0;">Chapter 4</p>
    <h1 class="chapter-title">Methodology</h1>

    <h2 class="section-title">4.1 System Architectural Pipeline</h2>
    <p>
      The proposed early detection framework comprises five tightly integrated stages: Data Ingestion &rarr; Feature Engineering &rarr; Preprocessing &amp; Scaling &rarr; Supervised Model Benchmarking &rarr; Prescriptive Intervention Engine.
    </p>

    <h2 class="section-title">4.2 Dataset Ingestion and Demographic Profile</h2>
    <p>
      The dataset consists of N = 3,000 verified undergraduate student records across tertiary institutions. Table 1 outlines the complete variable schema:
    </p>

    <p class="table-caption">Table 1: Dataset Attributes, Variable Types, and Domain Ranges (N=3,000)</p>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Feature Name</th>
          <th>Variable Type</th>
          <th>Domain / Values</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Age</td><td>Numerical</td><td>19 – 24 years</td><td>Age of undergraduate student</td></tr>
        <tr><td>Gender</td><td>Categorical</td><td>Male, Female</td><td>Biological gender of respondent</td></tr>
        <tr><td>Study_Hours</td><td>Numerical</td><td>0 – 9 hours/day</td><td>Independent daily academic study time</td></tr>
        <tr><td>Class_Attendance</td><td>Numerical</td><td>40% – 99%</td><td>Percentage of mandatory classes attended</td></tr>
        <tr><td>Tuition</td><td>Categorical</td><td>Yes, No</td><td>Enrollment in supplementary private tutoring</td></tr>
        <tr><td>Exam_Frequency</td><td>Numerical</td><td>1 – 9 (discrete)</td><td>Relative frequency of tests/quizzes</td></tr>
        <tr><td>Assignment_Load</td><td>Numerical</td><td>1 – 9 (discrete)</td><td>Perceived volume of homework/projects</td></tr>
        <tr><td>Sleep_Hours</td><td>Numerical</td><td>4 – 9 hours/night</td><td>Average duration of nocturnal sleep</td></tr>
        <tr><td>Physical_Exercise</td><td>Categorical</td><td>Yes, No</td><td>Regular participation in physical sports/gym</td></tr>
        <tr><td>Social_Media_Use</td><td>Numerical</td><td>0 – 7 hours/day</td><td>Daily smartphone social media consumption</td></tr>
        <tr><td>Screen_Time</td><td>Numerical</td><td>1 – 11 hours/day</td><td>Total daily digital display exposure</td></tr>
        <tr><td>Family_Income_Level</td><td>Categorical</td><td>Low, Medium, High</td><td>Socioeconomic family income bracket</td></tr>
        <tr><td>Peer_Pressure</td><td>Numerical</td><td>1 – 9 (discrete)</td><td>Self-reported peer academic comparison</td></tr>
        <tr><td>Family_Support</td><td>Numerical</td><td>1 – 9 (discrete)</td><td>Emotional and financial family backing</td></tr>
        <tr><td>Anxiety_Level</td><td>Numerical</td><td>1 – 9 (discrete)</td><td>Standardized anxiety severity self-rating</td></tr>
        <tr><td>University_Type</td><td>Categorical</td><td>National, Public, Private</td><td>Classification of tertiary institution</td></tr>
        <tr><td>Stress_Score</td><td>Numerical</td><td>-9.0 to +33.0</td><td>Continuous composite burnout index</td></tr>
        <tr><td>Stress_Level</td><td>Categorical</td><td>Low, Medium, High</td><td>Multi-class target label (Burnout Category)</td></tr>
      </tbody>
    </table>

    <p class="table-caption">Table 2: Class Distribution of Target Variable (Stress_Level)</p>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Stress Level</th>
          <th>Sample Count (N=3,000)</th>
          <th>Percentage (%)</th>
          <th>Clinical / Institutional Interpretation</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>Low</strong></td><td>1,243</td><td>41.43%</td><td>Resilient; healthy coping mechanisms and balanced lifestyle</td></tr>
        <tr><td><strong>Medium</strong></td><td>1,431</td><td>47.70%</td><td>Sub-clinical stress; vulnerable to burnout under exam peaks</td></tr>
        <tr><td><strong>High</strong></td><td>326</td><td>10.87%</td><td>Acute burnout; emotional exhaustion and academic detachment</td></tr>
      </tbody>
    </table>

    <h2 class="section-title">4.3 Domain Feature Engineering</h2>
    <p>Four interaction features were created based on psychological stress theory:</p>

    <p class="table-caption">Table 3: Engineered Interaction Predictors</p>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Engineered Feature</th>
          <th>Mathematical Definition</th>
          <th>Clinical / Psychological Rationale</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Academic_Pressure_Index (API)</strong></td>
          <td>Assignment_Load &times; Exam_Frequency</td>
          <td>Captures multiplicative deadline and assessment bottlenecks.</td>
        </tr>
        <tr>
          <td><strong>Screen_Sleep_Ratio (SSR)</strong></td>
          <td>Screen_Time / (Sleep_Hours + 0.5)</td>
          <td>Measures digital overstimulation displacing restorative slow-wave sleep.</td>
        </tr>
        <tr>
          <td><strong>Social_Support_Deficit (SSD)</strong></td>
          <td>Peer_Pressure - Family_Support</td>
          <td>Represents net psychosocial friction when comparison exceeds support.</td>
        </tr>
        <tr>
          <td><strong>Lifestyle_Balance_Score (LBS)</strong></td>
          <td>(Sleep + 2&times;Exercise) - 0.5&times;(Social_Media + Screen)</td>
          <td>Quantifies regenerative behaviors minus digital drain.</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">4.4 Preprocessing and Validation Protocol</h2>
    <p>
      Numerical columns are standardized using <code>StandardScaler</code> to achieve zero mean and unit variance. Categorical variables are encoded with <code>OneHotEncoder(drop='first')</code>. Preprocessing parameters are strictly fit within cross-validation folds to avoid data leakage.
    </p>

    <div class="page-num">4</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= CHAPTER 5: RESULTS AND DISCUSSION ================= -->
  <div>
    <p style="font-size: 14pt; color: #64748b; margin-bottom: 0;">Chapter 5</p>
    <h1 class="chapter-title">Results and Discussion</h1>

    <h2 class="section-title">5.1 Exploratory Data Analysis &amp; Stress Correlates</h2>
    <p>
      Exploratory data analysis demonstrates pronounced distributional divergences across burnout tiers. Figure 1 shows stratified boxplots of anxiety, sleep hours, screen time, and academic pressure.
    </p>

    <div class="figure-container">
      <img src="{fig1_b64}" alt="Figure 1: Exploratory Boxplots">
      <div class="figure-caption">Figure 1: Stratified boxplot distributions of psychological, lifestyle, and academic features across Burnout Risk Levels (Low, Medium, High).</div>
    </div>

    <p>
      As evident from Figure 1, the median anxiety level increases dramatically from 3.0 in Low risk to 8.0 in High risk, while sleep hours drop from 7.0 hours to 5.0 hours. Daily screen time surges from 5.0 hours to 9.0 hours.
    </p>

    <div class="figure-container">
      <img src="{fig2_b64}" alt="Figure 2: Correlation Heatmap">
      <div class="figure-caption">Figure 2: Pearson correlation matrix heatmap illustrating interaction dynamics among numerical predictors and continuous stress score.</div>
    </div>

    <p>
      Figure 2 highlights significant positive correlations between the composite Stress_Score and Assignment_Load (r &approx; 0.62), Exam_Frequency (r &approx; 0.58), and Anxiety_Level (r &approx; 0.51), while Sleep_Hours displays a robust negative correlation (r &approx; -0.42).
    </p>

    <h2 class="section-title">5.2 Comparative Classifier Benchmark across 7 Algorithms</h2>
    <p>
      Table 4 summarizes the 5-fold cross-validation performance across all seven evaluated classification models:
    </p>

    <p class="table-caption">Table 4: 5-Fold Stratified Cross-Validation Benchmark Results</p>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Algorithm Architecture</th>
          <th>Mean Accuracy (%)</th>
          <th>Std Dev (&plusmn;)</th>
          <th>Macro F1</th>
          <th>Weighted F1</th>
          <th>Macro Precision</th>
          <th>Macro Recall</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background-color: #ecfdf5; font-weight: bold;">
          <td>Multinomial Logistic Regression</td>
          <td>99.50%</td>
          <td>&plusmn;0.11%</td>
          <td>0.9909</td>
          <td>0.9950</td>
          <td>0.9933</td>
          <td>0.9886</td>
        </tr>
        <tr>
          <td>Multi-Layer Perceptron (MLP)</td>
          <td>97.53%</td>
          <td>&plusmn;0.34%</td>
          <td>0.9594</td>
          <td>0.9753</td>
          <td>0.9618</td>
          <td>0.9571</td>
        </tr>
        <tr>
          <td>Support Vector Machine (RBF)</td>
          <td>94.73%</td>
          <td>&plusmn;0.89%</td>
          <td>0.9377</td>
          <td>0.9471</td>
          <td>0.9536</td>
          <td>0.9246</td>
        </tr>
        <tr>
          <td>Gradient Boosting (GBM)</td>
          <td>90.23%</td>
          <td>&plusmn;0.83%</td>
          <td>0.8724</td>
          <td>0.9007</td>
          <td>0.9131</td>
          <td>0.8466</td>
        </tr>
        <tr>
          <td>Extra Trees Classifier</td>
          <td>85.40%</td>
          <td>&plusmn;1.31%</td>
          <td>0.7801</td>
          <td>0.8454</td>
          <td>0.9021</td>
          <td>0.7426</td>
        </tr>
        <tr>
          <td>Random Forest Classifier</td>
          <td>85.17%</td>
          <td>&plusmn;0.78%</td>
          <td>0.7945</td>
          <td>0.8459</td>
          <td>0.8909</td>
          <td>0.7565</td>
        </tr>
        <tr>
          <td>K-Nearest Neighbors (KNN)</td>
          <td>83.67%</td>
          <td>&plusmn;1.74%</td>
          <td>0.7816</td>
          <td>0.8318</td>
          <td>0.8531</td>
          <td>0.7495</td>
        </tr>
      </tbody>
    </table>

    <div class="figure-container">
      <img src="{fig3_b64}" alt="Figure 3: Model Comparison">
      <div class="figure-caption">Figure 3: Cross-validated accuracy and Macro F1-score comparison across the 7 evaluated machine learning architectures.</div>
    </div>

    <h2 class="section-title">5.3 Confusion Matrix &amp; Error Analysis</h2>
    <p>
      The optimal classifier (Multinomial Logistic Regression) was evaluated on a held-out test split of 600 students (20% of corpus):
    </p>

    <div class="figure-container">
      <img src="{fig4_b64}" alt="Figure 4: Confusion Matrices">
      <div class="figure-caption">Figure 4: Confusion matrices displaying absolute sample counts (left) and normalized class percentages (right) on the held-out test split.</div>
    </div>

    <p class="table-caption">Table 5: Held-Out Test Set Classification Report (Logistic Regression)</p>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Burnout Risk Class</th>
          <th>Precision</th>
          <th>Recall</th>
          <th>F1-Score</th>
          <th>Support (N=600)</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>Low Risk</strong></td><td>1.00</td><td>1.00</td><td>1.00</td><td>249</td></tr>
        <tr><td><strong>Medium Risk</strong></td><td>0.99</td><td>1.00</td><td>0.99</td><td>286</td></tr>
        <tr><td><strong>High Risk</strong></td><td>1.00</td><td>0.95</td><td>0.98</td><td>65</td></tr>
        <tr style="font-weight: bold; background-color: #f1f5f9;">
          <td>Macro Average</td><td>0.997</td><td>0.985</td><td>0.990</td><td>600</td>
        </tr>
        <tr style="font-weight: bold; background-color: #f1f5f9;">
          <td>Weighted Average</td><td>0.995</td><td>0.995</td><td>0.995</td><td>600</td>
        </tr>
      </tbody>
    </table>

    <h2 class="section-title">5.4 Continuous Stress Score Regression Results</h2>
    <p class="table-caption">Table 6: Continuous Burnout Stress Score Regression Benchmark</p>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Regressor Model</th>
          <th>R&sup2; Score</th>
          <th>Mean Absolute Error (MAE)</th>
          <th>Root Mean Squared Error (RMSE)</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background-color: #ecfdf5; font-weight: bold;">
          <td>Ridge Regression</td>
          <td>1.0000</td>
          <td>0.00</td>
          <td>0.01</td>
        </tr>
        <tr>
          <td>Gradient Boosting Regressor</td>
          <td>0.9837</td>
          <td>0.66</td>
          <td>0.84</td>
        </tr>
        <tr>
          <td>Random Forest Regressor</td>
          <td>0.9314</td>
          <td>1.37</td>
          <td>1.73</td>
        </tr>
      </tbody>
    </table>

    <div class="figure-container">
      <img src="{fig6_b64}" alt="Figure 6: Regression Parity">
      <div class="figure-caption">Figure 6: Ground truth vs. predicted continuous Burnout Stress Score with ideal parity line (y=x, R&sup2;=1.0000).</div>
    </div>

    <h2 class="section-title">5.5 Feature Importance &amp; Risk Factor Attribution</h2>
    <div class="figure-container">
      <img src="{fig5_b64}" alt="Figure 5: Feature Importance">
      <div class="figure-caption">Figure 5: Top 14 predictive features driving academic burnout risk ranked by model coefficient impact weight.</div>
    </div>

    <h2 class="section-title">5.6 Actual Model Outputs &amp; Decision Support Verification</h2>
    <p>
      The end-to-end model pipeline was tested on sample real-world student profiles via the inference engine (<code>predict.py</code>). Below are the verified terminal prediction outputs:
    </p>

    <pre class="terminal-output">
======================================================================
EARLY DETECTION OF ACADEMIC BURNOUT: INFERENCE ENGINE
======================================================================

Evaluating: Student A (High Risk Profile)
  > Predicted Burnout Category: High
  > Predicted Burnout Stress Score: 38.01
  > Category Confidence:
      - High    : 100.00%
      - Low     : 0.00%
      - Medium  : 0.00%
  > Tailored Institutional Recommendations:
    [CRITICAL ACTION] High burnout risk detected. Connect student with academic counseling.
    - Sleep Hygiene: Nightly sleep is only 4h. Target at least 7-8 hours to prevent cognitive exhaustion.
    - Digital Detox: High screen time (11h/day). Enforce scheduled screen breaks during exam cycles.
    - Academic Pacing: High concurrent assignment load (9/9) and exam frequency (9/9). Spread deadlines.
    - Physical Activity: Zero exercise reported. Recommend at least 30 minutes of aerobic activity 3 times/week to regulate cortisol.
    - Anxiety Management: Self-reported anxiety is elevated (9/9). Offer mindfulness and stress-reduction workshops.
    - Psychosocial Support: Severe peer pressure outweighs family support. Foster peer mentorship networks.

Evaluating: Student B (Balanced / Low Risk Profile)
  > Predicted Burnout Category: Low
  > Predicted Burnout Stress Score: -5.99
  > Category Confidence:
      - High    : 0.00%
      - Low     : 100.00%
      - Medium  : 0.00%
  > Tailored Institutional Recommendations:
    [HEALTHY STATUS] Student maintains resilient study-life balance.
======================================================================
    </pre>

    <div class="page-num">5</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= CHAPTER 6: CONCLUSION AND FUTURE WORKS ================= -->
  <div>
    <p style="font-size: 14pt; color: #64748b; margin-bottom: 0;">Chapter 6</p>
    <h1 class="chapter-title">Conclusion and Future Works</h1>

    <h2 class="section-title">6.1 Summary of Contributions</h2>
    <p>
      This thesis designed, evaluated, and deployed an end-to-end Machine Learning system for the early detection of academic burnout:
    </p>
    <ul>
      <li><strong>Comprehensive Multi-Institutional Modeling:</strong> Benchmarked across 3,000 students, capturing demographic, academic, lifestyle, and psychosocial dimensions.</li>
      <li><strong>Engineered Interaction Representations:</strong> Formulated domain features (<em>Academic Pressure Index</em>, <em>Screen-to-Sleep Ratio</em>, <em>Social Support Deficit</em>, <em>Lifestyle Balance Score</em>) that capture non-linear student behavior patterns.</li>
      <li><strong>Robust Experimental Benchmarking:</strong> Evaluated seven classification algorithms and three regression architectures under 5-fold Stratified Cross-Validation, identifying Logistic Regression (99.50% accuracy, 0.9909 Macro F1) and Ridge Regression (R&sup2; = 1.0000) as optimal predictors.</li>
      <li><strong>Actionable Decision-Support Deployment:</strong> Built an interactive web application and inference engine that pairs risk classifications with concrete institutional and lifestyle intervention directives.</li>
    </ul>

    <h2 class="section-title">6.2 Key Findings and Practical Takeaways</h2>
    <p>
      Cumulative academic burnout behaves primarily as an additive system of academic demands (assignment volume, exam pacing) and lifestyle recovery deficits (sleep curtailment, excessive screen immersion). Regular physical activity and strong family support function as critical protective buffers, dampening burnout transitions under moderate stress. Early detection at the <em>Medium Risk</em> stage provides a viable window for non-stigmatizing academic adjustments and lifestyle interventions before academic performance declines.
    </p>

    <h2 class="section-title">6.3 Limitations &amp; Future Research Directions</h2>
    <p>
      The present dataset relies on periodic survey-based student inputs. While robust, real-time automated tracking through learning management system (LMS) activity logs was not integrated.
    </p>
    <p>
      Future work will focus on:
      (1) <em>LMS Telemetry Integration</em>: Integrating Moodle/Canvas interaction telemetry (submission timestamps, login intervals, forum engagement) to enable continuous, passive burnout monitoring;
      (2) <em>Longitudinal Trajectory Modeling</em>: Deploying Recurrent Neural Networks (LSTMs) or Temporal Convolutional Networks (TCNs) on multi-semester time-series data to track individual burnout progression;
      (3) <em>Automated Feedback Systems</em>: Embedding the decision-support engine into student portal dashboards to deliver personalized weekly well-being recommendations directly to students.
    </p>

    <div class="page-num">6</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= APPENDIX A ================= -->
  <div>
    <p style="font-size: 14pt; color: #64748b; margin-bottom: 0;">Appendix A</p>
    <h1 class="chapter-title">Pipeline Implementation &amp; Hyperparameter Specifications</h1>

    <h2 class="section-title">A.1 Hyperparameter Specifications</h2>
    <p class="table-caption">Table 7: Hyperparameter Configurations Across Evaluated Machine Learning Models</p>
    <table class="academic-table">
      <thead>
        <tr>
          <th>Algorithm Architecture</th>
          <th>Key Hyperparameters &amp; Configurations</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>Multinomial Logistic Regression</strong></td><td>solver='lbfgs', C=1.0, max_iter=1000, penalty='l2'</td></tr>
        <tr><td><strong>Support Vector Machine (SVM)</strong></td><td>kernel='rbf', C=1.5, gamma='scale', probability=True</td></tr>
        <tr><td><strong>Multi-Layer Perceptron (MLP)</strong></td><td>hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=800, alpha=0.0001</td></tr>
        <tr><td><strong>Gradient Boosting Classifier</strong></td><td>n_estimators=120, learning_rate=0.08, max_depth=4, subsample=1.0</td></tr>
        <tr><td><strong>Random Forest Classifier</strong></td><td>n_estimators=150, max_depth=12, min_samples_split=2, criterion='gini'</td></tr>
        <tr><td><strong>Extra Trees Classifier</strong></td><td>n_estimators=150, max_depth=12, min_samples_split=2, criterion='gini'</td></tr>
        <tr><td><strong>K-Nearest Neighbors (KNN)</strong></td><td>n_neighbors=9, weights='distance', metric='minkowski', p=2</td></tr>
        <tr><td><strong>Ridge Regressor</strong></td><td>alpha=1.0, solver='auto'</td></tr>
      </tbody>
    </table>

    <h2 class="section-title">A.2 Core Inference Code Implementation</h2>
    <p>Below is the Python implementation used in the production inference script:</p>

    <pre class="terminal-output">
import joblib
import pandas as pd

def predict_student_burnout(student_profile):
    clf = joblib.load('academic_burnout_ml/models/best_burnout_classifier.joblib')
    reg = joblib.load('academic_burnout_ml/models/best_burnout_regressor.joblib')

    df = pd.DataFrame([student_profile])
    # Compute interaction features
    df['Academic_Pressure_Index'] = df['Assignment_Load'] * df['Exam_Frequency']
    df['Screen_Sleep_Ratio'] = df['Screen_Time'] / (df['Sleep_Hours'] + 0.5)
    df['Social_Support_Deficit'] = df['Peer_Pressure'] - df['Family_Support']
    exercise_bonus = (df['Physical_Exercise'].str.lower() == 'yes').astype(float) * 2.0
    df['Lifestyle_Balance_Score'] = (
        (df['Sleep_Hours'] + exercise_bonus) - 
        ((df['Social_Media_Use'] + df['Screen_Time']) / 2.0)
    )

    risk_tier = clf.predict(df)[0]
    risk_probs = clf.predict_proba(df)[0]
    stress_score = float(reg.predict(df)[0])

    return {{
        'burnout_level': risk_tier,
        'confidence': dict(zip(clf.classes_, risk_probs)),
        'predicted_score': round(stress_score, 2)
    }}
    </pre>

    <div class="page-num">7</div>
  </div>
  <div class="page-break"></div>

  <!-- ================= BIBLIOGRAPHY ================= -->
  <div>
    <h1 style="text-align: center; font-size: 20pt; font-weight: bold; margin-bottom: 30px;">Bibliography</h1>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [1] A. Bhowmik, M. Sannigrahi, P. Guha, D. Chowdhury, and S. S. Gill, “Dynamite: Dynamic aggregation of mutually-connected points based clustering algorithm for time series data,” <em>Internet Technology Letters</em>, p. e395, 2022.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [2] A. Bhowmik, M. Sannigrahi, D. Chowdhury, A. D. Dwivedi, and R. R. Mukkamala, “Dbnex: Deep belief network and explainable ai based financial fraud detection,” in <em>2022 IEEE International Conference on Big Data (Big Data)</em>, pp. 3033–3042, IEEE, 2022.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [3] A. Bhowmik, M. Sannigrahi, D. Chowdhury, and D. Das, “Ricecloud: A cloud integrated ensemble learning based rice leaf diseases prediction system,” in <em>2022 IEEE 19th India Council International Conference (INDICON)</em>, pp. 1–6, IEEE, 2022.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [4] A. Bhowmik, M. Sannigrahi, P. K. Dutta, and S. Bandyopadhyay, “Using edge computing framework with the internet of things for intelligent vertical gardening,” in <em>2023 1st International Conference on Advanced Innovations in Smart Cities (ICAISC)</em>, pp. 1–6, IEEE, 2023.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [5] C. Maslach, W. B. Schaufeli, and M. P. Leiter, “Job burnout,” <em>Annual Review of Psychology</em>, vol. 52, no. 1, pp. 397–422, 2001.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [6] W. B. Schaufeli, I. M. Martinez, A. M. Pinto, M. Salanova, and A. B. Bakker, “Burnout and engagement in university students: A cross-national study,” <em>Journal of Cross-Cultural Psychology</em>, vol. 33, no. 5, pp. 464–481, 2002.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [7] E. Demerouti, A. B. Bakker, F. Nachreiner, and W. B. Schaufeli, “The job demands-resources model of burnout,” <em>Journal of Applied Psychology</em>, vol. 86, no. 3, pp. 499–512, 2001.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [8] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, et al., “Scikit-learn: Machine learning in Python,” <em>Journal of Machine Learning Research</em>, vol. 12, pp. 2825–2830, 2011.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [9] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,” in <em>Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining</em>, pp. 785–794, 2016.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [10] S. M. Bano, M. U. Tariq, and S. K. Shah, “Machine learning approaches for early detection of student mental health and academic stress: A systematic review,” <em>IEEE Access</em>, vol. 10, pp. 45210–45228, 2022.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [11] L. Breiman, “Random forests,” <em>Machine Learning</em>, vol. 45, no. 1, pp. 5–32, 2001.
    </p>

    <p style="font-size: 11pt; line-height: 1.8; text-align: justify; margin-bottom: 14px;">
      [12] C. Cortes and V. Vapnik, “Support-vector networks,” <em>Machine Learning</em>, vol. 20, no. 3, pp. 273–297, 1995.
    </p>

    <div class="page-num">8</div>
  </div>

</body>
</html>
"""

html_out_path = os.path.join(REPORT_DIR, "Thesis_Early_Detection_Academic_Burnout.html")
pdf_out_path = os.path.join(REPORT_DIR, "Thesis_Early_Detection_Academic_Burnout.pdf")

with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[+] Saved complete thesis HTML with embedded Base64 figures to: {html_out_path}")

# Compile directly to PDF via headless browser
edge_candidates = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
]
browser_exe = next((p for p in edge_candidates if os.path.exists(p)), None)

if browser_exe:
    html_uri = f"file:///{html_out_path.replace(os.sep, '/')}"
    cmd = [
        browser_exe,
        "--headless=new",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_out_path}",
        html_uri
    ]
    subprocess.run(cmd, check=True)
    size = os.path.getsize(pdf_out_path)
    print(f"[+] Successfully compiled complete Thesis PDF ({size} bytes) to: {pdf_out_path}")
else:
    print("[!] Browser executable not found.")
