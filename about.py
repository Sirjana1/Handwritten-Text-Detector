import streamlit as st
from streamlit_option_menu import option_menu

def about():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('media/bg.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Hide Streamlit's default branding
    st.markdown(
        """
        <style>
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Custom CSS for card styling
    st.markdown(
        """
        <style>
        .card {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 20px;
            margin: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .card-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .card-content {
            font-size: 18px;
            line-height: 1.6;
        }
        .btn-primary {
            background-color: #007bff;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Home page content
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>Welcome to Handwriting Recognition System</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='card-content'>
        Our Handwriting Recognition System utilizes state-of-the-art technology to convert handwritten text into digital format.
   
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Features section
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-title'>Features</div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='card-content'>
        <ul>
            <li>High Accuracy in Recognizing Handwritten Text</li>
            <li>User-Friendly Interface</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Get Started button
    st.markdown("<div class='card' style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("Get Started", key="get_started_btn"):
        st.experimental_set_query_params(page="app")
    st.markdown("</div>", unsafe_allow_html=True)


# Main menu with options
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "About", "Account", "App", "Sample Images"],
        icons=["house", "info", "user", "app-indicator", "image"],
        menu_icon="cast",
        default_index=0,
    )

    # Display the selected page
if selected == "Home":
    st.write("Home")
elif selected == "About":
    st.write("About Page")
elif selected == "Account":
    st.write("Account Page")
elif selected == "App":
    st.write("App Page")
elif selected == "Sample Images":
    st.write("Sample Images Page")