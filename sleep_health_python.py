#!/usr/bin/env python
# coding: utf-8

# ![insomnia](insomnia.jpg)
# 

# SleepInc, has shared anonymized sleep data from their hot new sleep tracking app SleepScope. As their data science consultant, your mission is to analyze the lifestyle survey data with Python to discover relationships between exercise, gender, occupation, and sleep quality. 
# 
# ## 💾 The data: sleep_health_data.csv
# 
# SleepInc has provided you with an anonymized dataset of sleep and lifestyle metrics for 374 individuals. This dataset contains average values for each person calculated over the past six months. The data is saved as `sleep_health_data.csv`.
# 
# The dataset includes 13 columns covering sleep duration, quality, disorders, exercise, stress, diet, demographics, and other factors related to sleep health. 
# 
# | Column | Description |
# |---------|----------------------------------------|  
# | `Person ID` | An identifier for each individual. |
# | `Gender` | The gender of the person (Male/Female). |  
# | `Age` | The age of the person in years. |
# | `Occupation` | The occupation or profession of the person. |
# | `Sleep Duration (hours)` | The average number of hours the person sleeps per day. |
# | `Quality of Sleep (scale: 1-10)` | A subjective rating of the quality of sleep, ranging from 1 to 10. |
# | `Physical Activity Level (minutes/day)` | The average number of minutes the person engages in physical activity daily. |  
# | `Stress Level (scale: 1-10)` | A subjective rating of the stress level experienced by the person, ranging from 1 to 10. |
# | `BMI Category` | The BMI category of the person (e.g., Underweight, Normal, Overweight). |
# | `Blood Pressure (systolic/diastolic)` | The average blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure. |
# | `Heart Rate (bpm)` | The average resting heart rate of the person in beats per minute. |
# | `Daily Steps` | The average number of steps the person takes per day. |
# | `Sleep Disorder` | The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea). |

###############################################################################################################################
# import packages
###############################################################################################################################
import pandas as pd

pd.set_option('display.max_columns', None)

###############################################################################################################################
# read in data
###############################################################################################################################
sleep = pd.read_csv('sleep_health_data.csv')

###############################################################################################################################
# Review Data
###############################################################################################################################
print(sleep.columns)
print(sleep.shape)
print(sleep.dtypes)
print(sleep.describe())
print(sleep.head())

###############################################################################################################################
# Occupation with lowest average sleep duration
###############################################################################################################################
duration_occ_ave = sleep.groupby(['Occupation'])[['Sleep Duration']].mean().reset_index().sort_values(by='Sleep Duration')
lowest_sleep_occ = duration_occ_ave['Occupation'].iloc[0]

###############################################################################################################################
# Occupation with lowest average sleep quality
###############################################################################################################################
quality_occ_ave = sleep.groupby(['Occupation'])[['Quality of Sleep']].mean().reset_index().sort_values(by='Quality of Sleep')
lowest_sleep_quality_occ = quality_occ_ave['Occupation'].iloc[0]
# boolean value if occupation with lowers sleep duration also has the lowest sleep quality
same_occ = lowest_sleep_occ==lowest_sleep_quality_occ

###############################################################################################################################
# How does BMI affect insomnia rates
###############################################################################################################################

sleep['Insomnia?'] = sleep['Sleep Disorder'] == 'Insomnia'
bmi_insomnia_df =sleep.groupby(['BMI Category'])[['Insomnia?']].mean()
bmi_insomnia_df['Insomnia?'] = bmi_insomnia_df['Insomnia?'].round(2)

# get dictionary of bmi to insomnia ratios
bmi_insomnia_ratios = bmi_insomnia_df['Insomnia?'].to_dict()
