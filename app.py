# ==========================================
# ACC102 Mini Assignment - Streamlit App
# ==========================================

import streamlit as st
import pandas as pd

# 1. 网页标题与说明 (Product Design & Communication)
st.set_page_config(page_title="ACC102 QSR Dashboard", layout="wide")
st.title("🍔 Global Fast-Food Financial Dashboard")
st.write("An interactive tool to analyze the financial efficiency of top QSRs.")

# 2. 读取之前生成的清洗后数据
@st.cache_data
def load_data():
    return pd.read_csv('qsr_financials.csv')

df = load_data()

# 3. 【计算四大财务比率 Four Financial Ratios (W6 Part D)】
# 严格按照课件第 5 页的公式计算
df['Profit Margin (%)'] = (df['Net_Income'] / df['Revenue']) * 100
df['Asset Turnover'] = df['Revenue'] / df['Total_Assets']

# 【处理 Negative Equity Trap】
# 当 Equity <= 0 (如股票回购导致) 时，常规的 ROE 和 Leverage 会出现严重误导性的负数。
# 此时将这些值设为 None，避免图表出现异常失真。
df['ROE (%)'] = df.apply(
    lambda x: (x['Net_Income'] / x['Equity']) * 100 if x['Equity'] > 0 else None, axis=1
)
df['Leverage'] = df.apply(
    lambda x: x['Total_Assets'] / x['Equity'] if x['Equity'] > 0 else None, axis=1
)


# 4. 侧边栏交互设置 
st.sidebar.header("User Control Panel")

# 让用户选择想对比的公司
selected_companies = st.sidebar.multiselect(
    "1. Select Companies:",
    options=df['Company'].unique(),
    default=['MCD', 'YUM']
)

# 让用户选择想查看的财务指标
selected_metric = st.sidebar.selectbox(
    "2. Select Financial Ratio:",
    options=['ROE (%)', 'Profit Margin (%)', 'Asset Turnover', 'Leverage']
)

# 5. 动态图表展示
if selected_companies:
    # 根据用户选择过滤数据
    filtered_df = df[df['Company'].isin(selected_companies)]
    
    # 【使用 pivot 透视表以便画图 (W6 Page 6)】
    pivot_df = filtered_df.pivot(index='Year', columns='Company', values=selected_metric)
    
    # 绘制动态折线图
    st.subheader(f"{selected_metric} Comparison (2019-Present)")
    st.line_chart(pivot_df)
    
    # 展示原始数据表
    st.subheader("Raw Data Summary")
    st.dataframe(filtered_df)
else:
    st.warning("Please select at least one company from the sidebar to start.")