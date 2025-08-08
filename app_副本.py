import streamlit as st

st.set_page_config(page_title="测试应用")
st.title("🚀 基本功能测试")

st.success("应用已成功启动！")
st.info("这是一个最小化测试，确认Streamlit Cloud可以正常运行")

if st.button("点击测试"):
    st.balloons()
    st.success("🎉 测试成功！")
