import streamlit as st
from monkeylearn import MonkeyLearn
from io import StringIO
import time

def app():
	st.title('Sentiment Analysis')
	st.write('Sentiment Analysis is the task of interpreting and classifying emotions (positive or negative) in the input text.')
	text = st.text_input('Enter the text')
	st.write('or')
	uploaded_file = st.file_uploader("Upload a document", type='txt')
	if uploaded_file is not None:
		uploaded_file.seek(0)
		stringio = StringIO(uploaded_file.read().decode("utf-8"))
		file_text = stringio.read()
		st.write(file_text)

	if st.button('Execute'):
		ml = MonkeyLearn('b5c3a529126d072f0aa6d43003083ffdc3273a7f')
		model_id = 'cl_pi3C7JiL'
		with st.spinner('Classifying...'):
			if uploaded_file is not None:
				response = ml.classifiers.classify(model_id, [file_text])
			else:
				response = ml.classifiers.classify(model_id, [text])
			outputs = response.body[0]['classifications'][0]
		st.write('The model is are quite sure the sentence is', outputs['tag_name'],'. (', outputs["confidence"]*100, ' %)')



