# 📊 Loan Completion Prediction  

This project was developed as part of my **Summer Training with Applai** at the Faculty of Computer and Information Sciences, Ain Shams University 🎓.  
The goal of this project is to **predict the loan completion status** (e.g., Paid, Default, etc.) using Machine Learning techniques.  

---

## 📁 Project Overview  
- **Data Cleaning & Preprocessing**  
  - Removed unnecessary columns  
  - Handled missing values (mean/mode imputation)  
  - Encoded categorical features using **Label Encoding**  
- **Exploratory Data Analysis (EDA)**  
  - Visualized class distribution  
  - Checked for outliers using IQR  
  - Plotted correlations (heatmap)  
- **Balancing Classes**  
  - Applied **SMOTE** to handle class imbalance  
- **Model Training & Evaluation**  
  - Trained multiple models:  
    - Logistic Regression  
    - Decision Tree  
    - Random Forest  
    - Support Vector Machine (SVM)  
    - K-Nearest Neighbors (KNN)  
  - Used **Cross-Validation** to compare models  
  - Selected **Random Forest** as the best performing model  
- **Feature Importance**  
  - Visualized key features affecting prediction  

---

## 🏆 Results  
- **Best Model:** Random Forest  
- **Performance:** Achieved high accuracy and balanced classification report  
- **Key Insight:** Feature importance revealed which variables impact loan completion the most  

---

## 🖼️ Visualizations  
- Correlation Heatmap  
- Class Distribution (Before & After SMOTE)  
- Confusion Matrix  
- Feature Importance Barplot  

---

## 🛠️ Tech Stack  
- **Python** (pandas, numpy, scikit-learn, imbalanced-learn)  
- **Visualization:** matplotlib, seaborn  
- **ML Techniques:** Supervised Classification, Cross-Validation, Feature Importance  

---

## 🤝 Collaboration  
This project was a team effort!  

- **[Beshoy Karam](https://github.com/beshoy1612)**  

---

## ▶️ How to Run  
```bash
jupyter notebook Loan_Prediction.ipynb
