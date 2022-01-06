import pandas as pd
import matplotlib as mpl
import csv

rows = []

with open("final_total_stars.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

mass = []
radius = []
star_name=[]
for star_data in star_data_rows:
  mass.append(star_data[4])
  radius.append(star_data[5])
  star_name.append(star_data[2])

headers = rows[0]
star_data_rows = rows[1:]
print(headers)

star_gravity = []

for index, name in enumerate(star_name):
  gravity = (float(star_data[4])*1.989+30) / (float(star_data[5])*float(star_data[5])*6.957e+8)
  star_gravity.append(gravity)

final_dict={}

for index,planet_data in enumerate(star_data_rows):
  features_list=[]
  gravity = (float(star_data[4])*1.989+30) / (float(star_data[5])*float(star_data[5])*6.957e+8)
  try:
    if gravity>150 and gravity<350:
      features_list.append("gravity")
  except:pass
  try:
    if star_data[4]<100:
      features_list.append("distance")
  except:pass
  final_dict[index]=features_list

print(final_dict)



    