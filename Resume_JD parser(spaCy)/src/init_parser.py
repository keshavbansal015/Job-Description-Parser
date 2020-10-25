import pandas as pd
from spacy.matcher import PhraseMatcher

def init_parser_func(nlp, SKILL_FILE_PATH, file_type = 'csv'):
	"""
	This function initializes the nlp PhraseMatcher
	and reads the skill-set data file in an excel/csv format
	
	:param nlp: It is an NLP load instance, ex: nlp.load("en_core_web_sm")
	:param SKILL_FILE_PATH: Path for the data file
	:param file_type: csv/excel, default = csv
	:return: Returns a PhraseMatcher object.
	"""

	if file_type == 'csv':
		keyword_ = pd.read_csv(SKILL_FILE_PATH)
	else:
		try:
			keyword_ = pd.read_excel(SKILL_FILE_PATH)
			print("Success!")
		except Exception as e:
			print(e)

	matcher = PhraseMatcher(nlp.vocab)
	for each in keyword_.columns: 
		matcher.add(each, None, *[nlp(text) for text in keyword_[each].dropna(axis = 0)])

	return matcher