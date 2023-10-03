import streamlit as st

        # # Show user table 
colms = st.columns((1, 2, 2, 1, 1))
user_table = {
        "email": ["tests@test.com"],
        "uid": [123],
        "verified": ["no"],
        "url": ["www.google.com"]
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