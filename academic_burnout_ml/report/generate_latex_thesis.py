# -*- coding: utf-8 -*-
"""
Master Builder for 60-70 Page Amity University (ASET) Thesis LaTeX Source
Student: Palak Goenka (A357175124008)
"""

import os
import sys
import shutil
import zipfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LATEX_DIR = os.path.join(BASE_DIR, "latex_overleaf")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
TARGET_FILE = os.path.join(LATEX_DIR, "main.tex")
DESKTOP_DIR = r"D:\user files\New folder\Desktop\learner"
REPORT_DIR = os.path.join(BASE_DIR, "report")

# Add thesis_builder to sys.path
sys.path.insert(0, os.path.join(REPORT_DIR, "thesis_builder"))

import preamble_and_frontmatter
import chapter1_intro
import chapter2_litreview
import chapter3_dataset_eda
import chapter4_methodology
import chapter5_results
import chapter6_webapp
import chapter7_conclusion
import appendices_and_bib

# Ensure figures are copied
os.makedirs(os.path.join(LATEX_DIR, "figures"), exist_ok=True)
for f in os.listdir(FIGURES_DIR):
    if f.endswith(".png"):
        shutil.copy2(os.path.join(FIGURES_DIR, f), os.path.join(LATEX_DIR, "figures", f))

# Assemble complete LaTeX text
full_latex = (
    preamble_and_frontmatter.CONTENT + "\n" +
    chapter1_intro.CONTENT + "\n" +
    chapter2_litreview.CONTENT + "\n" +
    chapter3_dataset_eda.CONTENT + "\n" +
    chapter4_methodology.CONTENT + "\n" +
    chapter5_results.CONTENT + "\n" +
    chapter6_webapp.CONTENT + "\n" +
    chapter7_conclusion.CONTENT + "\n" +
    appendices_and_bib.CONTENT
)

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(full_latex)

print(f"[+] Successfully generated master LaTeX thesis: {TARGET_FILE}")
print(f"[+] Total characters: {len(full_latex)}, Total lines: {len(full_latex.splitlines())}")

# Create ZIP archive for Overleaf
def create_overleaf_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add main.tex at root of ZIP
        zipf.write(TARGET_FILE, arcname="main.tex")
        # Add figures directory
        figures_folder = os.path.join(LATEX_DIR, "figures")
        for root, dirs, files in os.walk(figures_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, LATEX_DIR)
                zipf.write(file_path, arcname=arc_name)
    print(f"[+] Overleaf ZIP created: {zip_path} ({os.path.getsize(zip_path)} bytes)")

desktop_zip = os.path.join(DESKTOP_DIR, "Amity_Thesis_Overleaf_Package.zip")
report_zip = os.path.join(REPORT_DIR, "Amity_Thesis_Overleaf_Package.zip")

create_overleaf_zip(desktop_zip)
create_overleaf_zip(report_zip)
