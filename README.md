# financial_statement
This Python script demonstrates how to fetch financial statements (Income Statement, Balance Sheet, Cash Flow) for companies using the yfinance library. For this example, it retrieves data for Amazon (AMZN) and Alibaba (BABA), but it can be easily adapted for other companies.

Here's a more concise version of the **description** and **README.md** that conveys the idea that Amazon and Alibaba were chosen as examples.

---

### **Description:**

This Python script demonstrates how to fetch financial statements (Income Statement, Balance Sheet, Cash Flow) for companies using the `yfinance` library. For this example, it retrieves data for Amazon (AMZN) and Alibaba (BABA), but it can be easily adapted for other companies.

The script exports the financial data into separate CSV files for each company.

---

### **README.md**

```markdown
# Financial Statements Example

This is a simple Python script that demonstrates how to fetch financial data using the `yfinance` library. For this example, we use **Amazon (AMZN)** and **Alibaba (BABA)** as sample companies, but you can modify the script to retrieve data for any other company.

## Requirements

- **Python 3.x**
- `yfinance` library

### Install `yfinance`:

```

```bash
pip install yfinance
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/t4fita/financial_statement.git
   ```

2. Navigate to the project directory:
   ```bash
   cd financial-statement
   ```

3. Run the script:
   ```bash
   python financial_statements_extractor.py
   ```

4. The script will generate CSV files containing financial data for Amazon and Alibaba:
    - Income Statement
    - Balance Sheet
    - Cash Flow Statement

## Output Files

For each company, three CSV files will be created:
- `amazon_income_statement.csv`
- `amazon_balance_sheet.csv`
- `amazon_cash_flow.csv`
- `alibaba_income_statement.csv`
- `alibaba_balance_sheet.csv`
- `alibaba_cash_flow.csv`

## Example Use

This script is a basic example to show how financial data can be fetched and exported using Python. You can easily modify it to get data for other companies by entering their tickers and the corresponding name.

## License

This project is licensed under the MIT License.
```
