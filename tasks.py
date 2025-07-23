from crewai import Task

# Define tasks
data_task = Task(
    agent=data_agent,
    description="Fetch historical price data for ['TCS.NS', 'INFY.NS', 'RELIANCE.NS', 'HDFCBANK.NS'] between 2020-01-01 and 2024-12-31.",
    expected_output="CSV strings of historical price data"
)

strategy_task = Task(
    agent=strategy_agent,
    description="Build an equal-weighted portfolio strategy for the above stocks.",
    expected_output="Dictionary of weights per stock"
)

backtest_task = Task(
    agent=backtest_agent,
    description="Backtest the portfolio using the historical data and weights.",
    expected_output="CSV string of portfolio returns"
)

analytics_task = Task(
    agent=analytics_agent,
    description="Compute portfolio metrics like Sharpe Ratio, Sortino Ratio, and Maximum Drawdown.",
    expected_output="Text summary of key performance metrics"
)

report_task = Task(
    agent=report_agent,
    description="Format the metrics and strategy summary into a clean Markdown report.",
    expected_output="A well-formatted markdown report"
)

education_task = Task(
    agent=UserEducationAgent,
    description="Explain the terms Sharpe Ratio, Sortino Ratio, and Max Drawdown in simple language.",
    expected_output="Easy-to-understand explanation of key finance concepts"
)
