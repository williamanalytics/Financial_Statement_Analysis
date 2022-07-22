import pandas as pd
import yfinance as yf
import streamlit as st
import datetime as dt


snp500 = pd.read_csv("constituents.csv")
symbols = snp500['Symbol'].sort_values().tolist()


ticker = st.sidebar.selectbox('Choose a S&P 500 Stock', symbols, index=3)

infoType = st.sidebar.radio(
    "Choose an info type",
    ('Fundamental Summary',
     'Quarterly Financials',
     'Quarterly Balance Sheet',
     'Quarterly Cashflow',
     'Quarterly Earnings',
     'Institutional Shareholders',
     'Analysts Recommendation')
)

if infoType == 'Fundamental Summary':

    if infoType == 'Fundamental Summary':
        stock = yf.Ticker(ticker)
        info = stock.info
        st.title('Company informations')
        st.subheader(info['longName'])
        st.markdown('**Sector**: ' + info['sector'])
        st.markdown('**Industry**: ' + info['industry'])
        st.markdown('**Website**: ' + info['website'])
        start = dt.datetime.today()
        df = yf.download(ticker, start).reset_index()
        df = float(df['Adj Close'][0])
        df = str(df)
        st.write('**The stock price is about:**'" " + df[:6] + " "'(USD)')

    fundInfo = {
        'Enterprise Value (USD)': info['enterpriseValue'],
        'Enterprise To Revenue Ratio': info['enterpriseToRevenue'],
        'Enterprise To Ebitda Ratio': info['enterpriseToEbitda'],
        'Net Income (USD)': info['netIncomeToCommon'],
        'Profit Margin Ratio': info['profitMargins'],
        'Forward PE Ratio': info['forwardPE'],
        'PEG Ratio': info['pegRatio'],
        'Price to Book Ratio': info['priceToBook'],
        'Forward EPS (USD)': info['forwardEps'],
        'Beta ': info['beta'],
        'Book Value (USD)': info['bookValue'],
        'Dividend Rate (%)': info['dividendRate'],
        'Five year Avg Dividend Yield (%)': info['fiveYearAvgDividendYield'],
        'Payout Ratio': info['payoutRatio'],
        'Free Cash flow': info['freeCashflow'],
        'Ebitda': info['ebitda'],
        'Ebitda Margins': info['ebitdaMargins'],
        'Earnings Growth': info['earningsGrowth'],
        'Gross Profits': info['grossProfits'],
        'Target Low Price': info['targetLowPrice'],
        'Return On Assets': info['returnOnAssets'],
        'Debt To Equity': info['debtToEquity'],
        'Current Ratio': info['currentRatio']
    }

    st.subheader('Fundamental Summary')
    fundDF = pd.DataFrame.from_dict(fundInfo, orient='index')
    fundDF = fundDF.rename(columns={0: 'Value'})
    st.table(fundDF)

    with st.expander("Explanation"):
        st.markdown("""**Enterprise Value**: It is a measure of a company's total value. EV includes in its calculation the market capitalization of a company but also 
            short-term and long-term debt as well as any cash on the company's balance sheet. Enterprise value is a popular metric used to value a company for a potential takeover.""")

        st.markdown("""**Enterprise To Revenue Ratio**:  is a measure of the value of a stock that compares a company's enterprise 
            value to its revenue. EV/R is one of several fundamental indicators that investors use to determine whether a stock is priced fairly.""")

        st.markdown("""**Enterprise To Ebitda Ratio**: is a ratio that compares a company’s Enterprise Value (EV) to its Earnings Before Interest, Taxes, Depreciation & Amortization (EBITDA).
            The EV/EBITDA ratio is commonly used as a valuation metric to compare the relative value of different businesses.""")

        st.markdown("""**Net Income**: It is an entity's income minus cost of goods sold, expenses, depreciation and amortization, interest, and taxes for an accounting period. It is computed as the residual of all revenues and gains less all expenses and losses 
            for the period, and has also been defined as the net increase in shareholders' equity that results from a company's operations.""")

        st.markdown("""**Profit Margin Ratio**: It is to gauge the degree to which a company or a business activity makes money. It represents what percentage of sales has turned into profits. Simply put, the percentage figure indicates how many cents of profit the business has generated for each dollar of sale.
            For instance, if a business reports that it achieved a 35% profit margin during the last quarter, it means that it had a net income of $0.35 for each dollar of sales generated.""")

        st.markdown(
            """**Forward PE Ratio**:  is a version of the ratio of price-to-earnings (P/E) that uses forecasted earnings for the P/E calculation.""")

        st.markdown("""**PEG Ratio**:  is a stock's price-to-earnings (P/E) ratio divided by the growth rate of its earnings for a specified time period. The PEG ratio is used to determine a stock's value while also factoring in 
            the company's expected earnings growth, and it is thought to provide a more complete picture than the more standard P/E ratio.""")

        st.markdown("""**Price to Book Ratio**: Companies use the price-to-book ratio (P/B ratio) to compare a firm's market capitalization to its book value. It's calculated by dividing the company's stock price per share by its book value per share (BVPS). An asset's book value is equal to 
            its carrying value on the balance sheet, and companies calculate it by netting the asset against its accumulated depreciation.""")

        st.markdown("""**Forward EPS**:  It involves making an estimation of a company’s upcoming earnings.Here’s how to calculate 
            the forward EPS: Divide the company’s current share price by the estimated future earnings per share.""")

        st.markdown("""**Beta**: Beta (β) is a measure of the volatility—or systematic risk—of a security or portfolio compared to the market as a whole (usually the S&P 500).
            Stocks with betas higher than 1.0 can be interpreted as more volatile than the S&P 500.""")

        st.markdown("""**Book Value**: It is equal to the cost of carrying an asset on a company's balance sheet, and firms calculate it netting the asset against its accumulated depreciation. As a result, book value can also be thought of as the net asset value (NAV) of a company, calculated as 
            its total assets minus intangible assets (patents, goodwill) and liabilities. For the initial outlay of an investment, book value may be net or gross of expenses such as trading costs, sales taxes, service charges, and so on.""")

        st.markdown("""**Dividend Rate**: It is the total expected dividend payments from an investment, fund or portfolio expressed on an annualized basis plus any additional non-recurring dividends 
            that an investor may receive during that period. """)

        st.markdown("""**Payout Ratio**: IT is a financial metric showing the proportion of earnings a company pays its 
            shareholders in the form of dividends, expressed as a percentage of the company's total earnings.""")

        st.markdown("""**Free Cash flow**: represents the cash a company generates after accounting for cash outflows to support operations and maintain its capital assets. Unlike earnings or net income, free cash flow is a measure of profitability that excludes the non-cash expenses of the income statement 
            and includes spending on equipment and assets as well as changes in working capital from the balance sheet.""")

        st.markdown(
            """**EBITDA**: EBITDA, or earnings before interest, taxes, depreciation, and amortization, is a measure of a company’s overall financial performance and is used as an alternative to net income in some circumstances.""")

        st.markdown("""**Ebitda Margins**: It is a measure of a company's operating profit as a percentage of its revenue. The acronym EBITDA stands for earnings before interest, taxes, depreciation, and amortization. Knowing the EBITDA margin allows
            for a comparison of one company's real performance to others in its industry. """)

        st.markdown(
            """**Earnings Growth**: It is the annual compound annual growth rate of earnings from investments.""")

        st.markdown("""**Gross Profits**: It is the profit a company makes after deducting the costs associated with making and selling its products, or the costs associated with providing its services. Gross profit will appear 
            on a company's income statement and can be calculated by subtracting the cost of goods sold (COGS) from revenue (sales).""")

        st.markdown("""**Target Price**:It is an analyst's projection of a security's future price.""")

        st.markdown("""**Return On Assets**: Refers to a financial ratio that indicates how profitable a company is in relation to its total assets. Corporate 
            management, analysts, and investors can use ROA to determine how efficiently a company uses its assets to generate a profit.
            The metric is commonly expressed as a percentage by using a company's net income and its average assets. A higher ROA means a company is more efficient
            and productive at managing its balance sheet to generate profits while a lower ROA indicates there is room for improvement.""")

        st.markdown("""**Debt To Equity**: It is used to evaluate a company's financial leverage and is calculated by dividing a company’s total liabilities by its shareholder equity. The D/E ratio is an important metric used in corporate finance.
            It is a measure of the degree to which a company is financing its operations through debt versus wholly owned funds.""")

        st.markdown("""**Current Ratio**: It is a liquidity ratio that measures a company’s ability to pay short-term obligations or those due within one year. It tells investors and analysts 
            how a company can maximize the current assets on its balance sheet to satisfy its current debt and other payables.
            In many cases, a company with a current ratio of less than 1.00 does not have the capital on hand to meet its short-term obligations if they were all due at once, while a current ratio 
            greater than 1.00 indicates that the company has the financial resources to remain solvent in the short term.""")

