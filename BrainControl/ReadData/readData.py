# Writen by Andrew Sullivan
# June 29, 2021
# amsullivan2@wpi.edu

# Import the libraries that we need
import csv
import pandas as pd



# Make the DataFrame, read the .CSV, and skip the header and information rows
df = pd.read_csv('SoniaThinking.csv', skiprows=5)


# Delete unnecessary columns
df.drop(df.columns[[0,21], axis=1) # Delete the "Sample Index" columns


# Convert DataFrame to a .CSV
df.to_csv('output.csv', index=False)