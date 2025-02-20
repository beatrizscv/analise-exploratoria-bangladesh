#Importing libraries

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import kagglehub
import os

#Downloading dataset
dir_path = kagglehub.dataset_download("arifmia/agricultural-land-suitability-and-soil-quality")
os.listdir(dir_path)

#Reading dataset
df = pd.read_csv(os.path.join(dir_path,'bangladesh_divisions_dataset.csv'))
df

#Finding missing values
df.isna().sum()

#Describing numerical data
df.describe()

#Quantifying 'Soil_Type' variable
soil_count = df.Soil_Type.value_counts().reset_index().sort_values(by='count', ascending=False)

fig, axs = plt.subplots(1, 2, figsize=(10, 6))

plt.suptitle('Distribution of Soil Types')
sns.barplot(x=soil_count['Soil_Type'],
            y=soil_count['count'],
            hue = soil_count['Soil_Type'],
            palette = sns.color_palette("Paired"),
            ax=axs[0])
for container in axs[0].containers:
    axs[0].bar_label(container)
axs[0].set_xlabel("Soil Types")
axs[0].set_ylabel("Count")
axs[1].pie(soil_count['count'],
           labels=soil_count['Soil_Type'],
           autopct='%1.1f%%',
           colors = sns.color_palette("Paired"))

soil_count_fig = plt.gcf()
soil_count_fig.savefig('images/Distribution_Soil_Types.png', format='png')

#Quantifying 'Land_Use_Type' variable
landuse_count = df.Land_Use_Type.value_counts().reset_index().sort_values(by='count', ascending=False)

fig, axs = plt.subplots(1, 2, figsize=(10, 6))

plt.suptitle('Distribution of Land Uses')
sns.barplot(x=landuse_count['Land_Use_Type'],
            y=landuse_count['count'],
            hue = landuse_count['Land_Use_Type'],
            palette = sns.color_palette("Paired"),
            ax=axs[0])
for container in axs[0].containers:
    axs[0].bar_label(container)
axs[0].set_xlabel("Land Uses")
axs[0].set_ylabel("Count")
axs[1].pie(landuse_count['count'],
           labels=landuse_count['Land_Use_Type'],
           autopct='%1.1f%%',
           colors = sns.color_palette("Paired"))

landuse_count_fig = plt.gcf()
landuse_count_fig.savefig('images/Distribution_LandUse_Types.png', format='png')

#Quantifying 'Crop_Suitability' variable
crop_count = df.Crop_Suitability.value_counts().reset_index().sort_values(by='count', ascending=False)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

plt.suptitle('Distribution of Crop Types')
plt.subplots_adjust(wspace=0.1)
sns.barplot(x=crop_count['Crop_Suitability'],
            y=crop_count['count'],
            hue = crop_count['Crop_Suitability'],
            palette = sns.color_palette("Paired"),
            ax=axs[0])
for container in axs[0].containers:
    axs[0].bar_label(container)
axs[0].set_xlabel("Crop Types")
axs[0].set_ylabel("Count")
axs[1].pie(crop_count['count'],
           labels=crop_count['Crop_Suitability'],
           autopct='%1.1f%%',
           colors = sns.color_palette("Paired"))

crop_count_fig = plt.gcf()
crop_count_fig.savefig('images/Distribution_Crop_Types.png', format='png')

#Relation between 'Soil_Type' and 'Fertility_Index'
soil_fertility = df.groupby(['Soil_Type'])['Fertility_Index'].describe().reset_index()

plt.figure(figsize=(10, 6))
plt.title('Fertility Index mean of each Soil Type')

sns.boxplot(data=df,
            x='Soil_Type',
            y='Fertility_Index',
            palette = sns.color_palette("Paired"),
            hue='Soil_Type')
plt.xlabel("Soil Types")
plt.ylabel("Fertility Index")

sns.pointplot(data=soil_fertility,
              x=soil_fertility['Soil_Type'],
              y=soil_fertility['mean'],
              color='yellow')

soil_fertility_fig = plt.gcf()
soil_fertility_fig.savefig('images/Fertility_Index_Soil_Types.png', format='png')

#Relation between 'Crop_Suitability' and 'Fertility_Index'
crop_fertility = df.groupby(['Crop_Suitability'])['Fertility_Index'].describe().reset_index()

plt.figure(figsize=(10, 6))
plt.title('Fertility Index mean of each Crop Type')

sns.boxplot(data=df,
            x='Crop_Suitability',
            y='Fertility_Index',
            palette = sns.color_palette("Paired"),
            hue='Crop_Suitability')
