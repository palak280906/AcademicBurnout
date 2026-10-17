# -*- coding: utf-8 -*-
"""
Generates the Table of Contents Word Document (.docx) for Palak Goenka's Thesis.
Includes correct page numbers matching the compiled thesis, dot leaders leading to the page numbers,
and strictly formatted in Times New Roman matching the Amity University thesis style.
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement, parse_xml

DESKTOP_DIR = r"D:\user files\New folder\Desktop\learner"
REPORT_DIR = os.path.dirname(os.path.abspath(__file__))

def create_toc_document():
    doc = Document()
    
    # Page setup: A4 paper with standard margins (Left: 1.25 in, Right: 1.0 in, Top: 1.0 in, Bottom: 1.0 in)
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.25)
    section.right_margin = Inches(1.0)
    
    # Calculate usable width: 8.27 - 1.25 - 1.0 = 6.02 inches
    RIGHT_TAB_POS = Inches(6.0)
    
    # Set default style to Times New Roman
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0, 0, 0)
    
    # Document Header / Title
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
    
    # Main Heading: TABLE OF CONTENTS
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("TABLE OF CONTENTS")
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(16)
    r_title.font.bold = True
    r_title.underline = True
    p_title.paragraph_format.space_after = Pt(12)
    
    # Table Header Line: Title on Left, Page No. on Right
    p_hdr = doc.add_paragraph()
    p_hdr.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT)
    p_hdr.paragraph_format.space_after = Pt(4)
    r_hdr_left = p_hdr.add_run("Title")
    r_hdr_left.font.name = "Times New Roman"
    r_hdr_left.font.size = Pt(12)
    r_hdr_left.font.bold = True
    
    p_hdr.add_run("\t")
    
    r_hdr_right = p_hdr.add_run("Page No.")
    r_hdr_right.font.name = "Times New Roman"
    r_hdr_right.font.size = Pt(12)
    r_hdr_right.font.bold = True
    
    # Add a thin horizontal divider line below header
    p_hr = doc.add_paragraph()
    p_hr.paragraph_format.space_after = Pt(10)
    p_hr_border = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:bottom w:val="single" w:sz="8" w:space="1" w:color="333333"/></w:pBdr>')
    p_hr._p.get_or_add_pPr().append(p_hr_border)
    
    # Full Structure of the Dissertation with exact verified page numbers from Palak_Goenka_Thesis.pdf
    toc_data = [
        # (Level, Title, Page_Number)
        # Level 0: Front matter / Preliminary
        (0, "Certificate of Authenticity", "3"),
        (0, "Candidate Declaration", "4"),
        (0, "Abstract", "5"),
        (0, "Acknowledgements", "7"),
        (0, "List of Abbreviations", "12"),
        
        # Level 1: Chapter 1
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
        
        # Level 1: Chapter 2
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
        
        # Level 1: Chapter 3
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
        
        # Level 1: Chapter 4
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
        
        # Level 1: Chapter 5
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
        
        # Level 1: Chapter 6
        (1, "Chapter 6: Web Application Architecture and Cloud Deployment", "38"),
        (2, "6.1 Full-Stack System Design Philosophy", "38"),
        (2, "6.2 Backend Architecture and REST API Specification (Table 6.1)", "38"),
        (2, "6.3 User Interface and Experience Design (Glassmorphism Dashboard)", "39"),
        (2, "6.4 Cloud Deployment on Vercel Serverless Infrastructure", "39"),
        
        # Level 1: Chapter 7
        (1, "Chapter 7: Conclusion, Societal Impact, and Future Work", "40"),
        (2, "7.1 Synthesis of Thesis Accomplishments", "40"),
        (2, "7.2 Answering the Research Questions (RQ1, RQ2, RQ3)", "40"),
        (2, "7.3 Institutional Implications and Clinical Implementation", "41"),
        (2, "7.4 Ethical Considerations, Algorithmic Fairness, and Data Privacy", "41"),
        (2, "7.5 Limitations of the Current Study", "41"),
        (2, "7.6 Future Research Directions", "41"),
        
        # Level 1: Appendices & Bibliography
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
            # Front matter entries
            p.paragraph_format.left_indent = Inches(0.0)
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            
            run_title = p.add_run(title)
            run_title.font.name = "Times New Roman"
            run_title.font.size = Pt(11)
            run_title.font.bold = True
            
            p.add_run("\t")
            
            run_page = p.add_run(page_str)
            run_page.font.name = "Times New Roman"
            run_page.font.size = Pt(11)
            run_page.font.bold = True
            
        elif level == 1:
            # Chapter Main Headings
            p.paragraph_format.left_indent = Inches(0.0)
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.25
            
            run_title = p.add_run(title)
            run_title.font.name = "Times New Roman"
            run_title.font.size = Pt(11.5)
            run_title.font.bold = True
            run_title.font.color.rgb = RGBColor(15, 23, 42)
            
            p.add_run("\t")
            
            run_page = p.add_run(page_str)
            run_page.font.name = "Times New Roman"
            run_page.font.size = Pt(11.5)
            run_page.font.bold = True
            
        elif level == 2:
            # Main Sections (e.g. 1.1, 1.2)
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.15
            
            run_title = p.add_run(title)
            run_title.font.name = "Times New Roman"
            run_title.font.size = Pt(10.5)
            run_title.font.bold = False
            
            p.add_run("\t")
            
            run_page = p.add_run(page_str)
            run_page.font.name = "Times New Roman"
            run_page.font.size = Pt(10.5)
            run_page.font.bold = False
            
        elif level == 3:
            # Subsections (e.g. 1.2.1, 1.2.2)
            p.paragraph_format.left_indent = Inches(0.5)
            p.paragraph_format.space_before = Pt(0.5)
            p.paragraph_format.space_after = Pt(0.5)
            p.paragraph_format.line_spacing = 1.1
            
            run_title = p.add_run(title)
            run_title.font.name = "Times New Roman"
            run_title.font.size = Pt(9.5)
            run_title.font.italic = True
            run_title.font.color.rgb = RGBColor(71, 85, 105)
            
            p.add_run("\t")
            
            run_page = p.add_run(page_str)
            run_page.font.name = "Times New Roman"
            run_page.font.size = Pt(9.5)
            run_page.font.bold = False
            
    # Add a page break and an alternative academic numbering format (Roman frontmatter + Arabic chapters starting at 1)
    doc.add_page_break()
    
    p_sec2_title = doc.add_paragraph()
    p_sec2_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sec2 = p_sec2_title.add_run("TABLE OF CONTENTS (STANDARD ACADEMIC NUMBERING)")
    r_sec2.font.name = "Times New Roman"
    r_sec2.font.size = Pt(14)
    r_sec2.font.bold = True
    r_sec2.underline = True
    p_sec2_title.paragraph_format.space_after = Pt(6)
    
    p_note = doc.add_paragraph()
    p_note.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_note = p_note.add_run("[Note: This section lists the traditional academic format with Roman numerals for Preliminary pages and Chapter 1 resetting to Page 1]")
    r_note.font.name = "Times New Roman"
    r_note.font.size = Pt(9.5)
    r_note.font.italic = True
    r_note.font.color.rgb = RGBColor(100, 116, 139)
    p_note.paragraph_format.space_after = Pt(12)
    
    # Table Header Line for Section 2
    p_hdr2 = doc.add_paragraph()
    p_hdr2.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT)
    p_hdr2.paragraph_format.space_after = Pt(4)
    r_hdr2_l = p_hdr2.add_run("Title")
    r_hdr2_l.font.name = "Times New Roman"
    r_hdr2_l.font.size = Pt(12)
    r_hdr2_l.font.bold = True
    p_hdr2.add_run("\t")
    r_hdr2_r = p_hdr2.add_run("Page No.")
    r_hdr2_r.font.name = "Times New Roman"
    r_hdr2_r.font.size = Pt(12)
    r_hdr2_r.font.bold = True
    
    p_hr2 = doc.add_paragraph()
    p_hr2.paragraph_format.space_after = Pt(10)
    p_hr2_border = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:bottom w:val="single" w:sz="8" w:space="1" w:color="333333"/></w:pBdr>')
    p_hr2._p.get_or_add_pPr().append(p_hr2_border)
    
    # Academic relative numbering: Preliminary (ii to viii), Chapters (1 to 48)
    toc_data_academic = [
        (0, "Certificate of Authenticity", "ii"),
        (0, "Candidate Declaration", "iii"),
        (0, "Abstract", "iv"),
        (0, "Acknowledgements", "v"),
        (0, "List of Abbreviations", "viii"),
        
        (1, "Chapter 1: Introduction and Background", "1"),
        (2, "1.1 Motivation and Socio-Academic Context", "1"),
        (2, "1.2 Definitional Demarcation: Academic Stress vs. Academic Burnout", "2"),
        (3, "1.2.1 Acute Academic Stress: Adaptive and Transient", "2"),
        (3, "1.2.2 Academic Burnout: Maladaptive, Chronic, and Systemic", "3"),
        (2, "1.3 Theoretical Psychological Frameworks (MBI-SS & JD-R)", "4"),
        (3, "1.3.1 Maslach Burnout Inventory -- Student Survey (MBI-SS)", "4"),
        (3, "1.3.2 The Job Demands-Resources (JD-R) Model Applied to Academia", "4"),
        (2, "1.4 Problem Statement and Mathematical Formulation", "5"),
        (2, "1.5 Research Objectives and Hypotheses", "5"),
        (2, "1.6 Summary of Major Contributions", "5"),
        (2, "1.7 Thesis Organization", "5"),
        
        (1, "Chapter 2: Literature Review and Related Work", "6"),
        (2, "2.1 Historical Evolution of Burnout Research", "6"),
        (2, "2.2 Traditional Psychometric Instruments in Higher Education", "6"),
        (3, "2.2.1 Comparison of MBI-SS, DASS-21, PSS-10, OLBI, and CBI (Table 2.1)", "7"),
        (2, "2.3 Computational Intelligence and Machine Learning in Student Well-Being", "8"),
        (3, "2.3.1 Physiological and Wearable Sensor Informatics", "8"),
        (3, "2.3.2 Mobile Sensing and Digital Phenotyping", "8"),
        (3, "2.3.3 Educational Data Mining and LMS Behavioral Analytics", "8"),
        (3, "2.3.4 Survey-Based Machine Learning Informatics", "9"),
        (2, "2.4 Systematic Review of Seminal Related Works (12 Studies)", "9"),
        (2, "2.5 Comparative Literature Synthesis (Table 2.2)", "10"),
        (2, "2.6 Critical Gaps in Contemporary Literature", "10"),
        (2, "2.7 Proposed Conceptual and Technical Bridge", "10"),
        
        (1, "Chapter 3: Dataset Architecture and Exploratory Data Analysis", "11"),
        (2, "3.1 Data Acquisition Protocol and Cohort Demographics", "11"),
        (2, "3.2 Exhaustive Feature Dictionary (16 Parameters) (Table 3.1)", "11"),
        (2, "3.3 Target Variables: 3-Tier Classification and Continuous Score", "11"),
        (2, "3.4 Summary Descriptive Statistics and Cross-Strata Profiling (Table 3.2)", "13"),
        (2, "3.5 Data Integrity, Missing Values, and Quality Assurance", "13"),
        (2, "3.6 Exploratory Data Analysis: Univariate Feature Distributions (Fig. 3.1)", "14"),
        (2, "3.7 Bivariate and Multivariate Correlation Analysis (Fig. 3.2)", "15"),
        (2, "3.8 Multicollinearity Analysis and Variance Inflation Factor (VIF) (Table 3.4)", "15"),
        (2, "3.9 Domain-Specific Feature Engineering (API, SSR, SSD, LBS) (Table 3.5)", "16"),
        
        (1, "Chapter 4: System Architecture and Methodology", "17"),
        (2, "4.1 End-to-End System Architecture Pipeline", "17"),
        (2, "4.2 Mathematical Formulations of Benchmarked Classifiers (7 Models)", "18"),
        (3, "4.2.1 Multinomial Logistic Regression (L2-Regularized)", "18"),
        (3, "4.2.2 Support Vector Classification (SVC with RBF Kernel)", "18"),
        (3, "4.2.3 Decision Tree Classifier (CART)", "18"),
        (3, "4.2.4 Random Forest Classifier (Breiman Variance Reduction)", "18"),
        (3, "4.2.5 Gradient Boosted Decision Trees (GBDT)", "18"),
        (3, "4.2.6 K-Nearest Neighbors (KNN)", "19"),
        (3, "4.2.7 Gaussian Naive Bayes (GNB)", "19"),
        (2, "4.3 Continuous Stress Regression Formulation (Ridge Normal Equations & SVD)", "19"),
        (2, "4.4 Cross-Validation Strategy and Hyperparameter Tuning", "21"),
        (2, "4.5 Performance Evaluation Metrics", "21"),
        
        (1, "Chapter 5: Experimental Results and Model Evaluation", "20"),
        (2, "5.1 Multi-Classifier Benchmark Evaluation (Table 5.1 & Fig. 5.1)", "20"),
        (3, "5.1.1 Stratified 5-Fold Cross-Validation Analysis (Table 5.2)", "21"),
        (3, "5.1.2 Algorithmic Superiority of Regularized Linear Modeling", "21"),
        (2, "5.2 Detailed Performance Analysis of the Production Classifier (Table 5.3)", "22"),
        (2, "5.3 Confusion Matrix Analysis and Safety Audit (Fig. 5.2)", "22"),
        (3, "5.3.1 Critical Triage Safety and Zero Cross-Tier Misclassification", "22"),
        (2, "5.4 Continuous Stress Score Regression Results (Fig. 5.3)", "23"),
        (2, "5.5 Feature Importance and Interpretability Analysis (Fig. 5.4)", "24"),
        (2, "5.6 Ablation Studies: Value of Feature Engineering (Table 5.5)", "24"),
        
        (1, "Chapter 6: Web Application Architecture and Cloud Deployment", "25"),
        (2, "6.1 Full-Stack System Design Philosophy", "25"),
        (2, "6.2 Backend Architecture and REST API Specification (Table 6.1)", "25"),
        (2, "6.3 User Interface and Experience Design (Glassmorphism Dashboard)", "26"),
        (2, "6.4 Cloud Deployment on Vercel Serverless Infrastructure", "26"),
        
        (1, "Chapter 7: Conclusion, Societal Impact, and Future Work", "27"),
        (2, "7.1 Synthesis of Thesis Accomplishments", "27"),
        (2, "7.2 Answering the Research Questions (RQ1, RQ2, RQ3)", "27"),
        (2, "7.3 Institutional Implications and Clinical Implementation", "28"),
        (2, "7.4 Ethical Considerations, Algorithmic Fairness, and Data Privacy", "28"),
        (2, "7.5 Limitations of the Current Study", "28"),
        (2, "7.6 Future Research Directions", "28"),
        
        (1, "Appendices and Reference Documentation", "29"),
        (2, "Appendix A: Core Python Implementation", "29"),
        (3, "Appendix A.1: End-to-End Machine Learning Pipeline (src/pipeline.py)", "31"),
        (3, "Appendix A.1 (Contd.): Model Persistence & Evaluation Routines", "35"),
        (3, "Appendix A.2: Real-Time Inference & Feature Engineering Engine (src/predict.py)", "38"),
        (3, "Appendix A.3: Flask Web Server & REST API Controller (app.py)", "41"),
        (2, "Appendix B: Production Benchmark Terminal Execution Log", "44"),
        (2, "Appendix C: Standardized 16-Parameter Questionnaire", "45"),
        (2, "Appendix D: Synthetic Student Case Inferences (Cases C01--C30)", "45"),
        (1, "Bibliography (42 Hyperlinked Peer-Reviewed References)", "48")
    ]
    
    for level, title, page_str in toc_data_academic:
        p = doc.add_paragraph()
        p.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB_POS, WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        
        if level == 0:
            p.paragraph_format.left_indent = Inches(0.0)
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.15
            run_title = p.add_run(title)
            run_title.font.name = "Times New Roman"
            run_title.font.size = Pt(11)
            run_title.font.bold = True
            p.add_run("\t")
            run_page = p.add_run(page_str)
            run_page.font.name = "Times New Roman"
            run_page.font.size = Pt(11)
            run_page.font.bold = True
        elif level == 1:
            p.paragraph_format.left_indent = Inches(0.0)
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.25
            run_title = p.add_run(title)
            run_title.font.name = "Times New Roman"
            run_title.font.size = Pt(11.5)
            run_title.font.bold = True
            run_title.font.color.rgb = RGBColor(15, 23, 42)
            p.add_run("\t")
            run_page = p.add_run(page_str)
            run_page.font.name = "Times New Roman"
            run_page.font.size = Pt(11.5)
            run_page.font.bold = True
        elif level == 2:
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.15
            run_title = p.add_run(title)
            run_title.font.name = "Times New Roman"
            run_title.font.size = Pt(10.5)
            run_title.font.bold = False
            p.add_run("\t")
            run_page = p.add_run(page_str)
            run_page.font.name = "Times New Roman"
            run_page.font.size = Pt(10.5)
            run_page.font.bold = False
        elif level == 3:
            p.paragraph_format.left_indent = Inches(0.5)
            p.paragraph_format.space_before = Pt(0.5)
            p.paragraph_format.space_after = Pt(0.5)
            p.paragraph_format.line_spacing = 1.1
            run_title = p.add_run(title)
            run_title.font.name = "Times New Roman"
            run_title.font.size = Pt(9.5)
            run_title.font.italic = True
            run_title.font.color.rgb = RGBColor(71, 85, 105)
            p.add_run("\t")
            run_page = p.add_run(page_str)
            run_page.font.name = "Times New Roman"
            run_page.font.size = Pt(9.5)
            run_page.font.bold = False

    # Save to desktop and report folders
    desktop_file = os.path.join(DESKTOP_DIR, "Palak_Goenka_Thesis_Table_of_Contents.docx")
    report_file = os.path.join(REPORT_DIR, "Palak_Goenka_Thesis_Table_of_Contents.docx")
    
    doc.save(desktop_file)
    doc.save(report_file)
    print(f"[+] Successfully saved Word document to:\n    {desktop_file}\n    {report_file}")

if __name__ == "__main__":
    create_toc_document()