from crewai import Agent, Task, Crew
from tools import (
    fetch_stock_data,
    build_equal_weight_portfolio,
    optimize_portfolio,
    backtest_portfolio,
    compute_portfolio_metrics,
    format_markdown_report
)

# === Agents ===
data_agent = Agent(
    role='Data Agent',
    goal='Fetch historical stock data',
    backstory='Expert in financial APIs and data cleaning.',
    tools=[fetch_stock_data]
)

strategy_agent = Agent(
    role='Strategy Agent',
    goal='Build portfolio strategy based on user preference',
    backstory='Portfolio strategist familiar with equal-weight and optimized allocation.',
    tools=[build_equal_weight_portfolio, optimize_portfolio]
)

backtest_agent = Agent(
    role='Backtest Agent',
    goal='Backtest portfolio on historical prices',
    backstory='Skilled in financial simulations and return analysis.',
    tools=[backtest_portfolio]
)

analytics_agent = Agent(
    role='Analytics Agent',
    goal='Compute portfolio risk-adjusted metrics',
    backstory='Quantitative analyst expert in performance metrics.',
    tools=[compute_portfolio_metrics]
)

report_agent = Agent(
    role='Report Agent',
    goal='Create a final portfolio report in Markdown',
    backstory='Writes clean, readable financial summaries.',
    tools=[format_markdown_report]
)

# === Workflow Inputs ===
tickers = ['AAPL', 'MSFT', 'GOOGL']
strategy_choice = 'optimized'  # or 'equal'

# === Tasks ===
task1 = Task(
    description=f"Download and return stock data from 2020-01-01 to 2024-12-31 for: {', '.join(tickers)}.",
    expected_output="List of CSV strings for each ticker.",
    agent=data_agent
)

task2 = Task(
    description=f"Build a {strategy_choice} portfolio for: {', '.join(tickers)}.",
    expected_output="Dictionary of weights for each ticker.",
    agent=strategy_agent
)

task3 = Task(
    description="Backtest the portfolio using the historical stock price CSVs and computed weights.",
    expected_output="CSV string of portfolio daily returns.",
    agent=backtest_agent
)

task4 = Task(
    description="Compute Sharpe Ratio, Sortino Ratio, and Max Drawdown from the backtest data.",
    expected_output="String summary of portfolio metrics.",
    agent=analytics_agent
)

task5 = Task(
    description="Write a final report in Markdown including metrics, strategy, and assets.",
    expected_output="Formatted Markdown string.",
    agent=report_agent
)

# === Crew ===
crew = Crew(
    agents=[data_agent, strategy_agent, backtest_agent, analytics_agent, report_agent],
    tasks=[task1, task2, task3, task4, task5],
    verbose=True
)

# === Run It ===
if __name__ == "__main__":
    result = crew.kickoff(inputs={'tickers': tickers, 'strategy_choice': strategy_choice})
    print("\n\n📄 Final Portfolio Report:\n")
    print(result)
