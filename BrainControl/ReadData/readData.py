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
    graphFileName = "".join(('SoniaThinking','Output.pdf'))

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
    
    ## Sets up groupings for the subplots
    c1 = df[['Timestamp', 'SMA_100_1']]
    c2 = df[['Timestamp', 'SMA_100_2']]
    c3 = df[['Timestamp', 'SMA_100_3']]
    c4 = df[['Timestamp', 'SMA_100_4']]
    c5 = df[['Timestamp', 'SMA_100_5']]
    c6 = df[['Timestamp', 'SMA_100_6']]
    c7 = df[['Timestamp', 'SMA_100_7']]
    c8 = df[['Timestamp', 'SMA_100_8']]
    c9 = df[['Timestamp', 'SMA_100_9']]
    c10 = df[['Timestamp', 'SMA_100_10']]
    c11 = df[['Timestamp', 'SMA_100_11']]
    c12 = df[['Timestamp', 'SMA_100_12']]
    c13 = df[['Timestamp', 'SMA_100_13']]
    c14 = df[['Timestamp', 'SMA_100_14']]
    c15 = df[['Timestamp', 'SMA_100_15']]
    c16 = df[['Timestamp', 'SMA_100_16']]
    
    ## Sets up layout of the plots
    fig, axes = plt.subplots(2, 2, sharex = 'col', sharey = 'row')
    
    ## Sets up variables for plotting
    x = df.Timestamp
    y1 = c1.SMA_100_1
    y2 = c2.SMA_100_2
    y3 = c3.SMA_100_3
    y4 = c4.SMA_100_4
    y5 = c5.SMA_100_5
    y6 = c6.SMA_100_6
    y7 = c7.SMA_100_7
    y8 = c8.SMA_100_8
    y9 = c9.SMA_100_9
    y10 = c10.SMA_100_10
    y11 = c11.SMA_100_11
    y12 = c12.SMA_100_12
    y13 = c13.SMA_100_13
    y14 = c14.SMA_100_14
    y15 = c15.SMA_100_15
    y16 = c16.SMA_100_16

    ## Plots the data    
    ### Row 1
    axes[0][0].plot(x,y1, label='Channel 1')
    axes[0][0].legend()
    axes[0][1].plot(x,y2, label='Channel 2')
    axes[0][1].legend()
    # axes[0][2].plot(x,y3, label='Channel 3')
    # axes[0][2].legend()
    # axes[0][3].plot(x,y4, label='Channel 4')
    # axes[0][3].legend()
    ### Row 2    
    axes[1][0].plot(x,y1, label='Channel 5')
    axes[1][0].legend()
    axes[1][1].plot(x,y2, label='Channel 6')
    axes[1][1].legend()
    # axes[1][2].plot(x,y3, label='Channel 7')
    # axes[1][2].legend()
    # axes[1][3].plot(x,y4, label='Channel 8')
    # axes[1][3].legend()
    # ### Row 3
    # axes[2][0].plot(x,y1, label='Channel 9')
    # axes[2][0].legend()
    # axes[2][1].plot(x,y2, label='Channel 10')
    # axes[2][1].legend()
    # axes[2][2].plot(x,y3, label='Channel 11')
    # axes[2][2].legend()
    # axes[2][3].plot(x,y4, label='Channel 12')
    # axes[2][3].legend()
    # ### Row 4
    # axes[3][0].plot(x,y1, label='Channel 13')
    # axes[3][0].legend()
    # axes[3][1].plot(x,y2, label='Channel 14')
    # axes[3][1].legend()
    # axes[3][2].plot(x,y3, label='Channel 15')
    # axes[3][2].legend()
    # axes[3][3].plot(x,y4, label='Channel 16')
    # axes[3][3].legend()
        
    # Save and Show the Graph
    plt.savefig(graphFileName, dpi=600)
    print('Graph .PDF Saved!')
    #plt.show() # Commented out to save time, this takes a LONG time to show the graph of

# Graceful exit
except (KeyboardInterrupt, SystemExit):
    print ("\nExiting.")
    exit