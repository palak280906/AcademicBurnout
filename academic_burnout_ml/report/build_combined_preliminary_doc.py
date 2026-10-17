# -*- coding: utf-8 -*-
"""
Combines Table of Contents, List of Figures, and List of Tables into a single
complete Preliminary Pages Word Document (.docx) for Palak Goenka's Thesis.
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import parse_xml

DESKTOP_DIR = r"D:\user files\New folder\Desktop\learner"
REPORT_DIR = os.path.dirname(os.path.abspath(__file__))

def create_combined_preliminary_doc():
    doc = Document()
    
    # A4 Page Margins
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.0)
    
    RIGHT_TAB_POS = Inches(6.0)
    
    # Default Font: Times New Roman
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0, 0, 0)
    
    # Helper to add institutional header
    def add_header(title_text):
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
        r_proj.font.size = Pt(10)
        r_proj.font.italic = True
        
        r_cand = p_inst.add_run("Candidate: Palak Goenka | Enrollment No: A357175124008 | B.Tech CSE (AI & ML)\n")
        r_cand.font.name = "Times New Roman"
        r_cand.font.size = Pt(9.5)
        r_cand.font.bold = True
        p_inst.paragraph_format.space_after = Pt(12)
        
        p_title = doc.add_paragraph()
        p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_title = p_title.add_run(title_text)
        r_title.font.name = "Times New Roman"
        r_title.font.size = Pt(16)
        r_title.font.bold = True
        r_title.underline = True
        p_title.paragraph_format.space_after = Pt(12)

    def add_table_header(left_lbl, right_lbl="Page No."):
        p_hdr = doc.add_paragraph()
        p_hdr.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT)
        p_hdr.paragraph_format.space_after = Pt(4)
        r_l = p_hdr.add_run(left_lbl)
        r_l.font.name = "Times New Roman"
        r_l.font.size = Pt(12)
        r_l.font.bold = True
        p_hdr.add_run("\t")
        r_r = p_hdr.add_run(right_lbl)
        r_r.font.name = "Times New Roman"
        r_r.font.size = Pt(12)
        r_r.font.bold = True
        
        p_line = doc.add_paragraph()
        p_line.paragraph_format.space_after = Pt(8)
        p_border = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:bottom w:val="single" w:sz="8" w:space="1" w:color="333333"/></w:pBdr>')
        p_line._p.get_or_add_pPr().append(p_border)

    # ==========================================
    # 1. TABLE OF CONTENTS
    # ==========================================
    add_header("TABLE OF CONTENTS")
    add_table_header("Title")
    
    # Load TOC items
    toc_data = [
        (0, "Certificate of Authenticity", "3"),
        (0, "Candidate Declaration", "4"),
        (0, "Abstract", "5"),
        (0, "Acknowledgements", "7"),
        (0, "List of Abbreviations", "12"),
        
        (1, "Chapter 1: Introduction and Background", "14"),
        (2, "1.1 Motivation and Socio-Academic Context", "14"),
        (2, "1.2 Definitional Demarcation: Academic Stress vs. Academic Burnout", "15"),
        (3, "1.2.1 Acute Academic Stress: Adaptive and Transient", "15"),
        (3, "1.2.2 Academic Burnout: Maladaptive, Chronic, and Systemic", "16"),
        (2, "1.3 Theoretical Psychological Frameworks (MBI-SS & JD-R)", "17"),
        (3, "1.3.1 Maslach Burnout Inventory -- Student Survey (MBI-SS)", "17"),
        (3, "1.3.2 The Job Demands-Resources (JD-R) Model Applied to Academia", "17"),
        (2, "1.4 Problem Statement and Mathematical Formulation", "18"),
        (2, "1.5 Research Objectives and Hypotheses", "18"),
        (2, "1.6 Summary of Major Contributions", "18"),
        (2, "1.7 Thesis Organization", "18"),
        
        (1, "Chapter 2: Literature Review and Related Work", "19"),
        (2, "2.1 Historical Evolution of Burnout Research", "19"),
        (2, "2.2 Traditional Psychometric Instruments in Higher Education", "19"),
        (3, "2.2.1 Comparison of MBI-SS, DASS-21, PSS-10, OLBI, and CBI (Table 2.1)", "20"),
        (2, "2.3 Computational Intelligence and Machine Learning in Student Well-Being", "21"),
        (3, "2.3.1 Physiological and Wearable Sensor Informatics", "21"),
        (3, "2.3.2 Mobile Sensing and Digital Phenotyping", "21"),
        (3, "2.3.3 Educational Data Mining and LMS Behavioral Analytics", "21"),
        (3, "2.3.4 Survey-Based Machine Learning Informatics", "22"),
        (2, "2.4 Systematic Review of Seminal Related Works (12 Studies)", "22"),
        (2, "2.5 Comparative Literature Synthesis (Table 2.2)", "23"),
        (2, "2.6 Critical Gaps in Contemporary Literature", "23"),
        (2, "2.7 Proposed Conceptual and Technical Bridge", "23"),
        
        (1, "Chapter 3: Dataset Architecture and Exploratory Data Analysis", "24"),
        (2, "3.1 Data Acquisition Protocol and Cohort Demographics", "24"),
        (2, "3.2 Exhaustive Feature Dictionary (16 Parameters) (Table 3.1)", "24"),
        (2, "3.3 Target Variables: 3-Tier Classification and Continuous Score", "24"),
        (2, "3.4 Summary Descriptive Statistics and Cross-Strata Profiling (Table 3.2)", "26"),
        (2, "3.5 Data Integrity, Missing Values, and Quality Assurance", "26"),
        (2, "3.6 Exploratory Data Analysis: Univariate Feature Distributions (Fig. 3.1)", "27"),
        (2, "3.7 Bivariate and Multivariate Correlation Analysis (Fig. 3.2)", "28"),
        (2, "3.8 Multicollinearity Analysis and Variance Inflation Factor (VIF) (Table 3.4)", "28"),
        (2, "3.9 Domain-Specific Feature Engineering (API, SSR, SSD, LBS) (Table 3.5)", "29"),
        
        (1, "Chapter 4: System Architecture and Methodology", "30"),
        (2, "4.1 End-to-End System Architecture Pipeline", "30"),
        (2, "4.2 Mathematical Formulations of Benchmarked Classifiers (7 Models)", "31"),
        (3, "4.2.1 Multinomial Logistic Regression (L2-Regularized)", "31"),
        (3, "4.2.2 Support Vector Classification (SVC with RBF Kernel)", "31"),
        (3, "4.2.3 Decision Tree Classifier (CART)", "31"),
        (3, "4.2.4 Random Forest Classifier (Breiman Variance Reduction)", "31"),
        (3, "4.2.5 Gradient Boosted Decision Trees (GBDT)", "31"),
        (3, "4.2.6 K-Nearest Neighbors (KNN)", "32"),
        (3, "4.2.7 Gaussian Naive Bayes (GNB)", "32"),
        (2, "4.3 Continuous Stress Regression Formulation (Ridge Normal Equations & SVD)", "32"),
        (2, "4.4 Cross-Validation Strategy and Hyperparameter Tuning", "34"),
        (2, "4.5 Performance Evaluation Metrics", "34"),
        
        (1, "Chapter 5: Experimental Results and Model Evaluation", "33"),
        (2, "5.1 Multi-Classifier Benchmark Evaluation (Table 5.1 & Fig. 5.1)", "33"),
        (3, "5.1.1 Stratified 5-Fold Cross-Validation Analysis (Table 5.2)", "34"),
        (3, "5.1.2 Algorithmic Superiority of Regularized Linear Modeling", "34"),
        (2, "5.2 Detailed Performance Analysis of the Production Classifier (Table 5.3)", "35"),
        (2, "5.3 Confusion Matrix Analysis and Safety Audit (Fig. 5.2)", "35"),
        (3, "5.3.1 Critical Triage Safety and Zero Cross-Tier Misclassification", "35"),
        (2, "5.4 Continuous Stress Score Regression Results (Fig. 5.3)", "36"),
        (2, "5.5 Feature Importance and Interpretability Analysis (Fig. 5.4)", "37"),
        (2, "5.6 Ablation Studies: Value of Feature Engineering (Table 5.5)", "37"),
        
        (1, "Chapter 6: Web Application Architecture and Cloud Deployment", "38"),
        (2, "6.1 Full-Stack System Design Philosophy", "38"),
        (2, "6.2 Backend Architecture and REST API Specification (Table 6.1)", "38"),
        (2, "6.3 User Interface and Experience Design (Glassmorphism Dashboard)", "39"),
        (2, "6.4 Cloud Deployment on Vercel Serverless Infrastructure", "39"),
        
        (1, "Chapter 7: Conclusion, Societal Impact, and Future Work", "40"),
        (2, "7.1 Synthesis of Thesis Accomplishments", "40"),
        (2, "7.2 Answering the Research Questions (RQ1, RQ2, RQ3)", "40"),
        (2, "7.3 Institutional Implications and Clinical Implementation", "41"),
        (2, "7.4 Ethical Considerations, Algorithmic Fairness, and Data Privacy", "41"),
        (2, "7.5 Limitations of the Current Study", "41"),
        (2, "7.6 Future Research Directions", "41"),
        
        (1, "Appendices and Reference Documentation", "42"),
        (2, "Appendix A: Core Python Implementation", "42"),
        (3, "Appendix A.1: End-to-End Machine Learning Pipeline (src/pipeline.py)", "44"),
        (3, "Appendix A.1 (Contd.): Model Persistence & Evaluation Routines", "48"),
        (3, "Appendix A.2: Real-Time Inference & Feature Engineering Engine (src/predict.py)", "51"),
        (3, "Appendix A.3: Flask Web Server & REST API Controller (app.py)", "54"),
        (2, "Appendix B: Production Benchmark Terminal Execution Log", "57"),
        (2, "Appendix C: Standardized 16-Parameter Questionnaire", "58"),
        (2, "Appendix D: Synthetic Student Case Inferences (Cases C01--C30)", "58"),
        (1, "Bibliography (42 Hyperlinked Peer-Reviewed References)", "61")
    ]
    
    for level, title, page_str in toc_data:
        p = doc.add_paragraph()
        p.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        if level == 0:
            p.paragraph_format.left_indent = Inches(0.0)
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            rt = p.add_run(title)
            rt.font.name = "Times New Roman"
            rt.font.size = Pt(11)
            rt.font.bold = True
            p.add_run("\t")
            rp = p.add_run(page_str)
            rp.font.name = "Times New Roman"
            rp.font.size = Pt(11)
            rp.font.bold = True
        elif level == 1:
            p.paragraph_format.left_indent = Inches(0.0)
            p.paragraph_format.space_before = Pt(7)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.2
            rt = p.add_run(title)
            rt.font.name = "Times New Roman"
            rt.font.size = Pt(11.5)
            rt.font.bold = True
            rt.font.color.rgb = RGBColor(15, 23, 42)
            p.add_run("\t")
            rp = p.add_run(page_str)
            rp.font.name = "Times New Roman"
            rp.font.size = Pt(11.5)
            rp.font.bold = True
        elif level == 2:
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.15
            rt = p.add_run(title)
            rt.font.name = "Times New Roman"
            rt.font.size = Pt(10.5)
            p.add_run("\t")
            rp = p.add_run(page_str)
            rp.font.name = "Times New Roman"
            rp.font.size = Pt(10.5)
        elif level == 3:
            p.paragraph_format.left_indent = Inches(0.5)
            p.paragraph_format.space_before = Pt(0.5)
            p.paragraph_format.space_after = Pt(0.5)
            p.paragraph_format.line_spacing = 1.1
            rt = p.add_run(title)
            rt.font.name = "Times New Roman"
            rt.font.size = Pt(9.5)
            rt.font.italic = True
            rt.font.color.rgb = RGBColor(71, 85, 105)
            p.add_run("\t")
            rp = p.add_run(page_str)
            rp.font.name = "Times New Roman"
            rp.font.size = Pt(9.5)

    # ==========================================
    # 2. LIST OF FIGURES
    # ==========================================
    doc.add_page_break()
    add_header("LIST OF FIGURES")
    add_table_header("Figure No. and Title")
    
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
        
        p.add_run("\t")
        
        r_pg = p.add_run(fpage)
        r_pg.font.name = "Times New Roman"
        r_pg.font.size = Pt(11)
        r_pg.font.bold = True

    # ==========================================
    # 3. LIST OF TABLES
    # ==========================================
    doc.add_page_break()
    add_header("LIST OF TABLES")
    add_table_header("Table No. and Title")
    
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
        
        p.add_run("\t")
        
        r_pg = p.add_run(tpage)
        r_pg.font.name = "Times New Roman"
        r_pg.font.size = Pt(11)
        r_pg.font.bold = True

    # Output paths
    desktop_file = os.path.join(DESKTOP_DIR, "Palak_Goenka_Thesis_Complete_Preliminary_Pages.docx")
    report_file = os.path.join(REPORT_DIR, "Palak_Goenka_Thesis_Complete_Preliminary_Pages.docx")
    
    doc.save(desktop_file)
    doc.save(report_file)
    print(f"[+] Successfully generated combined preliminary document at:\n    {desktop_file}")

if __name__ == "__main__":
    create_combined_preliminary_doc()
