import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
# Fetch the service account key JSON file contents
#cred = credentials.Certificate('keydb.json')
#firebase_admin.delete_app(firebase_admin.get_app())
cred = credentials.Certificate('keydb.json')

if (not len(firebase_admin._apps)):
    # Initialize the app with a service account, granting admin privileges
    app=firebase_admin.initialize_app(cred, {'databaseURL': 'https://db23-d2d60-default-rtdb.firebaseio.com/'})

st.set_page_config(page_title="MyWeb",page_icon="🧊",)
mymenu=st.sidebar.selectbox('Menu',('Home','Fill Form','View Data'))
st.image('https://www.python.org/static/img/python-logo@2x.png')
st.title("KK technologies")
st.text("This is tutorial on streamlit lib and firebase")
if(mymenu=='Home'):
    st.markdown('<center><h1>Welcome</h1></center>',unsafe_allow_html=True)
elif (mymenu=='Fill Form'):
    with st.form('ff'):
        id=st.text_input("Please enter ID")
        name=st.text_input("Please enter your Name ")
        age=st.text_input("Enter age")
        marks=st.slider("Marks")
        k=st.form_submit_button("Submit")
        if k:
            st.write('Name ',name,'age ', age,'Marks ',marks)
            d={"id ":id,"name ":name,"age ":age,"marks ":marks}
            k1='/'+id
            print("k1 ",k1, "d ",d)
            ref=db.reference(k1)
            ref.update(d)
elif (mymenu=='View Data'):
    st.header("View Data")
    ref=db.reference("")
    d=ref.get()
    st.text(d)
    #st.text('Name ',d.name,'age ', d.age,'Marks ',d.marks)