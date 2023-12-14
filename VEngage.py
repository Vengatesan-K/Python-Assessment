import streamlit as st
import pandas as pd
import json
from streamlit_option_menu import option_menu

st.set_page_config(page_title='python', layout='wide', page_icon="🎯")

reduce_header_height_style = """
    <style>
        div.block-container {padding-top:0rem;}
        div.Sidebar   {padding-top:0rem;}
    </style>
"""
st.markdown(reduce_header_height_style, unsafe_allow_html=True)

hide_st_style ="""
        <style>
        MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """      
st.markdown(hide_st_style,unsafe_allow_html=True)

selected = option_menu(None, ["Task1","Task2"], 
icons=["1-square","2-square"],
default_index=0,
orientation="horizontal",
styles={"nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "red", "transition": "color 0.3s ease, background-color 0.3s ease"},
        "icon": {"font-size": "25px"},
        "container": {"max-width": "3000px", "padding": "5px"},
        "nav-link-selected": {"background-color": "green", "color": "white"},
        "nav-link-0": {"icon": "fa-home", "background-color": "#4285F4", "color": "white", "padding-left": "15px"}})

if selected == "Task1":
 def read_json(file):
    data = json.load(file)
    return data

 def read_csv(file):
    data = pd.read_csv(file)
    return data

 def main():
    st.subheader('File Uploader and Reader')

    file1 = st.file_uploader("Upload Data Files", type=['json', 'csv'])

    if file1 is not None:
        file_type = file1.name.split('.')[-1]

        if file_type == 'json':
            data = read_json(file1)
            st.write("### JSON File Contents")
            st.write(data)

        elif file_type == 'csv':
            data = read_csv(file1)
            st.write("### CSV File Contents")
            st.write(data)
 if __name__ == "__main__":
    main()  
    
elif selected == "Task2":    
    def read_csv(file):
        try:
            return pd.read_csv(file)
        except pd.errors.EmptyDataError:
            st.error("The uploaded CSV file is empty or doesn't contain any readable data.")
            return None

    # Function to read JSON file
    def read_json(file):
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file: {e}")
            return None

    def execute_select_query_head(data):
        return data.head(10)
    # Function to execute SELECT query
    def execute_select_query(data):
        try:
            # Applying filter condition where name equals 'Doe'
            filtered_data = data[data['Name'] == 'Doe']
            return filtered_data
        except Exception as e:
            st.error(f"Error executing SELECT query: {e}")
            return None

    # Function to execute INSERT query
    def insert_row(data):
        new_row_data = {
            "Name": 'Test',
            "Email": 'test@test.xtyz',
            "Phone 1": '1234456',
            "Phone 2": '1233233'
        }
        # Append the new row to the DataFrame
        data.loc[len(data)] = new_row_data
        st.success("Row insertion performed successfully.")
        return data
    # Function to execute DELETE query
    def delete_rows_by_name(data):
        data = data[data['Name'] != 'John']
        st.success("Rows with Name 'John' deleted successfully.")
        return data
    def execute_select_query_top_10(data):
        return data[:10]  # Limit the output to the top 10 records
    def execute_select_query_by_name(data, name):
        selected_data = [record for record in data if record.get('Name') == 'jane']
        return selected_data


    def insert_row_json(data):
        new_row_data = {
            "Name": 'Test',
            "Email": 'test@test.xtyz',
            "Phone 1": '1234456',
            "Phone 2": '1233233'
        }
        data.append(new_row_data)
        return data

    # Function to delete rows based on a condition in JSON data
    def delete_rows_by_name_json(data):
        data = [record for record in data if record.get('Name') != 'John']
        return data




    def main():
        st.title('Parser for Phone Book Records')

        file = st.file_uploader("Upload CSV or JSON File", type=['csv', 'json'])
        file_type = None
        data = None  # Initialize data variable

        if file is not None:
            file_type = file.name.split('.')[-1]

        if file_type == 'json':
            data = read_json(file)
        elif file_type == 'csv':
            data = read_csv(file)
        else:
            st.error("Please upload a CSV or JSON file.")
            
        if data is not None:
            query_options = [
                "SELECT * FROM phone_records",
                "SELECT * FROM phone_records WHERE name='doe'",
                "INSERT INTO phone_records(name, email, phone1, phone2) VALUES('Test', 'test@test.xtyz', '1234456', '1233233')",
                "DELETE FROM phone_records WHERE name='John'"
            ]
            query = st.selectbox("Choose Problem Query", query_options)
            result = None
            
            if st.button("Execute"):
                if file_type == 'csv':
                    if query.endswith("phone_records"):
                        result = execute_select_query_top_10(data)
                    elif query.startswith("SELECT"):
                        result = execute_select_query(data)
                    elif query.startswith("INSERT"):
                        result = insert_row(data.copy())
                    elif query.startswith("DELETE"):
                        result = delete_rows_by_name(data)
                        
                    if isinstance(result, pd.DataFrame):
                        st.write("### SQL-Like Output:")
                        st.dataframe(result, use_container_width=True)
                        
                elif file_type == 'json':
                    # Ensure data is a list of dictionaries
                    if isinstance(data, str):
                        data = json.loads(data)

                    # Handle JSON operations based on the selected query
                    if query.endswith("phone_records"):
                        result = execute_select_query_top_10(data)
                    elif query.startswith("SELECT"):
                        result = [record for record in data if record.get('Name') == 'Doe']
                    elif query.startswith("INSERT"):
                        st.success("Inserted Successfully")
                        result = insert_row_json(data.copy())  # Ensure to work with a copy of the data
                    elif query.startswith("DELETE"):
                        st.success("Deleted Successfully")
                        result = [record for record in data if record.get('Name') != 'John']

                # Display the result based on the operation executed
                if result is not None and isinstance(result, list):
                    st.write("### JSON Data Output:")
                    st.json(result)

         

    if __name__ == "__main__":
     main()
