import streamlit as st
from investor.tasks import GenerateReportTask, FetchFinancialDataTask
from investor.openai_model import OpenAIModel

# Set up the Streamlit app
st.title("AI Investment Agent")
st.caption("Compare the performance of two stocks and generate detailed reports using GPT-4.")

# Get OpenAI API key from user
openai_api_key = st.text_input("Enter OpenAI API Key", type="password")

if openai_api_key:
    # Initialize OpenAI model with API key
    openai_model = OpenAIModel(api_key=openai_api_key)

    # Input fields for the stocks to compare
    stock1 = st.text_input("Enter the first stock symbol")
    stock2 = st.text_input("Enter the second stock symbol")

    if stock1 and stock2:
        # Fetch financial data and generate report
        fetch_data_task = FetchFinancialDataTask(ticker1=stock1, ticker2=stock2)
        financial_data = fetch_data_task.execute()

        generate_report_task = GenerateReportTask(api_key=openai_api_key, stock1=stock1, stock2=stock2, financial_data=financial_data)
        report = generate_report_task.execute()

        st.write("**Generated Report:**")
        st.write(report)
