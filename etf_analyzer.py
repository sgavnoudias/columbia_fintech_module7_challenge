#!/usr/bin/env python
# coding: utf-8

# # Create a Web Application for an ETF Analyzer
# 
# In this Challenge assignment, you’ll build a financial database and web application by using SQL, Python, and the Voilà library to analyze the performance of a hypothetical fintech ETF.
# 
# Instructions: 
# 
# Use this notebook to complete your analysis of a fintech ETF that consists of four stocks: GOST, GS, PYPL, and SQ. Each stock has its own table in the `etf.db` database, which the `Starter_Code` folder also contains.
# 
# Analyze the daily returns of the ETF stocks both individually and as a whole. Then deploy the visualizations to a web application by using the Voilà library.
# 
# The detailed instructions are divided into the following parts:
# 
# * Analyze a single asset in the ETF
# 
# * Optimize data access with Advanced SQL queries
# 
# * Analyze the ETF portfolio
# 
# * Deploy the notebook as a web application
# 
# #### Analyze a Single Asset in the ETF
# 
# For this part of the assignment, you’ll use SQL queries with Python, Pandas, and hvPlot to analyze the performance of a single asset from the ETF.
# 
# Complete the following steps:
# 
# 1. Write a SQL `SELECT` statement by using an f-string that reads all the PYPL data from the database. Using the SQL `SELECT` statement, execute a query that reads the PYPL data from the database into a Pandas DataFrame.
# 
# 2. Use the `head` and `tail` functions to review the first five and the last five rows of the DataFrame. Make a note of the beginning and end dates that are available from this dataset. You’ll use this information to complete your analysis.
# 
# 3. Using hvPlot, create an interactive visualization for the PYPL daily returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 
# 4. Using hvPlot, create an interactive visualization for the PYPL cumulative returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 
# #### Optimize Data Access with Advanced SQL Queries
# 
# For this part of the assignment, you’ll continue to analyze a single asset (PYPL) from the ETF. You’ll use advanced SQL queries to optimize the efficiency of accessing data from the database.
# 
# Complete the following steps:
# 
# 1. Access the closing prices for PYPL that are greater than 200 by completing the following steps:
# 
#     - Write a SQL `SELECT` statement to select the dates where the PYPL closing price was higher than 200.0.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 
#     - Select the “time” and “close” columns for those dates where the closing price was higher than 200.0.
# 
# 2. Find the top 10 daily returns for PYPL by completing the following steps:
# 
#     -  Write a SQL statement to find the top 10 PYPL daily returns. Make sure to do the following:
# 
#         * Use `SELECT` to select only the “time” and “daily_returns” columns.
# 
#         * Use `ORDER` to sort the results in descending order by the “daily_returns” column.
# 
#         * Use `LIMIT` to limit the results to the top 10 daily return values.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 
# #### Analyze the ETF Portfolio
# 
# For this part of the assignment, you’ll build the entire ETF portfolio and then evaluate its performance. To do so, you’ll build the ETF portfolio by using SQL joins to combine all the data for each asset.
# 
# Complete the following steps:
# 
# 1. Write a SQL query to join each table in the portfolio into a single DataFrame. To do so, complete the following steps:
# 
#     - Use a SQL inner join to join each table on the “time” column. Access the “time” column in the `GDOT` table via the `GDOT.time` syntax. Access the “time” columns from the other tables via similar syntax.
# 
#     - Using the SQL query, read the data from the database into a Pandas DataFrame. Review the resulting DataFrame.
# 
# 2. Create a DataFrame that averages the “daily_returns” columns for all four assets. Review the resulting DataFrame.
# 
#     > **Hint** Assuming that this ETF contains equally weighted returns, you can average the returns for each asset to get the average returns of the portfolio. You can then use the average returns of the portfolio to calculate the annualized returns and the cumulative returns. For the calculation to get the average daily returns for the portfolio, use the following code:
#     >
#     > ```python
#     > etf_portfolio_returns = etf_portfolio['daily_returns'].mean(axis=1)
#     > ```
#     >
#     > You can use the average daily returns of the portfolio the same way that you used the daily returns of a single asset.
# 
# 3. Use the average daily returns in the `etf_portfolio_returns` DataFrame to calculate the annualized returns for the portfolio. Display the annualized return value of the ETF portfolio.
# 
# > **Hint**  To calculate the annualized returns, multiply the mean of the `etf_portfolio_returns` values by 252.
# >
# > To convert the decimal values to percentages, multiply the results by 100.
# 
# 4. Use the average daily returns in the `etf_portfolio_returns` DataFrame to calculate the cumulative returns of the ETF portfolio.
# 
# 5. Using hvPlot, create an interactive line plot that visualizes the cumulative return values of the ETF portfolio. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 
# #### Deploy the Notebook as a Web Application
# 
# For this part of the assignment, complete the following steps:
# 
# 1. Use the Voilà library to deploy your notebook as a web application. You can deploy the web application locally on your computer.
# 
# 2. Take a screen recording or screenshots to show how the web application appears when using Voilà. Include the recording or screenshots in the `README.md` file for your GitHub repository.
# 

