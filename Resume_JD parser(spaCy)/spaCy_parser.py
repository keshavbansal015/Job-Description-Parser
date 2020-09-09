import pandas as pd
import matplotlib.pyplot as plt
import spacy
from func import *
from spacy.matcher import PhraseMatcher
from collections import Counter
import gc
gc.enable()
nlp = spacy.load('en_core_web_sm')

# Enter File paths:
# DATA_PATH = '<path for your resume/job description file>'
DATA_PATH = './JD.xlsx'
# SKILL_FILE_PATH = '<path for the skill-set file>'
SKILL_FILE_PATH = './skill-set.xlsx'

if __name__ == '__main__':
	
	# Initializing PhraseMatcher
	keyword_ = pd.read_excel(SKILL_FILE_PATH)
	matcher = PhraseMatcher(nlp.vocab)
	for each in keyword_.columns: 
		matcher.add(each, None, *[nlp(text) for text in keyword_[each].dropna(axis = 0)])
	final_database = pd.DataFrame()
	df = pd.read_excel(DATA_PATH)
	
	for each in range(len(df)):
		JD = df.loc[each,'JD']
		Company_name = df.loc[each,'Company']
		data = create_profile(JD,Company_name)
		final_database = final_database.append(data)
		each +=1
		print('####################',each,'####################')

	# Saving the database
	final_database.to_csv('data.csv')

	# Plot the final figures
	plot_JD(final_database)





