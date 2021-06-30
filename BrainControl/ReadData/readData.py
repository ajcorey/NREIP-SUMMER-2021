# Writen by Andrew Sullivan
# June 29, 2021
# amsullivan2@wpi.edu



# Import the libraries that we need
import os
import pandas as pd
from datetime import datetime
## The next line is for if you are getting a message in the terminal
## about matplotlib and its cache, comment out the next line if needed
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt


filePath = os.path.dirname(os.path.abspath(__file__))
os.makedirs(filePath + '/Outputs/', exist_ok = True)
filePath = os.path.dirname(os.path.abspath(__file__)) + '/Outputs/'


# Try loop that allows for a graceful exit if needed
try:

    # Set variable for the filename to make changing easier later on
    bciFilename = 'SoniaThinking'
    csvFilename = bciFilename + '.csv'
    outputCSVFilename = filePath + bciFilename + 'Output.csv'
    pdfFilename = filePath + bciFilename

    # Make the DataFrame, read the .CSV, and skip the header and information rows
    df = pd.read_csv(csvFilename, skiprows = 5, header = None)

    # Delete unnecessary columns and rename the remaining ones
    df = df.drop(df.columns[[0,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]], axis=1)
    df.columns = ['Channel1', 'Channel2', 'Channel3', 'Channel4', 'Channel5', 'Channel6', 'Channel7', 'Channel8', 'Channel9', 'Channel10', 'Channel11', 'Channel12', 'Channel13', 'Channel14', 'Channel15', 'Channel16', 'Timestamp']

    # Convert the formatted timestamp to UNIX
    print('Converting Timestamps!')
    for i in range(0, len(df)):
        formattedDate = df.iloc[i, 16]
        unixDate = datetime.strptime(formattedDate, ' %Y-%m-%d %H:%M:%S.%f').strftime("%s.%f")[:-3]
        df.iat[i, 16] = unixDate

    # Clean the data with a Simple Moving Average (SMA) with a window of 100
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
    df.to_csv(outputCSVFilename, index = False)
    print('Output .CSV Saved!')

    # Graph the data
    print('Now Graphing Data!')
    
    ## Sets up layout of the plots
    # fig, axes = plt.subplots(2, 2, sharex = 'col', sharey = 'row')
    f1 = plt.figure()

    ## Sets up variables for plotting
    x = df.Timestamp
    y1 = df.SMA_100_1
    y2 = df.SMA_100_2
    y3 = df.SMA_100_3
    y4 = df.SMA_100_4
    y5 = df.SMA_100_5
    y6 = df.SMA_100_6
    y7 = df.SMA_100_7
    y8 = df.SMA_100_8
    y9 = df.SMA_100_9
    y10 = df.SMA_100_10
    y11 = df.SMA_100_11
    y12 = df.SMA_100_12
    y13 = df.SMA_100_13
    y14 = df.SMA_100_14
    y15 = df.SMA_100_15
    y16 = df.SMA_100_16
    frame1 = plt.gca()
 
    # Plot the data, save the data as a PDF, clear the plot, and
    # start again and run one channel at a time.
    
    ## Channel 1 Plot and Save
    plt.title('Channel 1 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    frame1.axes.get_xaxis().set_visible(False)
    plt.plot(x, y1)
    plt.savefig((pdfFilename + '_Channel_1.pdf'), dpi=600)
    print('Channel 1 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 2 Plot and Save
    plt.title('Channel 2 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y2)
    plt.savefig((pdfFilename + '_Channel_2.pdf'), dpi=600)
    print('Channel 2 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 2 Plot and Save
    plt.title('Channel 2 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y2)
    plt.savefig((pdfFilename + '_Channel_2.pdf'), dpi=600)
    print('Channel 2 Data Graph Saved as PDF!')
    plt.clf()

    ## Channel 3 Plot and Save
    plt.title('Channel 3 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y3)
    plt.savefig((pdfFilename + '_Channel_3.pdf'), dpi=600)
    print('Channel 3 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 4 Plot and Save
    plt.title('Channel 4 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y4)
    plt.savefig((pdfFilename + '_Channel_4.pdf'), dpi=600)
    print('Channel 4 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 5 Plot and Save
    plt.title('Channel 5 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y5)
    plt.savefig((pdfFilename + '_Channel_5.pdf'), dpi=600)
    print('Channel 5 Data Graph Saved as PDF!')
    plt.clf()

    ## Channel 6 Plot and Save
    plt.title('Channel 6 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y6)
    plt.savefig((pdfFilename + '_Channel_6.pdf'), dpi=600)
    print('Channel 6 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 7 Plot and Save
    plt.title('Channel 7 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y7)
    plt.savefig((pdfFilename + '_Channel_7.pdf'), dpi=700)
    print('Channel 7 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 8 Plot and Save
    plt.title('Channel 8 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y8)
    plt.savefig((pdfFilename + '_Channel_8.pdf'), dpi=800)
    print('Channel 8 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 9 Plot and Save
    plt.title('Channel 9 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y9)
    plt.savefig((pdfFilename + '_Channel_9.pdf'), dpi=900)
    print('Channel 9 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 10 Plot and Save
    plt.title('Channel 10 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y10)
    plt.savefig((pdfFilename + '_Channel_10.pdf'), dpi=1000)
    print('Channel 10 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 11 Plot and Save
    plt.title('Channel 11 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y11)
    plt.savefig((pdfFilename + '_Channel_11.pdf'), dpi=1100)
    print('Channel 11 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 12 Plot and Save
    plt.title('Channel 12 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y12)
    plt.savefig((pdfFilename + '_Channel_12.pdf'), dpi=1200)
    print('Channel 12 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 13 Plot and Save
    plt.title('Channel 13 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y13)
    plt.savefig((pdfFilename + '_Channel_13.pdf'), dpi=1300)
    print('Channel 13 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 14 Plot and Save
    plt.title('Channel 14 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y14)
    plt.savefig((pdfFilename + '_Channel_14.pdf'), dpi=1400)
    print('Channel 14 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 15 Plot and Save
    plt.title('Channel 15 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y15)
    plt.savefig((pdfFilename + '_Channel_15.pdf'), dpi=1500)
    print('Channel 15 Data Graph Saved as PDF!')
    plt.clf()
    
    ## Channel 16 Plot and Save
    plt.title('Channel 16 Data')
    plt.xlabel('Time')
    plt.ylabel('Electrode Readings')
    plt.plot(x, y16)
    plt.savefig((pdfFilename + '_Channel_16.pdf'), dpi=1600)
    print('Channel 16 Data Graph Saved as PDF!')
    print('All Channels Successfully Graphed and Saved as PDFs!')
    plt.clf()

    ## Commented out to save time, feel free to uncomment for interactive plot
    # plt.show() 


# Graceful exit
except (KeyboardInterrupt, SystemExit):
    print ("Exiting.")
    exit