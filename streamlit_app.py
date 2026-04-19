# --- 在原有代码后面添加以下内容 ---

st.subheader(f"Visualizing {selected_metric} over Time")

# 准备绘图数据
chart_data = filtered_df.pivot(index='Year', columns='Company', values=selected_metric)

# 画折线图
st.line_chart(chart_data)

# 展示原始数据表格
st.subheader("Raw Data Summary")
st.write(filtered_df)
