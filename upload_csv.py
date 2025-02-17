import os
import sqlite3
import pandas as pd
import streamlit as st

def save_csv_to_data_folder(uploaded_file):
    data_folder = 'data'
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    file_path = os.path.join(data_folder, uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def insert_csv_to_db(csv_file_path, db_path='db/salary.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read CSV file into DataFrame
    df = pd.read_csv(csv_file_path)

    # Insert DataFrame into SQLite database
    df.to_sql('salaries', conn, if_exists='append', index=False)

    conn.commit()
    conn.close()

def csv_uploader():
    st.subheader("CSV to Database Uploader")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        # Save the uploaded file to the data folder
        csv_file_path = save_csv_to_data_folder(uploaded_file)

        # Insert the CSV data into the database
        insert_csv_to_db(csv_file_path)

        st.success("CSV file has been uploaded and data inserted into the database.")

def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the app mode", ["Upload CSV", "CSV Agent", "SQL Agent"])

    if app_mode == "Upload CSV":
        csv_uploader()
    elif app_mode == "CSV Agent":
        st.write("CSV Agent functionality goes here.")
    elif app_mode == "SQL Agent":
        st.write("CSV Agent functionality goes here.")

    main()
