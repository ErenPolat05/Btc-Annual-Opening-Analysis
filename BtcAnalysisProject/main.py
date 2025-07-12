import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Getting Csv File:
df = pd.read_csv("BtcAnalysisProject/BTC.csv")

#We Need To Convert It To Datetime For Filter:
df["Date"] = pd.to_datetime(df["Date"]) 

#We Filter to Select Data from the Beginning of Each Year:
df["Year"] = df["Date"].dt.year  
df["Jan1"] = df["Date"].dt.strftime("%m-%d")
jan1_df = df[df["Jan1"] == "01-01"]
yearopen = jan1_df[["Year","Open"]]

#To Further Simplify Values And Determine The Type Of Value:
yearopen["Label"] = np.round(yearopen["Open"]).astype(int).astype(str) + " USD"

#Making Our Assignments For The Grafic:
y = yearopen["Open"]
x = yearopen["Year"]
labels = yearopen["Label"]

#Making Grafic:
plt.figure(figsize = (10,6)) #To Make New Grafic
plt.plot(x,y, marker = "o",color = "orange",label="Btc Open Price Every 1 JAN") 

#To Take Each USD Information In Turn And Write It To The Points:
for i in range(len(x)):
    plt.annotate(labels.iloc[i], (x.iloc[i], y.iloc[i]), textcoords="offset points", xytext=(0,15), ha='center', fontsize=9, color="black")


plt.title("BTC Opening Price on Every January 1st Each Year") #For Our Title
plt.xlabel("Years")   #For Our X Title
plt.ylabel("Opening Price (USD)") #For Our Y Title
plt.legend() #To See What The Line Shows
plt.grid(True)#Adds Vertical And Horizontal Lines For Easier Viewing
plt.tight_layout() #To Prevent The Text From Overlapping

plt.savefig("BtcAnalysisProject/Btc_Grafic.png") #To Save Our Grafic (PNG)

"""
plt.show() #To See Our Grafic
"""


