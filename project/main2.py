import streamlit as st
import psycopg2

def authenticate(username, password):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="project",
            user=username,
            password=password,
            host="localhost",
            port="5432"
        )

        # If connection successful, return True
        return True

    except psycopg2.OperationalError as e:
        # If connection fails, return False
        return False

def main():
    st.title("DBMS Database Login")

    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            # Redirect to another page or display content after successful login
            # For example: st.write("Welcome, {}".format(username))
        else:
            st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()