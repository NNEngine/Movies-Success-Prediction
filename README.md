# Movie Prediction

This project aims to predict the success of the movie on the box office. The success of the movie is determined on the basis of it's gross collection.

<div align="center">
  <img src="https://cdn.shopify.com/s/files/1/0595/6970/1019/files/kevin-asia-Movie-Box.png?v=1633069302" width=auto/>
</div>

## About Model
- The Model is trained using LinearRegression having r2_score of 0.5135.
- The input to the model were normalized using StandardScaler.
- The model is saved in the format `.pkl`.

## Dataset Description

The Dataset for this model is taken from `kaggle` and can be found on `https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows`.

**Data**:-

- `Poster_Link` - Link of the poster that imdb using
- `Series_Title` = Name of the movie
- `Released_Year` - Year at which that movie released
- `Certificate` - Certificate earned by that movie
- `Runtime` - Total runtime of the movie
- `Genre` - Genre of the movie
- `IMDB_Rating` - Rating of the movie at IMDB site
- `Overview` - mini story/ summary
- `Meta_score` - Score earned by the movie
- `Director` - Name of the Director
- `Star1,Star2,Star3,Star4` - Name of the Stars
- `No_of_votes` - Total number of votes
- `Gross` - Money earned by that movie

## Data Preprocessing
- We removed null values instead of filling them.
- We removed the following columns:
	- *Poster_Link*
	- *Overview*
- We didn't handle Outliers.
