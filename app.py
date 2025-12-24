import streamlit as st

# ===============================
# 页面配置
# ===============================
st.set_page_config(
    page_title="中医 AI 饮食健康助手",
    layout="centered"
)

# ===============================
# Session 初始化
# ===============================
if "step" not in st.session_state:
    st.session_state.step = 0   # 0 = 欢迎页

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {}

if "meal_data" not in st.session_state:
    st.session_state.meal_data = {}

# ===============================
# Step 0：欢迎首页
# ===============================
if st.session_state.step == 0:
    st.title("🌿 中医 AI 饮食健康助手")

    st.success("欢迎使用！这是一个基于中医理念的饮食健康分析工具。")
    st.info("你可以通过拍照记录饮食，系统将从健康与结构角度进行分析。")

    if st.button("👉 开始使用"):
        st.session_state.step = 1
        st.rerun()

# ===============================
# Step 1：健康档案
# ===============================
elif st.session_state.step == 1:
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
# Step 2：饮食记录
# ===============================
elif st.session_state.step == 2:
    st.subheader("📸 今日饮食记录")

    st.markdown("### 🍽️ 饮食来源")
    source = st.radio(
        "请选择本次饮食来源：",
        ["自己做的", "餐厅堂食", "外卖"]
    )

    st.markdown("### 📷 上传或拍摄饮食照片")
    uploaded_file = st.file_uploader(
        "上传照片（jpg / png）",
        type=["jpg", "png", "jpeg"]
    )

    camera_image = st.camera_input("或直接拍照（手机端可用）")

    image = uploaded_file or camera_image

    if image:
        st.image(image, caption="你的饮食照片", use_column_width=True)

        if st.button("🤖 AI 识别并分析"):
            # ===== 模拟 AI 识别结果（后续可换真实模型）=====
            recognized_foods = ["米饭", "炸鸡", "奶茶"]

            st.session_state.meal_data = {
                "source": source,
                "foods": recognized_foods
            }

            st.session_state.step = 3
            st.rerun()

# ===============================
# Step 3：AI + 中医分析
# ===============================
elif st.session_state.step == 3:
    st.subheader("🤖 中医 AI 饮食分析")

    foods = st.session_state.meal_data.get("foods", [])
    source = st.session_state.meal_data.get("source", "")

    st.write("### 🍽️ 本次识别到的饮食：")
    for food in foods:
        st.write(f"- {food}")

    st.write("### 🧾 饮食来源：")
    st.info(source)

    # ===== 分来源分析逻辑 =====
    if source == "自己做的":
        analysis = (
            "本次饮食为自制饮食，原料与烹饪方式相对可控。\n\n"
            "从中医角度看，油炸与甜饮偏助湿生热，"
            "若频率不高，对脾胃影响相对可控。\n\n"
            "📌 建议：减少油炸频率，搭配清淡蔬菜。"
        )

    elif source == "餐厅堂食":
        analysis = (
            "本次饮食来自餐厅堂食。\n\n"
            "餐厅菜品通常油盐偏重，"
            "易加重脾胃负担，长期可能形成湿热内蕴。\n\n"
            "📌 建议：优先选择蒸煮类、少油菜品。"
        )

    else:
        analysis = (
            "本次饮食来自外卖。\n\n"
            "外卖饮食常见油重、糖高、加工度高，"
            "从中医角度更容易形成湿热积聚。\n\n"
            "📌 建议：降低外卖频率，避免甜饮与油炸组合。"
        )

    st.warning(analysis)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 再记录一餐"):
            st.session_state.step = 2
            st.rerun()

    with col2:
        if st.button("🏠 返回首页"):
            st.session_state.step = 0
            st.rerun()

# ===============================
# 页脚
# ===============================
st.markdown("---")
st.caption("⚠️ 本应用为健康管理辅助工具，不替代医疗诊断")
