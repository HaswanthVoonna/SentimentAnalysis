import streamlit as st
from multiapp import MultiApp
from apps import NER_Recognizer, SentimentAnalyzer # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Named Entity Recognization", NER_Recognizer.app)
app.add_app("Sentiment Analysis", SentimentAnalyzer.app)

# The main app
app.run()

