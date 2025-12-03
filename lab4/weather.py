import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

df = df.dropna()

df["date"] = pd.to_datetime(df["date"])

daily_mean = df["temperature"].mean()
daily_min = df["temperature"].min()
daily_max = df["temperature"].max()
daily_std = df["temperature"].std()

df["month"] = df["date"].dt.month

monthly_rain = df.groupby("month")["rainfall"].sum()

plt.plot(df["date"], df["temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("daily_temperature.png")
plt.close()

plt.bar(monthly_rain.index, monthly_rain.values)
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.savefig("monthly_rainfall.png")
plt.close()

plt.scatter(df["temperature"], df["humidity"])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.savefig("humidity_vs_temperature.png")
plt.close()

df.to_csv("cleaned_weather.csv", index=False)

summary = [
    "Arnav Kapil",
    "Roll No: 2501730045",
    "Daily Mean Temperature: " + str(daily_mean),
    "Daily Min Temperature: " + str(daily_min),
    "Daily Max Temperature: " + str(daily_max),
    "Daily Std Temperature: " + str(daily_std),
]

f = open("summary.txt", "w")
for line in summary:
    f.write(line + "\n")
f.close()
