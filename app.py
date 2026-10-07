import pickle
import pandas as pd
import streamlit as st

from login import login, logout
from chatbot import show_chatbot


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Laptop Price AI",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f5f7fb;
    }

    .section-title {
        font-size: 25px;
        font-weight: 700;
        color: #1f4e79;
        margin-bottom: 15px;
    }

    .prediction-box {
        background: white;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        margin-top: 25px;
        box-shadow: 0 5px 18px rgba(0,0,0,0.10);
        border-left: 6px solid #2e75b6;
    }

    .prediction-title {
        font-size: 18px;
        color: #666666;
        margin-bottom: 5px;
    }

    .prediction-price {
        font-size: 38px;
        font-weight: 700;
        color: #1f4e79;
    }

    [data-testid="stSidebar"] {
        background-color: #eef4fa;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2 {
        color: #1f4e79;
    }

    .stSelectbox label,
    .stNumberInput label,
    .stTextInput label {
        font-weight: 600;
        color: #333333;
    }

    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 48px;
        font-size: 17px;
        font-weight: 600;
    }

    .footer {
        text-align: center;
        color: #777777;
        font-size: 14px;
        padding: 25px 0 10px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)



# =========================================================
# LOGIN
# =========================================================

if not login():
    st.stop()


# =========================================================
# LOAD DATASET
# =========================================================

try:

    df = pd.read_csv("data/laptop_data.csv")

except Exception as e:

    st.error("Unable to load laptop dataset.")
    st.code(str(e))
    st.stop()


# =========================================================
# LOAD MODEL
# =========================================================

try:

    with open("laptop_price_model.pkl", "rb") as file:
        model = pickle.load(file)

