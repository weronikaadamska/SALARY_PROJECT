import streamlit as st
import pandas as pd
import pickle

# =====================================
# ZAŁADOWANIE COEFFICIENTS MODELU
# =====================================

with open("salary_model.pkl", "rb") as f:
    model_data = pickle.load(f)

model_params = model_data["params"]
model_columns = model_data["columns"]

# =====================================
# TYTUŁ APLIKACJI
# =====================================

st.title("Aplikacja prognozująca wynagrodzenie")
st.write("Prognozowanie wynagrodzenia na podstawie doświadczenia, edukacji, płci oraz obejmowanego stanowiska.")

# =====================================
# DANE WPROWADZANE PRZEZ UŻYTKOWNIKA
# =====================================

years = st.slider("Doświadczenie w latach", 0, 40, 5)

education = st.selectbox(
    "Osiągnięty poziom edukacji",
    ["Bachelor's", "Master's", "PhD"]
)

gender = st.selectbox(
    "Płeć",
    ["Female", "Male"]
)

# FULL JOB TITLE LIST
job_titles = [
"Account Manager",
"Accountant",
"Administrative Assistant",
"Business Analyst",
"Business Development Manager",
"Business Intelligence Analyst",
"CEO",
"Chief Data Officer",
"Content Marketing Manager",
"Copywriter",
"Creative Director",
"Customer Service Manager",
"Customer Service Representative",
"Customer Success Manager",
"Customer Success Representative",
"Data Analyst",
"Data Entry Clerk",
"Data Scientist",
"Digital Content Producer",
"Digital Marketing Manager",
"Director",
"Director of Business Development",
"Director of Engineering",
"Director of Finance",
"Director of HR",
"Director of Human Capital",
"Director of Marketing",
"Director of Operations",
"Director of Product Management",
"Director of Sales",
"Director of Sales and Marketing",
"Event Coordinator",
"Financial Advisor",
"Financial Analyst",
"Financial Manager",
"Graphic Designer",
"Help Desk Analyst",
"HR Generalist",
"HR Manager",
"IT Manager",
"IT Support",
"IT Support Specialist",
"Junior Account Manager",
"Junior Accountant",
"Junior Adversiting Coordinator",
"Junior Business Analyst",
"Junior Business Development Associate",
"Junior Business Operations Analyst",
"Junior Copywriter",
"Junior Customer Support Specialist",
"Junior Data Analyst",
"Junior Data Scientist",
"Junior Designer",
"Junior Developer",
"Junior Financial Advisor",
"Junior Financial Analyst",
"Junior HR Coordinator",
"Junior HR Generalist",
"Junior Marketing Analyst",
"Junior Marketing Coordinator",
"Junior Marketing Manager",
"Junior Marketing Specialist",
"Junior Operations Analyst",
"Junior Operations Coordinator",
"Junior Operations Manager",
"Junior Product Manager",
"Junior Project Manager",
"Junior Recruiter",
"Junior Research Scientist",
"Junior Sales Representative",
"Junior Social Media Manager",
"Junior Social Media Specialist",
"Junior Software Developer",
"Junior Software Engineer",
"Junior UX Designer",
"Junior Web Designer",
"Junior Web Developer",
"Marketing Analyst",
"Marketing Coordinator",
"Marketing Manager",
"Marketing Specialist",
"Network Engineer",
"Office Manager",
"Operations Analyst",
"Operations Director",
"Operations Manager",
"Principal Engineer",
"Principal Scientist",
"Product Designer",
"Product Manager",
"Product Marketing Manager",
"Project Engineer",
"Project Manager",
"Public Relations Manager",
"Recruiter",
"Research Director",
"Research Scientist",
"Sales Associate",
"Sales Director",
"Sales Executive",
"Sales Manager",
"Sales Operations Manager",
"Sales Representative",
"Senior Account Executive",
"Senior Account Manager",
"Senior Accountant",
"Senior Business Analyst",
"Senior Business Development Manager",
"Senior Consultant",
"Senior Data Analyst",
"Senior Data Engineer",
"Senior Data Scientist",
"Senior Engineer",
"Senior Financial Advisor",
"Senior Financial Analyst",
"Senior Financial Manager",
"Senior Graphic Designer",
"Senior HR Generalist",
"Senior HR Manager",
"Senior HR Specialist",
"Senior Human Resources Coordinator",
"Senior IT Consultant",
"Senior IT Project Manager",
"Senior IT Support Specialist",
"Senior Manager",
"Senior Marketing Analyst",
"Senior Marketing Coordinator",
"Senior Marketing Director",
"Senior Marketing Manager",
"Senior Marketing Specialist",
"Senior Operations Analyst",
"Senior Operations Coordinator",
"Senior Operations Manager",
"Senior Product Designer",
"Senior Product Development Manager",
"Senior Product Manager",
"Senior Product Marketing Manager",
"Senior Project Coordinator",
"Senior Project Manager",
"Senior Quality Assurance Analyst",
"Senior Research Scientist",
"Senior Researcher",
"Senior Sales Manager",
"Senior Sales Representative",
"Senior Scientist",
"Senior Software Architect",
"Senior Software Developer",
"Senior Software Engineer",
"Senior Training Specialist",
"Senior UX Designer",
"Social Media Manager",
"Social Media Specialist",
"Software Developer",
"Software Engineer",
"Software Manager",
"Software Project Manager",
"Strategy Consultant",
"Supply Chain Analyst",
"Supply Chain Manager",
"Technical Recruiter",
"Technical Support Specialist",
"Technical Writer",
"Training Specialist",
"UX Designer",
"UX Researcher",
"VP of Finance",
"VP of Operations",
"Web Developer"

]

