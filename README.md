Author: Jackie Zhang
Course: ACC102 Artificial Intelligence-Driven Data Analytics
Track: Track 4 - Interactive Data Analysis Tool
Product Link: [粘贴你的 Streamlit 部署链接，例如 https://xxx.streamlit.app]

1. Product Overview

This interactive dashboard is designed for financial analysts to evaluate the performance of leading Quick Service Restaurants (QSRs): McDonald's, Yum! Brands, Starbucks, and Shake Shack.

While raw financial statements can be overwhelming, this tool transforms complex WRDS data into intuitive visualizations. It enables users to compare companies across four key dimensions of financial health: profitability, efficiency, and financial structure.

2. Technical Workflow (ACC102 Core Skills)
This project serves as a comprehensive application of the Python and Data Analytics skills covered in the ACC102 curriculum:
•Data Acquisition (Week 5-6): Used wrds.Connection and Parameterised SQL with f-strings to securely and flexibly retrieve data from the comp.funda library.
•Data Cleaning (Week 6): Implemented the dict(zip()) method for efficient column renaming, converting cryptic WRDS identifiers (e.g., sale, at, ceq) into readable business terms.
•Robust Logic: Handled the "Negative Equity Trap" using Python lambda functions. This prevents misleading calculations (like negative ROE) for companies with massive share buybacks (e.g., MCD, SBUX).
•Interactive UI: Built with Streamlit, featuring dynamic filtering (st.multiselect) and synchronized charting to enhance user experience.

3. Financial Metrics Calculated
The dashboard computes the four core ratios taught in the Week 6 Practical:
	1.Profit Margin (%): Net Income / Revenue
	2.Asset Turnover: Revenue / Total Assets
	3.ROE (%): Net Income / Total Equity (Cleaned for negative equity)
	4.Leverage: Total Assets / Total Equity (Cleaned for negative equity)
4. How to Run Locally
If you wish to run the source code on your local machine:
	1.Install Dependencies:

	2.Run the App:
Navigate to the project folder and execute:

	3.Data Source: The app automatically loads the pre-processed qsr_financials.csv included in this repository.

5. File Structure
•app.py: The main frontend application file.
•data_prep.ipynb: Backend Jupyter Notebook showing the full SQL extraction and cleaning process.
•qsr_financials.csv: The cleaned dataset ready for analysis.
•Reflection_Report.pdf: Detailed project reflection and AI disclosure.