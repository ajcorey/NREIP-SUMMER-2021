#!/usr/bin/env python3

# Writen by Andrew Sullivan
# June 29, 2021
# amsullivan2@wpi.edu

# Import the libraries that we need
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Try loop that allows for a graceful exit if needed
try:

    # Ask the user for the file name
    fileNameInput = input("Please Input the File Name WITHOUT the Extension: ") # Ask user for mission command
    fileNameInput = str(fileNameInput.upper())

    # Set variable for the filename to make changing easier later on
    fileName = 'fileNameInput.csv'
    outputFileName = "".join(('fileNameInput', 'Output.csv'))
    graphFileName = "".join(('fileNameInput','Output.jpg'))

    # Make the DataFrame, read the .CSV, and skip the header and information rows
    df = pd.read_csv(fileName, skiprows = 5, header = None)


    # Delete unnecessary columns and rename the remaining ones
    df = df.drop(df.columns[[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]], axis=1)
    df.columns = ['Channel1', 'Timestamp']

    # Convert the formatted timestamp to UNIX
    for i in range(0, len(df)):
        formattedDate = df.iloc[i, 1]
        unixDate = datetime.strptime(formattedDate, ' %Y-%m-%d %H:%M:%S.%f').strftime("%s.%f")[:-3]
        df.iat[i, 1] = unixDate


    # Convert DataFrame to a .CSV
    df.to_csv(outputFileName, index = False)

    # Graph the data
    x = df.Timestamp
    y = df.Channel1

    plt.scatter(x,y)
    plt.savefig(graphFileName)
    plt.show()

# Graceful exit
except (KeyboardInterrupt, SystemExit):
    print "\nExiting."
    exit