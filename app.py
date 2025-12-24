import streamlit as st

# ===============================
# 页面基础设置
# ===============================
st.set_page_config(
    page_title="中医 AI 饮食健康助手",
    layout="centered"
)

st.title("🌿 中医 AI 饮食健康助手")

# ===============================
# Session 初始化
# ===============================
if "step" not in st.session_state:
    st.session_state.step = 1

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {}

if "meal_data" not in st.session_state:
    st.session_state.meal_data = {}

# ===============================
# Step 1：健康档案
# ===============================
if st.session_state.step == 1:
    st.subheader("👤 建立你的健康档案")

    gender = st.selectbox("性别", ["女", "男", "其他"])
    age = st.number_input("年龄", 10, 100)
    height = st.number_input("身高 (cm)", 130, 210)
    weight = st.number_input("体重 (kg)", 30, 150)
    goal = st.selectbox("你的主要目标", ["改善饮食结构", "控制体重", "日常调养"])

    if st.button("✅ 保存并进入饮食记录"):
        st.session_state.user_profile = {
            "gender": gender,
            "age": age,
            "height": height,
            "weight": weight,
            "goal": goal
        }
        st.session_state.step = 2
        st.rerun()

# ===============================
# Step 2：饮食记录（照片 + 来源）
# ===============================
elif st.session_state.step == 2:
    st.subheader("📸 今日饮食记录")

    st.markdown("### 🍽️ 这顿饭来自哪里？")
    source = st.radio(
        "请选择饮食来源",
        ["自己做的", "餐厅堂食", "外卖"]
    )

    st.markdown("### 📷 上传或拍摄饮食照片")
    uploaded_file = st.file_uploader(
        "上传照片（支持 jpg / png）",
        type=["jpg", "png", "jpeg"]
    )

    camera_image = st.camera_input("或直接拍照（手机端可用）")

    image = uploaded_file or camera_image

    if image:
        st.image(image, caption="你的饮食照片", use_column_width=True)

        if st.button("🤖 AI 识别并分析"):
            # ===============================
            # 🔴 AI 图像识别【占位示例】
            # 后期可接真实多模态模型
            # ===============================
            recognized_food = [
                "米饭",
                "炸鸡",
                "奶茶"
            ]

            st.session_state.meal_data = {
                "source": source,
                "foods": recognized_food
            }

            st.session_state.step = 3
            st.rerun()

# ===============================
# Step 3：中医 + AI 分析
# ===============================
elif st.session_state.step == 3:
    st.subheader("🤖 中医 AI 饮食分析结果")

    foods = st.session_state.meal_data.get("foods", [])
    source = st.session_state.meal_data.get("source", "")

    st.write("### 🍽️ 识别到的饮食内容：")
    for food in foods:
        st.write(f"- {food}")

    st.write("### 🧾 饮食来源：")
    st.info(source)

    # ===============================
    # 分来源的中医分析逻辑
    # ===============================
    if source == "自己做的":
        analysis = (
            "这顿饮食为自制饮食，整体可控性较高。\n\n"
            "从中医角度看，饮食结构中包含油炸与甜饮，"
            "虽不宜频繁，但若分量适中、制作油质较好，"
            "对脾胃影响相对可控。\n\n"
            "📌 建议：注意油温与甜饮频率，搭配清淡蔬菜。"
        )

    elif source == "餐厅堂食":
        analysis = (
            "这顿饮食来自餐厅堂食。\n\n"
            "餐厅饮食通常油盐偏重，易助湿生热，"
            "长期频繁摄入可能加重脾胃运化负担。\n\n"
            "📌 建议：减少油炸与含糖饮品，选择蒸煮类菜品。"
        )

    else:  # 外卖
        analysis = (
            "这顿饮食来自外卖。\n\n"
            "从中医角度看，外卖饮食常见特点为："
            "油重、糖高、制作与保温过程复杂，"
            "更容易形成湿热内蕴。\n\n"
            "📌 建议：降低外卖频率，优先选择清淡、少加工菜品，"
            "并注意搭配温性调养食物。"
        )

    st.warning(analysis)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 重新记录饮食"):
            st.session_state.step = 2
            st.rerun()

    with col2:
        if st.button("🏠 返回首页"):
            st.session_state.step = 1
            st.rerun()

# ===============================
# 页脚
# ===============================
st.markdown("---")
st.caption("⚠️ 本应用为健康管理辅助工具，不替代医疗诊断")