# ## Review the following code which imports the required libraries, initiates your SQLite database, popluates the database with records from the `etf.db` seed file that was included in your Starter_Code folder, creates the database engine, and confirms that data tables that it now contains.

# In[ ]:


# Importing the required libraries and dependencies
import numpy as np
import pandas as pd
import hvplot.pandas
import sqlalchemy

import warnings
warnings.filterwarnings('ignore')


# In[ ]:


# Create a temporary SQLite database and populate the database with content from the etf.db seed file
database_connection_string = 'sqlite:///etf.db'

# Create an engine to interact with the SQLite database
engine = sqlalchemy.create_engine(database_connection_string)

# Confirm that table names contained in the SQLite database.
engine.table_names()


# ## Analyze a single asset in the FinTech ETF
# 
# For this part of the assignment, you’ll use SQL queries with Python, Pandas, and hvPlot to analyze the performance of a single asset from the ETF.
# 
# Complete the following steps:
# 
# 1. Write a SQL `SELECT` statement by using an f-string that reads all the PYPL data from the database. Using the SQL `SELECT` statement, execute a query that reads the PYPL data from the database into a Pandas DataFrame.
# 
# 2. Use the `head` and `tail` functions to review the first five and the last five rows of the DataFrame. Make a note of the beginning and end dates that are available from this dataset. You’ll use this information to complete your analysis.
# 
# 3. Using hvPlot, create an interactive visualization for the PYPL daily returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 
# 4. Using hvPlot, create an interactive visualization for the PYPL cumulative returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 
# 

# ### Step 1: Write a SQL `SELECT` statement by using an f-string that reads all the PYPL data from the database. Using the SQL `SELECT` statement, execute a query that reads the PYPL data from the database into a Pandas DataFrame.

# In[ ]:


# Write a SQL query to SELECT all of the data from the PYPL table
query = f"""
SELECT * FROM pypl
"""

# Use the query to read the PYPL data into a Pandas DataFrame
pypl_dataframe = pd.read_sql_query(query, engine)

# Remvove 0 timestamps from the 'time' column, keep only dates
pypl_dataframe['time'] = pd.to_datetime(pypl_dataframe['time'])
# Set the index column to 'time'
pypl_dataframe = pypl_dataframe.set_index('time')


# ### Step 2: Use the `head` and `tail` functions to review the first five and the last five rows of the DataFrame. Make a note of the beginning and end dates that are available from this dataset. You’ll use this information to complete your analysis.

# In[ ]:


# View the first 5 rows of the DataFrame.
display(pypl_dataframe.head())


# In[ ]:


# View the last 5 rows of the DataFrame.
display(pypl_dataframe.tail())


# ### Step 3: Using hvPlot, create an interactive visualization for the PYPL daily returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.

# In[ ]:


# Create an interactive visualization with hvplot to plot the daily returns for PYPL.
pypl_dataframe['daily_returns'].hvplot.line(
    x = 'time',
    xlabel = "Time",
    y = 'daily_returns',
    ylabel = "Daily Returns",
    title = "(PYLP) Daily Returns",
    frame_width = 700,
    frame_height = 300    
).opts(
     yformatter='%.04f'
)


