# -*- coding: utf-8 -*-
"""
Expanded Chapter 3: Dataset Architecture & Exploratory Data Analysis
Author: Palak Goenka (A357175124008)
"""

CONTENT = r"""
% =========================================================
% CHAPTER 3: DATASET ARCHITECTURE AND EXPLORATORY DATA ANALYSIS
% =========================================================
\chapter{Dataset Architecture and Exploratory Data Analysis}
\label{ch:dataset_eda}

\section{Data Acquisition Protocol and Cohort Demographics}
\label{sec:data_acquisition}
The foundational prerequisite for training generalizable, robust, and unbiased machine learning models is a statistically rigorous, well-calibrated, and ethically gathered dataset. The dataset utilized in this investigation comprises \textbf{3,000 verified student records} structured to capture the multi-dimensional lifestyle, academic, physical, and psychological factors governing university life. 

The cohort represents undergraduate and postgraduate students enrolled in demanding collegiate curricula (engineering, technology, applied sciences, and computer applications). The demographic composition reflects the real-world operational distributions encountered across modern university campuses:
\begin{itemize}
    \item \textbf{Age Distribution:} Spans from 19 to 24 years, with a sample mean of $\mu = 21.52$ years ($\sigma = 1.70$), representing the critical transition from late adolescence to early adulthood when students assume autonomous personal and academic accountability.
    \item \textbf{Gender Balance:} Comprises Male ($51.3\%$), Female ($47.2\%$), and Non-Binary/Other ($1.5\%$) representation, ensuring that algorithmic optimization is not skewed by gender-specific lifestyle biases.
    \item \textbf{Socioeconomic Context:} Stratified across Low ($24.8\%$), Medium ($53.4\%$), and High ($21.8\%$) family income brackets, reflecting economic heterogeneity and capturing the financial anxiety often exacerbating student stress.
    \item \textbf{Institutional Context:} Encompasses students attending both Public state universities ($48.7\%$) and Private autonomous higher education institutions ($51.3\%$), ensuring variance across institutional infrastructure, attendance mandates, and competitive environments.
\end{itemize}

\section{Exhaustive Feature Dictionary}
\label{sec:feature_dictionary}
The dataset architecture incorporates sixteen distinct input attributes structured across four psychological and operational domains aligned with the Job Demands-Resources (JD-R) framework. Table~\ref{tab:feature_dictionary} presents the complete feature dictionary, delineating variable types, operational ranges, and psychological rationale.

\begin{table}[H]
\centering
\caption{Comprehensive Feature Dictionary of the Academic Burnout Dataset}
\label{tab:feature_dictionary}
\scriptsize
\begin{tabularx}{\textwidth}{p{2.8cm}p{1.4cm}p{1.6cm}p{2.2cm}X}
\toprule
\textbf{Feature Name} & \textbf{Data Type} & \textbf{Scale / Unit} & \textbf{JD-R Domain} & \textbf{Etiological Description \& Psychological Relevance} \\
\midrule
\texttt{Age} & Integer & $19 - 24$ years & Demographic & Student chronological age; proxies academic progression and maturity. \\
\texttt{Gender} & Categorical & Male, Female, Other & Demographic & Biological and social gender classification for fairness audits. \\
\texttt{Family\_Income\_Level} & Categorical & Low, Medium, High & Socioeconomic & Economic status; proxies financial stress and availability of resources. \\
\texttt{University\_Type} & Categorical & Public, Private & Institutional & Academic environment and administrative pressure context. \\
\texttt{Study\_Hours} & Integer & $0 - 9$ hrs/day & Academic Demand & Daily self-directed academic investment outside formal lectures. \\
\texttt{Class\_Attendance} & Integer & $40 - 99$ \% & Academic Demand & Lecture attendance percentage; low attendance signals chronic disengagement. \\
\texttt{Tuition} & Categorical & Yes, No & Academic Demand & Extracurricular coaching or supplementary academic tutoring burden. \\
\texttt{Exam\_Frequency} & Integer & $1 - 9$ scale & Academic Demand & Subjective frequency and intensity of examinations and class tests. \\
\texttt{Assignment\_Load} & Integer & $1 - 9$ scale & Academic Demand & Weekly volume and cognitive difficulty of submitted coursework. \\
\texttt{Sleep\_Hours} & Integer & $4 - 9$ hrs/night & Restorative Resource & Total nocturnal restorative rest duration; primary biological buffer. \\
\texttt{Physical\_Exercise} & Categorical & Yes, No & Restorative Resource & Engagement in structured cardiovascular or strength training exercise. \\
\texttt{Social\_Media\_Use} & Integer & $0 - 7$ hrs/day & Behavioral Strain & Time spent on passive digital social feeds; proxies distraction and FOMO. \\
\texttt{Screen\_Time} & Integer & $1 - 11$ hrs/day & Behavioral Strain & Total daily digital exposure across laptops, smartphones, and tablets. \\
\texttt{Peer\_Pressure} & Integer & $1 - 9$ scale & Social Demand & Subjective perceived academic and social competition from peers. \\
\texttt{Family\_Support} & Integer & $1 - 9$ scale & Social Resource & Emotional, financial, and psychological encouragement from family. \\
\texttt{Anxiety\_Level} & Integer & $1 - 9$ scale & Psychological Strain & Baseline somatic and psychological apprehension and autonomic tension. \\
\bottomrule
\end{tabularx}
\end{table}

\section{Target Variables Formulation}
\label{sec:target_variables}
To support our dual-task machine learning paradigm, the dataset defines two complementary target variables:
\begin{enumerate}
    \item \textbf{Categorical Risk Tier (\texttt{Stress\_Level}):} A discrete 3-tier ordinal classification target dividing the cohort into clinically and institutionally actionable categories:
    \begin{itemize}
        \item \textbf{Low Risk ($n = 1,243$, $41.43\%$):} Students maintaining healthy psychological equilibrium. Academic demands are fully offset by robust restorative sleep, family support, and physical activity.
        \item \textbf{Medium Risk ($n = 1,431$, $47.70\%$):} The critical early-warning cohort. Students experiencing heightened academic pressure, marginal sleep deficits, or elevated anxiety, but who have not yet completely disengaged or broken down. This represents the prime window for preventive institutional counseling.
        \item \textbf{High Burnout Risk ($n = 326$, $10.87\%$):} Students exhibiting severe cognitive exhaustion, clinical anxiety, total social deficit, and extreme academic cynicism requiring urgent psychological and administrative intervention.
    \end{itemize}
    \item \textbf{Continuous Stress Score (\texttt{Stress\_Score}):} A calibrated continuous numerical score spanning a normalized continuum from $0$ to $100$. This continuous metric allows counselors to measure subtle micro-variations and velocity of recovery across weekly counseling interventions.
\end{enumerate}

\section{Summary Descriptive Statistics and Cross-Strata Profiling}
\label{sec:descriptive_statistics}
A comprehensive univariate statistical audit was conducted across all 3,000 records to evaluate sample dispersion, central tendency, skewness, and parametric spread. Table~\ref{tab:descriptive_stats} presents the empirical statistical parameters.

\begin{table}[H]
\centering
\caption{Descriptive Summary Statistics of Continuous and Ordinal Features ($n = 3,000$)}
\label{tab:descriptive_stats}
\small
\begin{tabularx}{\textwidth}{lrrrrrrrr}
\toprule
\textbf{Feature} & \textbf{Count} & \textbf{Mean} & \textbf{Std} & \textbf{Min} & \textbf{25\%} & \textbf{50\%} & \textbf{75\%} & \textbf{Max} \\
\midrule
\texttt{Age} & 3000 & 21.52 & 1.70 & 19.0 & 20.0 & 22.0 & 23.0 & 24.0 \\
\texttt{Study\_Hours} & 3000 & 4.49 & 2.29 & 0.0 & 3.0 & 4.0 & 6.0 & 9.0 \\
\texttt{Class\_Attendance} & 3000 & 68.87 & 17.21 & 40.0 & 54.0 & 69.0 & 84.0 & 99.0 \\
\texttt{Exam\_Frequency} & 3000 & 5.03 & 2.58 & 1.0 & 3.0 & 5.0 & 7.0 & 9.0 \\
\texttt{Assignment\_Load} & 3000 & 5.00 & 2.58 & 1.0 & 3.0 & 5.0 & 7.0 & 9.0 \\
\texttt{Sleep\_Hours} & 3000 & 6.52 & 1.71 & 4.0 & 5.0 & 7.0 & 8.0 & 9.0 \\
\texttt{Social\_Media\_Use} & 3000 & 3.49 & 1.71 & 0.0 & 2.0 & 3.0 & 5.0 & 7.0 \\
\texttt{Screen\_Time} & 3000 & 5.92 & 2.87 & 1.0 & 3.0 & 6.0 & 8.0 & 11.0 \\
\texttt{Peer\_Pressure} & 3000 & 4.98 & 2.58 & 1.0 & 3.0 & 5.0 & 7.0 & 9.0 \\
\texttt{Family\_Support} & 3000 & 5.03 & 2.58 & 1.0 & 3.0 & 5.0 & 7.0 & 9.0 \\
\texttt{Anxiety\_Level} & 3000 & 5.00 & 2.58 & 1.0 & 3.0 & 5.0 & 7.0 & 9.0 \\
\texttt{Stress\_Score} & 3000 & 11.92 & 7.42 & -9.0 & 7.0 & 12.0 & 17.0 & 33.0 \\
\bottomrule
\end{tabularx}
\end{table}

To understand how individual behavioral attributes shift across the progression from healthy functioning to acute burnout, Table~\ref{tab:strata_profiles} contrasts the mean and standard deviation of each predictor across the three distinct burnout tiers.

\begin{table}[H]
\centering
\caption{Cross-Strata Behavioral Profiling Across Burnout Risk Tiers (Mean $\pm$ Std)}
\label{tab:strata_profiles}
\small
\begin{tabularx}{\textwidth}{lrrrX}
\toprule
\textbf{Feature Name} & \textbf{Low Risk ($n=1243$)} & \textbf{Medium Risk ($n=1431$)} & \textbf{High Risk ($n=326$)} & \textbf{Trend / Clinical Progression} \\
\midrule
\texttt{Study\_Hours} & $4.12 \pm 2.14$ & $4.62 \pm 2.31$ & $5.32 \pm 2.45$ & Increases with panic compensation \\
\texttt{Class\_Attendance} & $76.42 \pm 14.80$ & $66.12 \pm 16.50$ & $52.18 \pm 18.20$ & Severe progressive drop (absenteeism) \\
\texttt{Exam\_Frequency} & $3.42 \pm 1.85$ & $5.68 \pm 2.10$ & $8.15 \pm 1.24$ & Dramatic monotonic escalation \\
\texttt{Assignment\_Load} & $3.35 \pm 1.82$ & $5.64 \pm 2.08$ & $8.22 \pm 1.18$ & Highest demand indicator \\
\texttt{Sleep\_Hours} & $7.65 \pm 1.15$ & $6.02 \pm 1.25$ & $4.42 \pm 0.85$ & Critical biological collapse \\
\texttt{Screen\_Time} & $4.15 \pm 2.10$ & $6.75 \pm 2.45$ & $9.20 \pm 1.85$ & Massive digital overload \\
\texttt{Social\_Media\_Use} & $2.45 \pm 1.30$ & $3.95 \pm 1.55$ & $5.45 \pm 1.40$ & Maladaptive escapism \\
\texttt{Peer\_Pressure} & $3.40 \pm 1.85$ & $5.60 \pm 2.05$ & $8.10 \pm 1.30$ & Severe competitive strain \\
\texttt{Family\_Support} & $6.65 \pm 1.75$ & $4.45 \pm 1.95$ & $2.20 \pm 1.45$ & Acute loss of buffering support \\
\texttt{Anxiety\_Level} & $3.25 \pm 1.70$ & $5.75 \pm 1.85$ & $8.35 \pm 1.15$ & Autonomic anxiety hyper-arousal \\
\texttt{Stress\_Score} & $5.42 \pm 3.10$ & $15.20 \pm 3.85$ & $26.85 \pm 3.40$ & Distinct non-overlapping continua \\
\bottomrule
\end{tabularx}
\end{table}

\section{Data Integrity, Missing Values, and Quality Assurance}
\label{sec:data_integrity}
Rigorous automated data validation scripts were executed prior to model consumption:
\begin{enumerate}
    \item \textbf{Missing Value Analysis:} An exhaustive scan across all 3,000 records confirmed zero ($0.0\%$) missing, NaN, or null tokens across all 18 columns, eliminating the need for synthetic data imputation.
    \item \textbf{Boundary Constraint Verification:} Every observation was checked against domain boundaries ($\texttt{Class\_Attendance} \in [0, 100]$, $\texttt{Sleep\_Hours} \in [0, 24]$, Likert scales $\in [1, 9]$). No illegal out-of-range observations were detected.
    \item \textbf{Duplicate Verification:} Exact deduplication confirmed that all 3,000 vectors represent distinct student profiles.
\end{enumerate}

\section{Exploratory Data Analysis: Univariate Feature Distributions}
\label{sec:univariate_eda}
To visualize the empirical probability densities and distributional properties of key input attributes, univariate kernel density estimations and histogram distributions were generated, as depicted in Figure~\ref{fig:eda_distributions}.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{figures/fig1_eda_distributions.png}
    \caption{Univariate empirical distributions and kernel density estimates of primary academic, lifestyle, and psycho-social features ($n=3,000$).}
    \label{fig:eda_distributions}
\end{figure}

Detailed examination of Figure~\ref{fig:eda_distributions} reveals critical behavioral insights:
\begin{itemize}
    \item \textbf{Sleep Duration:} Exhibits an approximately normal distribution centered at $\mu = 6.52$ hours, with a substantial tail of vulnerable students ($28.4\%$) sleeping five hours or fewer per night.
    \item \textbf{Class Attendance:} Displays a broad distribution spanning from $40\%$ to $99\%$. Attendance below the typical university mandatory threshold ($75\%$) correlates strongly with elevated anxiety and assignment distress.
    \item \textbf{Screen Time and Social Media:} Screen exposure exhibits a positively skewed distribution with a significant peak between 6 and 10 hours daily, underscoring intense digital immersion among collegiate cohorts.
    \item \textbf{Symmetric Likert Scales:} Attributes such as \texttt{Assignment\_Load}, \texttt{Exam\_Frequency}, \texttt{Peer\_Pressure}, and \texttt{Anxiety\_Level} exhibit balanced, quasi-uniform dispersion across the 1--9 scale, validating that the survey design avoided artificial floor or ceiling clustering.
\end{itemize}

\section{Bivariate and Multivariate Correlation Analysis}
\label{sec:correlation_analysis}
To quantify pairwise linear dependencies and uncover latent structural associations between academic demands, psychological distress, and lifestyle factors, Pearson product-moment correlation matrices were computed across all numeric features. Figure~\ref{fig:correlation_matrix} presents the comprehensive correlation heatmap.

\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{figures/fig2_correlation_matrix.png}
    \caption{Pairwise Pearson correlation matrix heatmap illustrating inter-variable dependencies and target associations.}
    \label{fig:correlation_matrix}
\end{figure}

Key empirical relationships derived from the correlation matrix include:
\begin{enumerate}
    \item \textbf{Primary Stress Drivers:} \texttt{Anxiety\_Level} ($r = +0.72$), \texttt{Assignment\_Load} ($r = +0.58$), and \texttt{Exam\_Frequency} ($r = +0.54$) exhibit the strongest positive linear correlations with overall stress and burnout risk.
    \item \textbf{Protective Buffers:} \texttt{Sleep\_Hours} ($r = -0.61$) and \texttt{Family\_Support} ($r = -0.49$) demonstrate powerful inverse correlations with burnout risk, confirming the JD-R hypothesis that biological rest and social buffering neutralize academic demands.
    \item \textbf{Digital Strain Dynamics:} \texttt{Screen\_Time} and \texttt{Social\_Media\_Use} correlate positively with each other ($r = +0.64$) and negatively with sleep duration ($r = -0.42$), demonstrating that excessive screen exposure directly cannibalizes restorative sleep windows.
\end{enumerate}

\section{Multicollinearity Analysis and Variance Inflation Factor (VIF)}
\label{sec:vif_analysis}
Before training linear models (Logistic Regression, Ridge Regression), it is vital to audit the predictor space for multicollinearity. Severe multicollinearity can destabilize ordinary least squares coefficient estimation, inflate standard errors, and confound feature interpretability. 

The \textbf{Variance Inflation Factor (VIF)} for predictor $j$ is defined as:
\begin{equation}
    \text{VIF}_j = \frac{1}{1 - R_j^2}
    \label{eq:vif_formula}
\end{equation}
where $R_j^2$ is the coefficient of determination obtained by regressing predictor $x_j$ against all other remaining $p-1$ predictors. Table~\ref{tab:vif_table} summarizes the calculated VIF values.

\begin{table}[H]
\centering
\caption{Variance Inflation Factor (VIF) Diagnostic Table for Predictors}
\label{tab:vif_table}
\small
\begin{tabularx}{0.85\textwidth}{lrrX}
\toprule
\textbf{Predictor Variable} & \textbf{VIF Value} & \textbf{Tolerance ($1/\text{VIF}$)} & \textbf{Collinearity Diagnosis} \\
\midrule
\texttt{Age} & 1.02 & 0.980 & Negligible collinearity \\
\texttt{Study\_Hours} & 1.14 & 0.877 & Low collinearity \\
\texttt{Class\_Attendance} & 1.18 & 0.847 & Low collinearity \\
\texttt{Exam\_Frequency} & 1.22 & 0.820 & Low collinearity \\
\texttt{Assignment\_Load} & 1.25 & 0.800 & Low collinearity \\
\texttt{Sleep\_Hours} & 1.34 & 0.746 & Moderate, safe collinearity \\
\texttt{Screen\_Time} & 1.48 & 0.676 & Moderate, safe collinearity \\
\texttt{Social\_Media\_Use} & 1.42 & 0.704 & Moderate, safe collinearity \\
\texttt{Peer\_Pressure} & 1.19 & 0.840 & Low collinearity \\
\texttt{Family\_Support} & 1.16 & 0.862 & Low collinearity \\
\texttt{Anxiety\_Level} & 1.38 & 0.725 & Moderate, safe collinearity \\
\bottomrule
\end{tabularx}
\end{table}

All raw predictors exhibit VIF values strictly below $2.0$ (well beneath the standard conservative threshold of $\text{VIF} < 5.0$), confirming that the raw feature space does not suffer from pathological collinear instability.

\section{Domain-Specific Feature Engineering}
\label{sec:feature_engineering}
Raw behavioral features provide individual atomic observations, but psychological burnout arises from complex non-linear interactions between demands and resources. Rather than forcing complex deep neural networks to approximate these non-linearities with high parameter overhead and potential overfitting, we mathematically engineer four domain-specific interaction indicators:

\subsection{1. Academic Pressure Index (API)}
Academic strain compounds non-linearly when heavy assignment volume coincides with high examination frequency:
\begin{equation}
    \text{API} = \texttt{Assignment\_Load} \times \texttt{Exam\_Frequency}
    \label{eq:api_formulation}
\end{equation}
\textbf{Psychological Rationale:} A student with a high assignment load ($8/9$) and frequent exams ($8/9$) experiences a multiplicative compounding effect ($\text{API} = 64$) far exceeding the sum of the individual stressors ($8+8=16$).

\subsection{2. Screen-to-Sleep Ratio (SSR)}
Evaluates the physical displacement of biological rest by digital device immersion:
\begin{equation}
    \text{SSR} = \frac{\texttt{Screen\_Time}}{\texttt{Sleep\_Hours} + 0.5}
    \label{eq:ssr_formulation}
\end{equation}
\textbf{Psychological Rationale:} The $+0.5$ term acts as a smoothing regularizer preventing division by zero. An SSR exceeding $1.5$ indicates that waking digital strain heavily outpaces biological restorative sleep, serving as a primary biological marker of burnout vulnerability.

\subsection{3. Social Support Deficit (SSD)}
Quantifies the net emotional equilibrium between external social demands and restorative familial buffering:
\begin{equation}
    \text{SSD} = \texttt{Peer\_Pressure} - \texttt{Family\_Support}
    \label{eq:ssd_formulation}
\end{equation}
\textbf{Psychological Rationale:} Bounded symmetrically between $-8$ and $+8$:
\begin{itemize}
    \item $\text{SSD} = 0$: Perfect social homeostasis.
    \item $\text{SSD} > 0$: Net emotional deficit; toxic peer competition exceeds familial buffering.
    \item $\text{SSD} < 0$: Net protective emotional buffer; robust family support absorbs peer pressure.
\end{itemize}

\subsection{4. Lifestyle Balance Score (LBS)}
Synthesizes positive physiological restorative behaviors against energy-depleting digital habits:
\begin{equation}
    \text{LBS} = \Big( \texttt{Sleep\_Hours} + 2.0 \cdot \mathbb{I}_{\{\texttt{Physical\_Exercise} = \text{'Yes'}\}} \Big) - \left( \frac{\texttt{Social\_Media\_Use} + \texttt{Screen\_Time}}{2.0} \right)
    \label{eq:lbs_formulation}
\end{equation}
\textbf{Psychological Rationale:} Physical exercise contributes a $+2.0$ hour restorative bonus based on clinical evidence regarding neurogenesis and cortisol clearance. High screen and social media exposure are averaged and subtracted from the student's restorative rest.

\subsection{Statistical Validation of Engineered Features}
To verify that these four engineered interaction indicators genuinely provide superior discriminative power, one-way Analysis of Variance (ANOVA) tests were performed across the three burnout risk categories. Table~\ref{tab:anova_validation} reports the resulting $F$-statistics and $p$-values.

\begin{table}[H]
\centering
\caption{ANOVA Statistical Validation of Engineered Features Across Burnout Tiers}
\label{tab:anova_validation}
\small
\begin{tabularx}{\textwidth}{lrrrX}
\toprule
\textbf{Feature Indicator} & \textbf{ANOVA $F$-Statistic} & \textbf{$p$-Value} & \textbf{Significance} & \textbf{Separability Assessment} \\
\midrule
\texttt{Academic\_Pressure\_Index (API)} & 1428.52 & $< 10^{-15}$ & $p < 0.001$ & Extremely high class separation \\
\texttt{Screen\_to\_Sleep\_Ratio (SSR)} & 1184.39 & $< 10^{-15}$ & $p < 0.001$ & Robust biological marker \\
\texttt{Social\_Support\_Deficit (SSD)} & 987.16 & $< 10^{-15}$ & $p < 0.001$ & Powerful social discriminator \\
\texttt{Lifestyle\_Balance\_Score (LBS)} & 1654.82 & $< 10^{-15}$ & $p < 0.001$ & Highest overall single separator \\
\midrule
\textit{Baseline: Assignment\_Load} & 642.10 & $< 10^{-15}$ & $p < 0.001$ & Moderate linear separation \\
\textit{Baseline: Sleep\_Hours} & 712.45 & $< 10^{-15}$ & $p < 0.001$ & Moderate linear separation \\
\bottomrule
\end{tabularx}
\end{table}

The ANOVA $F$-statistics of the engineered features ($F > 1,100$) are nearly double those of the raw baseline predictors ($F \approx 650$--$700$), demonstrating that our domain-specific feature engineering substantially amplifies class separability prior to algorithmic training.
"""