plt.xlabel("Crop Types")
plt.ylabel("Fertility Index")

sns.pointplot(data=crop_fertility,
              x=crop_fertility['Crop_Suitability'],
              y=crop_fertility['mean'],
              color='yellow')

crop_fertility_fig = plt.gcf()
crop_fertility_fig.savefig('images/Fertility_Index_Crop_Types.png', format='png')

#Relation between 'Soil_Type' and 'Crop_Suitability'
soil_crop = df.groupby(['Soil_Type'])['Crop_Suitability'].value_counts().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
plt.suptitle('Relation between Soil Types and Crop Types')

sns.barplot(x=soil_crop['Soil_Type'],
            y=soil_crop['count'],
            hue=soil_crop['Crop_Suitability'],
            palette = sns.color_palette("Paired"),
            ax=ax)
for container in ax.containers:
    ax.bar_label(container)
plt.xlabel("Soil Types")
plt.ylabel("Count")
plt.legend(loc='upper center', ncol = 7, borderaxespad=-2.5)

soil_crop_fig = plt.gcf()
soil_crop_fig.savefig('images/Soil_Crop_Types.png', format='png')

#Relation between 'Soil_Type' and 'Land_Use_Type'
soil_landuse = df.groupby(['Soil_Type'])['Land_Use_Type'].value_counts().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
plt.suptitle('Relation between Soil Types and Land Uses')

sns.barplot(x=soil_landuse['Soil_Type'],
            y=soil_landuse['count'],
            hue=soil_landuse['Land_Use_Type'],
            palette = sns.color_palette("Paired"),
            ax=ax)
for container in ax.containers:
    ax.bar_label(container)
plt.xlabel("Soil Types")
plt.ylabel("Count")
plt.legend(loc='upper center', ncol = 4, borderaxespad=-2.5)

soil_landuse_fig = plt.gcf()
soil_landuse_fig.savefig('images/Soil_LandUse_Types.png', format='png')

#Best growing season for each Crop Type
season_crop = df.groupby(['Crop_Suitability'])['Season'].value_counts().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
plt.suptitle('Best growing season for each Crop Type')

sns.barplot(x=season_crop['Crop_Suitability'],
            y=season_crop['count'],
            hue=season_crop['Season'],
            palette = sns.color_palette("Paired"),
            ax=ax)
for container in ax.containers:
    ax.bar_label(container)
ax.set_xlabel("Crop_Suitability")
ax.set_ylabel("Count")
plt.legend(loc='upper center', ncol = 4, borderaxespad=-2.5)

season_crop_fig = plt.gcf()
season_crop_fig.savefig('images/Season_Crop.png', format='png')

#Transforming 'Satellite_Observation_Date' column to datetime
df['Satellite_Observation_Date'] = pd.to_datetime(df['Satellite_Observation_Date'])

#Creating 'Month' column
df['Month'] = df['Satellite_Observation_Date'].dt.month

#Relation between 'Month' and 'Average_Rainfall(mm)'
rain_month = df.groupby(['Month'])['Average_Rainfall(mm)'].describe().reset_index()

plt.figure(figsize=(10, 6))
plt.suptitle('Average Rainfall of each Month of 2024')

sns.boxplot(data=df,
            x='Month',
            y='Average_Rainfall(mm)',
            palette = sns.color_palette("Paired"),
            hue='Month')
plt.xlabel("Months")
plt.ylabel("Average Rainfall (mm)")

sns.pointplot(data=rain_month,
              x=rain_month['Month'],
              y=rain_month['mean'],
              color='yellow')
plt.legend(loc = 'upper center',
           ncol = 12,
           borderaxespad = -2.5,
           columnspacing = 1.5)

rain_month_fig = plt.gcf()
rain_month_fig.savefig('images/Rainfall_Month.png', format='png')

#Relation between 'Month' and 'Temperature(°C)'
temp_month = df.groupby(['Month'])['Temperature(°C)'].describe().reset_index()

plt.figure(figsize=(10, 6))
plt.suptitle('Temperature mean of each Month of 2024')

sns.boxplot(data=df,
            x='Month',
            y='Temperature(°C)',
            palette = sns.color_palette("Paired"),
            hue='Month')
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")

sns.pointplot(data=temp_month,
              x=temp_month['Month'],
              y=temp_month['mean'],
              color='yellow')
plt.legend(loc = 'upper center',
           ncol = 12,
           borderaxespad = -2.5,
           columnspacing = 1.5)

temp_month_fig = plt.gcf()
temp_month_fig.savefig('images/Temperature_Month.png', format='png')
