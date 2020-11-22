import streamlit as st
from monkeylearn import MonkeyLearn
from io import StringIO

def app():
	st.title('Named Entity Recognization')
	st.write("Named Entity Recognition is the task of identifying named entities (people, locations, organizations, etc.) in the input text.")
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
		model_id = 'ex_SmwSdZ3C'
		if uploaded_file is not None:
			response = ml.extractors.extract(model_id, data=[file_text])
		else:
			response = ml.extractors.extract(model_id, data=[text])
		outputs = response.body[0]['extractions']
		st.write('PERSON : ')
		for output in outputs:
			st.write('         ', output['extracted_text'])
		
