# 📈 Sales Prediction using Linear Regression

This project predicts product sales based on advertising spend across TV, Radio, and Newspaper channels. As part of the CodSoft Data Science Internship , we created and used a **synthetic dataset** to build and evaluate the model.

---

## ✨ Project Overview

The objective is to:

✅ Generate synthetic advertising data  
✅ Train a Linear Regression model  
✅ Evaluate and visualize model performance  
✅ Predict sales for new advertising budgets  

---

## 🗂️ Dataset

We generated a **synthetic dataset** with 1000 records and 4 columns because the original dataset was too small to train a stable model. The synthetic dataset follows realistic patterns by using random distributions and added noise to simulate real-world variability.

Columns include:

- `TV`: Budget spent on TV ads
- `Radio`: Budget spent on radio ads
- `Newspaper`: Budget spent on newspaper ads
- `Sales`: Generated sales values

Example of the dataset:

| TV        | Radio     | Newspaper | Sales   |
|-----------|-----------|-----------|---------|
| 81.05     | -2.14     | 39.04     | 6.78    |
| 55.66     | 12.66     | 13.85     | 8.75    |
| ...       | ...       | ...       | ...     |

---

## 🧠 Model

- **Algorithm**: Linear Regression
- **Libraries Used**: pandas, numpy, scikit-learn, matplotlib, seaborn

---

## 🛠️ Steps Performed

1. **Data Generation**
   - Created synthetic data with random normal distributions and added noise.
2. **Data Loading & Exploration**
   - Checked shape, nulls, and descriptive statistics.
3. **EDA**
   - Visualized distributions and correlations.
4. **Data Splitting**
   - Train/test split (80/20).
5. **Model Training**
   - Fitted Linear Regression model.
6. **Evaluation**
   - MAE, MSE, RMSE, R² Score calculated.
   - Plotted:
     - Actual vs Predicted Sales
     - Residual Plot
7. **Prediction**
   - Predicted sales for manual inputs.

---

## 📊 Evaluation Metrics

**Model Performance on Synthetic Data:**

- **MAE (Mean Absolute Error)**: 0.79
- **MSE (Mean Squared Error)**: 0.98
- **RMSE (Root Mean Squared Error)**: 0.99
- **R² Score**: 0.96

These scores indicate a **very good fit**, as expected with synthetic data.

---

## 📸 Output

The final **sales prediction output** is available as a **PNG image** (sales_prediction_output.png) inside the project folder. This shows manual user input's output

---

