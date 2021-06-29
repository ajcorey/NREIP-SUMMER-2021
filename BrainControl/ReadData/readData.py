# Writen by Andrew Sullivan
# June 29, 2021
# amsullivan2@wpi.edu

# Import the libraries that we need
import csv
import pandas as pd



# Skip the header and information rows
df = pandas.read_csv('SoniaThinking.csv', skiprows=4)


# Print the data frame
df 