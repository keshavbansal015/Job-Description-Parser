import pandas as pd
import spacy
from func import *
from constants import *
from init_parser import init_parser_func
from tqdm import tqdm

nlp = spacy.load('en_core_web_sm')


if __name__ == '__main__':
	
	matcher = init_parser_func(nlp, SKILL_FILE_PATH, file_type="excel")
	
	final_database = pd.DataFrame()
	df = pd.read_excel(DATA_PATH)
	

	for each in tqdm(range(len(df))):

		text = df.loc[each,'Text']
		application_subject = df.loc[each,'Company']
		data = create_profile(nlp,matcher,text,application_subject)
		final_database = final_database.append(data)

	# Saving the database
	final_database.to_csv('../output/Data.csv', index=False)

	# Plot the final figures
	plot_df(final_database)
 




