# Writen by Andrew Sullivan
# June 29, 2021
# amsullivan2@wpi.edu

# If you are getting a message in the terminal 
# about matplotlib and its cache, uncomment the next two lines
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

# Import the libraries that we need
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt


# Try loop that allows for a graceful exit if needed
try:

    # # Ask the user for the file name
    # fileNameInput = input('Please Input the File Name WITHOUT the Extension: ') # Ask user for mission command
    # fileNameInput = str(fileNameInput)

    # Set variable for the filename to make changing easier later on
    fileName = "".join(('SoniaThinking', '.csv'))
    outputFileName = "".join(('SoniaThinking', 'Output.csv'))
    graphFileName = "".join(('SoniaThinking','Output.jpg'))

    # Make the DataFrame, read the .CSV, and skip the header and information rows
    df = pd.read_csv(fileName, skiprows = 5, header = None)


    # Delete unnecessary columns and rename the remaining ones
    df = df.drop(df.columns[[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]], axis=1)
    df.columns = ['Channel1', 'Timestamp']

    # Convert the formatted timestamp to UNIX
    print('Converting Timestamps!')
    for i in range(0, len(df)):
        formattedDate = df.iloc[i, 1]
        unixDate = datetime.strptime(formattedDate, ' %Y-%m-%d %H:%M:%S.%f').strftime("%s.%f")[:-3]
        df.iat[i, 1] = unixDate

    # Clean the data with a Simple Moving Average (SMA)
    print('Cleaning Data!')
    df['SMA_100'] = df.iloc[:,0].rolling(window=100).mean()
    

    # Convert DataFrame to a .CSV
    df.to_csv(outputFileName, index = False)
    print('Output .CSV Saved!')

    # Graph the data
    print('Now Graphing Data!')
    x = df.Timestamp
    y = df.SMA_100
    plt.scatter(x,y)
    
    # Save and Show the Graph
    plt.savefig(graphFileName, dpi=1600)
    print('Graph .JPG saved!')
    plt.show()

# Graceful exit
except (KeyboardInterrupt, SystemExit):
    print ("\nExiting.")
    exit
