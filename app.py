import streamlit as st
from schema_parser import load_schema
from sql_generator import generate_sql
from sql_explainer import explain_sql

st.title("🧠 Natural Language to SQL Generator")

nl_query = st.text_input("Enter your question:")
schema_file = st.file_uploader("Upload database schema (.sql or .txt)", type=['sql', 'txt'])

if st.button("Generate SQL"):
    if not nl_query or not schema_file:
        st.error("Please provide a question and upload a schema.")
    else:
        schema = load_schema(schema_file)
        sql = generate_sql(nl_query, schema)
        explanation = explain_sql(sql)
        
        st.subheader("🔍 Generated SQL")
        st.code(sql, language="sql")

        st.subheader("📝 Explanation")
        st.write(explanation)
