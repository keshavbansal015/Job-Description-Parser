from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def create_profile(nlp, matcher,text,application_subject):
	"""
	This funciton creates a profile of one sample row 
	in the dataset

	:param nlp: nlp load object with phrasematcher already initialized
	:param matcher: Custom PhraseMatcher object
	:param text: Resume/JD text data
	:param application_subject: company/applicant's name 
	:return: returns the particular profile in a dataframe format
	"""	

	# Get the matches from the text
	doc = nlp(text)
	matches = matcher(doc)
	
	# Create a dataframe to return
	d = []
	for match_id, start, end in matches:
		rule_id = nlp.vocab.strings[match_id]  # get the Skill, eg: 'Machine Learning'
		span = doc[start : end]  # get the Sub-skill, eg: 'Regression'
		d.append((rule_id, span.text))
	data = []
	for each,count in Counter(d).items():
		data.append([application_subject,*each,count])
	dataf = pd.DataFrame(data,columns=['Company/Candidate Name','Skill','Sub-skill','Count'])
	return(dataf)

def plot_df(final_database):
	"""
	This function simply plots the final
	plot for skill analysis
	And also saves the final png file

	:param final_database: dataframe of employees/JD and skills
	:output 1: saves a png file
	:output 2: saves a final excel sheet 
	"""

	final_database2 = final_database['Sub-skill'].groupby([final_database['Company/Candidate Name'], final_database['Skill']]).count().unstack()
	final_database2.reset_index(inplace = True)
	final_database2.fillna(0,inplace=True)
	new_data = final_database2.iloc[:,1:]
	new_data.index = final_database2['Company/Candidate Name']
	
	# Execute the below line if you want to see the JD profile in a csv format
	new_data.to_csv('../output/skillset.csv')
	
	plt.rcParams.update({'font.size': 8	})
	ax = new_data.plot.barh(title="JD/Resume keywords by category", legend=True, figsize=(25,7), stacked=True)
	labels = []
	for j in new_data.columns:
		for i in new_data.index:
			label = str(j)+": " + str(new_data.loc[i][j])
			labels.append(label)
	patches = ax.patches
	for label, rect in zip(labels, patches):
		width = rect.get_width()
		if width > 0:
			x = rect.get_x()
			y = rect.get_y()
			height = rect.get_height()
			ax.text(x + width/2., y + height/2., label, ha='center', va='center')
	plt.savefig('../output/graph.png')
	plt.show()
