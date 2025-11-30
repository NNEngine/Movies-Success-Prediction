import streamlit as st

#=================================================================
#              			sidebar UI
#=================================================================
def sidebar_config():
	st.sidebar.title("Movie Success Prediction on the basis of Gross Collection.")
	st.sidebar.image("image/boxoffice_image.png")
	st.sidebar.markdown("---")
	st.sidebar.info(
		"""
			A movie success predictor, based on ML, predicts the success of the movie on
			box office.
			It predicts the movie success on the following factors:
		"""
	)
	st.sidebar.info(
		"""
			- `Series_Title` = Name of the movie
			- `Released_Year` - Year at which that movie released
			- `Certificate` - Certificate earned by that movie
			- `Runtime` - Total runtime of the movie
			- `Genre` - Genre of the movie
			- `IMDB_Rating` - Rating of the movie at IMDB site
			- `Meta_score` - Score earned by the movie
			- `Director` - Name of the Director
			- `Star1,Star2,Star3,Star4` - Name of the Stars
			- `No_of_votes` - Total number of votes
			- `Gross` - Money earned by that movie
		"""
	)
	st.sidebar.markdown("---")
	st.sidebar.image("social media icons/csv.png")
	st.sidebar.markdown("[Dataset](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)")
	st.sidebar.markdown("---")
	st.sidebar.markdown(">Made by Shivam Sharma")

	with st.sidebar:
		col1, col2 = st.columns([0.1,0.5], gap = "medium")
		with col1:
			st.image("social media icons/github.png")
			st.markdown("[Github](https://github.com/NNEngine)")
		with col2:
			st.image("social media icons/linkedin.png")
			st.markdown("[LinkedIn](https://www.linkedin.com/in/shivam-sharma-33a77b22b/)")
