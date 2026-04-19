import streamlit as st
import pandas as pd

# 1. 网页配置
st.set_page_config(page_title="ACC102 QSR Dashboard", layout="wide")
st.title("🍔 Global Fast-Food Financial Dashboard")
st.write("An interactive tool to analyze the financial efficiency of top QSRs.")

# 2. 读取数据
@st.cache_data
def load_data():
    # 确保你的 csv 文件名在 GitHub 里也是这个名字
    df = pd.read_csv('qsr_financials.csv')
    
    # 计算关键财务比率 (Task 2 & 3 核心逻辑)
    df['Profit Margin (%)'] = (df['Net_Income'] / df['Revenue']) * 100
    df['Asset Turnover'] = df['Revenue'] / df['Total_Assets']
    
    # 处理 MCD 权益为负的情况：如果 Equity <= 0，ROE 设为 0 或 NaN 避免图表拉跨
    df['ROE (%)'] = df.apply(lambda x: (x['Net_Income'] / x['Equity'] * 100) if x['Equity'] > 0 else 0, axis=1)
    return df

try:
    df = load_data()

    # 3. 侧边栏交互设计
    st.sidebar.header("Filter Options")
    all_companies = df['Company'].unique()
    selected_companies = st.sidebar.multiselect("Select Companies", options=all_companies, default=all_companies)
    
    metrics = ["Profit Margin (%)", "Asset Turnover", "ROE (%)"]
    selected_metric = st.sidebar.selectbox("Select Financial Metric", options=metrics)

    # 4. 根据用户选择过滤数据
    filtered_df = df[df['Company'].isin(selected_companies)]

    # 5. 动态图表展示
    st.subheader(f"Visualizing {selected_metric} over Time")
    if not filtered_df.empty:
        # 转换成 Streamlit 绘图专用格式
        chart_data = filtered_df.pivot(index='Year', columns='Company', values=selected_metric)
        st.line_chart(chart_data)
    else:
        st.warning("Please select at least one company in the sidebar.")

    # 6. 数据原始表格
    st.subheader("Raw Data Summary")
    st.dataframe(filtered_df)

except Exception as e:
    st.error(f"Error loading data: {e}")
    st.write("Please ensure 'qsr_financials.csv' is uploaded to your GitHub repository.")
