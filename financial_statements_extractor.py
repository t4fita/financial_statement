import yfinance as yf

# List of companies and tickers
tickers = {
    'AMZN': 'amazon',
    'BABA': 'alibaba'
}

# Function to fetch and export all financial statements
def fetch_and_export_financials(ticker, company_name):
    stock = yf.Ticker(ticker)

    # Fetching the financial statements
    income_statement = stock.financials.T
    balance_sheet = stock.balance_sheet.T
    cash_flow = stock.cashflow.T

    # Export to CSV files
    income_statement.to_csv(f'{company_name}_income_statement.csv')
    balance_sheet.to_csv(f'{company_name}_balance_sheet.csv')
    cash_flow.to_csv(f'{company_name}_cash_flow.csv')

    print(f"Financial data for {ticker} has been exported to {company_name}'s CSV files")

# Loop through the tickers and export their financial statements
for ticker, company_name in tickers.items():
    fetch_and_export_financials(ticker, company_name)
