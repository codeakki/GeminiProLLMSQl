from dotenv import load_dotenv
load_dotenv()#take environment variables from .env.

import streamlit as st
import os 
import  sqlite3

import google.generativeai as genai

#Configure genAi key 


genai.configure(api_key=os.getenv("GENAI_API_KEY"))

#Function to load Google Gemini Model 


def get_gemini_Response(question,promopt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content([promopt[0],question])
    return response.text


## function to retrive query form the db 

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
         print(row)
         st.write(row)
    return rows



##Define Your Prompt 

prompt=[
    """
    You are an expert in a converting english questions to SQL query !
    The SQL database has the name STUDENT and has the following columns - NAME,CLASS,SECTION   
    \n\n

    Example 1- How many entries of reacords are there in the table STUDENT ?,
    The sql command will be something like SELECT COUNT(*) FROM STUDENT;
    \n 
    Example 2-tell me all the Students studying in Data Science class ?,
    The sql command will be something like SELECT * FROM STUDENT where CLASS='Data Science';

    also the sql code should not have ``` in the beginning and end and sql word in output 
  """

]




##Streamlit APplication

st.set_page_config(page_title="SQL Query Generator",page_icon="🔍",layout="wide")

st.header("Gemini App to return SQL data from the database")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")


#if submit is cliked 

if submit:
    response = get_gemini_Response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    print(data)
    st.subheader("Response is : ")
    for row in data:
        print(row)
        st.header(row)  






