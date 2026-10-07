import streamlit as st

from database import authenticate_user
from database import initialize_database


def login():
    """
    Display the login page and check the user.
    """

    # Create the database and default admin
    initialize_database()

    # Create login session values
    if "logged_in" not in st.session_state:

        st.session_state.logged_in = False

    if "username" not in st.session_state:

        st.session_state.username = None

    # User is already logged in
    if st.session_state.logged_in:

        return True

    # Login heading
    st.title("Laptop AI")

    st.subheader("User Login")

    st.write(
        "Enter your username and password."
    )

    # Login form
    with st.form("login_form"):

        username = st.text_input(
            "User ID"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        login_button = st.form_submit_button(
            "Login",
            use_container_width=True
        )

    # Check login details
    if login_button:

        user = authenticate_user(
            username,
            password
        )

        if user:

            st.session_state.logged_in = True

            st.session_state.username = user[1]

            st.success("Login successful.")

            st.rerun()

        else:

            st.error(
                "Incorrect User ID or Password."
            )

    return False


def logout():
    """
    Log out the current user.
    """

    if st.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.username = None

        st.rerun()


def get_logged_in_user():
    """
    Return the logged-in username.
    """

    return st.session_state.get(
        "username",
        "User"
    )