# ### Step 4: Using hvPlot, create an interactive visualization for the PYPL cumulative returns. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.

# In[ ]:


# Create an interactive visaulization with hvplot to plot the cumulative returns for PYPL.

#Calculate the cumalitive returns (from the 'daily_returns' column)
pypl_dataframe_cum_returns = (1 + pypl_dataframe['daily_returns']).cumprod() - 1

# Interactive plot
pypl_dataframe_cum_returns.hvplot.line(
    xlabel = "Time",
    ylabel = "Cumulative Returns",
    title = "(PYLP) Cumulative Returns",
    frame_width = 700,
    frame_height = 300    
).opts(
     yformatter='%.02f'
)


# ## Optimize the SQL Queries
# 
# For this part of the assignment, you’ll continue to analyze a single asset (PYPL) from the ETF. You’ll use advanced SQL queries to optimize the efficiency of accessing data from the database.
# 
# Complete the following steps:
# 
# 1. Access the closing prices for PYPL that are greater than 200 by completing the following steps:
# 
# 1. Access the closing prices for PYPL that are greater than 200 by completing the following steps:
# 
#     - Write a SQL `SELECT` statement to select the dates where the PYPL closing price was higher than 200.0.
# 
#     - Select the “time” and “close” columns for those dates where the closing price was higher than 200.0.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 
# 2. Find the top 10 daily returns for PYPL by completing the following steps:
# 
#     -  Write a SQL statement to find the top 10 PYPL daily returns. Make sure to do the following:
# 
#         * Use `SELECT` to select only the “time” and “daily_returns” columns.
# 
#         * Use `ORDER` to sort the results in descending order by the “daily_returns” column.
# 
#         * Use `LIMIT` to limit the results to the top 10 daily return values.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 

# ### Step 1: Access the closing prices for PYPL that are greater than 200 by completing the following steps:
# 
#     - Write a SQL `SELECT` statement to select the dates where the PYPL closing price was higher than 200.0.
# 
#     - Select the “time” and “close” columns for those dates where the closing price was higher than 200.0.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 

# In[ ]:


# Write a SQL SELECT statement to select the time and close columns 
# where the PYPL closing price was higher than 200.0.
query = f"""
SELECT time, close FROM pypl
WHERE close > 200.0
"""

# Using the query, read the data from the database into a Pandas DataFrame
pypl_higher_than_200 =  pd.read_sql_query(query, engine)

# Remvove 0 timestamps from the 'time' column, keep only dates
pypl_higher_than_200['time'] = pd.to_datetime(pypl_higher_than_200['time'])
# Set the index column to 'time'
pypl_higher_than_200 = pypl_higher_than_200.set_index('time')

# Review the resulting DataFrame
display(pypl_higher_than_200)


# ### Step 2: Find the top 10 daily returns for PYPL by completing the following steps:
# 
#     -  Write a SQL statement to find the top 10 PYPL daily returns. Make sure to do the following:
# 
#         * Use `SELECT` to select only the “time” and “daily_returns” columns.
# 
#         * Use `ORDER` to sort the results in descending order by the “daily_returns” column.
# 
#         * Use `LIMIT` to limit the results to the top 10 daily return values.
# 
#     - Using the SQL statement, read the data from the database into a Pandas DataFrame, and then review the resulting DataFrame.
# 

# In[ ]:


# Write a SQL SELECT statement to select the time and daily_returns columns
# Sort the results in descending order and return only the top 10 return values
query = f"""
SELECT time, daily_returns FROM pypl
ORDER BY daily_returns DESC
LIMIT 10 
"""

# Using the query, read the data from the database into a Pandas DataFrame
pypl_top_10_returns = pd.read_sql_query(query, engine)

# Remvove 0 timestamps from the 'time' column, keep only dates
pypl_top_10_returns['time'] = pd.to_datetime(pypl_top_10_returns['time'])
# Set the index column to 'time'
pypl_top_10_returns = pypl_top_10_returns.set_index('time')

# Review the resulting DataFrame
display(pypl_top_10_returns)


