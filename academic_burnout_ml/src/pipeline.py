"""
End-to-End Machine Learning Pipeline for Early Detection of Academic Burnout
Author: B.Tech (Artificial Intelligence), Amity University
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, r2_score, mean_squared_error, mean_absolute_error
)

# Classifiers
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, Ridge
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

# Regressors
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# Set styling
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "academic_burnout_dataset.csv")
MODELS_DIR = os.path.join(BASE_DIR, "models")
FIGURES_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)


def load_and_engineer_features(data_path):
    print(f"[*] Loading dataset from: {data_path}")
    df = pd.read_csv(data_path)
    print(f"    Raw Shape: {df.shape}")

    # Domain Feature Engineering
    # 1. Academic Pressure Index: interaction of assignment load and exam frequency
    df['Academic_Pressure_Index'] = df['Assignment_Load'] * df['Exam_Frequency']

    # 2. Screen-to-Sleep Ratio: digital overload indicator
    df['Screen_Sleep_Ratio'] = df['Screen_Time'] / (df['Sleep_Hours'] + 0.5)

    # 3. Social Support Deficit: peer pressure minus family support
    df['Social_Support_Deficit'] = df['Peer_Pressure'] - df['Family_Support']

    # 4. Lifestyle Balance Score: Sleep + Exercise boost - (Social Media + Screen Time)/2
    exercise_bonus = (df['Physical_Exercise'].str.lower() == 'yes').astype(float) * 2.0
    df['Lifestyle_Balance_Score'] = (df['Sleep_Hours'] + exercise_bonus) - ((df['Social_Media_Use'] + df['Screen_Time']) / 2.0)

    print(f"    Engineered Shape: {df.shape}")
    return df


def generate_eda_figures(df):
    print("[*] Generating exploratory figures...")

    # Fig 1: Feature distributions across Stress Level
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    palette = {'Low': '#2ecc71', 'Medium': '#f39c12', 'High': '#e74c3c'}
    order = ['Low', 'Medium', 'High']

    sns.boxplot(data=df, x='Stress_Level', y='Anxiety_Level', order=order, hue='Stress_Level', palette=palette, legend=False, ax=axes[0, 0])
    axes[0, 0].set_title("Anxiety Level by Burnout/Stress Category", fontsize=12, fontweight='bold')
    axes[0, 0].set_ylabel("Anxiety Level (1-9)")

    sns.boxplot(data=df, x='Stress_Level', y='Sleep_Hours', order=order, hue='Stress_Level', palette=palette, legend=False, ax=axes[0, 1])
    axes[0, 1].set_title("Sleep Hours by Burnout/Stress Category", fontsize=12, fontweight='bold')
    axes[0, 1].set_ylabel("Sleep Hours per Night")

    sns.boxplot(data=df, x='Stress_Level', y='Screen_Time', order=order, hue='Stress_Level', palette=palette, legend=False, ax=axes[1, 0])
    axes[1, 0].set_title("Daily Screen Time by Burnout/Stress Category", fontsize=12, fontweight='bold')
    axes[1, 0].set_ylabel("Screen Time (Hours)")

    sns.boxplot(data=df, x='Stress_Level', y='Academic_Pressure_Index', order=order, hue='Stress_Level', palette=palette, legend=False, ax=axes[1, 1])
    axes[1, 1].set_title("Academic Pressure Index by Burnout/Stress Category", fontsize=12, fontweight='bold')
    axes[1, 1].set_ylabel("Exam Freq × Assignment Load")

    plt.tight_layout()
    fig1_path = os.path.join(FIGURES_DIR, "fig1_eda_distributions.png")
    plt.savefig(fig1_path, dpi=300)
    plt.close()
    print(f"    Saved: {fig1_path}")

    # Fig 2: Correlation Heatmap of Numeric Features
    plt.figure(figsize=(14, 11))
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr = df[numeric_cols].corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', cbar_kws={'shrink': .8}, linewidths=0.5)
    plt.title("Correlation Matrix of Academic, Lifestyle, and Psychological Predictors", fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    fig2_path = os.path.join(FIGURES_DIR, "fig2_correlation_matrix.png")
    plt.savefig(fig2_path, dpi=300)
    plt.close()
    print(f"    Saved: {fig2_path}")


def train_classification_models(df):
    print("\n" + "="*60)
    print("STAGE 1: MULTI-CLASS BURNOUT RISK CLASSIFICATION (Low, Medium, High)")
    print("="*60)

    target_col = 'Stress_Level'
    drop_cols = ['Stress_Level', 'Stress_Score']  # Stress_Score is continuous proxy

    X = df.drop(columns=drop_cols)
    y = df[target_col]

    categorical_features = ['Gender', 'Tuition', 'Physical_Exercise', 'Family_Income_Level', 'University_Type']
    numerical_features = [col for col in X.columns if col not in categorical_features]

    # Preprocessor
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features)
        ]
    )

    # 7 Candidate ML Classifiers
    models = {
        'Random Forest': RandomForestClassifier(n_estimators=150, max_depth=12, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=120, learning_rate=0.08, max_depth=4, random_state=42),
        'Extra Trees': ExtraTreesClassifier(n_estimators=150, max_depth=12, random_state=42),
        'Support Vector Machine': SVC(kernel='rbf', C=1.5, probability=True, random_state=42),
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=9, weights='distance'),
        'Multi-Layer Perceptron': MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=800, random_state=42)
    }

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_results = {}

    print(f"Running 5-Fold Stratified Cross-Validation across {len(models)} algorithms...")
    for name, model in models.items():
        clf_pipeline = Pipeline([
            ('preprocessor', preprocessor),
            ('classifier', model)
        ])
        scores = cross_validate(
            clf_pipeline, X, y, cv=cv,
            scoring=['accuracy', 'f1_macro', 'f1_weighted', 'precision_macro', 'recall_macro'],
            n_jobs=-1
        )
        cv_results[name] = {
            'accuracy_mean': float(np.mean(scores['test_accuracy'])),
            'accuracy_std': float(np.std(scores['test_accuracy'])),
            'f1_macro_mean': float(np.mean(scores['test_f1_macro'])),
            'f1_macro_std': float(np.std(scores['test_f1_macro'])),
            'f1_weighted_mean': float(np.mean(scores['test_f1_weighted'])),
            'precision_macro_mean': float(np.mean(scores['test_precision_macro'])),
            'recall_macro_mean': float(np.mean(scores['test_recall_macro']))
        }
        print(f"  > {name:<24}: Acc = {cv_results[name]['accuracy_mean']*100:.2f}% (+/- {cv_results[name]['accuracy_std']*100:.2f}%), Macro F1 = {cv_results[name]['f1_macro_mean']:.4f}")

    # Train-test split for deep evaluation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, stratify=y, random_state=42)

    # Fit and evaluate best model on test set
    best_name = max(cv_results, key=lambda k: cv_results[k]['f1_macro_mean'])
    print(f"\n[*] Best Classifier Selected: {best_name}")

    best_pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', models[best_name])
    ])
    best_pipeline.fit(X_train, y_train)
    y_pred = best_pipeline.predict(X_test)

    test_acc = accuracy_score(y_test, y_pred)
    test_f1_macro = f1_score(y_test, y_pred, average='macro')
    test_f1_weighted = f1_score(y_test, y_pred, average='weighted')
    report_dict = classification_report(y_test, y_pred, output_dict=True)
    report_text = classification_report(y_test, y_pred)

    print("\n--- Test Set Classification Report ---")
    print(report_text)

    # Save pipeline
    model_save_path = os.path.join(MODELS_DIR, "best_burnout_classifier.joblib")
    joblib.dump(best_pipeline, model_save_path)
    print(f"[*] Serialized best classifier to: {model_save_path}")

    # Fig 3: Model Comparison Bar Chart
    fig, ax = plt.subplots(figsize=(12, 6))
    names = list(cv_results.keys())
    accs = [cv_results[n]['accuracy_mean'] * 100 for n in names]
    f1s = [cv_results[n]['f1_macro_mean'] * 100 for n in names]

    x = np.arange(len(names))
    width = 0.35

    rects1 = ax.bar(x - width/2, accs, width, label='Mean Accuracy (%)', color='#3498db')
    rects2 = ax.bar(x + width/2, f1s, width, label='Macro F1-Score (%)', color='#2ecc71')

    ax.set_ylabel('Percentage (%)', fontsize=11, fontweight='bold')
    ax.set_title('Cross-Validated Performance Benchmark across 7 Machine Learning Models', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=20, ha='right', fontsize=10)
    ax.set_ylim(0, 100)
    ax.legend(frameon=True)

    for rect in rects1 + rects2:
        h = rect.get_height()
        ax.annotate(f'{h:.1f}%',
                    xy=(rect.get_x() + rect.get_width() / 2, h),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    fig3_path = os.path.join(FIGURES_DIR, "fig3_model_comparison.png")
    plt.savefig(fig3_path, dpi=300)
    plt.close()
    print(f"    Saved: {fig3_path}")

    # Fig 4: Confusion Matrix for best model
    cm = confusion_matrix(y_test, y_pred, labels=['Low', 'Medium', 'High'])
    cm_norm = confusion_matrix(y_test, y_pred, labels=['Low', 'Medium', 'High'], normalize='true') * 100

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Low', 'Medium', 'High'], yticklabels=['Low', 'Medium', 'High'], ax=axes[0])
    axes[0].set_title(f"Confusion Matrix (Counts) - {best_name}", fontsize=11, fontweight='bold')
    axes[0].set_xlabel("Predicted Burnout Level")
    axes[0].set_ylabel("True Burnout Level")

    sns.heatmap(cm_norm, annot=True, fmt='.1f', cmap='Greens', xticklabels=['Low', 'Medium', 'High'], yticklabels=['Low', 'Medium', 'High'], ax=axes[1])
    axes[1].set_title(f"Normalized Confusion Matrix (%) - {best_name}", fontsize=11, fontweight='bold')
    axes[1].set_xlabel("Predicted Burnout Level")
    axes[1].set_ylabel("True Burnout Level")

    plt.tight_layout()
    fig4_path = os.path.join(FIGURES_DIR, "fig4_confusion_matrices.png")
    plt.savefig(fig4_path, dpi=300)
    plt.close()
    print(f"    Saved: {fig4_path}")

    # Fig 5: Feature Importances
    clf_model = best_pipeline.named_steps['classifier']
    if hasattr(clf_model, 'feature_importances_'):
        # Get feature names from ColumnTransformer
        cat_encoder = best_pipeline.named_steps['preprocessor'].named_transformers_['cat']
        encoded_cat_names = list(cat_encoder.get_feature_names_out(categorical_features))
        all_features = numerical_features + encoded_cat_names

        importances = clf_model.feature_importances_
        feat_df = pd.DataFrame({'Feature': all_features, 'Importance': importances})
        feat_df = feat_df.sort_values(by='Importance', ascending=False).head(12)

        plt.figure(figsize=(10, 6))
        sns.barplot(data=feat_df, x='Importance', y='Feature', palette='mako')
        plt.title(f"Top 12 Most Predictive Features of Academic Burnout ({best_name})", fontsize=12, fontweight='bold')
        plt.xlabel("Gini Feature Importance / Weight")
        plt.ylabel("Predictor Variable")
        plt.tight_layout()
        fig5_path = os.path.join(FIGURES_DIR, "fig5_feature_importance.png")
        plt.savefig(fig5_path, dpi=300)
        plt.close()
        print(f"    Saved: {fig5_path}")
    else:
        feat_df = pd.DataFrame()

    return {
        'best_model_name': best_name,
        'cv_results': cv_results,
        'test_accuracy': float(test_acc),
        'test_f1_macro': float(test_f1_macro),
        'test_f1_weighted': float(test_f1_weighted),
        'report_dict': report_dict,
        'confusion_matrix': cm.tolist(),
        'top_features': feat_df.to_dict(orient='records') if not feat_df.empty else []
    }


def train_regression_models(df):
    print("\n" + "="*60)
    print("STAGE 2: CONTINUOUS BURNOUT STRESS SCORE REGRESSION")
    print("="*60)

    X = df.drop(columns=['Stress_Level', 'Stress_Score'])
    y = df['Stress_Score']

    categorical_features = ['Gender', 'Tuition', 'Physical_Exercise', 'Family_Income_Level', 'University_Type']
    numerical_features = [col for col in X.columns if col not in categorical_features]

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features)
        ]
    )

    regressors = {
        'Ridge Regression': Ridge(alpha=1.0),
        'Random Forest Regressor': RandomForestRegressor(n_estimators=120, max_depth=10, random_state=42),
        'Gradient Boosting Regressor': GradientBoostingRegressor(n_estimators=120, learning_rate=0.08, max_depth=4, random_state=42)
    }

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    reg_results = {}

    best_reg_name = None
    best_reg_r2 = -float('inf')
    best_reg_pipeline = None

    for name, reg in regressors.items():
        pipe = Pipeline([
            ('preprocessor', preprocessor),
            ('regressor', reg)
        ])
        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        reg_results[name] = {
            'R2': float(r2),
            'MAE': float(mae),
            'RMSE': float(rmse)
        }
        print(f"  > {name:<26}: R² = {r2:.4f}, MAE = {mae:.2f}, RMSE = {rmse:.2f}")

        if r2 > best_reg_r2:
            best_reg_r2 = r2
            best_reg_name = name
            best_reg_pipeline = pipe

    # Save regressor
    reg_model_path = os.path.join(MODELS_DIR, "best_burnout_regressor.joblib")
    joblib.dump(best_reg_pipeline, reg_model_path)
    print(f"[*] Serialized best regressor ({best_reg_name}) to: {reg_model_path}")

    # Fig 6: True vs Predicted Stress Score
    y_test_pred = best_reg_pipeline.predict(X_test)
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_test_pred, alpha=0.5, color='#8e44ad', edgecolors='none', s=35)
    p1 = max(max(y_test_pred), max(y_test))
    p2 = min(min(y_test_pred), min(y_test))
    plt.plot([p2, p1], [p2, p1], 'r--', lw=2, label='Perfect Prediction Line (y=x)')
    plt.xlabel('Actual Academic Burnout Stress Score', fontsize=11)
    plt.ylabel('Predicted Burnout Stress Score', fontsize=11)
    plt.title(f'Continuous Stress Score Prediction ({best_reg_name}: R² = {best_reg_r2:.3f})', fontsize=12, fontweight='bold')
    plt.legend()
    plt.tight_layout()
    fig6_path = os.path.join(FIGURES_DIR, "fig6_stress_score_regression.png")
    plt.savefig(fig6_path, dpi=300)
    plt.close()
    print(f"    Saved: {fig6_path}")

    return {
        'best_regressor_name': best_reg_name,
        'reg_results': reg_results
    }


def main():
    print("="*60)
    print("EARLY DETECTION OF ACADEMIC BURNOUT: ML SYSTEM EXECUTION")
    print("="*60)

    # 1. Load data and engineer features
    df = load_and_engineer_features(DATA_PATH)

    # 2. EDA visual generation
    generate_eda_figures(df)

    # 3. Model training & benchmark (Classification)
    clf_summary = train_classification_models(df)

    # 4. Model training & benchmark (Regression)
    reg_summary = train_regression_models(df)

    # 5. Export comprehensive results summary JSON
    full_summary = {
        'dataset_stats': {
            'total_samples': len(df),
            'features_count': df.shape[1] - 2,
            'stress_level_distribution': df['Stress_Level'].value_counts().to_dict(),
            'stress_score_stats': {
                'mean': float(df['Stress_Score'].mean()),
                'std': float(df['Stress_Score'].std()),
                'min': float(df['Stress_Score'].min()),
                'max': float(df['Stress_Score'].max())
            }
        },
        'classification': clf_summary,
        'regression': reg_summary
    }

    summary_file = os.path.join(MODELS_DIR, "metrics_summary.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(full_summary, f, indent=4)
    print(f"\n[+] Complete metrics and model metadata saved to: {summary_file}")
    print("[+] All figures successfully written to:", FIGURES_DIR)
    print("\nPipeline execution complete!\n")


if __name__ == "__main__":
    main()
