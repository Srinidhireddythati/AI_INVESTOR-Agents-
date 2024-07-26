import yfinance as yf
from investor.openai_model import OpenAIModel

class FetchFinancialDataTask:
    def __init__(self, ticker1, ticker2):
        self.ticker1 = ticker1
        self.ticker2 = ticker2

    def execute(self):
        ticker1 = yf.Ticker(self.ticker1)
        ticker2 = yf.Ticker(self.ticker2)
        data = {
            'ticker1': ticker1.info.get('regularMarketPreviousClose', 'N/A'),
            'ticker2': ticker2.info.get('regularMarketPreviousClose', 'N/A')
        }
        return data

class GenerateReportTask:
    def __init__(self, api_key, stock1, stock2, financial_data):
        self.api_key = api_key
        self.stock1 = stock1
        self.stock2 = stock2
        self.financial_data = financial_data
        self.openai_model = OpenAIModel(api_key=api_key)

    def execute(self):
        query = f"""
        Compare the performance of {self.stock1} and {self.stock2}. 
        Analyze their historical data, current market trends, analyst recommendations, and generate a comprehensive report highlighting key investment insights.
        
        Financial data:
        {self.stock1}: {self.financial_data['ticker1']}
        {self.stock2}: {self.financial_data['ticker2']}
        """
        return self.openai_model.generate_report(query)
