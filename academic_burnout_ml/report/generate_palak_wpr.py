"""
Script to generate Palak Goenka's NTCC Weekly Progress Report (WPR) PDF
Strictly matching the layout, font, table styling, and formatting of Raj_wpr.pdf.
"""

import os
import subprocess

DESKTOP_DIR = r"D:\user files\New folder\Desktop\learner"
WORKSPACE_REPORT_DIR = r"d:\user files\New folder\Downloads\learner\learner\academic_burnout_ml\report"

wpr_data = [
    {
        "wk_no": 1,
        "duration": "06/08/2026 – 14/08/2026",
        "entries": [
            ("THU / 06/08/2026", "Reviewed NTCC project guidelines, finalized problem statement, and outlined project deliverables for academic burnout detection."),
            ("FRI / 07/08/2026", "Studied psychological burnout frameworks, including the Maslach Burnout Inventory (MBI-SS) and Job Demands-Resources (JD-R) model."),
            ("MON / 10/08/2026", "Researched machine learning applications in educational data mining, cognitive fatigue, and student well-being monitoring."),
            ("TUE / 11/08/2026", "Explored behavioral feature representation across academic workload, sleep patterns, screen time, and psychosocial indicators."),
            ("WED / 12/08/2026", "Listed and evaluated required tools, libraries (Python, Scikit-Learn, Pandas, NumPy, Seaborn), and environment dependencies."),
            ("THU / 13/08/2026", "Drafted initial system architecture blueprint and prepared roadmap for data preprocessing, modeling, and evaluation.")
        ]
    },
    {
        "wk_no": 2,
        "duration": "15/08/2026 – 23/08/2026",
        "entries": [
            ("MON / 17/08/2026", "Acquired multi-institutional survey dataset comprising 3,000 verified university student records across 18 behavioral attributes."),
            ("TUE / 18/08/2026", "Conducted data cleaning, verified zero null/missing values, and inspected variable data types using Pandas."),
            ("WED / 19/08/2026", "Analyzed target variable distribution across Low (41.4%), Medium (47.7%), and High (10.9%) burnout tiers."),
            ("THU / 20/08/2026", "Configured categorical encoding using OneHotEncoder with drop-first settings for gender, tuition, and university type."),
            ("FRI / 21/08/2026", "Configured numerical feature standardization using StandardScaler within an integrated ColumnTransformer pipeline."),
            ("SAT / 22/08/2026", "Created reproducible preprocessing scripts and partitioned dataset into 80% training and 20% held-out test splits.")
        ]
    },
    {
        "wk_no": 3,
        "duration": "24/08/2026 – 01/09/2026",
        "entries": [
            ("MON / 24/08/2026", "Computed Pearson correlation matrix to quantify statistical dependencies between lifestyle predictors and stress score."),
            ("TUE / 25/08/2026", "Generated correlation matrix heatmap plot to visualize collinearity among academic and mental health variables."),
            ("WED / 26/08/2026", "Plotted stratified boxplots analyzing the distribution of anxiety, sleep hours, and screen time across burnout tiers."),
            ("THU / 27/08/2026", "Formulated and coded the Academic Pressure Index (API = Assignment Load × Exam Frequency) interaction feature."),
            ("FRI / 28/08/2026", "Formulated and coded Screen-to-Sleep Ratio (SSR) and Social Support Deficit (SSD = Peer Pressure - Family Support)."),
            ("MON / 31/08/2026", "Implemented Lifestyle Balance Score (LBS) combining sleep hours, physical exercise, and screen time deductions.")
        ]
    },
    {
        "wk_no": 4,
        "duration": "02/09/2026 – 10/09/2026",
        "entries": [
            ("WED / 02/09/2026", "Configured 5-Fold Stratified Cross-Validation schema to prevent data leakage and handle class imbalance."),
            ("THU / 03/09/2026", "Implemented and evaluated baseline distance-based K-Nearest Neighbors (KNN) classification algorithm."),
            ("SAT / 05/09/2026", "Developed and trained Extremely Randomized Trees (Extra Trees) classifier with 150 decision trees."),
            ("MON / 07/09/2026", "Constructed Random Forest ensemble classifier with 150 estimators and constrained max depth of 12."),
            ("TUE / 08/09/2026", "Evaluated ensemble bagging performance and analyzed Gini impurity splits across decision trees."),
            ("WED / 09/09/2026", "Implemented Gradient Boosting Classifier (GBM) with 120 estimators and sequential pseudo-residual learning.")
        ]
    },
    {
        "wk_no": 5,
        "duration": "11/09/2026 – 19/09/2026",
        "entries": [
            ("FRI / 11/09/2026", "Implemented Support Vector Machine (SVM) utilizing non-linear Radial Basis Function (RBF) kernel."),
            ("SAT / 12/09/2026", "Configured RBF kernel hyperparameter tuning across cost parameter C and gamma scaling factors."),
            ("MON / 14/09/2026", "Constructed Multi-Layer Perceptron (MLP) neural network with two hidden layers (64, 32 units) and ReLU activations."),
            ("TUE / 15/09/2026", "Configured Adam optimizer and backpropagation routines for MLP neural network training."),
            ("WED / 16/09/2026", "Implemented Multinomial Logistic Regression model with L2 regularization and softmax link function."),
            ("THU / 17/09/2026", "Executed 5-fold cross-validation benchmarking across all seven candidate classification architectures.")
        ]
    },
    {
        "wk_no": 6,
        "duration": "20/09/2026 – 28/09/2026",
        "entries": [
            ("MON / 21/09/2026", "Benchmarked cross-validation results and identified Multinomial Logistic Regression as optimal model with 99.50% accuracy."),
            ("TUE / 22/09/2026", "Generated comparative performance bar chart visualizing Accuracy and Macro F1-score across all 7 models."),
            ("WED / 23/09/2026", "Evaluated the optimal classifier on the 600-student test split and computed Precision, Recall, and Macro F1 (0.9909)."),
            ("THU / 24/09/2026", "Generated absolute count and normalized percentage confusion matrices for the test evaluation split."),
            ("FRI / 25/09/2026", "Developed continuous regression models for predicting Stress_Score; trained Ridge Regression, Random Forest, and GBM regressors."),
            ("SAT / 26/09/2026", "Validated Ridge Regression achieving R² = 1.0000 (MAE: 0.00, RMSE: 0.01) and plotted regression parity scatter plot.")
        ]
    },
    {
        "wk_no": 7,
        "duration": "29/09/2026 – 07/10/2026",
        "entries": [
            ("TUE / 29/09/2026", "Extracted model coefficient weights and ranked top 14 predictive features driving student academic burnout."),
            ("WED / 30/09/2026", "Plotted feature importance bar chart identifying assignment load, exam frequency, and sleep hours as primary drivers."),
            ("THU / 01/10/2026", "Designed rule-based prescriptive intervention logic to deliver personalized lifestyle and academic counseling recommendations."),
            ("SAT / 03/10/2026", "Built standalone CLI inference script (predict.py) and serialized trained models into persistent joblib binary artifacts."),
            ("MON / 05/10/2026", "Developed Flask web application backend (app.py) supporting REST API endpoints for single and batch predictions."),
            ("TUE / 06/10/2026", "Configured batch CSV upload processor with dynamic feature engineering and bulk prediction output handling.")
        ]
    },
    {
        "wk_no": 8,
        "duration": "08/10/2026 – 15/10/2026",
        "entries": [
            ("THU / 08/10/2026", "Designed responsive glassmorphic web dashboard UI (index.html) with interactive sliders, badges, and charts."),
            ("FRI / 09/10/2026", "Wrote comprehensive unit and integration test suite (test_model.py) verifying data integrity, feature math, and APIs."),
            ("SAT / 10/10/2026", "Executed automated test suite, confirming all 7 unit tests passed successfully in 0.145 seconds."),
            ("MON / 12/10/2026", "Compiled 17-page formal academic thesis document matching Amity University Jharkhand template with embedded figures."),
            ("WED / 14/10/2026", "Deployed web application to Vercel cloud platform (academic-burnout.vercel.app) and synced GitHub repository."),
            ("THU / 15/10/2026", "Finalized NTCC weekly progress reports, validated all project deliverables, and completed report submission.")
        ]
    }
]

