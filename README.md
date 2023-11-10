[![CI](https://github.com/farazjawedd/week10_fj49/actions/workflows/cicd.yml/badge.svg)](https://github.com/farazjawedd/week10_fj49/actions/workflows/cicd.yml)


## Data Processing with Spark

### Project Overview

#### Data
This project performs data processing on a large CSV dataset using PySpark and Spark SQL. I am using a `spotify.csv` dataset which is in the default directory of the folder.

#### Loading & Exploring the dataset

I loaded the dataset into a pyspark dataframe, here is how the dataset looks:

<img width="1428" alt="Screenshot 2023-11-10 at 5 12 37 AM" src="https://github.com/farazjawedd/week10_fj49/assets/101464414/4d56e4e2-986f-4715-9a13-c95c4d5fe98c">

#### Transforming the year from string to datetime format

Check the change in the year variable (2nd row in both before and after)

<img width="461" alt="Screenshot 2023-11-10 at 5 14 09 AM" src="https://github.com/farazjawedd/week10_fj49/assets/101464414/8d0c0c4b-07c8-4f55-9e98-2326d2d379fb">

#### Analyzing the data

Then I analyzed the top 10 songs all-time in the dataset which have the highest danceability:

<img width="372" alt="Screenshot 2023-11-10 at 5 15 58 AM" src="https://github.com/farazjawedd/week10_fj49/assets/101464414/531c084d-1fd9-489e-9d49-a6ab49a5fbe8">

#### Saving the data to a csv file

These results were then written into a csv file and stored as `top10.csv` in the directory.
