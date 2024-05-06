#Essentials

import streamlit as st
import mysql.connector
import pandas as pd

#Streamlit

st.set_page_config(layout='wide')
st.header('1Project', divider='orange')
st.title("🗃️:blue[Youtube Data Harvesting and Warehousing using SQL & Streamlit]📡")

with st.sidebar:
    st.header(":violet[Skills Take Away]⤵️")
    st.write("1️⃣:green[API]✔️")
    st.write("2️⃣:green[Python Scripting]✔️")
    st.write("3️⃣:green[Data Collection]✔️")
    st.write("4️⃣:green[Data Management using SQL]✔️")
    st.write("5️⃣:green[Streamlit]✔️")

    query_select=st.selectbox("🔹Queries🔹",("Select your Query",
    "1.What are the names of all the videos and their corresponding channels?",
    "2.Which channels have the most number of videos, and how many videos do they have?",
    "3.What are the top 10 most viewed videos and their respective channels?",
    "4.How many comments were made on each video, and what are their corresponding video names?",
    "5.Which videos have the highest number of likes, and what are their corresponding channel names?",
    "6.What is the total number of likes and dislikes for each video, and what are their corresponding video names?",
    "7.What is the total number of views for each channel, and what are their corresponding channel names?",
    "8.What are the names of all the channels that have published videos in the year 2022?",
    "9.What is the average duration of all videos in each channel, and what are their corresponding channel names?",
"10.Which videos have the highest number of comments, and what are their corresponding channel names?"))

#SQL Connector

mydb = mysql.connector.connect(host="localhost",user="root",password="")
mycursor = mydb.cursor(buffered=True)
mycursor.execute('USE 1project')

#Queries:

#1
if query_select=="1.What are the names of all the videos and their corresponding channels?":
    mycursor.execute("SELECT videos.Video_title, channels.channel_name \
    FROM 1Project.videos \
    INNER JOIN channels ON videos.channel_id = channels.channel_id")

    df=pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    st.write(":green[name of videos and corresponding channels]")
    st.write(df)

#2
elif query_select=="2.Which channels have the most number of videos, and how many videos do they have?":
    mycursor.execute('SELECT channel_name,max(channel_vidcount) as max_videocount FROM 1Project.channels LIMIT 1')

    df=pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    st.write(":blue[Maximum video count]")
    st.write(df)

#3
elif query_select== "3.What are the top 10 most viewed videos and their respective channels?":
    mycursor.execute("SELECT channels.channel_name, videos.Video_viewcount \
                FROM 1Project.videos \
                JOIN channels ON videos.channel_id = channels.channel_id \
                ORDER BY videos.Video_viewcount DESC LIMIT 10")
    df=pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    st.write(":green[Top 10 Most viewed video and their channel name]")
    st.write(df)

#4
elif query_select=="4.How many comments were made on each video, and what are their corresponding video names?":
    mycursor.execute("SELECT Video_title,Video_commentcount FROM 1Project.videos ORDER BY Video_commentcount DESC")

    df=pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    st.write(":green[comments on each video and cor video name]")
    st.write(df)

#5
elif query_select=="5.Which videos have the highest number of likes, and what are their corresponding channel names?":
    mycursor.execute("SELECT channels.channel_name, videos.Video_likecount \
    FROM 1Project.videos \
    JOIN channels ON videos.channel_id = channels.channel_id \
    WHERE videos.Video_likecount = (SELECT MAX(Video_likecount) FROM videos)")

    df=pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    st.write(":green[Highest Likes and their channel name]")
    st.write(df)

#6
elif query_select=="6.What is the total number of likes and dislikes for each video, and what are their corresponding video names?":
    mycursor.execute("SELECT Video_title,Video_likecount FROM 1Project.videos GROUP BY Video_title ORDER BY Video_likecount DESC")
    st.write(":green[Total number of likes and their channel names]")
    df=pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    st.write(df)

#7
elif query_select== "7.What is the total number of views for each channel, and what are their corresponding channel names?":
    mycursor.execute('SELECT channel_name,channel_viewcount  FROM 1Project.channels ORDER by channel_viewcount  DESC')
    
    df=pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    st.write(":green[views for each channel]")
    st.write(df)

#8
elif query_select=="8.What are the names of all the channels that have published videos in the year 2022?":
    mycursor.execute("SELECT DISTINCT channels.channel_name \
                FROM 1Project.channels \
                JOIN videos ON channels.channel_id = videos.channel_id \
                WHERE YEAR(Video_pubdate) = 2022")

    df=pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    st.write(":green[name of channels published video on 2022]")
    st.write(df)

#9
elif query_select== "9.What is the average duration of all videos in each channel, and what are their corresponding channel names?":
    mycursor.execute("SELECT channels.channel_name, SEC_TO_TIME(AVG(videos.Video_duration)) AS average_duration \
                FROM 1Project.videos \
                JOIN channels ON videos.channel_id = channels.channel_id \
                GROUP BY channels.channel_name")

    df=pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    st.write(":green[Average video duration for each channels]")
    st.write(df)

#10
elif query_select== "10.Which videos have the highest number of comments, and what are their corresponding channel names?":
    mycursor.execute("SELECT channels.channel_name, videos.Video_title, videos.Video_commentcount \
                FROM 1Project.videos \
                JOIN channels ON videos.channel_id = channels.channel_id \
                ORDER by (Video_commentcount) DESC LIMIT 10")

    df=pd.DataFrame(mycursor.fetchall(),columns=mycursor.column_names)
    st.write(":green[Highest number of comments and their channel name]")
    st.write(df)
