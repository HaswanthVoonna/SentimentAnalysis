import streamlit as st
from monkeylearn import MonkeyLearn
from io import StringIO
import time

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
		models = ['ex_SmwSdZ3C', 'ex_vqBQ7V9B', 'ex_A9nCcXfn']
		model_name = ['PERSON','LOCATION', 'COMPANY']
		responses = [None for _ in range(len(models))]
		outputs = [None for _ in range(len(models))]
		with st.spinner('Extracting...'):
			if uploaded_file is not None:
				data = file_text
			else:
				data = text
			for idx, model_id in enumerate(models):
				responses[idx] = ml.extractors.extract(model_id, data=[data])
				outputs[idx] = responses[idx].body[0]['extractions']
		for idx,output in enumerate(outputs):
			st.write(model_name[idx], ' :')
			for item in output:
				st.write(item['extracted_text'])
		
