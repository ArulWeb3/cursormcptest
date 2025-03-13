import streamlit as st
import requests
import math

# Configure page settings
st.set_page_config(
    page_title="Advanced Calculator",
    page_icon="🧮",
    layout="centered"
)

# Add custom CSS
st.markdown("""
<style>
.stApp {
    max-width: 800px;
    margin: 0 auto;
}
.calculator-container {
    padding: 2rem;
    border-radius: 10px;
    background-color: #f0f2f6;
}
.result-container {
    padding: 1rem;
    background-color: white;
    border-radius: 5px;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# API endpoint
API_BASE_URL = "http://localhost:8000"

def make_api_request(endpoint, data):
    try:
        response = requests.post(f"{API_BASE_URL}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()["result"]
    except requests.exceptions.RequestException as e:
        if response.status_code == 400:
            return f"Error: {response.json()['detail']}"
        return f"Error: {str(e)}"

# Title and description
st.title("🧮 Advanced Calculator")
st.markdown("""
    Welcome to the Advanced Calculator! This application provides both basic 
    arithmetic operations and advanced mathematical functions.
""")

# Create tabs for different calculator modes
tab1, tab2 = st.tabs(["Basic Operations", "Advanced Operations"])

# Basic Operations Tab
with tab1:
    st.header("Basic Operations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, key="basic_num1")
    
    with col2:
        num2 = st.number_input("Enter second number", value=0.0, key="basic_num2")
    
    operation = st.selectbox(
        "Select operation",
        ["Add", "Subtract", "Multiply", "Divide", "Power"]
    )
    
    if st.button("Calculate", key="basic_calc"):
        data = {"a": num1, "b": num2}
        
        endpoint_map = {
            "Add": "add",
            "Subtract": "subtract",
            "Multiply": "multiply",
            "Divide": "divide",
            "Power": "power"
        }
        
        result = make_api_request(endpoint_map[operation], data)
        
        st.markdown("### Result")
        st.markdown(f"<div class='result-container'>{result}</div>", unsafe_allow_html=True)

# Advanced Operations Tab
with tab2:
    st.header("Advanced Operations")
    
    operation = st.selectbox(
        "Select operation",
        ["Square Root", "Factorial"]
    )
    
    number = st.number_input("Enter number", value=0.0, key="adv_num")
    
    if st.button("Calculate", key="adv_calc"):
        data = {"number": number}
        
        endpoint_map = {
            "Square Root": "square-root",
            "Factorial": "factorial"
        }
        
        result = make_api_request(endpoint_map[operation], data)
        
        st.markdown("### Result")
        st.markdown(f"<div class='result-container'>{result}</div>", unsafe_allow_html=True)

# Add information section
with st.expander("ℹ️ Information"):
    st.markdown("""
    ### Available Operations
    
    #### Basic Operations
    - **Add**: Adds two numbers
    - **Subtract**: Subtracts second number from first
    - **Multiply**: Multiplies two numbers
    - **Divide**: Divides first number by second
    - **Power**: Raises first number to the power of second
    
    #### Advanced Operations
    - **Square Root**: Calculates square root of a number
    - **Factorial**: Calculates factorial of a number
    
    ### Notes
    - Division by zero is not allowed
    - Square root of negative numbers is not allowed
    - Factorial only works with positive integers
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Made with ❤️ using Streamlit and FastAPI</p>
</div>
""", unsafe_allow_html=True)