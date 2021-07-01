#!/usr/bin/env python3
# File Name:
# singlePDFReadData.py
# Author Information:
# Andrew Sullivan
# amsullivan2@wpi.edu
# Decription:
# June 30, 2021
# This program takes a .CSV generated by OpenBCI's Cyton board,
# processes the data to remove extraneous data points, graphs the data points,
# and then saves the graphs as PDFs. This version saves the graphs for the 16
# channels as one PDF. multiPDFReadData.py saves them as seperate PDFs.
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/ajcorey/NREIP-SUMMER-2021/blob/main/LICENSE


# Import the libraries that we need
import os
import pandas as pd
from datetime import datetime

## The next line is for if you are getting a message in the terminal
## about matplotlib and its cache, comment out the next line if needed
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt


# Ask the user for the file name
print('Please ensure that the dataset file is in the Datasets/ directory')
fileNameInput = input('Please Input the file name WITHOUT the file extension: ')


# Set up the filepaths and for later
filePath = os.path.dirname(os.path.abspath(__file__))
os.makedirs(filePath + '/Outputs/' + str(fileNameInput) + '/', exist_ok = True)
inputFilePath = filePath + '/Datasets/'
filePath = os.path.dirname(os.path.abspath(__file__)) + '/Outputs/' + str(fileNameInput) + '/'


# Set variable for the filename to make changing easier later on
bciFileName = str(fileNameInput)
outputCSVFileName = filePath + bciFileName + 'Output.csv'
pdfFileName = filePath + bciFileName


# Convert the file from .TXT to .CSV if needed
continueFlag = True
while continueFlag:
    print('Does this file need to be converted from .TXT to .CSV?')
    needsConversion = input('Y/N: ')
    needsConversion = str(needsConversion.upper())
    if needsConversion == 'Y' or needsConversion == 'YES':
        csvFileName = inputFilePath + bciFileName + '.txt'
        tempName = inputFilePath + bciFileName + '.csv'
        os.rename(csvFileName, tempName)
        csvFileName = inputFilePath + bciFileName + '.csv'
        print('File converted successfully!')
        continueFlag = False

    elif needsConversion == 'N' or needsConversion == 'NO':
        csvFileName = inputFilePath + bciFileName + '.csv'
        print('File will not be converted!')
        continueFlag = False

    else:
        print('Invalid option, please try again!')
        print()


