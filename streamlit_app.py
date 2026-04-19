import streamlit as st
import pandas as pd

# 1. 标题 (Product Design)
st.title("🍔 Global Fast-Food Financial Dashboard")
st.write("An interactive tool to analyze the financial efficiency of top QSRs.")

# 2. 读取数据 (Data Loading)
df = pd.read_csv('qsr_financials.csv')

# 3. 计算四大财务比率 (Strictly following W6 Part D formulae)
df['Profit Margin (%)'] = (df['Net_Income'] / df['Revenue']) * 100
df['Asset Turnover'] = df['Revenue'] / df['Total_Assets']

# 处理 Equity 为负的情况，这是 Task 2 的清洗逻辑
df['ROE (%)'] = df.apply(lambda x: (x['Net_Income'] / x['Equity'] * 100) if x['Equity'] > 0 else 0, axis=1)

# 4. 指标切换选择器 (Standard Interaction)
# 自由切换 Profit Margin, Asset Turnover 和 ROE 
metrics = ["Profit Margin (%)", "Asset Turnover", "ROE (%)"]
selected_metric = st.selectbox("Choose a financial metric to visualize:", options=metrics)

# 5. 绘图逻辑 (Visualization)
st.subheader(f"Visualizing {selected_metric} over Time")

# 为了让 st.line_chart 能出图，必须先用 pivot 转换格式
chart_data = df.pivot(index='Year', columns='Company', values=selected_metric)

# 画图
st.line_chart(chart_data)

# 6. 展示数据表格 (Raw Data Summary)
st.subheader("Raw Data Summary")
st.write(df)
