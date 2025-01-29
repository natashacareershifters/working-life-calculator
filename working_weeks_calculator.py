import streamlit as st

def calculate_working_weeks_left(current_age, retirement_age, working_weeks_per_year=48):
    if current_age >= retirement_age:
        return "You have already reached retirement age!"
    remaining_years = retirement_age - current_age
    remaining_weeks = remaining_years * working_weeks_per_year
    return remaining_weeks

st.title("Working Weeks Left Calculator")

current_age = st.number_input("Enter your current age:", min_value=0, max_value=100, value=30)
retirement_age = st.number_input("Enter your expected retirement age:", min_value=current_age, max_value=100, value=65)
working_weeks_per_year = st.number_input("Enter your working weeks per year:", min_value=1, max_value=52, value=48)

if st.button("Calculate"):
    weeks_left = calculate_working_weeks_left(current_age, retirement_age, working_weeks_per_year)
    st.write(f"You have approximately {weeks_left} working weeks left until retirement.")