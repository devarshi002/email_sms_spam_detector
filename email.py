import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

# Load the dataset
dataset = pd.read_csv('emails.csv')

# Vectorize the email text
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(dataset['text'])

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, dataset['spam'], test_size=0.2, random_state=42)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(x_train, y_train)

# Function to predict whether a message is spam or ham
def predict_message(message):
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)
    return 'Spam' if prediction[0] == 1 else 'Ham'

# Streamlit user interface
st.title("Spam Message Classifier")
st.write("Enter a message below to check if it's spam or ham:")

user_message = st.text_area("Message", height=150)

if st.button("Predict"):
    if user_message:
        prediction = predict_message(user_message)
        if prediction == 'Spam':
            st.markdown(f"<h2 style='color:red;'>The message is: **{prediction}**</h2>", unsafe_allow_html=True)
        else:
            st.success(f'The message is: **{prediction}**')
    else:
        st.error("Please enter a message.")

# To run the Streamlit app, save this code in a file named app.py and run the following command:
# streamlit run app.py

