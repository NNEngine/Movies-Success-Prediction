import streamlit as st
import numpy as np
import joblib
import plotly.graph_objects as go #plots

from src.page_config import page_config
from src.main import main_config
from src.sidebar_ui import sidebar_config

# page configuration
page_config()

# sidebar configuration
sidebar_config()

# main page configuration
main_config()


#=====================================================================
#						Model predection section UI
#=====================================================================

inputs = ["Series_Title", "Released_Year", "Certificate", "Runtime", "Genre", "IMDB_Rating", "Meta_score", "Director", "Star1", "Star2","Star3", "Star4", "No_of_votes"]

columns = st.columns(3)

with  columns[0]:
	Series_Title_values 	= 	st.number_input("Series Title", min_value = 0, max_value = 713)
	Released_Year_values    =     st.number_input("Released Year", min_value = 1930, max_value = 2019)
	Certificate_values 	 = 	st.number_input("Certificate", min_value = 0, max_value = 11)
	Runtime_values 		 =     st.number_input("Runtime", min_value = 72, max_value = 238)

with columns[1]:
	Genre_values 		   = 	st.number_input("Genre", min_value = 0, max_value = 171)
	IMDB_Rating_values      = 	st.number_input("IMDB Rating", min_value = 6, max_value = 10)
	Meta_score_score        = 	st.number_input("Meta_score", min_value = 28, max_value = 100)
	Director_values         = 	st.number_input("Director", min_value = 0, max_value = 401)

with columns[2]:
	Star1_values 		   = 	st.number_input("Star1", min_value = 0, max_value = 471)
	Star2_values 		   = 	st.number_input("Star2", min_value = 0, max_value = 598)
	Star3_values 		   = 	st.number_input("Star3", min_value = 0, max_value = 625)
	Star4_values            = 	st.number_input("Star4", min_value = 0, max_value = 670)

No_of_votes_values = st.number_input("No_of_votes", min_value = 25229, max_value = 2343110)

input_values = [Series_Title_values, Released_Year_values, Certificate_values, Runtime_values, Genre_values, IMDB_Rating_values,
				Meta_score_score, Director_values, Star1_values, Star2_values, Star3_values, Star4_values, No_of_votes_values]

input_values_array = np.array(input_values).reshape(1, -1)

st.markdown("---")

# errror handling for proper model loading
try:
	model = joblib.load("model/movie_model.pkl")
	# model weights graph
	fig = go.Figure(
			data = [
				go.Bar(
					x = inputs,
					y = model.coef_,
					marker =  dict(color = "royalblue")

				)
			]
		)
	st.plotly_chart(fig)

	st.markdown("---")

	if st.button("Predict"):
		preds = model.predict(input_values_array)
		st.success(f"Gross Collection is $ {int(preds[0])}")

		avg_gross_value = 78379890
		max_gross_value = 936662225

		if preds[0] < avg_gross_value:
			st.warning("Movie is a failure 😞")
			fig = go.Figure(
				data = [
					go.Bar(
						x = ["Failure", "average", "maximum"],
						y = [preds[0], avg_gross_value, max_gross_value],
						marker =  dict(color = ["red", "blue", "orange"])
					)
				]
			)
			st.plotly_chart(fig)
		else:
			st.success("Movie is a hit 😃")
			st.snow()
			fig = go.Figure(
				data = [
					go.Bar(
						x = ["average", "Success", "maximum"],
						y = [avg_gross_value, preds[0], max_gross_value],
						marker =  dict(color = ["blue","green", "orange"])
					)
				]
			)
			st.plotly_chart(fig)

except OSError as e:
	st.warning(e)
