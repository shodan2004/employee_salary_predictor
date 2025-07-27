# 💼 Employee Salary Predictor

A machine learning-powered web app that predicts employee salaries based on demographic and job-related inputs. Built with **Streamlit** and **XGBoost**, this app provides intuitive visuals, salary breakdowns, and trend projections.

---

## 🚀 Features

✅ Predict salary using real-world inputs  
✅ Visual salary breakdown & projections  
✅ Interactive charts (bar, pie, line)  
✅ Built with XGBoost and deployed via Streamlit  
✅ Clean UI with job and education-based insights  

---

## 🧠 How It Works

1. Model: Trained using **XGBoost Regressor**  
2. Input: Age, Gender, Education, Job Title, Experience  
3. Output: Estimated Monthly & Yearly Salary  
4. Extras: Time-based salary growth chart and salary distribution

---

## 🖥️ App Structure

```bash
employee-salary-predictor/
│
├── app.py                    # Streamlit web app
├── requirements.txt          # Python dependencies
│
├── data/
│   └── Salary_Data.csv       # Input dataset
│
├── models/
│   └── XGBoost_salary_model.pkl
│
├── notebooks/
│   ├── salary_prediction.ipynb
│   ├── predicted_vs_actual.png
│   ├── salary_distribution.png
│   └── salary_vs_education.png
│
├── assets/                   # Charts or logos used in app 
└── README.md                 # You're here!

📦 Setup Instructions
🔧 1. Clone the Repo
git clone https://github.com/shodan2004/emmployee-salary-predictor.git
cd employee-salary-predictor

🐍 2. Create Virtual Environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

📥 3. Install Dependencies
pip install -r requirements.txt

🚪 4. Run the App
streamlit run app.py
📊 Sample Visuals
📈 Salary Prediction vs Actual

🧠 Salary vs Education Level

🕒 Projected Salary Over Time

🥧 Salary Breakdown by Components

👤 Author
Shodhan Vemulapalli
📧 shodan.v3@gmail.com
🔗 http://www.linkedin.com/in/shodhan-vemulapalli

