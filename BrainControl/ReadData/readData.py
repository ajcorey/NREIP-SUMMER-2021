# Writen by Andrew Sullivan
# June 29, 2021
# amsullivan2@wpi.edu

# If you are getting a message in the terminal 
# about matplotlib and its cache, uncomment the next two lines
#import os
#os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

# Import the libraries that we need
import pandas as pd
from datetime import datetime
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
    df = df.drop(df.columns[[0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]], axis=1)
    df.columns = ['Channel1', 'Channel2', 'Timestamp']

    # Convert the formatted timestamp to UNIX
    print('Converting Timestamps!')
    for i in range(0, len(df)):
        formattedDate = df.iloc[i, 2]
        unixDate = datetime.strptime(formattedDate, ' %Y-%m-%d %H:%M:%S.%f').strftime("%s.%f")[:-3]
        df.iat[i, 2] = unixDate

    # Clean the data with a Simple Moving Average (SMA)
    print('Cleaning Data!')
    df['SMA_100_1'] = df.iloc[:,0].rolling(window=100).mean()
    df['SMA_100_2'] = df.iloc[:,1].rolling(window=100).mean()

    # Convert DataFrame to a .CSV
    df.to_csv(outputFileName, index = False)
    print('Output .CSV Saved!')

    # Graph the data
    print('Now Graphing Data!')
    plt.xlabel('UNIX Timestamp')
    plt.ylabel('Reading from Channel')
    x = df.Timestamp  # UNIX Timestamp Data
    y1 = df.SMA_100_1 # Channel1 Data
    y2 = df.SMA_100_2 # Channel2 Data
    plt.plot(x, y1, label = 'Channel 1')
    plt.plot(x, y2, label = 'Channel 2')
    plt.legend(loc = 2)
    
    # Save and Show the Graph
    plt.savefig(graphFileName, dpi=600)
    print('Graph .JPG Saved!')
    plt.show()

# Graceful exit
except (KeyboardInterrupt, SystemExit):
    print ("\nExiting.")
    exit
    
# # For tomorrow
# -Add multiple streams of data
# -Record data and do different tasks, then print items
# -Add one channel at a time
# -Figure out cleaning the data and if you need to do the SMA_100 for each channel or need seperate one for each
# -change type of graph to be a line graph
# -need to label them
# -will need to change all the variables for the timestamp column
# -may want to do graphs for each one too since there are LARGE differences in what we see