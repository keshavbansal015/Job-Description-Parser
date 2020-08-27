# Job-Description-Parser
Using spaCy (an NLP library) I created a custom project for semantic analysis and custom rule matcher for Job Descriptions/ Resumes.
You can parse multiple resumes/job descriptions at once and check the perfect profile-match for your future.

## Packages required:
* Python 3.7+
* Pandas
* Matplotlib
* spaCy library (for anaconda)
    * command for installing: conda install -c conda-forge spacy
* spaCy english core language package 
    * command for downloading: python -m spacy download en_core_web_sm
* For any confusion you can visit https://spacy.io/ and check out their documentation.

## Files Required:
* An excel file with 2 sheets:
  * Keywords: for custom rule matching
  * JDs/Resume: list of company/candidate names and their Job Descriptions/resumes.

## Output Files:
* An Excel sheet with company/candidate names, Main-Skill domain, Specific-skill, Specific-skill count(no. of time a particular skill is mentioned).
* An Excel sheet with proportions of skill domains for each profile.
* A bar graph chart(.png file) visualizing the skill-set and their ratios for each and every profile.