html_pages = []

for item in wpr_data:
    table_rows = []
    for day_date, summary in item["entries"]:
        table_rows.append(f"""
        <tr>
          <td class="col-date"><strong>{day_date}</strong></td>
          <td class="col-summary">{summary}</td>
        </tr>
        """)
    
    rows_html = "".join(table_rows)

    page_html = f"""
    <div class="page-container">
      <div class="header">
        <h1 class="main-title">AMITY SCHOOL OF ENGINEERING AND TECHNOLOGY</h1>
        <div class="sub-title">---AMITY UNIVERSITY JHARKHAND, RANCHI---</div>
      </div>

      <div class="meta-section">
        <div class="meta-row">
          <div class="meta-left"><strong>Student Name:</strong> <u>Palak Goenka</u></div>
          <div class="meta-right"><strong>Program:</strong> <u>B.Tech CSE (AI &amp; ML), Sem–V</u></div>
        </div>
        <div class="meta-row">
          <div class="meta-left"><strong>Enroll No.:</strong> <u>A357175124008</u></div>
        </div>
        <div class="meta-row" style="margin-top: 4px;">
          <div><strong>Title:</strong> <u>Early Detection of Academic Burnout using Machine Learning</u></div>
        </div>
        <div class="meta-report-row">
          <em><u>NTCC Weekly Progress Report (Minor Project): Wk. No: {item['wk_no']}</u></em> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em><u>Duration: {item['duration']}</u></em>
        </div>
      </div>

      <table class="report-table">
        <thead>
          <tr>
            <th class="col-date">DAYS / Date</th>
            <th class="col-summary">Summary</th>
          </tr>
        </thead>
        <tbody>
          {rows_html}
        </tbody>
      </table>

      <div class="footer-signatures">
        <div class="sig-left">(Student Signature with Date)</div>
        <div class="sig-right">(Faculty Guide Signature with Date)</div>
      </div>
    </div>
    """
    html_pages.append(page_html)

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Palak Goenka - NTCC Weekly Progress Report</title>
  <style>
    @page {{
      size: A4 landscape;
      margin: 10mm 15mm 10mm 15mm;
    }}
    *, *:before, *:after {{
      box-sizing: border-box;
    }}
    body {{
      font-family: 'Times New Roman', Times, Georgia, serif;
      font-size: 11pt;
      color: #000000;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }}
    .page-container {{
      width: 100%;
      height: 100%;
      page-break-after: always;
      break-after: page;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 10px 15px;
    }}
    .page-container:last-child {{
      page-break-after: avoid;
      break-after: avoid;
    }}
    .header {{
      text-align: center;
      margin-bottom: 8px;
    }}
    .main-title {{
      font-size: 15pt;
      font-weight: bold;
      letter-spacing: 0.5px;
      margin: 0 0 2px 0;
      text-transform: uppercase;
    }}
    .sub-title {{
      font-size: 9.5pt;
      font-weight: bold;
      letter-spacing: 0.5px;
    }}
    .meta-section {{
      font-size: 11pt;
      margin-bottom: 12px;
      line-height: 1.45;
    }}
    .meta-row {{
      display: flex;
      justify-content: space-between;
      margin-bottom: 2px;
    }}
    .meta-left {{
      flex: 1;
    }}
    .meta-right {{
      text-align: right;
    }}
    .meta-report-row {{
      text-align: center;
      margin-top: 6px;
      font-size: 10.5pt;
    }}
    table.report-table {{
      width: 100%;
      border-collapse: collapse;
      border: 1.5px solid #000000;
      margin-bottom: 20px;
    }}
    table.report-table th, table.report-table td {{
      border: 1px solid #000000;
      padding: 8px 12px;
      vertical-align: middle;
    }}
    table.report-table th {{
      font-size: 11.5pt;
      font-weight: bold;
      text-align: center;
    }}
    th.col-date, td.col-date {{
      width: 18%;
      text-align: center;
      font-size: 10.5pt;
      white-space: nowrap;
    }}
    th.col-summary, td.col-summary {{
      width: 82%;
      font-size: 10pt;
      text-align: left;
      line-height: 1.35;
    }}
    .footer-signatures {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 15px;
      padding: 0 10px;
      font-size: 11pt;
      font-weight: bold;
    }}
    .sig-left {{
      text-align: left;
    }}
    .sig-right {{
      text-align: right;
    }}
  </style>
</head>
<body>
  {"".join(html_pages)}
</body>
</html>
"""

html_out_path = os.path.join(WORKSPACE_REPORT_DIR, "Palak_Goenka_wpr.html")
pdf_workspace_path = os.path.join(WORKSPACE_REPORT_DIR, "Palak_Goenka_wpr.pdf")
pdf_desktop_path = os.path.join(DESKTOP_DIR, "Palak_Goenka_wpr.pdf")

with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"[+] Generated WPR HTML at: {html_out_path}")

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
        f"--print-to-pdf={pdf_workspace_path}",
        html_uri
    ]
    subprocess.run(cmd, check=True)
    print(f"[+] Compiled workspace PDF ({os.path.getsize(pdf_workspace_path)} bytes) to: {pdf_workspace_path}")

    # Copy to Desktop folder as well
    import shutil
    shutil.copyfile(pdf_workspace_path, pdf_desktop_path)
    print(f"[+] Saved requested PDF on Desktop at: {pdf_desktop_path}")
else:
    print("[!] No headless browser executable found.")
