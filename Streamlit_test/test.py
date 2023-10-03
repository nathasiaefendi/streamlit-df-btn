import streamlit as st

        # # Show user table 
colms = st.columns((1, 2, 2, 1, 1))
user_table = {
        "email": ["testsssss@test.com", "nayanae@test.com", "@@@"],
        "uid": [123, 456, 789],
        "verified": ["no", "yes", "no"],
        "url": ["www.google.com", "www.yahoo.com", "goo.gle"]
}
fields = ["№", 'email', 'uid', 'verified', "action"]

for col, field_name in zip(colms, fields):
        # header
        col.write(field_name)

for x, email in enumerate(user_table['email']):
        col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1))
        col1.write(x)  # index
        col2.write(user_table['email'][x])  # email
        col3.write(user_table['uid'][x])  # unique ID
        col4.write(user_table['verified'][x])   # email status
        do_action = col5.button("View", key=x) # button
