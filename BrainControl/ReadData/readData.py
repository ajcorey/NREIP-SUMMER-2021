# Writen by Andrew Sullivan
# June 29, 2021
# amsullivan2@wpi.edu

# The next two lines are for if you are getting a message in the terminal
# about matplotlib and its cache, comment out the next two lines if needed
import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"

# Import the libraries that we need
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


# Try loop that allows for a graceful exit if needed
try:

    # Set variable for the filename to make changing easier later on
    fileName = "".join(('SoniaThinking', '.csv'))
    outputFileName = "".join(('SoniaThinking', 'Output.csv'))
    graphFileName = "".join(('SoniaThinking','Output.jpg'))

    # Make the DataFrame, read the .CSV, and skip the header and information rows
    df = pd.read_csv(fileName, skiprows = 5, header = None)

    # Delete unnecessary columns and rename the remaining ones
    df = df.drop(df.columns[[0,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]], axis=1)
    df.columns = ['Channel1', 'Channel2', 'Channel3', 'Channel4', 'Channel5', 'Channel6', 'Channel7', 'Channel8', 'Channel9', 'Channel10', 'Channel11', 'Channel12', 'Channel13', 'Channel14', 'Channel15', 'Channel16', 'Timestamp']

    # Convert the formatted timestamp to UNIX
    print('Converting Timestamps!')
    for i in range(0, len(df)):
        formattedDate = df.iloc[i, 16]
        unixDate = datetime.strptime(formattedDate, ' %Y-%m-%d %H:%M:%S.%f').strftime("%s.%f")[:-3]
        df.iat[i, 16] = unixDate

    # Clean the data with a Simple Moving Average (SMA)
    print('Cleaning Data!')
    df['SMA_100_1'] = df.iloc[:,0].rolling(window=100).mean()
    df['SMA_100_2'] = df.iloc[:,1].rolling(window=100).mean()
    df['SMA_100_3'] = df.iloc[:,2].rolling(window=100).mean()
    df['SMA_100_4'] = df.iloc[:,3].rolling(window=100).mean()
    df['SMA_100_5'] = df.iloc[:,4].rolling(window=100).mean()
    df['SMA_100_6'] = df.iloc[:,5].rolling(window=100).mean()
    df['SMA_100_7'] = df.iloc[:,6].rolling(window=100).mean()
    df['SMA_100_8'] = df.iloc[:,7].rolling(window=100).mean()
    df['SMA_100_9'] = df.iloc[:,8].rolling(window=100).mean()
    df['SMA_100_10'] = df.iloc[:,9].rolling(window=100).mean()
    df['SMA_100_11'] = df.iloc[:,10].rolling(window=100).mean()
    df['SMA_100_12'] = df.iloc[:,11].rolling(window=100).mean()
    df['SMA_100_13'] = df.iloc[:,12].rolling(window=100).mean()
    df['SMA_100_14'] = df.iloc[:,13].rolling(window=100).mean()
    df['SMA_100_15'] = df.iloc[:,14].rolling(window=100).mean()
    df['SMA_100_16'] = df.iloc[:,15].rolling(window=100).mean()

    # Convert DataFrame to a .CSV
    df.to_csv(outputFileName, index = False)
    print('Output .CSV Saved!')

    # Graph the data
    print('Now Graphing Data!')
    
    
    ChannelOne = df[['Timestamp', 'Channel1']]
    ChannelTwo = df[['Timestamp', 'Channel2']]
    ChannelThree = df[['Timestamp', 'Channel3']]
    ChannelFour = df[['Timestamp', 'Channel4']]
    x = df.Timestamp
    y1 = ChannelOne.Channel1
    y2 = ChannelTwo.Channel2
    y3 = ChannelThree.Channel3
    y4 = ChannelFour.Channel4
    
    
    axes[0][0].plot(x,y1, label='Channel1')
    axes[0][0].legend()
    axes[0][1].plot(x,y2, label='Channel2')
    axes[0][1].legend()
    axes[1][0].plot(x,y3, label='Channel3')
    axes[1][0].legend()
    axes[1][1].plot(x,y4, label='Channel3')
    axes[1][1].legend()
    
    
    
    
    
    
    # plt.xlabel('UNIX Timestamp')
    # plt.ylabel('Reading from Channel')
    # x = df.Timestamp    # UNIX Timestamp Data
    # y1 = df.SMA_100_1   # Channel1 Data
    # y2 = df.SMA_100_2   # Channel2 Data
    # y3 = df.SMA_100_3   # Channel3 Data
    # y4 = df.SMA_100_4   # Channel4 Data
    # y5 = df.SMA_100_5   # Channel5 Data
    # y6 = df.SMA_100_6   # Channel6 Data
    # y7 = df.SMA_100_7   # Channel7 Data
    # y8 = df.SMA_100_8   # Channel8 Data
    # y9 = df.SMA_100_9   # Channel9 Data
    # y10 = df.SMA_100_10 # Channel10 Data
    # y11 = df.SMA_100_11 # Channel11 Data
    # y12 = df.SMA_100_12 # Channel12 Data
    # y13 = df.SMA_100_13 # Channel13 Data
    # y14 = df.SMA_100_14 # Channel14 Data
    # y15 = df.SMA_100_15 # Channel15 Data
    # y16 = df.SMA_100_16 # Channel16 Data
    # plt.plot(x, y1, label = 'Channel 1')
    # plt.plot(x, y2, label = 'Channel 2')
    # plt.plot(x, y3, label = 'Channel 3')
    # plt.plot(x, y4, label = 'Channel 4')
    # plt.plot(x, y5, label = 'Channel 5')
    # plt.plot(x, y6, label = 'Channel 6')
    # plt.plot(x, y7, label = 'Channel 7')
    # plt.plot(x, y8, label = 'Channel 8')
    # plt.plot(x, y9, label = 'Channel 9')
    # plt.plot(x, y10, label = 'Channel 10')
    # plt.plot(x, y11, label = 'Channel 11')
    # plt.plot(x, y12, label = 'Channel 12')
    # plt.plot(x, y13, label = 'Channel 13')
    # plt.plot(x, y14, label = 'Channel 14')
    # plt.plot(x, y15, label = 'Channel 15')
    # plt.plot(x, y16, label = 'Channel 16')
    # plt.legend(loc = 2)
    
    # Save and Show the Graph
    plt.savefig(graphFileName, dpi=600)
    print('Graph .JPG Saved!')
    plt.show()

# Graceful exit
except (KeyboardInterrupt, SystemExit):
    print ("\nExiting.")
    exit