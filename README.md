# 1project
# YOUTUBE DATE HARVESTING AND WAREHOUSING USING SQL & STREAMLIT

  This project aims to develop a user-friendly Streamlit application that utilizes the Google API to extract information on a YouTube channel, stores it in a SQL database, and enables users to search for channel details and join tables to view data in the Streamlit app.

# INTRODUCTION:

  YouTube, the online video-sharing platform, has revolutionized the way we consume and interact with media. Launched in 2005, it has grown into a global phenomenon, serving as a hub for entertainment, education, and community engagement. With its vast user base and diverse content library, YouTube has become a powerful tool for individuals, creators, and businesses to share their stories, express themselves, and connect with audiences worldwide.

# FILES:

(1)ipynb file;
 
  It has the program for collecting data with the help of Google API of YouTube and inputing a YouTube channel ID to retrieve all the relevant data (Channel name, subscribers, description, total video count, total view count, playlist ID for each channel, video ID, video title, video description, publication date, thumblnails, views, likes, duration, caption and comments of each video, author name, comment text, published date for each comments).

(2)py file;

  It has the program streamlit interface and for input a Query to get answers from mysql and display in Streamlit application.

# ESSENTIAL LIBRARIES:

import googleapiclient.discovery, 
import mysql.connector,
import pandas as pd,
from sqlalchemy import create_engine,
from googleapiclient.errors import HttpError and 
import streamlit as st

# WORK FLOW:

  This project extracts the particular youtube channel data by using the youtube channel id, processes the data, and stores it in the MYSQL database. It has the option to migrate the data to MySQL using SQLAlchemy then analyse the data and give the results in the streamlit depending on the customer questions. The step by step procedures are shown below;
  
STEP 1 : In the .ipynb file, !pip install google-api-python-client, mysql-connector-python, sqlalchemy & pandas.

STEP 2 : Import Libraries Youtube API libraries, import googleapiclient.discovery, import mysql.connector, import sqlalchemy from sqlalchemy import create_engine & import pandas as pd.

STEP 3 : Extract data from the particular youtube channel data by using the youtube channel id, with the help of the youtube API developer console.  

STEP 4 : Takes the required details such as channel details, Video Ids, Video Details & Comments from the extraction data and transforn it into data frame using pandas.

STEP 5 : Load data After the transformation process, we transfer the data to local database(XAMPP) using SQLalchemy. 

STEP 6 : Create Connection After transforn data using sqlalchemy we create a connection to database mysql connector. 

STEP 7 : Filter and process the collected data from the tables depending on the given requirements by using SQL queries and transform the processed data into a DataFrame format.

STEP 8 : In the .py file, Import streamlit import mysql.connector & import pandas as pd.

STEP 9 : Setup the streamlit Page configurations, Sidebar details, Query select box & Enter SQL Connector.

STEP 10 : Visualization Finally, create a Dashboard by using Streamlit and give dropdown options on the Dashboard to the user and select a queries from that menu to analyse the data, 
          which is stored in mysql and show the output in Dataframe Table.

# LESSONS LEARNED:

API integration, Python scripting, Data Collection, Data Management using SQL, Streamlit.

# LINK:

http://localhost:8501/#youtube-data-harvesting-and-warehousing