# Try loop that allows for a graceful exit if needed
try:
    # Make the DataFrame, read the .CSV, and skip the header and information rows
    df = pd.read_csv(csvFileName, skiprows = 5, header = None)


    # Delete unnecessary columns and rename the remaining ones
    df = df.drop(df.index[17:32], axis = 1)
    df = df.drop(df.columns[[0]], axis = 1)
    df.columns = ['Channel01', 'Channel02', 'Channel03', 'Channel04', 'Channel05', 'Channel06', 'Channel07', 'Channel08', 'Channel09', 'Channel10', 'Channel11', 'Channel12', 'Channel13', 'Channel14', 'Channel15', 'Channel16', 'Timestamp']


    # Convert the formatted timestamp to UNIX
    print('Converting Timestamps!')
    for i in range(0, len(df)):
        formattedDate = df.iloc[i, 16]
        unixDate = datetime.strptime(formattedDate, ' %Y-%m-%d %H:%M:%S.%f').strftime("%s.%f")[:-3]
        df.iat[i, 16] = unixDate


    # Clean the data with a Simple Moving Average (SMA) with a window of 100
    print('Cleaning Data!')
    df['SMA_100_01'] = df.iloc[:,0].rolling(window=100).mean()
    df['SMA_100_02'] = df.iloc[:,1].rolling(window=100).mean()
    df['SMA_100_03'] = df.iloc[:,2].rolling(window=100).mean()
    df['SMA_100_04'] = df.iloc[:,3].rolling(window=100).mean()
    df['SMA_100_05'] = df.iloc[:,4].rolling(window=100).mean()
    df['SMA_100_06'] = df.iloc[:,5].rolling(window=100).mean()
    df['SMA_100_07'] = df.iloc[:,6].rolling(window=100).mean()
    df['SMA_100_08'] = df.iloc[:,7].rolling(window=100).mean()
    df['SMA_100_09'] = df.iloc[:,8].rolling(window=100).mean()
    df['SMA_100_10'] = df.iloc[:,9].rolling(window=100).mean()
    df['SMA_100_11'] = df.iloc[:,10].rolling(window=100).mean()
    df['SMA_100_12'] = df.iloc[:,11].rolling(window=100).mean()
    df['SMA_100_13'] = df.iloc[:,12].rolling(window=100).mean()
    df['SMA_100_14'] = df.iloc[:,13].rolling(window=100).mean()
    df['SMA_100_15'] = df.iloc[:,14].rolling(window=100).mean()
    df['SMA_100_16'] = df.iloc[:,15].rolling(window=100).mean()


    # Convert DataFrame to a .CSV
    df.to_csv(outputCSVFileName, index = False)
    print('Output .CSV Saved!')


    # Plot the data
    print('Now Plotting Data!')

    ## Sets up layout of the plots
    fig, axes = plt.subplots(4, 4)
    fig.suptitle('Data from All 16 Channels Displayed Left to Right')

    ## Sets up variables for plotting
    x = df.Timestamp
    y01 = df.SMA_100_01
    y02 = df.SMA_100_02
    y02 = df.SMA_100_02
    y03 = df.SMA_100_03
    y04 = df.SMA_100_04
    y05 = df.SMA_100_05
    y06 = df.SMA_100_06
    y07 = df.SMA_100_07
    y08 = df.SMA_100_08
    y09 = df.SMA_100_09
    y10 = df.SMA_100_10
    y11 = df.SMA_100_11
    y12 = df.SMA_100_12
    y13 = df.SMA_100_13
    y14 = df.SMA_100_14
    y15 = df.SMA_100_15
    y16 = df.SMA_100_16

    ## Plots the data
    ### Row 1
    axes[0][0].plot(x, y01,  label = '_nolegend_', linewidth = 0.1, color = '#FF1B8D')
    axes[0][1].plot(x, y02,  label = '_nolegend_', linewidth = 0.1, color = '#9b8507')
    axes[0][2].plot(x, y03,  label = '_nolegend_', linewidth = 0.1, color = '#9b8507')
    axes[0][3].plot(x, y04,  label = '_nolegend_', linewidth = 0.1, color = '#1BB3FF')
    ### Row 2
    axes[1][0].plot(x, y05,  label = '_nolegend_', linewidth = 0.1, color = '#FF1B8D')
    axes[1][1].plot(x, y06,  label = '_nolegend_', linewidth = 0.1, color = '#9b8507')
    axes[1][2].plot(x, y07,  label = '_nolegend_', linewidth = 0.1, color = '#9b8507')
    axes[1][3].plot(x, y08,  label = '_nolegend_', linewidth = 0.1, color = '#1BB3FF')
    ### Row 3
    axes[2][0].plot(x, y09,  label = '_nolegend_', linewidth = 0.1, color = '#FF1B8D')
    axes[2][1].plot(x, y10, label = '_nolegend_', linewidth = 0.1, color = '#9b8507')
    axes[2][2].plot(x, y11, label = '_nolegend_', linewidth = 0.1, color = '#9b8507')
    axes[2][3].plot(x, y12, label = '_nolegend_', linewidth = 0.1, color = '#1BB3FF')
    ### Row 4
    axes[3][0].plot(x, y13, label = '_nolegend_', linewidth = 0.1, color = '#FF1B8D')
    axes[3][1].plot(x, y14, label = '_nolegend_', linewidth = 0.1, color = '#9b8507')
    axes[3][2].plot(x, y15, label = '_nolegend_', linewidth = 0.1, color = '#9b8507')
    axes[3][3].plot(x, y16, label = '_nolegend_', linewidth = 0.1, color = '#1BB3FF')


    # Save and Show the Plot
    plt.setp(axes, xticks=[], yticks=[])
    plt.savefig((pdfFileName + '_AllChannels.pdf'), dpi = 38400)
    print('Plot .PDF Saved!')
    ## Commented out to save time, feel free to uncomment for interactive plot
    #plt.show()


# Graceful exit
except (KeyboardInterrupt, SystemExit):
    print ("Exiting.")
    exit