job_title = st.selectbox("Stanowisko", job_titles)

# =====================================
# MAPOWANIE STANOWISK
# =====================================

seniority_map = {
    "Account Manager": "Manager",
    "Accountant": "Mid",
    "Administrative Assistant": "Mid",
    "Business Analyst": "Mid",
    "Business Development Manager": "Manager",
    "Business Intelligence Analyst": "Mid",
    "CEO": "Executive",
    "Chief Data Officer": "Executive",
    "Content Marketing Manager": "Manager",
    "Copywriter": "Mid",
    "Creative Director": "Executive",
    "Customer Service Manager": "Manager",
    "Customer Service Representative": "Mid",
    "Customer Success Manager": "Manager",
    "Customer Success Representative": "Mid",
    "Data Analyst": "Mid",
    "Data Entry Clerk": "Mid",
    "Data Scientist": "Mid",
    "Digital Content Producer": "Mid",
    "Digital Marketing Manager": "Manager",
    "Director": "Executive",
    "Director of Business Development": "Executive",
    "Director of Engineering": "Executive",
    "Director of Finance": "Executive",
    "Director of HR": "Executive",
    "Director of Human Capital": "Executive",
    "Director of Marketing": "Executive",
    "Director of Operations": "Executive",
    "Director of Product Management": "Executive",
    "Director of Sales": "Executive",
    "Director of Sales and Marketing": "Executive",
    "Event Coordinator": "Mid",
    "Financial Advisor": "Mid",
    "Financial Analyst": "Mid",
    "Financial Manager": "Manager",
    "Graphic Designer": "Mid",
    "Help Desk Analyst": "Mid",
    "HR Generalist": "Mid",
    "HR Manager": "Manager",
    "IT Manager": "Manager",
    "IT Support": "Mid",
    "IT Support Specialist": "Mid",
    "Junior Account Manager": "Manager",
    "Junior Accountant": "Junior",
    "Junior Adversiting Coordinator": "Junior",
    "Junior Business Analyst": "Junior",
    "Junior Business Development Associate": "Junior",
    "Junior Business Operations Analyst": "Junior",
    "Junior Copywriter": "Junior",
    "Junior Customer Support Specialist": "Junior",
    "Junior Data Analyst": "Junior",
    "Junior Data Scientist": "Junior",
    "Junior Designer": "Junior",
    "Junior Developer": "Junior",
    "Junior Financial Advisor": "Junior",
    "Junior Financial Analyst": "Junior",
    "Junior HR Coordinator": "Junior",
    "Junior HR Generalist": "Junior",
    "Junior Marketing Analyst": "Junior",
    "Junior Marketing Coordinator": "Junior",
    "Junior Marketing Manager": "Manager",
    "Junior Marketing Specialist": "Junior",
    "Junior Operations Analyst": "Junior",
    "Junior Operations Coordinator": "Junior",
    "Junior Operations Manager": "Manager",
    "Junior Product Manager": "Manager",
    "Junior Project Manager": "Manager",
    "Junior Recruiter": "Junior",
    "Junior Research Scientist": "Junior",
    "Junior Sales Representative": "Junior",
    "Junior Social Media Manager": "Manager",
    "Junior Social Media Specialist": "Junior",
    "Junior Software Developer": "Junior",
    "Junior Software Engineer": "Junior",
    "Junior UX Designer": "Junior",
    "Junior Web Designer": "Junior",
    "Junior Web Developer": "Junior",
    "Marketing Analyst": "Mid",
    "Marketing Coordinator": "Mid",
    "Marketing Manager": "Manager",
    "Marketing Specialist": "Mid",
    "Network Engineer": "Mid",
    "Office Manager": "Manager",
    "Operations Analyst": "Mid",
    "Operations Director": "Executive",
    "Operations Manager": "Manager",
    "Principal Engineer": "Mid",
    "Principal Scientist": "Mid",
    "Product Designer": "Mid",
    "Product Manager": "Manager",
    "Product Marketing Manager": "Manager",
    "Project Engineer": "Mid",
    "Project Manager": "Manager",
    "Public Relations Manager": "Manager",
    "Recruiter": "Mid",
    "Research Director": "Executive",
    "Research Scientist": "Mid",
    "Sales Associate": "Mid",
    "Sales Director": "Executive",
    "Sales Executive": "Executive",
    "Sales Manager": "Manager",
    "Sales Operations Manager": "Manager",
    "Sales Representative": "Mid",
    "Senior Account Executive": "Executive",
    "Senior Account Manager": "Manager",
    "Senior Accountant": "Mid",
    "Senior Business Analyst": "Senior",
    "Senior Business Development Manager": "Manager",
    "Senior Consultant": "Senior",
    "Senior Data Analyst": "Senior",
    "Senior Data Engineer": "Senior",
    "Senior Data Scientist": "Senior",
    "Senior Engineer": "Senior",
    "Senior Financial Advisor": "Senior",
    "Senior Financial Analyst": "Senior",
    "Senior Financial Manager": "Manager",
    "Senior Graphic Designer": "Senior",
    "Senior HR Generalist": "Senior",
    "Senior HR Manager": "Manager",
    "Senior HR Specialist": "Senior",
    "Senior Human Resources Coordinator": "Senior",
    "Senior IT Consultant": "Senior",
    "Senior IT Project Manager": "Manager",
    "Senior IT Support Specialist": "Senior",
    "Senior Manager": "Manager",
    "Senior Marketing Analyst": "Senior",
    "Senior Marketing Coordinator": "Senior",
    "Senior Marketing Director": "Executive",
    "Senior Marketing Manager": "Manager",
    "Senior Marketing Specialist": "Senior",
    "Senior Operations Analyst": "Senior",
    "Senior Operations Coordinator": "Senior",
    "Senior Operations Manager": "Manager",
    "Senior Product Designer": "Senior",
    "Senior Product Development Manager": "Manager",
    "Senior Product Manager": "Manager",
    "Senior Product Marketing Manager": "Manager",
    "Senior Project Coordinator": "Senior",
    "Senior Project Manager": "Manager",
    "Senior Quality Assurance Analyst": "Senior",
    "Senior Research Scientist": "Senior",
    "Senior Researcher": "Senior",
    "Senior Sales Manager": "Manager",
    "Senior Sales Representative": "Senior",
    "Senior Scientist": "Senior",
    "Senior Software Architect": "Senior",
    "Senior Software Developer": "Senior",
    "Senior Software Engineer": "Senior",
    "Senior Training Specialist": "Senior",
    "Senior UX Designer": "Senior",
    "Social Media Manager": "Manager",
    "Social Media Specialist": "Mid",
    "Software Developer": "Mid",
    "Software Engineer": "Mid",
    "Software Manager": "Manager",
    "Software Project Manager": "Manager",
    "Strategy Consultant": "Mid",
    "Supply Chain Analyst": "Mid",
    "Supply Chain Manager": "Manager",
    "Technical Recruiter": "Mid",
    "Technical Support Specialist": "Mid",
    "Technical Writer": "Mid",
    "Training Specialist": "Mid",
    "UX Designer": "Mid",
    "UX Researcher": "Mid",
    "VP of Finance": "Executive",
    "VP of Operations": "Executive",
    "Web Developer": "Mid"
}

seniority = seniority_map[job_title]

# =====================================
# CREATE INPUT DATAFRAME
# =====================================

input_df = pd.DataFrame(0, index=[0], columns=model_columns)

# const
if "const" in input_df.columns:
    input_df["const"] = 1

# Doświadczenie
input_df["Years of Experience"] = years

# Edukacja
if education == "Master's":
    input_df["Education Level_Master's"] = 1
elif education == "PhD":
    input_df["Education Level_PhD"] = 1

# Płeć
if gender == "Male":
    input_df["Gender_Male"] = 1

# Stanowisko
if seniority != "Junior":
    col_name = f"Seniority_{seniority}"
    if col_name in input_df.columns:
        input_df[col_name] = 1

# =====================================
# MANUAL OLS PREDICTION (Xβ)
# =====================================

prediction = float((input_df * model_params).sum(axis=1))

# =====================================
# OUTPUT
# =====================================

st.subheader("Prognozowane wynagrodzenie:")
formatted_salary = f"{prediction:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
st.success(formatted_salary)