# ## Analyze the Fintech ETF Portfolio
# 
# For this part of the assignment, you’ll build the entire ETF portfolio and then evaluate its performance. To do so, you’ll build the ETF portfolio by using SQL joins to combine all the data for each asset.
# 
# Complete the following steps:
# 
# 1. Write a SQL query to join each table in the portfolio into a single DataFrame. To do so, complete the following steps:
# 
#     - Use a SQL inner join to join each table on the “time” column. Access the “time” column in the `GDOT` table via the `GDOT.time` syntax. Access the “time” columns from the other tables via similar syntax.
# 
#     - Using the SQL query, read the data from the database into a Pandas DataFrame. Review the resulting DataFrame.
# 
# 2. Create a DataFrame that averages the “daily_returns” columns for all four assets. Review the resulting DataFrame.
# 
#     > **Hint** Assuming that this ETF contains equally weighted returns, you can average the returns for each asset to get the average returns of the portfolio. You can then use the average returns of the portfolio to calculate the annualized returns and the cumulative returns. For the calculation to get the average daily returns for the portfolio, use the following code:
#     >
#     > ```python
#     > etf_portfolio_returns = etf_portfolio['daily_returns'].mean(axis=1)
#     > ```
#     >
#     > You can use the average daily returns of the portfolio the same way that you used the daily returns of a single asset.
# 
# 3. Use the average daily returns in the `etf_portfolio_returns` DataFrame to calculate the annualized returns for the portfolio. Display the annualized return value of the ETF portfolio.
# 
# > **Hint**  To calculate the annualized returns, multiply the mean of the `etf_portfolio_returns` values by 252.
# >
# > To convert the decimal values to percentages, multiply the results by 100.
# 
# 4. Use the average daily returns in the `etf_portfolio_returns` DataFrame to calculate the cumulative returns of the ETF portfolio.
# 
# 5. Using hvPlot, create an interactive line plot that visualizes the cumulative return values of the ETF portfolio. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.
# 

# ### Step 1: Write a SQL query to join each table in the portfolio into a single DataFrame. To do so, complete the following steps:
# 
#     - Use a SQL inner join to join each table on the “time” column. Access the “time” column in the `GDOT` table via the `GDOT.time` syntax. Access the “time” columns from the other tables via similar syntax.
# 
#     - Using the SQL query, read the data from the database into a Pandas DataFrame. Review the resulting DataFrame.

# In[ ]:


# First, lets review all the individual asset dataframes...

query = f"""
SELECT * FROM gdot
"""
GDOT_dataframe = pd.read_sql_query(query, engine)
display(GDOT_dataframe.tail())

query = f"""
SELECT * FROM gs
"""
GS_dataframe = pd.read_sql_query(query, engine)
display(GS_dataframe.tail())

query = f"""
SELECT * FROM pypl
"""
PYPL_dataframe = pd.read_sql_query(query, engine)
display(PYPL_dataframe.tail())

query = f"""
SELECT * FROM sq
"""
SQ_dataframe = pd.read_sql_query(query, engine)
display(SQ_dataframe.tail())


# In[ ]:


# Method #1: Select all columns from each asset

# Wreate a SQL query to join each table in the portfolio into a single DataFrame 
# Use the time column from each table as the basis for the join
query = f"""
SELECT * FROM gdot
INNER JOIN gs   ON gdot.time = gs.time
INNER JOIN pypl ON gdot.time = pypl.time
INNER JOIN sq   ON gdot.time = sq.time    
"""

# Using the query, read the data from the database into a Pandas DataFrame
etf_portfolio = pd.read_sql_query(query, engine)

# Remove redundant time columns
etf_portfolio = etf_portfolio.T.drop_duplicates().T

# Remvove 0 timestamps from the 'time' column, keep only dates
etf_portfolio['time'] = pd.to_datetime(etf_portfolio['time'])
# Set the index column to 'time'
etf_portfolio = etf_portfolio.set_index('time')

