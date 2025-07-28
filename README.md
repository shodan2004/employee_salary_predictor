# 💼 Employee Salary Predictor 
A machine learning-powered web app that predicts employee salaries based on demographic and job-related inputs. Built with **Streamlit** and **XGBoost**, this app provides intuitive visuals, salary breakdowns, and trend projections.

---

## 🚀 Features

- ✅ Predict salary using real-world user inputs  
- ✅ Visual salary breakdown (pie chart)  
- ✅ Time-based salary projection (line chart)  
- ✅ Feature comparison (radar chart)  
- ✅ Built with XGBoost and deployed via Streamlit  
- ✅ Clean UI and responsive inputs  

---

## 🧠 How It Works

1. **Model**: Trained using XGBoost Regressor  
2. **Input**: Age, Gender, Education, Job Title, Hours per Week, Native Country, etc.  
3. **Output**: Estimated Monthly & Yearly Salary  
4. **Extras**:
   - Time-based salary growth chart  
   - Feature importance radar chart  
   - Salary distribution (by education and other categories)

---

## 🖥️ App Structure


employee-salary-predictor/
│
├── app.py                      # Streamlit web app
├── requirements.txt            # Python dependencies
│
├── data/
│   └── adult 3.csv             # Input dataset
│
├── models/
│   └── best\_model.pkl          # Trained XGBoost model
│
├── notebooks/
│   ├── salary\_prediction.ipynb
│   ├── predicted\_vs\_actual.png
│   ├── salary\_distribution.png
│   └── salary\_vs\_education.png
│
├── assets/                     # Charts or logos used in the app
├── .gitignore
└── README.md                   # This file


## 📦 Setup Instructions

### 🔧 1. Clone the Repo
git clone https://github.com/shodan2004/emmployee-salary-predictor.git
cd emmployee-salary-predictor


### 🐍 2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

### 📥 3. Install Dependencies
pip install -r requirements.txt


### 🚪 4. Run the App
streamlit run app.py

## 📊 Sample Visuals

* 📈 **Prediction vs Actual Salary**
* 🧠 **Salary vs Education Level**
* 🕒 **Projected Salary Over Time**
* 🥧 **Salary Component Breakdown**

---

## 👤 Author

**Shodhan Vemulapalli**
📧 [shodan.v3@gmail.com](mailto:shodan.v3@gmail.com)
🔗 [LinkedIn](http://www.linkedin.com/in/shodhan-vemulapalli)
