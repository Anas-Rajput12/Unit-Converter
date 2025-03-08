import streamlit as st

# Set Page Title
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# UI Styling
st.markdown(
    """
    <style>
    .stApp {background-color: #f7f7f7;}
    .stTextInput, .stSelectbox, .stNumberInput, .stButton button {
        border-radius: 10px;
        text-align: center;
    }
    .stSuccess {background-color: #d4edda; padding: 10px; border-radius: 10px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("🔄 Simple Unit Converter")
st.write("Convert between common units easily!")

# Unit Categories
categories = {
    "Length": {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084},
    "Weight": {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Select Conversion Category
category = st.selectbox("Choose a category:", list(categories.keys()))

# Conversion Logic
def convert(value, from_unit, to_unit, unit_dict):
    if category == "Temperature":
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius":
            return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
        elif from_unit == "Fahrenheit":
            return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    else:
        return value * unit_dict[to_unit] / unit_dict[from_unit]

# Select Units
if category == "Temperature":
    from_unit = st.selectbox("Convert from:", categories["Temperature"])
    to_unit = st.selectbox("Convert to:", categories["Temperature"])
else:
    from_unit = st.selectbox("Convert from:", categories[category].keys())
    to_unit = st.selectbox("Convert to:", categories[category].keys())

# Input Value
value = st.number_input("Enter value:", value=0.0, step=0.1)

# Convert Button
if st.button("Convert"):
    result = convert(value, from_unit, to_unit, categories.get(category, {}))
    st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")

# Footer
st.write("🌟 Built with ❤️ using Streamlit")