# Since each of the portfolios have the same column names (open, high, close, etc.), renaming the columns prepending asset names
# Create heirarchical columns names based on symbol
columns = [('GDOT','open'), ('GDOT','high'), ('GDOT','low'), ('GDOT','close'), ('GDOT','volume'), ('GDOT','daily_returns'),
           ('GS','open'),   ('GS','high'),   ('GS','low'),   ('GS','close'),   ('GS','volume'),   ('GS','daily_returns'),
           ('PYPL','open'), ('PYPL','high'), ('PYPL','low'), ('PYPL','close'), ('PYPL','volume'), ('PYPL','daily_returns'),
           ('SQ','open'),   ('SQ','high'),   ('SQ','low'),   ('SQ','close'),   ('SQ','volume'),   ('SQ','daily_returns')]                                           
etf_portfolio.columns = pd.MultiIndex.from_tuples(columns)

# Review the resulting DataFrame
display(etf_portfolio)


# In[ ]:


# Method #2: Filter out time from only one of the portfolios, and select which columns from each asset to extract

# Wreate a SQL query to join each table in the portfolio into a single DataFrame 
# Use the time column from each table as the basis for the join
query = f"""
SELECT 
    gdot.time, gdot.open, gdot.high, gdot.low, gdot.close, gdot.volume, gdot.daily_returns,
               gs.open,   gs.high,   gs.low,   gs.close,   gs.volume,   gs.daily_returns,
               pypl.open, pypl.high, pypl.low, pypl.close, pypl.volume, pypl.daily_returns,
               sq.open,   sq.high,   gdot.low, sq.close,   sq.volume,   sq.daily_returns
FROM gdot
INNER JOIN gs   ON gdot.time = gs.time
INNER JOIN pypl ON gdot.time = pypl.time
INNER JOIN sq   ON gdot.time = sq.time    
"""

# Using the query, read the data from the database into a Pandas DataFrame
etf_portfolio = pd.read_sql_query(query, engine)

# Remvove 0 timestamps from the 'time' column, keep only dates
etf_portfolio['time'] = pd.to_datetime(etf_portfolio['time'])
# Set the index column to 'time'
etf_portfolio = etf_portfolio.set_index('time')

# Since each of the portfolios have the same column names (open, high, close, etc.), renaming the columns prepending asset names
# Create heirarchical columns names based on symbol
columns = [('GDOT','open'), ('GDOT','high'), ('GDOT','low'), ('GDOT','close'), ('GDOT','volume'), ('GDOT','daily_returns'),
           ('GS','open'),   ('GS','high'),   ('GS','low'),   ('GS','close'),   ('GS','volume'),   ('GS','daily_returns'),
           ('PYPL','open'), ('PYPL','high'), ('PYPL','low'), ('PYPL','close'), ('PYPL','volume'), ('PYPL','daily_returns'),
           ('SQ','open'),   ('SQ','high'),   ('SQ','low'),   ('SQ','close'),   ('SQ','volume'),   ('SQ','daily_returns')]                                           
etf_portfolio.columns = pd.MultiIndex.from_tuples(columns)

display(etf_portfolio)


# ### Step 2: Create a DataFrame that averages the “daily_returns” columns for all four assets. Review the resulting DataFrame.

# In[ ]:


# Create a DataFrame that displays the mean value of the “daily_returns” columns for all four assets.

#  Filter via SQL
query = f"""
SELECT 
    gdot.time, gdot.daily_returns,
               gs.daily_returns,
               pypl.daily_returns,
               sq.daily_returns
FROM gdot
INNER JOIN gs   ON gdot.time = gs.time
INNER JOIN pypl ON gdot.time = pypl.time
INNER JOIN sq   ON gdot.time = sq.time    
"""
# Using the query, read the data from the database into a Pandas DataFrame
etf_portfolio_returns_sql = pd.read_sql_query(query, engine)
# Remvove 0 timestamps from the 'time' column, keep only dates
etf_portfolio_returns_sql['time'] = pd.to_datetime(etf_portfolio_returns_sql['time'])
# Set the index column to 'time'
etf_portfolio_returns_sql = etf_portfolio_returns_sql.set_index('time')

# Choose method #2 (SQL) approach (preferred to filter via SQL)
etf_portfolio_returns = etf_portfolio_returns_sql