except Exception as e:

    st.error("Unable to load laptop price prediction model.")
    st.code(str(e))
    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    # Laptop image
    try:

        st.image(
            "images/laptop.png",
            use_container_width=True
        )

    except Exception:

        st.info("Laptop image not found.")

    st.markdown(
        """
        <h1 style="text-align:center;">
            💻 Laptop Price AI
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("📌 About the Project")

    st.write(
        """
        Laptop Price AI is a machine learning application
        that predicts the estimated price of a laptop based
        on its technical specifications.
        """
    )

    st.markdown("---")

    st.subheader("🔍 Features Used")

    features = [
        "Brand",
        "Model",
        "Type",
        "Year",
        "Screen Size",
        "Resolution",
        "CPU",
        "RAM",
        "Storage",
        "GPU",
        "Operating System",
        "Weight"
    ]

    for feature in features:
        st.write("• " + feature)

    st.markdown("---")

    st.subheader("🤖 Machine Learning")

    st.write(
        """
        The application uses a trained machine learning
        model to estimate laptop prices.
        """
    )

    st.markdown("---")

    # st.caption("Data Science Project | Laptop Price AI")
    st.caption("💻 Laptop Price AI |Machine Learning Project | Data Science")


# =========================================================
# MAIN HEADER
# =========================================================

st.html(
    """
    <div style="
        background: linear-gradient(135deg, #1f4e79, #2e75b6);
        padding: 30px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.12);
    ">

        <h1 style="
            color: white;
            font-size: 42px;
            margin: 0 0 8px 0;
            font-weight: 700;
        ">
            💻 Laptop Price AI
        </h1>

        <p style="
            color: #eaf3ff;
            font-size: 18px;
            margin: 0;
        ">
            Used Laptop Price Prediction Application
        </p>

    </div>
    """
)



# =========================================================
# MAIN LAPTOP IMAGE
# =========================================================

try:

    st.image(
        "images/laptop_banner.jpg",
        use_container_width=True
    )

except Exception:

    pass


# =========================================================
# INTRODUCTION
# =========================================================

st.html(
    """
    <div style="
        background: white;
        padding: 18px;
        border-radius: 14px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.07);
        margin-bottom: 15px;
    ">

        <h3 style="
            color: #1f4e79;
            margin: 0 0 8px 0;
        ">
            📊 Predict Your Laptop Price
        </h3>

        <p style="
            color: #555555;
            margin: 0;
            line-height: 1.6;
        ">
            Enter the laptop specifications below and
            click <b>Predict Laptop Price</b> to get
            an estimated price.
        </p>

    </div>
    """
)


# =========================================================
# LAPTOP INPUT SECTION
# =========================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-title">📝 Enter Laptop Details</div>',
        unsafe_allow_html=True
    )

    column1, column2, column3 = st.columns(3)


    # =====================================================
    # COLUMN 1
    # =====================================================

    with column1:

        brand = st.text_input(
            "Brand",
            value="Dell",
            placeholder="Example: Dell"
        )

        model_name = st.text_input(
            "Model",
            value="Inspiron",
            placeholder="Example: Inspiron"
        )

        laptop_type = st.selectbox(
            "Type",
            [
                "Notebook",
                "Ultrabook",
                "Gaming",
                "2 in 1 Convertible",
                "Workstation",
                "Netbook"
            ]
        )

        year = st.number_input(
            "Year",
            min_value=2010,
            max_value=2026,
            value=2022,
            step=1
        )


    # =====================================================
    # COLUMN 2
    # =====================================================

    with column2:

        screen_size = st.number_input(
            "Screen Size (inches)",
            min_value=10.0,
            max_value=18.0,
            value=15.6,
            step=0.1
        )

        resolution = st.selectbox(
            "Screen Resolution",
            [
                "1366x768",
                "1600x900",
                "1920x1080",
                "2560x1440",
                "3840x2160"
            ]
        )

        cpu = st.text_input(
            "CPU",
            value="Intel Core i5",
            placeholder="Example: Intel Core i5"
        )

        ram = st.selectbox(
            "RAM (GB)",
            [
                4,
                8,
                16,
                32,
                64
            ]
        )


    # =====================================================
    # COLUMN 3
    # =====================================================

    with column3:

        storage = st.text_input(
            "Storage",
            value="512GB SSD",
            placeholder="Example: 512GB SSD"
        )

        gpu = st.text_input(
            "GPU",
            value="Intel Iris Xe",
            placeholder="Example: Intel Iris Xe"
        )

        operating_system = st.selectbox(
            "Operating System",
            [
                "Windows",
                "macOS",
                "Linux",
                "Chrome OS",
                "No OS"
            ]
        )

        weight = st.number_input(
            "Weight (KG)",
            min_value=0.5,
            max_value=5.0,
            value=1.8,
            step=0.1
        )


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.markdown("")

predict_button = st.button(
    "🔮 Predict Laptop Price",
    use_container_width=True
)


# =========================================================
# MAKE PREDICTION
# =========================================================

if predict_button:

    # Create input DataFrame
    input_data = pd.DataFrame(
        {
            "Brand": [brand],
            "Model": [model_name],
            "Type": [laptop_type],
            "Year": [year],
            "Screen_Size_Inches": [screen_size],
            "Screen_Resolution": [resolution],
            "CPU": [cpu],
            "RAM_GB": [ram],
            "Storage": [storage],
            "GPU": [gpu],
            "Operating_System": [operating_system],
            "Weight_KG": [weight]
        }
    )

    try:

        # Make prediction
        predicted_price = model.predict(input_data)[0]

        # Success message
        st.success("✅ Prediction completed successfully!")

        # Display result
        st.html(
    f"""
    <div style="
        background: white;
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        margin-top: 25px;
        box-shadow: 0 5px 18px rgba(0,0,0,0.10);
        border-left: 6px solid #2e75b6;
    ">

        <div style="
            font-size: 18px;
            color: #666666;
            margin-bottom: 5px;
        ">
            Estimated Laptop Price
        </div>

        <div style="
            font-size: 38px;
            font-weight: 700;
            color: #1f4e79;
        ">
            ₹{predicted_price:,.0f}
        </div>

    </div>
    """
)

        # Display entered specifications
        st.markdown("")

        st.subheader("📋 Laptop Specifications")

        display_data = pd.DataFrame(
            {
                "Specification": [
                    "Brand",
                    "Model",
                    "Type",
                    "Year",
                    "Screen Size",
                    "Resolution",
                    "CPU",
                    "RAM",
                    "Storage",
                    "GPU",
                    "Operating System",
                    "Weight"
                ],
                "Value": [
                    brand,
                    model_name,
                    laptop_type,
                    year,
                    f"{screen_size} inches",
                    resolution,
                    cpu,
                    f"{ram} GB",
                    storage,
                    gpu,
                    operating_system,
                    f"{weight} KG"
                ]
            }
        )

        st.dataframe(
            display_data,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:

        st.error("❌ Prediction failed.")

        st.warning(
            """
            The model may expect different input values
            or preprocessing.
            """
        )

        st.code(str(e))


# =========================================================
# LOGOUT
# =========================================================

# st.markdown("---")

top_left, top_right = st.columns([10, 1])

with top_right:

    logout()





# # =========================================================
# # FOOTER
# # =========================================================

# st.markdown(
#     """
#     <div class="footer">

#         💻 Laptop Price AI |
#         Machine Learning Project |
#         Data Science

#     </div>
#     """,
#     unsafe_allow_html=True
# )


# =========================================================
# Chatbot section
# =========================================================
st.markdown("---")

st.header("🤖 Laptop AI Assistant")

show_chatbot(df)  