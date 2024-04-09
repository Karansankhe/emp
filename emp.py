import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Set your MongoDB URI here
MONGO_URI = "mongodb://sankhe00009:NKg4IMJx1FhI5a3K@hostname:27017/emp management"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client.employee_db
collection = db.employees

# Streamlit UI
st.title('Employee Management System')

option = st.sidebar.selectbox('Menu', ['Add Employee', 'Delete Employee', 'View Employees'])

if option == 'Add Employee':
    name = st.text_input('Enter Name:')
    position = st.text_input('Enter Position:')
    salary = st.number_input('Enter Salary:')
    if st.button('Add'):
        new_employee = {'Name': name, 'Position': position, 'Salary': salary}
        collection.insert_one(new_employee)
        st.success('Employee added successfully!')

elif option == 'Delete Employee':
    name = st.text_input('Enter Name to Delete:')
    if st.button('Delete'):
        collection.delete_one({'Name': name})
        st.success('Employee deleted successfully!')

elif option == 'View Employees':
    employees = list(collection.find())
    if employees:
        employee_df = pd.DataFrame(employees)
        st.table(employee_df)
    else:
        st.info('No employees found.')
