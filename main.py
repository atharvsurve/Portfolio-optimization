# main_app.py
import streamlit as st
from lm_prompts import run_model_on_stock
from stock_analysis import get_stock_returns, plot_daily_returns

st.set_page_config(page_title="LM Studio Indian Stock Portfolio AI", layout="wide")
st.title("📊 Indian Stock Portfolio + LLM Analysis")

st.markdown("""
Enter Indian stock symbols (e.g., `RELIANCE.NS`, `TCS.NS`) one per line.
You'll get:
- Daily return plot (only for "overview")
- LLM-powered explanation
""")

stock_list = st.text_area("Enter stock symbols:", height=200).splitlines()

operation = st.selectbox("Choose the type of LLM analysis:", [
    "overview",
    "volatility_analysis",
    "compare_with_sector",
    "news_summary",
    "long_term_prospects"
])

if st.button("Run Analysis"):
    if not stock_list:
        st.warning("Please enter stock symbols first.")
    else:
        st.success(f"Running analysis for {len(stock_list)} stocks...")

        for stock in stock_list:
            st.markdown(f"---\n### 📈 {stock.upper()}")

            # Only fetch and show plot if 'overview' is selected
            if operation == "overview":
                try:
                    returns = get_stock_returns(stock)
                    plot_path = plot_daily_returns(returns, stock.replace(".", "_"))
                    st.image(plot_path, caption=f"{stock.upper()} Daily Returns")
                except Exception as e:
                    st.error(f"Could not load or plot data for {stock}: {e}")
                    continue

            # Get LLM explanation
            with st.spinner(f"LLM analyzing {stock}..."):
                result = run_model_on_stock(stock, operation , "explain the graphs in detail and hwy is there a dip or rise in the graph , give the corresponding news and reason for it ")
                st.markdown("**🧠 LLM Explanation:**")
                st.write(result)
