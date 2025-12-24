import streamlit as st

st.set_page_config(page_title="中医AI饮食健康助手", layout="centered")
st.title("🌿 中医 AI 饮食健康助手")

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {}

if not st.session_state.user_profile:
    st.subheader("👤 建立你的健康档案")
    gender = st.selectbox("性别", ["女", "男", "其他"])
    age = st.number_input("年龄", 10, 100)
    height = st.number_input("身高 (cm)", 130, 210)
    weight = st.number_input("体重 (kg)", 30, 150)
    goal = st.selectbox("你的主要目标", ["改善饮食结构", "控制体重", "日常调养"])

    if st.button("保存并开始"):
        st.session_state.user_profile = {
            "gender": gender,
            "age": age,
            "height": height,
            "weight": weight,
            "goal": goal
        }
        st.success("健康档案已保存！")
        st.rerun()
else:
    st.success("欢迎回来！你可以开始饮食记录啦 🍽️")
    st.info("（这是可运行示例，后续可继续扩展功能）")
