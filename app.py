import streamlit as st

st.title('🎇 Unit Converter App ')
st.markdown("### Convert units of length, temperature, time, and weight. ")

category = st.selectbox("Choose a category", ["Length", "Temperature", "Time", "Weight"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9
        
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24
        
    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
        
if category == "Length":
    unit = st.selectbox("📏 Choose a unit", ["Kilometers to miles", "Miles to kilometers"])
elif category == "Temperature":
    unit = st.selectbox("🌡 Choose a unit", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
elif category == "Time":
    unit = st.selectbox("⏱ Choose a unit", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to hours"])
elif category == "Weight":
    unit = st.selectbox("⚖ Choose a unit", ["Kilograms to pounds", "Pounds to kilograms"])

value = st.number_input("Enter the value to convert")


st.markdown("""
 <style>
    .stButton>button {
        background-color: #FF0000;
        color: white;
    }
    .stButton>button:hover {
        background-color: #1e1e1e;
    }
 </style>
    """, unsafe_allow_html=True)
    
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")



