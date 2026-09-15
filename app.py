import streamlit as st

st.title("🎓 Student Assistant")

st.header("Student Details")

name = st.text_input("Student Name")
roll_number = st.text_input("Roll Number")

st.header("Attendance")

attendance = st.number_input(
    "Enter Attendance Percentage",
    min_value=0,
    max_value=100,
    value=75
)

if st.button("Check Attendance"):

    st.write("### Student Information")
    st.write("Name:", name)
    st.write("Roll Number:", roll_number)
    st.write("Attendance:", attendance, "%")

    if attendance >= 75:
        st.success("✅ Attendance is sufficient.")
    else:
        st.warning("⚠️ Attendance is below 75%.")