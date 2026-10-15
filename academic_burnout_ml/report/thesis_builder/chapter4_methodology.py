# -*- coding: utf-8 -*-
"""
Expanded Chapter 4: Methodology & Mathematical Formulations
Author: Palak Goenka (A357175124008)
"""

CONTENT = r"""
% =========================================================
% CHAPTER 4: METHODOLOGY AND MATHEMATICAL FORMULATIONS
% =========================================================
\chapter{System Architecture and Methodology}
\label{ch:methodology}

\section{End-to-End System Architecture}
\label{sec:system_architecture}
The proposed academic burnout early warning system is engineered as an integrated, multi-stage machine learning pipeline. Figure~\ref{fig:methodology_flow} illustrates the end-to-end operational architecture, tracing the transformation of raw behavioral data through feature synthesis, isolated preprocessing, dual-model inference, and real-time cloud delivery.

\begin{figure}[H]
\centering
\begin{tabular}{|c|}
\hline
\textbf{\large Phase 1: Multi-Dimensional Behavioral Data Ingestion} \\
$\left[ \text{Demographics} \;\vert\; \text{Academic Demands} \;\vert\; \text{Restorative Habits} \;\vert\; \text{Psycho-Social Buffers} \right]$ \\
\hline
$\Downarrow$ \\
\hline
\textbf{\large Phase 2: Domain-Specific Feature Engineering} \\
$\text{Compute: } \text{API} = \text{Load} \times \text{Exams}, \quad \text{SSR} = \frac{\text{Screen}}{\text{Sleep}+0.5}, \quad \text{SSD} = \text{Peer} - \text{Family}, \quad \text{LBS} = (\text{Sleep}+\text{Ex}) - \frac{\text{Media}+\text{Screen}}{2}$ \\
\hline
$\Downarrow$ \\
\hline
\textbf{\large Phase 3: Isolated Preprocessing Pipeline (Data Leakage Guard)} \\
$\text{Stratified Train/Test Split } (80/20) \;\longrightarrow\; \text{Fit Pipeline strictly on } \mathcal{D}_{\text{train}}$ \\
$\bullet \text{ StandardScaler on Continuous Features: } z = (x - \mu_{\text{train}}) / \sigma_{\text{train}}$ \\
$\bullet \text{ OneHotEncoder on Categorical Features: Gender, Tuition, Income, University}$ \\
\hline
$\Downarrow$ \\
\hline
\textbf{\large Phase 4: Dual-Task Algorithmic Inference Engines} \\
\begin{tabular}{cc}
\textbf{Task A: Multi-Class Triage Classifier} & \textbf{Task B: Continuous Stress Regressor} \\
\textit{Multinomial Logistic Regression (L2)} & \textit{Ridge Regression (L2 Tikhonov)} \\
$\hat{y} \in \{ \text{Low, Medium, High Risk} \}$ & $\hat{s} = \mathbf{w}^T \mathbf{x} + b \in [0, 100]$ \\
$\text{Outputs: Class Probabilities } P(Y=k \mid \mathbf{x})$ & $\text{Outputs: Calibrated Stress Score}$ \\
\end{tabular} \\
\hline
$\Downarrow$ \\
\hline
\textbf{\large Phase 5: Production Cloud Web Deployment (Vercel / Flask)} \\
$\text{Real-Time Single Student Evaluation } \;\vert\; \text{High-Throughput Batch CSV Screening}$ \\
$\text{Multi-Tiered Automated Counseling Recommendation Engine}$ \\
\hline
\end{tabular}
\caption{End-to-end architectural workflow of the Academic Burnout Early Detection Platform}
\label{fig:methodology_flow}
\end{figure}

\section{Data Preprocessing Pipeline and Leakage Prevention}
\label{sec:preprocessing_pipeline}
A primary methodological deficiency in published educational data mining literature is \emph{data leakage}—the inadvertent contamination of training data with statistical properties of the test evaluation fold. When z-score normalization ($\mu, \sigma$) or target encoding is computed over the entire unpartitioned dataset prior to splitting, the model gains unearned prior knowledge about the test distribution, yielding artificially inflated, brittle performance metrics.

\subsection{Stratified Train-Test Splitting}
To guarantee methodological integrity:
\begin{enumerate}
    \item The complete dataset $\mathcal{D} = \{(\mathbf{x}_i, y_i, s_i)\}_{i=1}^{3000}$ was partitioned using stratified random sampling based on the target class labels $y_i \in \{\text{Low}, \text{Medium}, \text{High}\}$.
    \item Exactly $80\%$ of the data ($n_{\text{train}} = 2,400$) was allocated to the training corpus $\mathcal{D}_{\text{train}}$, while $20\%$ ($n_{\text{test}} = 600$) was strictly sequestered as an untouched hold-out test corpus $\mathcal{D}_{\text{test}}$.
    \item Stratification ensured identical class frequency ratios across both splits ($41.4\%$ Low, $47.7\%$ Medium, $10.9\%$ High).
\end{enumerate}

\subsection{Encapsulated ColumnTransformer Preprocessing}
All feature transformations were packaged within an immutable Scikit-learn \texttt{Pipeline} and \texttt{ColumnTransformer}:
\begin{itemize}
    \item \textbf{Continuous Feature Standardization:} For continuous and Likert predictors ($\mathbf{x}_{\text{num}}$), the standard scaler was fitted \emph{strictly on $\mathcal{D}_{\text{train}}$}:
    \begin{equation}
        \mu_j = \frac{1}{N_{\text{train}}} \sum_{i=1}^{N_{\text{train}}} x_{ij}, \qquad \sigma_j = \sqrt{\frac{1}{N_{\text{train}}} \sum_{i=1}^{N_{\text{train}}} (x_{ij} - \mu_j)^2}
    \end{equation}
    Transformation of test vectors used only these frozen training parameters:
    \begin{equation}
        \tilde{x}_{ij}^{\text{test}} = \frac{x_{ij}^{\text{test}} - \mu_j}{\sigma_j}
    \end{equation}
    \item \textbf{Categorical Encoding:} Categorical attributes (\texttt{Gender}, \texttt{Tuition}, \texttt{Family\_Income\_Level}, \texttt{University\_Type}) were transformed using One-Hot Encoding with parameter \texttt{handle\_unknown='ignore'}, mapping categorical tokens into orthogonal binary indicator vectors.
\end{itemize}

\section{Mathematical Formulations of Benchmarked Classifiers}
\label{sec:classifier_formulations}
To systematically evaluate the decision landscape, seven distinct classification algorithms spanning parametric, non-parametric, margin-based, and ensemble paradigms were formulated, trained, and benchmarked.

\subsection{1. Multinomial Logistic Regression (L2-Regularized)}
Logistic Regression models the posterior probabilities of the $K=3$ burnout classes via the softmax transformation:
\begin{equation}
    P(Y = k \mid \mathbf{x}) = \frac{\exp(\mathbf{w}_k^T \mathbf{x} + b_k)}{\sum_{j=1}^K \exp(\mathbf{w}_j^T \mathbf{x} + b_j)}, \quad k \in \{1, 2, 3\}
    \label{eq:softmax_formulation}
\end{equation}
where $\mathbf{w}_k \in \mathbb{R}^d$ and $b_k \in \mathbb{R}$ represent the weight vector and bias for class $k$. The model parameters are optimized by minimizing the multi-class cross-entropy loss augmented with an $L_2$ Tikhonov regularization penalty:
\begin{equation}
    \mathcal{J}_{\text{LogReg}}(\mathbf{W}) = -\frac{1}{N} \sum_{i=1}^N \sum_{k=1}^K y_{ik} \log P(Y = k \mid \mathbf{x}_i) + \frac{\lambda}{2} \sum_{k=1}^K \|\mathbf{w}_k\|_2^2
    \label{eq:logreg_loss}
\end{equation}
where $y_{ik} \in \{0, 1\}$ is the one-hot indicator of true class membership, and $\lambda = 1/C$ dictates regularization strength. 

\subsubsection{Gradient and Hessian Derivation}
The gradient of the regularized objective with respect to the weight vector of class $k$ is given by:
\begin{equation}
    \nabla_{\mathbf{w}_k} \mathcal{J} = \frac{1}{N} \sum_{i=1}^N \Big( P(Y = k \mid \mathbf{x}_i) - y_{ik} \Big) \mathbf{x}_i + \lambda \mathbf{w}_k
\end{equation}
The corresponding Hessian matrix $\mathbf{H}_{kj} = \frac{\partial^2 \mathcal{J}}{\partial \mathbf{w}_k \partial \mathbf{w}_j^T}$ is positive semi-definite:
\begin{equation}
    \mathbf{H}_{kk} = \frac{1}{N} \sum_{i=1}^N P(Y = k \mid \mathbf{x}_i)\Big(1 - P(Y = k \mid \mathbf{x}_i)\Big) \mathbf{x}_i \mathbf{x}_i^T + \lambda \mathbf{I}
\end{equation}
Guaranteeing that the objective function is strictly convex with a unique global minimum. Optimization was executed using the quasi-Newton \textbf{L-BFGS} (Limited-memory Broyden-Fletcher-Goldfarb-Shanno) algorithm with a convergence tolerance of $\epsilon = 10^{-4}$ and maximum iterations $T = 1,000$.

\subsection{2. Support Vector Classification (SVC with RBF Kernel)}
Support Vector Machines construct optimal separating hyperplanes maximizing the geometric margin between classes in a transformed Hilbert feature space $\Phi(\mathbf{x})$. For multi-class triage, the one-vs-rest (OvR) formulation solves the following primal optimization problem:
\begin{equation}
    \min_{\mathbf{w}_k, b_k, \boldsymbol{\xi}} \frac{1}{2} \|\mathbf{w}_k\|_2^2 + C \sum_{i=1}^N \xi_{ik}
\end{equation}
subject to the constraints:
\begin{equation}
    y_{ik} (\mathbf{w}_k^T \Phi(\mathbf{x}_i) + b_k) \ge 1 - \xi_{ik}, \quad \xi_{ik} \ge 0, \quad \forall i \in \{1, \dots, N\}
\end{equation}
where $\xi_{ik}$ are slack variables permitting margin violations for non-linearly separable instances. We deploy the non-linear \textbf{Radial Basis Function (RBF) Kernel}:
\begin{equation}
    K(\mathbf{x}, \mathbf{x}') = \exp\left( -\gamma \|\mathbf{x} - \mathbf{x}'\|_2^2 \right)
    \label{eq:rbf_kernel}
\end{equation}
where $\gamma = \frac{1}{d \cdot \text{Var}(\mathbf{X})}$. The dual optimization is solved via Sequential Minimal Optimization (SMO) with penalty parameter $C = 1.0$.

\subsection{3. Decision Tree Classifier (CART)}
Classification and Regression Trees (CART) construct a binary recursive partitioning tree. At each internal node $t$, the algorithm selects the feature $j$ and split threshold $\theta$ that maximizes the reduction in \textbf{Gini Impurity} $I_G(t)$:
\begin{equation}
    I_G(t) = 1 - \sum_{k=1}^K p(k \mid t)^2
    \label{eq:gini_impurity}
\end{equation}
where $p(k \mid t)$ is the empirical proportion of class $k$ instances present at node $t$. The split criterion seeks:
\begin{equation}
    \Delta I_G(t, j, \theta) = I_G(t) - \frac{N_L}{N_t} I_G(t_L) - \frac{N_R}{N_t} I_G(t_R)
\end{equation}
To prevent pathological memorization, tree depth was regularized with $\text{max\_depth} = 10$ and $\text{min\_samples\_split} = 5$.

\subsection{4. Random Forest Classifier}
Random Forest operates as an ensemble of $B$ decorrelated decision trees $\{T_b\}_{b=1}^B$ constructed via \textbf{bootstrap aggregating (bagging)} and random feature subspace projection:
\begin{enumerate}
    \item For each tree $b \in \{1, \dots, B\}$, draw a bootstrap sample $\mathcal{D}_b$ of size $N$ with replacement from $\mathcal{D}_{\text{train}}$.
    \item At each node split, randomly sample a candidate feature subset of size $m = \lfloor \sqrt{d} \rfloor$ rather than the full feature set $d$.
    \item Grow tree $T_b$ to terminal depth without pruning.
\end{enumerate}
The variance of the averaged ensemble prediction $\bar{f}(\mathbf{x}) = \frac{1}{B} \sum_{b=1}^B T_b(\mathbf{x})$ is governed by Breiman's theorem:
\begin{equation}
    \text{Var}(\bar{f}) = \rho \sigma^2 + \frac{1 - \rho}{B} \sigma^2
\end{equation}
where $\sigma^2$ is the individual tree variance, and $\rho$ is the pairwise correlation between trees. By randomizing feature selection at each split, Random Forest forces $\rho \to 0$, driving ensemble variance down dramatically as $B \to \infty$.

\subsection{5. Gradient Boosted Decision Trees (GBDT)}
Gradient Boosting constructs an additive predictive model in a forward stagewise manner:
\begin{equation}
    F_M(\mathbf{x}) = \sum_{m=1}^M \eta h_m(\mathbf{x})
\end{equation}
where $h_m(\mathbf{x})$ are shallow regression trees fit to the pseudo-residuals of the multi-class log-loss:
\begin{equation}
    r_{ikm} = -\left[ \frac{\partial \mathcal{L}(y_i, F(\mathbf{x}_i))}{\partial F_k(\mathbf{x}_i)} \right]_{F = F_{m-1}} = y_{ik} - P(Y = k \mid \mathbf{x}_i)
\end{equation}
The shrinkage parameter (learning rate) was set to $\eta = 0.1$ across $M = 100$ sequential boosting iterations.

\subsection{6. K-Nearest Neighbors (KNN)}
KNN is an instance-based non-parametric classifier. Given query vector $\mathbf{x}$, the algorithm identifies the $k$ training points $\mathcal{N}_k(\mathbf{x})$ closest to $\mathbf{x}$ according to the Euclidean metric:
\begin{equation}
    d(\mathbf{x}, \mathbf{x}_i) = \|\mathbf{x} - \mathbf{x}_i\|_2 = \sqrt{\sum_{j=1}^d (x_j - x_{ij})^2}
\end{equation}
Class assignment is determined by uniform majority vote:
\begin{equation}
    \hat{y} = \arg\max_{c \in \{1, \dots, K\}} \sum_{i \in \mathcal{N}_k(\mathbf{x})} \mathbb{I}(y_i = c)
\end{equation}
We tuned the neighborhood size to $k = 5$ with standard Euclidean distance weighting.

\subsection{7. Gaussian Naive Bayes (GNB)}
GNB applies Bayes' theorem under the conditional independence assumption that all features $x_j$ are mutually independent given class $C_k$:
\begin{equation}
    P(Y = C_k \mid \mathbf{x}) \propto P(C_k) \prod_{j=1}^d P(x_j \mid C_k)
\end{equation}
Continuous features are modeled via class-conditional univariate Gaussian distributions:
\begin{equation}
    P(x_j \mid C_k) = \frac{1}{\sqrt{2\pi \sigma_{jk}^2}} \exp\left( -\frac{(x_j - \mu_{jk})^2}{2\sigma_{jk}^2} \right)
\end{equation}
where parameters $\mu_{jk}$ and $\sigma_{jk}^2$ are estimated using maximum likelihood on $\mathcal{D}_{\text{train}}$.

\section{Continuous Stress Regression Formulation (Ridge Regression)}
\label{sec:regression_formulation}
To estimate the continuous \texttt{Stress\_Score} ($0$--$100$), we implement \textbf{Ridge Regression} ($L_2$-penalized ordinary least squares). 

Given design matrix $\mathbf{X} \in \mathbb{R}^{N \times d}$ and target vector $\mathbf{s} \in \mathbb{R}^N$, the objective is to find weight vector $\mathbf{w} \in \mathbb{R}^d$ minimizing the penalized sum of squared residuals:
\begin{equation}
    \mathcal{J}_{\text{Ridge}}(\mathbf{w}) = \frac{1}{2N} \|\mathbf{s} - \mathbf{X}\mathbf{w}\|_2^2 + \frac{\alpha}{2} \|\mathbf{w}\|_2^2
    \label{eq:ridge_objective}
\end{equation}
where $\alpha > 0$ is the Tikhonov regularization hyperparameter.

\subsection{Analytical Closed-Form Derivation and SVD Spectral Analysis}
Taking the matrix derivative of $\mathcal{J}(\mathbf{w})$ with respect to $\mathbf{w}$:
\begin{equation}
    \nabla_{\mathbf{w}} \mathcal{J} = -\frac{1}{N} \mathbf{X}^T (\mathbf{s} - \mathbf{X}\mathbf{w}) + \alpha \mathbf{w}
\end{equation}
Setting the gradient to zero for optimality:
\begin{equation}
    \mathbf{X}^T \mathbf{X}\mathbf{w} + N\alpha \mathbf{w} = \mathbf{X}^T \mathbf{s} \implies \left( \mathbf{X}^T \mathbf{X} + N\alpha \mathbf{I} \right) \mathbf{w} = \mathbf{X}^T \mathbf{s}
\end{equation}
Yielding the closed-form normal equation solution:
\begin{equation}
    \mathbf{w}^* = \left( \mathbf{X}^T \mathbf{X} + \alpha' \mathbf{I}_d \right)^{-1} \mathbf{X}^T \mathbf{s}
    \label{eq:ridge_solution}
\end{equation}
where $\alpha' = N\alpha$ and $\mathbf{I}_d$ is the $d \times d$ identity matrix.

Using Singular Value Decomposition (SVD), let $\mathbf{X} = \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$, where $\mathbf{\Sigma} = \text{diag}(\sigma_1, \dots, \sigma_d)$. The Ridge predictions can be written as:
\begin{equation}
    \hat{\mathbf{s}}_{\text{Ridge}} = \mathbf{X} \mathbf{w}^* = \sum_{j=1}^d \mathbf{u}_j \left( \frac{\sigma_j^2}{\sigma_j^2 + \alpha'} \right) \mathbf{u}_j^T \mathbf{s}
\end{equation}
Notice that for singular values $\sigma_j$ associated with noisy or highly collinear directions ($\sigma_j \to 0$), the shrinkage factor $\frac{\sigma_j^2}{\sigma_j^2 + \alpha'} \to 0$. Ridge regression automatically suppresses high-variance, collinear directions while leaving prominent signal directions ($\sigma_j^2 \gg \alpha'$) intact, delivering absolute numerical stability.

\section{Cross-Validation Strategy and Hyperparameter Tuning}
\label{sec:cross_validation}
To prevent overfitting and secure hyperparameter configurations, a **Stratified 5-Fold Cross-Validation** protocol was executed strictly on the training partition $\mathcal{D}_{\text{train}}$ ($n=2,400$). The training corpus was partitioned into five non-overlapping folds $\{F_1, \dots, F_5\}$. During each cross-validation iteration, four folds were used for parameter estimation while the remaining fold served as the validation hold-out.

Table~\ref{tab:hyperparameters} outlines the hyperparameter search spaces and optimal parameters selected via grid search.

\begin{table}[H]
\centering
\caption{Hyperparameter Search Grids and Optimal Configurations}
\label{tab:hyperparameters}
\small
\begin{tabularx}{\textwidth}{lp{5.0cm}X}
\toprule
\textbf{Model} & \textbf{Evaluated Search Grid} & \textbf{Optimal Parameter Selected} \\
\midrule
\textbf{Logistic Regression} & $C \in \{0.01, 0.1, 1.0, 10.0, 100\}$, Solver: L-BFGS & $C = 1.0$, $\text{penalty} = \text{'l2'}$, $\text{tol} = 10^{-4}$ \\
\textbf{Support Vector Classifier} & $C \in \{0.1, 1.0, 10.0\}$, $\gamma \in \{\text{'scale'}, \text{'auto'}, 0.01\}$ & $C = 1.0$, $\text{kernel} = \text{'rbf'}$, $\gamma = \text{'scale'}$ \\
\textbf{Random Forest} & $\text{n\_estimators} \in \{50, 100, 200\}$, $\text{max\_depth} \in \{5, 10, \text{None}\}$ & $\text{n\_estimators} = 100$, $\text{max\_depth} = 15$, criterion = 'gini' \\
\textbf{Gradient Boosting} & $\text{learning\_rate} \in \{0.01, 0.1, 0.2\}$, $\text{n\_est} \in \{50, 100\}$ & $\text{learning\_rate} = 0.1$, $\text{n\_estimators} = 100$, depth = 3 \\
\textbf{Decision Tree (CART)} & $\text{max\_depth} \in \{3, 5, 10, 15\}$, criterion $\in \{\text{'gini'}, \text{'entropy'}\}$ & $\text{max\_depth} = 10$, criterion = 'gini' \\
\textbf{K-Nearest Neighbors} & $k \in \{3, 5, 7, 11, 15\}$, weights $\in \{\text{'uniform'}, \text{'distance'}\}$ & $k = 5$, weights = 'uniform', metric = 'minkowski' \\
\textbf{Ridge Regression} & $\alpha \in \{0.001, 0.01, 0.1, 1.0, 10.0, 100.0\}$ & $\alpha = 1.0$, solver = 'auto' \\
\bottomrule
\end{tabularx}
\end{table}

\section{Performance Evaluation Metrics}
\label{sec:evaluation_metrics}
Model performance was comprehensively evaluated using a multi-metric battery.

\subsection{Classification Metrics}
For a multi-class confusion matrix, let $TP_k, FP_k, FN_k, TN_k$ represent true positives, false positives, false negatives, and true negatives for class $k \in \{\text{Low}, \text{Medium}, \text{High}\}$:
\begin{enumerate}
    \item \textbf{Overall Accuracy:}
    \begin{equation}
        \text{Accuracy} = \frac{\sum_{k=1}^K TP_k}{N}
    \end{equation}
    \item \textbf{Precision and Recall for Class $k$:}
    \begin{equation}
        \text{Precision}_k = \frac{TP_k}{TP_k + FP_k}, \qquad \text{Recall}_k = \frac{TP_k}{TP_k + FN_k}
    \end{equation}
    \item \textbf{Macro F1-Score:} To guarantee that high accuracy on majority classes does not mask poor performance on the critical High-Risk minority class, we compute the unweighted arithmetic mean of class F1-scores:
    \begin{equation}
        F1_k = 2 \cdot \frac{\text{Precision}_k \cdot \text{Recall}_k}{\text{Precision}_k + \text{Recall}_k}, \qquad \text{Macro } F1 = \frac{1}{K} \sum_{k=1}^K F1_k
        \label{eq:macro_f1}
    \end{equation}
\end{enumerate}

\subsection{Continuous Regression Metrics}
For continuous stress score estimation with ground truth $s_i$ and prediction $\hat{s}_i$:
\begin{enumerate}
    \item \textbf{Mean Squared Error (MSE):}
    \begin{equation}
        \text{MSE} = \frac{1}{N} \sum_{i=1}^N (s_i - \hat{s}_i)^2
    \end{equation}
    \item \textbf{Root Mean Squared Error (RMSE):}
    \begin{equation}
        \text{RMSE} = \sqrt{\text{MSE}}
    \end{equation}
    \item \textbf{Mean Absolute Error (MAE):}
    \begin{equation}
        \text{MAE} = \frac{1}{N} \sum_{i=1}^N |s_i - \hat{s}_i|
    \end{equation}
    \item \textbf{Coefficient of Determination ($R^2$):}
    \begin{equation}
        R^2 = 1 - \frac{\sum_{i=1}^N (s_i - \hat{s}_i)^2}{\sum_{i=1}^N (s_i - \bar{s})^2}
    \end{equation}
\end{enumerate}
"""
