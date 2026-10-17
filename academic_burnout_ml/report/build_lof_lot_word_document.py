# -*- coding: utf-8 -*-
"""
Generates the List of Figures and List of Tables Word Document (.docx) for Palak Goenka's Thesis.
Features:
- Strictly formatted in Times New Roman matching the Amity University thesis style.
- Right-aligned tab stops with dot leaders (WD_TAB_LEADER.DOTS) leading to exact page numbers.
- Verified page numbers matching the 64-page compiled thesis (Palak_Goenka_Thesis.pdf).
- Includes both Verified Thesis Sheet Numbers (Pages 1-64) and Standard Academic Numbering.
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import parse_xml

DESKTOP_DIR = r"D:\user files\New folder\Desktop\learner"
REPORT_DIR = os.path.dirname(os.path.abspath(__file__))

def create_lof_lot_document():
    doc = Document()
    
    # Page setup: A4 with standard margins (Left: 1.25 in, Right: 1.0 in, Top: 1.0 in, Bottom: 1.0 in)
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.0)
    
    RIGHT_TAB_POS = Inches(6.0)
    
    # Set default style font to Times New Roman
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0, 0, 0)
    
    # Institutional Header
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_inst = p_inst.add_run("AMITY UNIVERSITY JHARKHAND, RANCHI\n")
    r_inst.font.name = "Times New Roman"
    r_inst.font.size = Pt(13)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(30, 41, 59)
    
    r_aset = p_inst.add_run("AMITY SCHOOL OF ENGINEERING AND TECHNOLOGY (ASET)\n")
    r_aset.font.name = "Times New Roman"
    r_aset.font.size = Pt(11)
    r_aset.font.bold = True
    r_aset.font.color.rgb = RGBColor(71, 85, 105)
    
    r_proj = p_inst.add_run("Major Project Dissertation: Early Detection of Academic Burnout using Machine Learning\n")
    r_proj.font.name = "Times New Roman"
    r_proj.font.size = Pt(10.5)
    r_proj.font.italic = True
    
    r_cand = p_inst.add_run("Candidate: Palak Goenka | Enrollment No: A357175124008 | B.Tech CSE (AI & ML)\n")
    r_cand.font.name = "Times New Roman"
    r_cand.font.size = Pt(10)
    r_cand.font.bold = True
    p_inst.paragraph_format.space_after = Pt(14)
    
    # =========================================================================
    # PART 1: LIST OF FIGURES
    # =========================================================================
    p_fig_title = doc.add_paragraph()
    p_fig_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_ft = p_fig_title.add_run("LIST OF FIGURES")
    r_ft.font.name = "Times New Roman"
    r_ft.font.size = Pt(16)
    r_ft.font.bold = True
    r_ft.underline = True
    p_fig_title.paragraph_format.space_after = Pt(12)
    
    # Table Header Line: Figure No. & Title on Left, Page No. on Right
    p_fhdr = doc.add_paragraph()
    p_fhdr.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT)
    p_fhdr.paragraph_format.space_after = Pt(4)
    r_fhl = p_fhdr.add_run("Figure No. and Title")
    r_fhl.font.name = "Times New Roman"
    r_fhl.font.size = Pt(12)
    r_fhl.font.bold = True
    p_fhdr.add_run("\t")
    r_fhr = p_fhdr.add_run("Page No.")
    r_fhr.font.name = "Times New Roman"
    r_fhr.font.size = Pt(12)
    r_fhr.font.bold = True
    
    p_fhr_line = doc.add_paragraph()
    p_fhr_line.paragraph_format.space_after = Pt(10)
    p_fhr_border = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:bottom w:val="single" w:sz="8" w:space="1" w:color="333333"/></w:pBdr>')
    p_fhr_line._p.get_or_add_pPr().append(p_fhr_border)
    
    # Verified Figure Data: (Fig_Number, Title, Sheet_No)
    figures_data = [
        ("Figure 3.1", "Univariate empirical distributions and kernel density estimates of primary academic, lifestyle, and psycho-social features (n = 3,000)", "27"),
        ("Figure 3.2", "Pairwise Pearson correlation matrix heatmap illustrating inter-variable dependencies and burnout target associations", "28"),
        ("Figure 5.1", "Comparative cross-algorithmic accuracy, macro precision, recall, and Macro F1-score benchmark across all seven models", "34"),
        ("Figure 5.2", "Normalized confusion matrices for Training (left) and Hold-Out Test (right) sets, confirming zero cross-tier Low-High error", "35"),
        ("Figure 5.3", "Predicted versus actual continuous stress score regression fit, demonstrating perfect calibration along identity line (R^2 = 1.0000)", "36"),
        ("Figure 5.4", "Standardized feature importance weights illustrating dominant behavioral indicators (Anxiety, Screen-to-Sleep Ratio, Assignment Load)", "37")
    ]
    
    for fnum, ftitle, fpage in figures_data:
        p = doc.add_paragraph()
        p.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.2
        
        r_num = p.add_run(fnum + ": ")
        r_num.font.name = "Times New Roman"
        r_num.font.size = Pt(11)
        r_num.font.bold = True
        
        r_desc = p.add_run(ftitle)
        r_desc.font.name = "Times New Roman"
        r_desc.font.size = Pt(10.5)
        r_desc.font.bold = False
        
        p.add_run("\t")
        
        r_pg = p.add_run(fpage)
        r_pg.font.name = "Times New Roman"
        r_pg.font.size = Pt(11)
        r_pg.font.bold = True
    
    # Spacer between sections
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(16)
    p_space.paragraph_format.space_after = Pt(10)
    
    # =========================================================================
    # PART 2: LIST OF TABLES
    # =========================================================================
    p_tbl_title = doc.add_paragraph()
    p_tbl_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_tt = p_tbl_title.add_run("LIST OF TABLES")
    r_tt.font.name = "Times New Roman"
    r_tt.font.size = Pt(16)
    r_tt.font.bold = True
    r_tt.underline = True
    p_tbl_title.paragraph_format.space_after = Pt(12)
    
    p_thdr = doc.add_paragraph()
    p_thdr.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT)
    p_thdr.paragraph_format.space_after = Pt(4)
    r_thl = p_thdr.add_run("Table No. and Title")
    r_thl.font.name = "Times New Roman"
    r_thl.font.size = Pt(12)
    r_thl.font.bold = True
    p_thdr.add_run("\t")
    r_thr = p_thdr.add_run("Page No.")
    r_thr.font.name = "Times New Roman"
    r_thr.font.size = Pt(12)
    r_thr.font.bold = True
    
    p_thr_line = doc.add_paragraph()
    p_thr_line.paragraph_format.space_after = Pt(10)
    p_thr_border = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:bottom w:val="single" w:sz="8" w:space="1" w:color="333333"/></w:pBdr>')
    p_thr_line._p.get_or_add_pPr().append(p_thr_border)
    
    # Verified Table Data: (Tbl_Number, Title, Sheet_No)
    tables_data = [
        ("Table 1.1", "Taxonomical and Operational Comparison: Acute Academic Stress vs. Chronic Academic Burnout", "16"),
        ("Table 2.1", "Taxonomical Comparison of Standardized Psychometric Instruments in Higher Education (MBI-SS, DASS-21, PSS-10, OLBI, CBI)", "19"),
        ("Table 2.2", "Comparative Synthesis of Prior Machine Learning Works vs. Proposed Multi-Dimensional Predictive Framework", "23"),
        ("Table 3.1", "Exhaustive Feature Dictionary and Descriptive Summary Statistics of Numeric Features (n = 3,000)", "24"),
        ("Table 3.2", "Cross-Strata Behavioral Profiling Across Burnout Risk Tiers (Mean +/- Std: Low, Medium, and High Cohorts)", "26"),
        ("Table 3.4", "Multicollinearity Diagnostics and Variance Inflation Factor (VIF) Analysis for Predictor Variables", "28"),
        ("Table 3.5", "Mathematical Formulations and ANOVA F-Statistic Validation of Four Engineered Interaction Features (API, SSR, SSD, LBS)", "29"),
        ("Table 4.1", "Hyperparameter Search Grids and Optimal Tuned Parameters for the Seven Evaluated Machine Learning Classifiers", "32"),
        ("Table 5.1", "Comprehensive Multi-Classifier Benchmark Performance Matrix on Hold-Out Test Set (n_test = 600)", "33"),
        ("Table 5.2", "Stratified 5-Fold Cross-Validation Accuracy Matrix across Evaluated Models Confirming Algorithmic Stability", "34"),
        ("Table 5.3", "Granular Classification Report for Production Logistic Regression Model (Precision, Recall, and F1 per Risk Class)", "35"),
        ("Table 5.4", "Empirical Evaluation Metrics for Continuous Stress Score Regression Model (R^2 = 1.0000, MSE = 0.0000)", "36"),
        ("Table 5.5", "Ablation Study: Quantifying the Impact of Domain-Specific Feature Engineering on Linear and Non-Linear Models", "37"),
        ("Table 6.1", "Production REST API Specification for Real-Time Inference (/predict) and Batch File Evaluation (/batch-predict)", "38"),
        ("Table A.1", "Standardized 16-Parameter Student Burnout Assessment Questionnaire (Psychometric Formulation and Valid Input Ranges)", "58"),
        ("Table A.2", "Empirical Inferences and Risk Probability Distributions for 30 Diverse Synthetic Student Case Scenarios (Cases C01--C30)", "58")
    ]
    
    for tnum, ttitle, tpage in tables_data:
        p = doc.add_paragraph()
        p.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        p.paragraph_format.space_before = Pt(3.5)
        p.paragraph_format.space_after = Pt(3.5)
        p.paragraph_format.line_spacing = 1.2
        
        r_num = p.add_run(tnum + ": ")
        r_num.font.name = "Times New Roman"
        r_num.font.size = Pt(11)
        r_num.font.bold = True
        
        r_desc = p.add_run(ttitle)
        r_desc.font.name = "Times New Roman"
        r_desc.font.size = Pt(10.5)
        r_desc.font.bold = False
        
        p.add_run("\t")
        
        r_pg = p.add_run(tpage)
        r_pg.font.name = "Times New Roman"
        r_pg.font.size = Pt(11)
        r_pg.font.bold = True
        
    # =========================================================================
    # PART 3: ALTERNATIVE STANDARD ACADEMIC NUMBERING (PAGE BREAK)
    # =========================================================================
    doc.add_page_break()
    
    p_sec2 = doc.add_paragraph()
    p_sec2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_s2 = p_sec2.add_run("LIST OF FIGURES & TABLES (STANDARD ACADEMIC NUMBERING)")
    r_s2.font.name = "Times New Roman"
    r_s2.font.size = Pt(14)
    r_s2.font.bold = True
    r_s2.underline = True
    p_sec2.paragraph_format.space_after = Pt(4)
    
    p_s2_note = doc.add_paragraph()
    p_s2_note.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_s2_n = p_s2_note.add_run("[Note: This section lists the traditional academic format with Chapter 1 resetting to Page 1]")
    r_s2_n.font.name = "Times New Roman"
    r_s2_n.font.size = Pt(9.5)
    r_s2_n.font.italic = True
    r_s2_n.font.color.rgb = RGBColor(100, 116, 139)
    p_s2_note.paragraph_format.space_after = Pt(12)
    
    # Subheading: List of Figures (Academic)
    p_af_sub = doc.add_paragraph()
    r_afs = p_af_sub.add_run("LIST OF FIGURES")
    r_afs.font.name = "Times New Roman"
    r_afs.font.size = Pt(12)
    r_afs.font.bold = True
    p_af_sub.paragraph_format.space_after = Pt(4)
    
    p_af_hdr = doc.add_paragraph()
    p_af_hdr.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT)
    p_af_hdr.paragraph_format.space_after = Pt(4)
    r_afl = p_af_hdr.add_run("Figure No. and Title")
    r_afl.font.name = "Times New Roman"
    r_afl.font.size = Pt(11)
    r_afl.font.bold = True
    p_af_hdr.add_run("\t")
    r_afr = p_af_hdr.add_run("Page No.")
    r_afr.font.name = "Times New Roman"
    r_afr.font.size = Pt(11)
    r_afr.font.bold = True
    
    p_af_line = doc.add_paragraph()
    p_af_line.paragraph_format.space_after = Pt(8)
    p_af_border = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:bottom w:val="single" w:sz="6" w:space="1" w:color="333333"/></w:pBdr>')
    p_af_line._p.get_or_add_pPr().append(p_af_border)
    
    academic_figures = [
        ("Figure 3.1", "Univariate empirical distributions and kernel density estimates of primary academic, lifestyle, and psycho-social features (n = 3,000)", "14"),
        ("Figure 3.2", "Pairwise Pearson correlation matrix heatmap illustrating inter-variable dependencies and burnout target associations", "15"),
        ("Figure 5.1", "Comparative cross-algorithmic accuracy, macro precision, recall, and Macro F1-score benchmark across all seven models", "21"),
        ("Figure 5.2", "Normalized confusion matrices for Training (left) and Hold-Out Test (right) sets, confirming zero cross-tier Low-High error", "22"),
        ("Figure 5.3", "Predicted versus actual continuous stress score regression fit, demonstrating perfect calibration along identity line (R^2 = 1.0000)", "23"),
        ("Figure 5.4", "Standardized feature importance weights illustrating dominant behavioral indicators (Anxiety, Screen-to-Sleep Ratio, Assignment Load)", "24")
    ]
    
    for fnum, ftitle, fpage in academic_figures:
        p = doc.add_paragraph()
        p.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        
        r_num = p.add_run(fnum + ": ")
        r_num.font.name = "Times New Roman"
        r_num.font.size = Pt(10.5)
        r_num.font.bold = True
        
        r_desc = p.add_run(ftitle)
        r_desc.font.name = "Times New Roman"
        r_desc.font.size = Pt(10)
        
        p.add_run("\t")
        
        r_pg = p.add_run(fpage)
        r_pg.font.name = "Times New Roman"
        r_pg.font.size = Pt(10.5)
        r_pg.font.bold = True
        
    # Subheading: List of Tables (Academic)
    p_at_sub = doc.add_paragraph()
    p_at_sub.paragraph_format.space_before = Pt(14)
    p_at_sub.paragraph_format.space_after = Pt(4)
    r_ats = p_at_sub.add_run("LIST OF TABLES")
    r_ats.font.name = "Times New Roman"
    r_ats.font.size = Pt(12)
    r_ats.font.bold = True
    
    p_at_hdr = doc.add_paragraph()
    p_at_hdr.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT)
    p_at_hdr.paragraph_format.space_after = Pt(4)
    r_atl = p_at_hdr.add_run("Table No. and Title")
    r_atl.font.name = "Times New Roman"
    r_atl.font.size = Pt(11)
    r_atl.font.bold = True
    p_at_hdr.add_run("\t")
    r_atr = p_at_hdr.add_run("Page No.")
    r_atr.font.name = "Times New Roman"
    r_atr.font.size = Pt(11)
    r_atr.font.bold = True
    
    p_at_line = doc.add_paragraph()
    p_at_line.paragraph_format.space_after = Pt(8)
    p_at_border = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:bottom w:val="single" w:sz="6" w:space="1" w:color="333333"/></w:pBdr>')
    p_at_line._p.get_or_add_pPr().append(p_at_border)
    
    academic_tables = [
        ("Table 1.1", "Taxonomical and Operational Comparison: Acute Academic Stress vs. Chronic Academic Burnout", "3"),
        ("Table 2.1", "Taxonomical Comparison of Standardized Psychometric Instruments in Higher Education (MBI-SS, DASS-21, PSS-10, OLBI, CBI)", "6"),
        ("Table 2.2", "Comparative Synthesis of Prior Machine Learning Works vs. Proposed Multi-Dimensional Predictive Framework", "10"),
        ("Table 3.1", "Exhaustive Feature Dictionary and Descriptive Summary Statistics of Numeric Features (n = 3,000)", "11"),
        ("Table 3.2", "Cross-Strata Behavioral Profiling Across Burnout Risk Tiers (Mean +/- Std: Low, Medium, and High Cohorts)", "13"),
        ("Table 3.4", "Multicollinearity Diagnostics and Variance Inflation Factor (VIF) Analysis for Predictor Variables", "15"),
        ("Table 3.5", "Mathematical Formulations and ANOVA F-Statistic Validation of Four Engineered Interaction Features (API, SSR, SSD, LBS)", "16"),
        ("Table 4.1", "Hyperparameter Search Grids and Optimal Tuned Parameters for the Seven Evaluated Machine Learning Classifiers", "19"),
        ("Table 5.1", "Comprehensive Multi-Classifier Benchmark Performance Matrix on Hold-Out Test Set (n_test = 600)", "20"),
        ("Table 5.2", "Stratified 5-Fold Cross-Validation Accuracy Matrix across Evaluated Models Confirming Algorithmic Stability", "21"),
        ("Table 5.3", "Granular Classification Report for Production Logistic Regression Model (Precision, Recall, and F1 per Risk Class)", "22"),
        ("Table 5.4", "Empirical Evaluation Metrics for Continuous Stress Score Regression Model (R^2 = 1.0000, MSE = 0.0000)", "23"),
        ("Table 5.5", "Ablation Study: Quantifying the Impact of Domain-Specific Feature Engineering on Linear and Non-Linear Models", "24"),
        ("Table 6.1", "Production REST API Specification for Real-Time Inference (/predict) and Batch File Evaluation (/batch-predict)", "25"),
        ("Table A.1", "Standardized 16-Parameter Student Burnout Assessment Questionnaire (Psychometric Formulation and Valid Input Ranges)", "45"),
        ("Table A.2", "Empirical Inferences and Risk Probability Distributions for 30 Diverse Synthetic Student Case Scenarios (Cases C01--C30)", "45")
    ]
    
    for tnum, ttitle, tpage in academic_tables:
        p = doc.add_paragraph()
        p.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        
        r_num = p.add_run(tnum + ": ")
        r_num.font.name = "Times New Roman"
        r_num.font.size = Pt(10.5)
        r_num.font.bold = True
        
        r_desc = p.add_run(ttitle)
        r_desc.font.name = "Times New Roman"
        r_desc.font.size = Pt(10)
        
        p.add_run("\t")
        
        r_pg = p.add_run(tpage)
        r_pg.font.name = "Times New Roman"
        r_pg.font.size = Pt(10.5)
        r_pg.font.bold = True

    # Output paths
    desktop_file = os.path.join(DESKTOP_DIR, "Palak_Goenka_Thesis_List_of_Figures_and_Tables.docx")
    desktop_copy1 = os.path.join(DESKTOP_DIR, "Thesis_List_of_Figures_and_Tables.docx")
    desktop_copy2 = os.path.join(DESKTOP_DIR, "List_of_Figures_and_Tables.docx")
    report_file = os.path.join(REPORT_DIR, "Palak_Goenka_Thesis_List_of_Figures_and_Tables.docx")
    
    doc.save(desktop_file)
    doc.save(desktop_copy1)
    doc.save(desktop_copy2)
    doc.save(report_file)
    print(f"[+] Successfully generated and saved:\n    {desktop_file}")

if __name__ == "__main__":
    create_lof_lot_document()
