# Writen by Andrew Sullivan
# June 29, 2021
# amsullivan2@wpi.edu

# Import the libraries that we need
import csv
import pandas as pd



# Make the DataFrame, read the .CSV, and skip the header and information rows
df = pd.read_csv('SoniaThinking.csv', skiprows=5)


# Delete unnecessary columns
df = .drop(df.columns[[0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]], axis=1)


# Convert DataFrame to a .CSV
df.to_csv('output.csv', index=False)

