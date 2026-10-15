# -*- coding: utf-8 -*-
"""
Comprehensive 60-70 Page Thesis Generator for Amity University (ASET)
Author: Palak Goenka (A357175124008)
Project: Early Detection of Academic Burnout using Machine Learning
"""

import os
import shutil
import subprocess
import zipfile
import base64

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LATEX_DIR = os.path.join(BASE_DIR, "latex_overleaf")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
REPORT_DIR = os.path.join(BASE_DIR, "report")
DESKTOP_DIR = r"D:\user files\New folder\Desktop\learner"

os.makedirs(LATEX_DIR, exist_ok=True)
os.makedirs(os.path.join(LATEX_DIR, "figures"), exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

# Copy figures
for f in os.listdir(FIGURES_DIR):
    if f.endswith(".png"):
        shutil.copy2(os.path.join(FIGURES_DIR, f), os.path.join(LATEX_DIR, "figures", f))

def get_base64_img(name):
    p = os.path.join(FIGURES_DIR, name)
    if os.path.exists(p):
        with open(p, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

fig1_b64 = get_base64_img("fig1_eda_distributions.png")
fig2_b64 = get_base64_img("fig2_correlation_matrix.png")
fig3_b64 = get_base64_img("fig3_model_comparison.png")
fig4_b64 = get_base64_img("fig4_confusion_matrices.png")
fig5_b64 = get_base64_img("fig5_feature_importance.png")
fig6_b64 = get_base64_img("fig6_stress_score_regression.png")

print("[+] Assets loaded. Constructing LaTeX main.tex...")
