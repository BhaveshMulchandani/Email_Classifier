import streamlit as st
import pickle

model = pickle.load(open('spam.pkl','rb'))
cv = pickle.load(open('vectorizer.pkl','rb'))

st.title("Email spam classification application")
st.write("this is a machine learning application to classify emails as spam or ham")
st.subheader("classification")
user_input = st.text_area("Enter an Email")

if st.button("classify"):
    data=[user_input]
    vect=cv.transform(data)
    pred=model.predict(vect)

    if user_input:
        if pred[0] == 1:
           st.write("email is spam")
        else:
            st.write("email is not spam")
    else:
        st.write("please enter your email")
     