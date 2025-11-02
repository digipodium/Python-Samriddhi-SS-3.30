import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

df = sns.load_dataset("titanic")

st.title("Explore the insights here👇")

#filtering options
st.sidebar.title("Filter Options")

#gender filter
gender = st.sidebar.multiselect("Gender",
                                options=df["sex"].unique(),
                                )

#class filter
pclass = st.sidebar.multiselect("Passenger Class",
                                options=df["class"].unique(),
                                )

#age filter
age = st.sidebar.slider("Age Range",
                        min_value=int(df["age"].min()),
                        max_value=int(df["age"].max()),
                        value=(int(df["age"].min()), int(df["age"].max()))
                        )

#applying filters
filtered_df = df.copy()
if gender:
    filtered_df = filtered_df[filtered_df["sex"].isin(gender)] #this line filters the dataframe based on selected genders, isin checks if the value is in the list
if pclass:
    filtered_df = filtered_df[filtered_df["class"].isin(pclass)]
if age:     
    filtered_df = filtered_df[(filtered_df["age"] >= age[0]) & (filtered_df["age"] <= age[1])] #we are using 1 for maximum range, this is the concept of boolean indexing
st.dataframe(filtered_df)

#histogram of age distribution
fig = px.histogram(filtered_df, x="age", nbins=30, title="Age Distribution")
st.plotly_chart(fig)
#conclusion point
st.markdown("**Conclusion:** The age distribution of Titanic passengers is right-skewed, with a higher concentration of younger passengers. There is a noticeable drop in the number of passengers above 60 years old.")

#bar chart of survival count by passenger class
fig2 = px.bar(filtered_df, x = 'class', y='survived', 
              labels={'index':'Survived', 'survived':'Count'}, 
              title="Survival Count by Passenger Class")
st.plotly_chart(fig2)

#pie chart of class distribution
fig3 = px.pie(filtered_df, names='class', title="Class Distribution")
st.plotly_chart(fig3)

