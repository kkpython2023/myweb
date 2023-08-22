import streamlit as st
st.set_page_config(page_title="Myapp",page_icon='shark')
mymenu=st.sidebar.selectbox('Menu',('Home','Fill Form','Downloads'))
st.image('https://www.python.org/static/img/python-logo@2x.png')
st.title("KK technologies")
st.header('kk')
st.text("This is tutorial on streamlit lib")
if(mymenu=='Home'):
    st.markdown('<center><h1>Welcome</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg')
elif (mymenu=='Fill Form'):
    with st.form('ff'):
        name=st.text_input("Please enter your Name ")
        dob=st.date_input("Enter Choose DOB")
        marks=st.slider("Marks")
        k=st.form_submit_button("Submit")
        if k:
            st.write('Name ',name,'DOB ', dob,'Marks ',marks)
elif (mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('Download Now',"hello this is download file","abc.txt")