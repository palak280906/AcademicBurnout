# -*- coding: utf-8 -*-
"""
Fixes Overleaf Timeout and formatting issues in the LaTeX Thesis:
1. Disables microtype (the #1 cause of Overleaf free plan 60s compilation timeout on 60+ page documents).
2. Sets columns=flexible in lstdefinestyle for fast listings processing.
3. Fixes tabularx environments without X columns to avoid iterative solver loop overhead.
4. Cleans all non-ASCII replacement artifacts to clean standard LaTeX (--, ---, etc.).
5. Updates and packages the zip file for 1-click upload to Overleaf.
"""

import os
import zipfile
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LATEX_DIR = os.path.join(BASE_DIR, "latex_overleaf")
MAIN_TEX = os.path.join(LATEX_DIR, "main.tex")
DESKTOP_ZIP = r"D:\user files\New folder\Desktop\learner\Amity_Thesis_Overleaf_Package.zip"
REPORT_ZIP = os.path.join(BASE_DIR, "report", "Amity_Thesis_Overleaf_Package.zip")

with open(MAIN_TEX, "r", encoding="utf-8", errors="replace") as f:
    text = f.read()

# 1. Disable microtype
text = text.replace(
    r"\usepackage{microtype}",
    r"% \usepackage{microtype} % Disabled to prevent Overleaf free tier compilation timeouts"
)

# 2. Add columns=flexible to lstdefinestyle
if "columns=flexible," not in text:
    text = text.replace(
        r"breakatwhitespace=false,",
        "columns=flexible,\n    breakatwhitespace=false,"
    )

# 3. Fix tabularx environments without X column (solves internal iterative loop)
text = text.replace(r"\begin{tabularx}{\textwidth}{lrrrrrrrr}", r"\begin{tabularx}{\textwidth}{Xrrrrrrrr}")
text = text.replace(r"\begin{tabularx}{\textwidth}{lrrrrrr}", r"\begin{tabularx}{\textwidth}{Xrrrrrr}")
text = text.replace(r"\begin{tabularx}{0.9\textwidth}{lrrrr}", r"\begin{tabularx}{0.9\textwidth}{Xrrrr}")

# 4. Clean non-ASCII characters to standard ASCII / LaTeX dashes
cleaned_chars = []
for c in text:
    if ord(c) > 127:
        cleaned_chars.append("--")
    else:
        cleaned_chars.append(c)

text = "".join(cleaned_chars)

with open(MAIN_TEX, "w", encoding="utf-8") as f:
    f.write(text)

print(f"[+] Successfully optimized {MAIN_TEX}")
print(f"    Non-ASCII character count: {sum(1 for c in text if ord(c) > 127)}")

# 5. Rebuild Overleaf ZIP package
for zip_target in [DESKTOP_ZIP, REPORT_ZIP]:
    os.makedirs(os.path.dirname(zip_target), exist_ok=True)
    with zipfile.ZipFile(zip_target, "w", zipfile.ZIP_DEFLATED) as zf:
        # main.tex at root
        zf.write(MAIN_TEX, arcname="main.tex")
        # figures directory
        fig_dir = os.path.join(LATEX_DIR, "figures")
        for f in os.listdir(fig_dir):
            if f.endswith(".png"):
                full_fig = os.path.join(fig_dir, f)
                zf.write(full_fig, arcname=f"figures/{f}")
    print(f"[+] Rebuilt ZIP archive at: {zip_target} ({os.path.getsize(zip_target)} bytes)")

print("[+] All Overleaf fixes applied successfully!")
