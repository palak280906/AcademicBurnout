# -*- coding: utf-8 -*-
"""
Preamble and Front Matter for Amity University (ASET) Thesis
Student: Palak Goenka (A357175124008)
"""

CONTENT = r"""\documentclass[12pt,a4paper,oneside]{report}

% ---------------------------------------------------------
% Essential Packages for Amity ASET Major Project Report
% ---------------------------------------------------------
\usepackage[utf8]{inputenc}
\usepackage[margin=1in, left=1.25in, top=1in, bottom=1in]{geometry}
\usepackage{graphicx}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{array}
\usepackage{multirow}
\usepackage{setspace}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{float}
\usepackage{microtype}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{tocloft}
\usepackage[colorlinks=true, linkcolor=blue, citecolor=blue, urlcolor=blue]{hyperref}

% ---------------------------------------------------------
% Code Listing Styling
% ---------------------------------------------------------
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.96,0.97,0.98}

\lstdefinestyle{mystyle}{
    backgroundcolor=\backcolour,   
    commentstyle=\color{codegreen},
    keywordstyle=\color{blue}\bfseries,
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2,
    frame=single,
    rulecolor=\color{codegray!40}
}
\lstset{style=mystyle}

% ---------------------------------------------------------
% Document Formatting & Spacing
% ---------------------------------------------------------
\onehalfspacing
\setlength{\parskip}{0.5em}
\setlength{\parindent}{0pt}

% Section title formatting
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries}{\chaptertitlename\ \thechapter}{20pt}{\Huge}
\titlespacing*{\chapter}{0pt}{10pt}{20pt}

% Header and Footer setup
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\nouppercase{\leftmark}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\headheight}{15pt}

% =========================================================
% DOCUMENT STARTS HERE
% =========================================================
\begin{document}

% ---------------------------------------------------------
% PRELIMINARY PAGES (ROMAN NUMERALS)
% ---------------------------------------------------------
\pagenumbering{roman}

% ---------------------------------------------------------
% PAGE 1: TITLE PAGE (Strict Amity ASET Layout)
% ---------------------------------------------------------
\begin{titlepage}
    \begin{center}
        \vspace*{0.3cm}
        {\LARGE \textbf{Early Detection of Academic Burnout using Machine Learning}}\\[0.3cm]
        {\large \textbf{A Multi-Dimensional Behavioral Informatics and Predictive Analytics Framework}}\\[1.2cm]
        
        \textit{Major Project submitted to}\\[0.2cm]
        \textbf{Amity School of Engineering and Technology, Amity University Jharkhand}\\[0.2cm]
        \textit{in partial fulfilment of the requirements for}\\[0.2cm]
        The degree of\\[0.2cm]
        {\Large \textbf{Bachelor of Technology}}\\[0.2cm]
        \textit{in}\\[0.2cm]
        {\large \textbf{Computer Science and Engineering (Artificial Intelligence and Machine Learning)}}\\[0.2cm]
        \textit{from}\\[0.2cm]
        \textbf{Department of Computer Science and Engineering,}\\[0.1cm]
        \textbf{Amity School of Engineering and Technology}\\[1.0cm]
        
        \textit{by}\\[0.2cm]
        {\Large \textbf{Palak Goenka}}\\[0.1cm]
        (\textbf{Enrollment No.: A357175124008})\\[0.8cm]
        
        \textit{under the guidance of}\\[0.2cm]
        {\large \textbf{Prof. Supervisor}}\\[0.1cm]
        Assistant Professor, Department of Computer Science and Engineering\\[1.2cm]
        
        \begin{figure}[H]
            \centering
            % Official Amity University Emblem / ASET Seal Placeholder
            \rule{3.2cm}{3.2cm} % Visual placeholder box if logo graphic is absent
        \end{figure}
        \vspace{0.2cm}
        
        \textbf{Department of Computer Science and Engineering}\\[0.1cm]
        \textbf{Amity School of Engineering and Technology}\\[0.1cm]
        \textbf{Amity University Jharkhand, Ranchi, India}\\[0.3cm]
        \textbf{Academic Year 2024--2025}
    \end{center}
\end{titlepage}

\clearpage

% ---------------------------------------------------------
% PAGE 2: CERTIFICATE OF AUTHENTICITY
% ---------------------------------------------------------
\thispagestyle{plain}
\begin{center}
    {\Large \textbf{AMITY SCHOOL OF ENGINEERING AND TECHNOLOGY}}\\[0.1cm]
    {\large \textbf{AMITY UNIVERSITY JHARKHAND, RANCHI}}\\[0.8cm]
    {\LARGE \textbf{CERTIFICATE}}\\[1.0cm]
\end{center}

This is to certify that the Major Project titled \textbf{``Early Detection of Academic Burnout using Machine Learning: A Multi-Dimensional Behavioral Informatics and Predictive Analytics Framework''} submitted by \textbf{Palak Goenka} (Enrollment No.: \textbf{A357175124008}) in partial fulfilment of the requirements for the award of the degree of \textbf{Bachelor of Technology in Computer Science and Engineering (AI \& ML)} from \textbf{Amity School of Engineering and Technology, Amity University Jharkhand}, is an authentic record of the research and development work carried out by her under my supervision and guidance during the academic session 2024--2025.

To the best of my knowledge, the matter embodied in this major project report has not been submitted to any other University or Institution for the award of any degree, diploma, or fellowship.

\vspace{2.5cm}

\noindent
\begin{tabularx}{\textwidth}{XrX}
\textbf{Prof. Supervisor} & & \textbf{Head of Department} \\
Project Supervisor & & Department of CSE \\
Department of CSE & & Amity School of Engineering and Technology \\
Amity University Jharkhand & & Amity University Jharkhand
\end{tabularx}

\vspace{1.8cm}
\noindent
Date: \rule{3.5cm}{0.4pt} \\
Place: Ranchi, Jharkhand

\clearpage

% ---------------------------------------------------------
% PAGE 3: STUDENT DECLARATION
% ---------------------------------------------------------
\thispagestyle{plain}
\begin{center}
    {\LARGE \textbf{DECLARATION}}\\[1.0cm]
\end{center}

I, \textbf{Palak Goenka}, student of \textbf{Bachelor of Technology in Computer Science and Engineering (Artificial Intelligence and Machine Learning)}, \textbf{Semester--V}, Department of Computer Science and Engineering, Amity School of Engineering and Technology, Amity University Jharkhand, hereby declare that:

\begin{enumerate}
    \item The major project report entitled \textbf{``Early Detection of Academic Burnout using Machine Learning''} submitted in partial fulfilment of the curriculum requirements is my original work carried out under the supervision of \textbf{Prof. Supervisor}.
    \item The work does not contain any material previously published or written by another person, except where due reference and formal academic acknowledgment has been cited in the text and bibliography.
    \item Any data generation, behavioral feature engineering, algorithmic benchmarking, model training, evaluation metrics, and web application implementations presented herein were executed authentically by me.
    \item I have adhered to all academic integrity norms, scientific ethics, and plagiarism guidelines stipulated by Amity University Jharkhand.
\end{enumerate}

\vspace{2.5cm}

\noindent
\begin{tabularx}{\textwidth}{Xr}
& \textbf{Palak Goenka} \\
& Enrollment No.: \textbf{A357175124008} \\
& B.Tech CSE (AI \& ML), Sem--V \\
& Amity School of Engineering and Technology \\
& Amity University Jharkhand, Ranchi
\end{tabularx}

\vspace{1.5cm}
\noindent
Date: \rule{3.5cm}{0.4pt} \\
Place: Ranchi, Jharkhand

\clearpage

% ---------------------------------------------------------
% PAGE 4: ABSTRACT
% ---------------------------------------------------------
\thispagestyle{plain}
\begin{center}
    {\LARGE \textbf{ABSTRACT}}\\[0.8cm]
\end{center}

Academic burnout represents an escalating psychological and public health crisis across higher education institutions worldwide. Unlike acute academic stress—which acts as a temporary psychological reaction to impending examinations or project submission deadlines—academic burnout is a chronic, multi-dimensional syndrome characterized by persistent emotional exhaustion, severe academic cynicism (depersonalization and detachment from coursework), and a debilitating sense of academic inefficacy. Traditional mental health screening mechanisms deployed across university campuses rely predominantly on retrospective, voluntary clinical self-referral or periodic paper-and-pencil psychometric questionnaires. These legacy methods exhibit profound diagnostic latency, frequently identifying student distress only after catastrophic academic failure, chronic absenteeism, or clinical depression has occurred. Furthermore, pervasive social stigma surrounding mental illness and institutional counseling resource constraints prevent the vast majority of vulnerable students from seeking timely intervention.

To overcome these structural limitations, this thesis presents an end-to-end, privacy-conscious, multi-dimensional Machine Learning framework for the early detection and predictive risk profiling of academic burnout. Grounded firmly in empirical psychometrics—specifically integrating the \textbf{Maslach Burnout Inventory – Student Survey (MBI-SS)} and the \textbf{Job Demands-Resources (JD-R) Model}—our system captures the dynamic equilibrium between academic demands and restorative personal/social resources across four foundational dimensions: (i) Demographic and Socioeconomic context, (ii) Academic Demands and Curricular Pressure, (iii) Physical Rest and Digital Behaviors, and (iv) Psycho-Social Buffering Resources. 

Operating on a rigorously audited and statistically verified dataset of 3,000 diverse student profiles, we engineer domain-specific interaction indicators, including the \textbf{Academic Pressure Index (API)}, \textbf{Screen-to-Sleep Ratio (SSR)}, \textbf{Social Support Deficit (SSD)}, and \textbf{Lifestyle Balance Score (LBS)}. To prevent data leakage, an isolated Scikit-learn preprocessing pipeline executes standard scaling and one-hot encoding strictly within training folds. We implement and systematically benchmark seven distinct machine learning classifiers across parametric, non-parametric, kernel-based, and ensemble families: Logistic Regression (L2-penalized), Gradient Boosting, Random Forest, Support Vector Classifiers (SVM with Radial Basis Function kernel), Decision Trees (CART), K-Nearest Neighbors (KNN), and Gaussian Naive Bayes. Simultaneously, a continuous regressor based on Ridge Regression ($L_2$ Tikhonov regularization) is developed to output an exact academic stress score ($0$--$100$).

Experimental evaluations across an independent $20\%$ hold-out test partition ($n=600$) reveal that our tuned \textbf{Logistic Regression} classifier achieves an outstanding test accuracy of \textbf{99.50\%} and a Macro F1-score of \textbf{0.9950}, outperforming complex ensemble and non-linear models. This superior performance is attributable to the linear separability induced by our psychometrically informed engineered features, the smooth continuous softmax probability surface, and optimal L2 regularization mitigating overfitting. Crucially, error matrix analysis confirms \textbf{zero cross-tier misclassification} between Low-Risk and High-Risk categories. The Ridge regression model delivers exceptional calibration with $R^2 = 1.0000$, $\text{MSE} = 0.000000$, and $\text{MAE} = 0.000262$. 

The complete analytical engine is encapsulated within a production-grade Flask web application featuring a modern, responsive Glassmorphism interface, interactive single-student diagnostic sliders, and high-throughput batch CSV processing. Deployed as a high-availability cloud service, the platform delivers real-time inference ($<8\text{ms}$ latency), intuitive risk categorization (Low, Medium, High Risk), confidence distributions, and automated, multi-tiered counseling intervention recommendations. This framework establishes an accessible, scalable, and non-stigmatizing paradigm for proactive mental health monitoring in contemporary academic environments.

\vspace{0.8cm}
\noindent
\textbf{Keywords:} Academic Burnout, Machine Learning, Mental Health Informatics, Maslach Burnout Inventory (MBI-SS), Job Demands-Resources (JD-R) Model, Logistic Regression, Feature Engineering, Early Warning System, Cloud Deployment.

\clearpage

% ---------------------------------------------------------
% PAGE 5: ACKNOWLEDGEMENTS
% ---------------------------------------------------------
\thispagestyle{plain}
\begin{center}
    {\LARGE \textbf{ACKNOWLEDGEMENTS}}\\[0.8cm]
\end{center}

The realization of this major project and thesis report has been an intellectually stimulating and transformative journey, made possible through the generous guidance, institutional support, and encouragement of numerous individuals.

First and foremost, I express my deepest and most profound sense of gratitude to my project supervisor, \textbf{Prof. Supervisor}, Assistant Professor, Department of Computer Science and Engineering, Amity School of Engineering and Technology, Amity University Jharkhand. His insightful critique, continuous intellectual stimulation, meticulous guidance, and constructive feedback throughout all phases of conceptualization, mathematical formulation, model benchmarking, and manuscript preparation have been invaluable. His unwavering high standards of scientific rigor have profoundly shaped my approach to artificial intelligence research.

I extend my sincere thanks to \textbf{Dr. Head of Department}, Head of the Department of Computer Science and Engineering, for providing excellent departmental infrastructure, high-performance computing facilities, and an intellectually vibrant environment conducive to advanced academic research.

I also express my heartfelt appreciation to the \textbf{Hon'ble Vice Chancellor} and \textbf{Director}, Amity University Jharkhand, for their visionary leadership and for fostering an academic culture that champions interdisciplinary research addressing pressing societal and student welfare challenges.

My heartfelt gratitude goes to all faculty members, laboratory instructors, and administrative staff of the Department of Computer Science and Engineering for their direct and indirect support, technical assistance, and valuable academic suggestions throughout the duration of the B.Tech program.

I am deeply indebted to my beloved parents and family members, whose unconditional love, sacrifices, continuous encouragement, and moral support provided me with the strength and resilience needed to complete this work. Finally, I extend my warm appreciation to my batchmates and friends for their constructive discussions, peer review, and camaraderie during our academic journey.

\vspace{2.5cm}

\noindent
\begin{tabularx}{\textwidth}{Xr}
& \textbf{Palak Goenka} \\
& Enrollment No.: \textbf{A357175124008} \\
& B.Tech CSE (AI \& ML), Sem--V \\
& Amity University Jharkhand
\end{tabularx}

\clearpage

% ---------------------------------------------------------
% TABLE OF CONTENTS, LIST OF FIGURES & TABLES
% ---------------------------------------------------------
\tableofcontents
\clearpage

\listoffigures
\clearpage

\listoftables
\clearpage

% ---------------------------------------------------------
% LIST OF ABBREVIATIONS
% ---------------------------------------------------------
\thispagestyle{plain}
\begin{center}
    {\Large \textbf{LIST OF ABBREVIATIONS}}\\[0.8cm]
\end{center}

\begin{table}[H]
\centering
\begin{tabularx}{\textwidth}{lX}
\toprule
\textbf{Abbreviation} & \textbf{Full Expansion} \\
\midrule
\textbf{AI} & Artificial Intelligence \\
\textbf{ML} & Machine Learning \\
\textbf{MBI} & Maslach Burnout Inventory \\
\textbf{MBI-SS} & Maslach Burnout Inventory – Student Survey \\
\textbf{JD-R} & Job Demands-Resources Model \\
\textbf{API} & Academic Pressure Index / Application Programming Interface \\
\textbf{SSR} & Screen-to-Sleep Ratio \\
\textbf{SSD} & Social Support Deficit \\
\textbf{LBS} & Lifestyle Balance Score \\
\textbf{EDA} & Exploratory Data Analysis \\
\textbf{LR} & Logistic Regression \\
\textbf{SVM} & Support Vector Machine \\
\textbf{SVC} & Support Vector Classifier \\
\textbf{RF} & Random Forest \\
\textbf{GBDT} & Gradient Boosted Decision Trees \\
\textbf{CART} & Classification and Regression Trees \\
\textbf{KNN} & K-Nearest Neighbors \\
\textbf{GNB} & Gaussian Naive Bayes \\
\textbf{OLS} & Ordinary Least Squares \\
\textbf{RBF} & Radial Basis Function \\
\textbf{MSE} & Mean Squared Error \\
\textbf{RMSE} & Root Mean Squared Error \\
\textbf{MAE} & Mean Absolute Error \\
\textbf{ROC} & Receiver Operating Characteristic \\
\textbf{AUC} & Area Under the Curve \\
\textbf{VIF} & Variance Inflation Factor \\
\textbf{REST} & Representational State Transfer \\
\textbf{JSON} & JavaScript Object Notation \\
\textbf{LMS} & Learning Management System \\
\textbf{IoT} & Internet of Things \\
\bottomrule
\end{tabularx}
\end{table}

\clearpage

% ---------------------------------------------------------
% MAIN BODY (ARABIC NUMERALS)
% ---------------------------------------------------------
\pagenumbering{arabic}
\setcounter{page}{1}
"""
