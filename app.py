from fpdf import FPDF
import base64
import datetime
import streamlit as st
import random
import matplotlib.pyplot as plt
import time
from logic import quiz, evaluate_quiz

st.set_page_config(page_title="Skill 'o' Matrix", page_icon="🧠", layout="wide")

# 🌟 Team Branding
st.markdown("<h5 style='text-align: left; color: grey;'>💼 Powered by <b>Team Strategix</b></h5>", unsafe_allow_html=True)

# Sidebar domain options
st.sidebar.title("🧪 Choose Skill Domain")
main_domains = ["Select a domain", "Data Science", "Software Fundamentals", "Core"]
selected_main = st.sidebar.selectbox("Select a domain to begin:", main_domains, index=0)

# Show welcome message
st.title("👋 Welcome to Skill 'o' Matrix")
st.markdown("### 🚀 Test your knowledge and get instant results!\nSelect a domain from the sidebar to begin your skill test.")
import pandas as pd
import altair as alt
st.markdown("#### ✨ *Because skills win over degrees in career discovery.*")




with st.expander("📌 General Rules & Instructions", expanded=True):
    st.markdown("""
    - 🔢 You will get **10 random questions** from the selected domain   
    - ✅ You must answer **all questions** to submit  
    - 🔁 You can **retake** the test with a new set of questions  
    - 🧾 After submission, you will see:
        - A **pie chart** of correct/incorrect answers  
        - A **detailed answer breakdown**  
        - A **certificate of completion** you can download 🎓  
    """)

# Stop execution if nothing is selected
if selected_main == "Select a domain":
    st.session_state.clear()
    st.stop()

# Handle Core domain with a second dropdown
if selected_main == "Core":
    core_departments = sorted([
        "Biotechnology Engineering",
        "Biomedical Engineering",
        "Ceramic Engineering",
        "Chemical Engineering",
        "Civil Engineering",
        "Computer Science Engineering",
        "Electrical Engineering",
        "Electronics and Communication Engineering",
        "Food Processing Engineering",
        "Industrial Design",
        "Mechanical Engineering",
        "Metallurgical and Materials Engineering",
        "Mining Engineering"
    ])
    selected_core = st.sidebar.selectbox("🎓 Select your Core department:", ["Select department"] + core_departments)

    if selected_core == "Select department":
        st.stop()

    domain = f"Core: {selected_core}"
else:
    domain = selected_main

# Generate questions only when a valid domain is selected
if "selected_domain" not in st.session_state or st.session_state.selected_domain != domain:
    st.session_state.selected_domain = domain
    st.session_state.questions = random.sample(quiz[domain]["questions"], 10)
    st.session_state.start_time = time.time()

questions = st.session_state.questions
st.header(f"📘 Skill Test: {domain}")
user_answers = []

st.write("### Answer the following questions:")

import datetime

# Initialize timers for each question
if "question_timers" not in st.session_state:
    st.session_state.question_timers = [time.time()] * len(questions)

# Set timer duration (in seconds)
question_duration = 30

for i, q in enumerate(questions):
    st.write(f"**Q{i+1}. {q['question']}**")
    user_choice = st.radio("", q["options"], key=f"{domain}_{i}", index=None)
    if user_choice:
        user_answers.append(user_choice.split(".")[0])
    else:
        user_answers.append("")



if st.button("Submit Quiz"):
    if "" in user_answers:
        st.warning("Please answer all the questions before submitting.")
    else:
        end_time = time.time()
        total_time = end_time - st.session_state.start_time
        minutes = int(total_time // 60)
        seconds = int(total_time % 60)

        temp_quiz = {domain: {"questions": questions}}
        result = evaluate_quiz(domain, user_answers, temp_quiz)


        def generate_certificate(score, domain, percentage):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=20)
            pdf.cell(200, 20, txt="Skill Tester Certificate", ln=True, align="C")
            pdf.set_font("Arial", size=14)
            pdf.ln(10)
            pdf.cell(200, 10, txt=f"Congratulations!", ln=True, align="C")
            pdf.cell(200, 10, txt=f"You have successfully completed the skill test in:", ln=True, align="C")
            pdf.set_font("Arial", 'B', size=16)
            pdf.cell(200, 10, txt=f"{domain}", ln=True, align="C")
            pdf.set_font("Arial", size=14)
            pdf.ln(5)
            pdf.cell(200, 10, txt=f"Score: {score}/10  ({percentage:.1f}%)", ln=True, align="C")
            pdf.cell(200, 10, txt=f"Date: {datetime.datetime.today().strftime('%d-%m-%Y')}", ln=True, align="C")
            pdf.ln(10)
            pdf.set_font("Arial", 'I', size=12)
            pdf.cell(200, 10, txt="Keep learning and growing!", ln=True, align="C")

            filename = "skill_certificate.pdf"
            pdf.output(filename)
            return filename


        st.success(f"Your Score: {result['score']}/{result['total_questions']} ({result['percentage']}%)")
        st.info(f"🕒 Time Taken: {minutes} minutes {seconds} seconds")

        if result['percentage'] >= 80:
            st.balloons()
            st.markdown("### 🏅 Congratulations! You're a Pro!")
        elif result['percentage'] >= 50:
            st.markdown("### 👍 Good Job! Keep Practicing.")
        else:
            st.markdown("### 💡 Don't Worry! Learn and Try Again.")

        st.markdown("### 📊 Performance Summary")
        correct = result['score']
        incorrect = result['total_questions'] - correct

        fig, ax = plt.subplots()
        ax.pie([correct, incorrect], labels=['Correct', 'Incorrect'], autopct='%1.1f%%',
               startangle=90, colors=['#00c853', '#d50000'])
        ax.axis('equal')
        st.pyplot(fig)

        st.markdown("### 🔍 Analysis of Your Test")
        for f in result["feedback"]:
            st.write("----")
            st.write(f"**Q: {f['question']}**")
            st.write(f"Your Answer: {f['your_answer']}")
            st.write(f"Correct Answer: {f['correct_answer']}")
            st.write("✅ Correct!" if f["is_correct"] else "❌ Incorrect")
        # 🎓 Certificate generation
        # 🎓 Certificate generation
        st.markdown("**📜 Want a certificate of completion?**")
        if st.button("🎓 Generate Certificate"):
            filepath = generate_certificate(result['score'], domain, result['percentage'])

            try:
                with open(filepath, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                    pdf_link = f'<a href="data:application/octet-stream;base64,{base64_pdf}" download="Skill_Certificate.pdf">📥 Click here to download your certificate</a>'
                    st.markdown(pdf_link, unsafe_allow_html=True)
            except Exception as e:
                st.error("⚠️ Could not generate certificate. Please check if `fpdf` is installed and you have write permissions.")


        st.markdown("**🔁 Want to try again with different questions?**")
        if st.button("Retake Test"):
            del st.session_state.questions
            del st.session_state.selected_domain
            del st.session_state.start_time
            st.rerun()