elif infoType == 'Quarterly Financials':

    if (infoType == 'Quarterly Financials'):
        stock = yf.Ticker(ticker)
        st.subheader("""**Quarterly financials** for """ + ticker)
        display_financials = (stock.quarterly_financials)
        if display_financials.empty == True:
            st.write("No data available at the moment")
        else:
            st.dataframe(display_financials, width=1000, height=500)
            pass


elif infoType == 'Quarterly Balance Sheet':

    if (infoType == 'Quarterly Balance Sheet'):
        stock = yf.Ticker(ticker)
        st.subheader("""**Quarterly Balance Sheet** for """ + ticker)
        display_balance = (stock.quarterly_balance_sheet)
        if display_balance.empty == True:
            st.write("No data available at the moment")
        else:
            st.dataframe(display_balance, width=1000, height=500)
            pass

elif infoType == 'Quarterly Cashflow':

    if (infoType == 'Quarterly Cashflow'):
        stock = yf.Ticker(ticker)
        st.subheader("""**Quarterly Cashflow** for """ + ticker)
        display_cash = (stock.quarterly_cashflow)
        if display_cash.empty == True:
            st.write("No data available at the moment")
        else:
            st.dataframe(display_cash, width=1200, height=500)
            pass

elif infoType == 'Quarterly Earnings':

    if (infoType == 'Quarterly Earnings'):
        stock = yf.Ticker(ticker)
        st.subheader("""**Quarterly Earnings** for """ + ticker)
        display_earnings = (stock.quarterly_earnings)
        if display_earnings.empty == True:
            st.write("No data available at the moment")
        else:
            st.table(display_earnings.style.highlight_max(axis=0))

            st.bar_chart(display_earnings)
            pass


elif infoType == 'Institutional Shareholders':

    if (infoType == 'Institutional Shareholders'):
        stock = yf.Ticker(ticker)
        st.subheader("""**Institutional Shareholders** for """ + ticker)
        display_shareholder = (stock.institutional_holders)
        if display_shareholder.empty == True:
            st.write("No data available at the moment")
        else:

            st.table(display_shareholder)

            pass


elif infoType == 'Analysts Recommendation':

    if (infoType == 'Analysts Recommendation'):
        stock = yf.Ticker(ticker)
        info = stock.info
        st.subheader("""**Analysts Recommendation** for """ + ticker)
        display_analyst = (stock.recommendations)
        if display_analyst.empty == True:
            st.write("No data available at the moment")
        else:
            st.info('**Recommendation**: ' + info['recommendationKey'])
            hide_dataframe_row_index = """
                        <style>
                        .row_heading.level0 {display:none}
                        .blank {display:none}
                        </style>
                        """
            st.table(data=display_analyst.tail(20))

            pass


