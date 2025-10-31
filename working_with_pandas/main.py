import csv
import pandas as pd

DATA_URL = "/Users/elvisboves/Desktop/projects/working_with_pandas/weather_data.csv"

# with open(DATA_URL, mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     temperature = []
#     for row in reader:
#         temp = row["temp"]
#         temperature.append(temp)
#     print("TEMPERATURE", temperature)


#USIN PANDAS
# this calculats the mean using long way and logic
df = pd.read_csv(DATA_URL)
to_list = df['temp'].to_list()
# print(to_list)
length = len(to_list)
total = 0
for i in to_list:
    total += i
ave = round(total/length, 2)
# print(ave)

# Calculating the mean using PANDAS

pandas_average = df['temp'].mean()
# print(pandas_average)


#printing the largest number using pandas
max_number = df['temp'].max()
print(max_number)