# Since each of the portfolios have the same column names (daily returns), renaming the columns prepending the asset names.
#etf_portfolio_returns.columns = ['GDOT_daily_returns', 'GS_daily_returns', 'PYPL_daily_returns', 'SQ_daily_returns']
columns = [('GDOT','daily_returns',), ('GS','daily_returns',), ('PYPL','daily_returns',), ('SQ','daily_returns',)] 
etf_portfolio_returns.columns = pd.MultiIndex.from_tuples(columns)

# Add a column to the etf portfolio dataframe to include the mean daily returns
etf_portfolio_returns[('ETF','mean_daily_returns',)] = etf_portfolio_returns.mean(axis=1)

# Review the resulting DataFrame
display(etf_portfolio_returns)


# ### Step 3: Use the average daily returns in the etf_portfolio_returns DataFrame to calculate the annualized returns for the portfolio. Display the annualized return value of the ETF portfolio.

# In[ ]:


# Use the average daily returns provided by the etf_portfolio_returns DataFrame 
# to calculate the annualized return for the portfolio. 
annualized_etf_portfolio_returns = etf_portfolio_returns['ETF']['mean_daily_returns'] * 252

# Convert decimal to percentages (multiply by 100)
annualized_etf_portfolio_returns_percent = annualized_etf_portfolio_returns * 100

# Display the annualized return value of the ETF portfolio.
display(annualized_etf_portfolio_returns_percent)

# Add a column to the etf portfolio dataframe to include the annualized mean daily returns
etf_portfolio_returns[('ETF','ann_mean_daily_returns_per')] = annualized_etf_portfolio_returns_percent
display(etf_portfolio_returns)


# ### Step 4: Use the average daily returns in the `etf_portfolio_returns` DataFrame to calculate the cumulative returns of the ETF portfolio.

# In[ ]:


# Use the average daily returns provided by the etf_portfolio_returns DataFrame 
# to calculate the cumulative returns
etf_cumulative_returns = (1 + etf_portfolio_returns['ETF']['mean_daily_returns']).cumprod() - 1

# Display the final cumulative return value
display(etf_cumulative_returns)

# Add a column to the etf portfolio dataframe to include the cumulative returns
etf_portfolio_returns[('ETF','cum_returns')] = etf_cumulative_returns
display(etf_portfolio_returns)


# ### Step 5: Using hvPlot, create an interactive line plot that visualizes the cumulative return values of the ETF portfolio. Reflect the “time” column of the DataFrame on the x-axis. Make sure that you professionally style and format your visualization to enhance its readability.

# In[ ]:


# Create an interactive visualization with hvplot to plot the daily returns for PYPL.
# Create a dataframe of the individual dataframe asset daily returns
asset_daily_returns_df = pd.concat([etf_portfolio_returns.iloc[:,0], etf_portfolio_returns.iloc[:,1], etf_portfolio_returns.iloc[:,2], etf_portfolio_returns.iloc[:,3]], axis=1)
asset_daily_returns_df.columns = ['GDOT',' GS', 'PYPL', 'SQ']

asset_daily_returns_df.hvplot.line(
    xlabel = "Time",
    ylabel = "Cumulative Returns",
    title = "(GDOT, GS, PYPL, SQ) Daily Returns",
    frame_width = 700,
    frame_height = 300    
).opts(
     yformatter='%.02f'
)


# In[ ]:


# Create an interactive visaulization with hvplot to plot the cumulative returns for PYPL.

etf_cumulative_return_ppyls = (1 + asset_daily_returns_df).cumprod() - 1

etf_cumulative_return_ppyls.hvplot.line(
    xlabel = "Time",
    ylabel = "Cumulative Returns",
    title = "(GDOT, GS, PYPL, SQ) Cumulative Returns",
    frame_width = 700,
    frame_height = 300    
).opts(
     yformatter='%.02f'
)


# In[ ]:


# Using hvplot, create an interactive line plot that visualizes the ETF portfolios cumulative return values.
etf_portfolio_returns['ETF']['cum_returns'].hvplot.line(
    xlabel = "Time",
    ylabel = "Cumulative Returns",
    title = "ETF Cumulative Returns",
    frame_width = 700,
    frame_height = 300    
).opts(
     yformatter='%.02f'
)


# In[ ]:




