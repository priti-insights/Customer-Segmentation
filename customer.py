import pickle
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained model
model = pickle.load(open("customer.pkl","rb"))

# 🎨 Page config
st.set_page_config(
    page_title="🧑‍🤝‍🧑 Customer Segmentation",
    page_icon="👥",
    layout="centered"
)

# 🎨 Styles: gradient background & glass card
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top, #ffe5d9, #ffb4a2, #f45b69);
        background-attachment: fixed;
    }
    .main-card {
        background: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 1rem;
        max-width: 700px;
        margin: 2rem auto;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }
    h1 {
        color: #c21807;
        text-align: center;
    }
    label {
        color: #333 !important;
        font-weight: bold;
    }
    div.stButton > button {
        background-color: #c21807;
        color: white;
        padding: 0.5rem 2rem;
        border-radius: 8px;
    }
    div.stButton > button:hover {
        background-color: #ff7868;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main-card'>", unsafe_allow_html=True)

# 🎯 Title
st.title("👥 Customer Segmentation Prediction")
st.markdown("#### Fill the details to predict the customer segment\n---")

# 📄 Input form
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        sex = st.selectbox(
            "Gender",
            options=[0, 1],
            help="0 = Female, 1 = Male"
        )
        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=25
        )
    with col2:
        income = st.number_input(
            "Annual Income (k$)",
            min_value=0,
            max_value=200,
            value=50
        )
        spscore = st.slider(
            "Spending Score (1-100)",
            min_value=1,
            max_value=100,
            value=50
        )
    submit_button = st.form_submit_button(label="🔍 Predict Segment")

# 🎯 Prediction
if submit_button:
    output = model.predict([[sex, age, income, spscore]])
    st.markdown("---")

    if output[0] == 0:
        st.success(
            "✅ Customer Segment: **Average**\n\n"
            "This customer falls into the average-spending segment."
        )
    else:
        st.info(
            "⭐ Customer Segment: **BEST**\n\n"
            "This customer is one of the most valuable customers."
        )

    # 📊 Plot scatter without fixed palette
    st.markdown("#### 📊 Customer Spend vs Income")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.scatterplot(
        x=[income],
        y=[spscore],
        hue=output,
        s=200,
        ax=ax
    )
    ax.set_xlabel("Annual Income (k$)")
    ax.set_ylabel("Spending Score (1-100)")
    ax.set_title("Customer's Spend vs Income")
    st.pyplot(fig)

st.markdown("</div>", unsafe_allow_html=True)
