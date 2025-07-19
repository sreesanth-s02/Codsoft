🎬 Movie Rating Prediction  
A Machine Learning Project for CodSoft Data Science Internship

📌 Project Overview  
This project predicts the **rating of a movie** based on features like genre, director, and leading actors using regression models. It is developed as **Task 2** under the **CodSoft July Batch – Data Science Internship**.

📁 Folder Structure  
CODSOFT/  
├── Task_2_MovieRating/  
│   ├── Task2_MovieRating_EDA_Model.ipynb  
│   ├── IMDb Movies India.csv  
│   ├── model_comparison_plot.png   
│   └── README.md  

🧠 Workflow & Task Structure  

📚 Data Loading  
Loaded the movie ratings dataset (IMDb Movies India.csv) using encoding='atin1.

🧹 Data Cleaning  
- Checked for null values, duplicates, and inconsistencies  
- Filtered out unknown or invalid entries  
- Limited genres, directors, and actors to top 10 for simplicity  

📊 Exploratory Data Analysis (EDA)  
- Analyzed the distribution of movie ratings  
- Visualized top genres, most frequent directors and actors  
- Checked correlation among features  

🧪 Feature Engineering  
- Label encoded string columns: Genre, Director, Actor 1, Actor 2, Actor 3  
- Extracted top 10 most frequent values in each category  
- Finalized feature set for training  

🤖 Model Building  
Built and evaluated two regression models:  
- **Linear Regression**  
- **Random Forest Regressor** ✅ (Best performing)

📈 Model Evaluation  
Used performance metrics:
- MAE (Mean Absolute Error)  
- MSE (Mean Squared Error)  
- RMSE (Root Mean Squared Error)  
- R² Score

🧮 Prediction Output  
- Accepted manual user input in console  
- Predicted movie rating based on trained model  
- Used same encoding as the model for accurate prediction

✨ Key Features Used in Model  
['Genre', 'Duration', 'Year', 'Director', 'Actor 1', 'Actor 2', 'Actor 3', 'Votes']

🏆 Top 5 Insights from EDA  
🎭 Certain genres like Drama, Action, and Comedy dominate the dataset  
🎬 A small number of directors consistently produce higher-rated movies  
🎤 Popular actors appear frequently in high-rated films  
📈 Ratings are moderately correlated with vote count  
📅 Release year has minor influence on ratings compared to genre and cast

🔍 Model Performance  

✅ Random Forest Regressor (Best Model)  
- MAE: ~0.27  
- RMSE: ~0.33  
- R² Score: ~0.78  

💡 Sample Prediction  
Based on the following user input:  

Genre: 2 (Action)  
Duration: 120  
Year: 2012  
Director: 3  
Actor 1: 4  
Actor 2: 6  
Actor 3: 1  
Votes: 35000  

🎯 Predicted Rating: **7.6 / 10**

📌 Notes:  
- Code ➝ Name mappings for Genre, Director, and Actors are shown in notebook output  
- Input values must match encoding used by the model  

---

✅ Task 2 Completed!
