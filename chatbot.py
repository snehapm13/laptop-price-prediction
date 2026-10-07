import streamlit as st
import pandas as pd


def show_chatbot(df):

    # st.subheader("🤖 Laptop Price AI Assistant")

    st.write(
        "Ask me about the laptop dataset."
    )

    # -----------------------------------------------------
    # CHAT HISTORY
    # -----------------------------------------------------

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    # Display previous messages
    for message in st.session_state.chat_messages:

        with st.chat_message(message["role"]):

            st.write(message["content"])

    # -----------------------------------------------------
    # CHAT INPUT
    # -----------------------------------------------------

    user_question = st.chat_input(
        "Ask something about laptops..."
    )

    if user_question:

        # Save user message
        st.session_state.chat_messages.append(
            {
                "role": "user",
                "content": user_question
            }
        )

        # Display user message
        with st.chat_message("user"):
            st.write(user_question)

        # -------------------------------------------------
        # SIMPLE DATASET RESPONSES
        # -------------------------------------------------

        question = user_question.lower()

        if "brand" in question:

            if "Brand" in df.columns:

                brands = (
                    df["Brand"]
                    .dropna()
                    .value_counts()
                    .head(10)
                )

                answer = (
                    "The most common laptop brands are:\n\n"
                    + "\n".join(
                        f"- {brand}: {count}"
                        for brand, count in brands.items()
                    )
                )

            else:

                answer = "The dataset does not contain a Brand column."

        elif "ram" in question:

            if "RAM_GB" in df.columns:

                ram_values = (
                    df["RAM_GB"]
                    .dropna()
                    .value_counts()
                    .sort_index()
                )

                answer = (
                    "RAM distribution:\n\n"
                    + "\n".join(
                        f"- {ram} GB: {count} laptops"
                        for ram, count in ram_values.items()
                    )
                )

            else:

                answer = "The dataset does not contain a RAM_GB column."

        elif "price" in question:

            if "Price" in df.columns:

                average_price = df["Price"].mean()
                minimum_price = df["Price"].min()
                maximum_price = df["Price"].max()

                answer = (
                    f"Here is the price information:\n\n"
                    f"- Average price: ₹{average_price:,.0f}\n"
                    f"- Minimum price: ₹{minimum_price:,.0f}\n"
                    f"- Maximum price: ₹{maximum_price:,.0f}"
                )

            else:

                answer = "The dataset does not contain a Price column."

        elif "how many" in question or "count" in question:

            answer = (
                f"The dataset contains "
                f"{len(df):,} laptop records."
            )

        elif "column" in question or "feature" in question:

            answer = (
                "The dataset contains these columns:\n\n"
                + "\n".join(
                    f"- {column}"
                    for column in df.columns
                )
            )

        else:

            answer = (
                "I can currently answer questions about:\n\n"
                "• Laptop prices\n"
                "• Laptop brands\n"
                "• RAM\n"
                "• Number of laptops\n"
                "• Dataset columns"
            )

        # -------------------------------------------------
        # DISPLAY ASSISTANT RESPONSE
        # -------------------------------------------------

        with st.chat_message("assistant"):

            st.write(answer)

        # Save assistant message
        st.session_state.chat_messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
