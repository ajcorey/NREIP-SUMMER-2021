#!/usr/bin/env python3
# File Name:
# dataLogging.py
# Author Information:
# Drew Mulcare
# NREIP2021@mxdrew.com
# July 8, 2021
# Decription:
# This program gets a live stream of data from the OpenBCI Cyton + Daisy Board,
# factors it, converts it to a .CSV, and then plots the data and saves the 
# plots for each channel in a separate .PDF file.
# Reference Code and Library:
# https://github.com/openbci-archive/pyOpenBCI
# License:
# Software License Agreement (BSD License)
# Find the full agreement at https://github.com/ajcorey/NREIP-SUMMER-2021/blob/main/LICENSE


# Import the libraries that we need
from pyOpenBCI import OpenBCICyton
import numpy as np
import time
import pandas as pd
import os

# The next line is for if you are getting a message in the terminal
# about matplotlib and its cache, comment out the next line if needed
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt


# Set up the scale factor provided by the pyOpenBCI documentation
SCALE_FACTOR_EEG = (4500000)/24/(2**23-1) # uV/count to convert the channels_data to uVolts_per_count


# Ask the user for the file name
fileNameInput = input('Please input the name for your output files: ')
fileNameInput = str(fileNameInput)

# Set up the filepaths and for later
filePath = os.path.dirname(os.path.abspath(__file__))
os.makedirs(filePath + '/Outputs/' + fileNameInput + '/', exist_ok = True)
filePath = os.path.dirname(os.path.abspath(__file__)) + '/Outputs/' + fileNameInput + '/'


# Set variable for the filename to make changing easier later on
csvFileName = filePath + fileNameInput + 'Output.csv'
pdfFileName = filePath + fileNameInput

# These are the user and group id respectively, you will likely have to change them
# run the 'id' command to find yours and replace the two below
uid = 1000
gid = 1000

# Set up variable for the .CSV file used later
headerRow = 'Timestamp, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 \n'


# Open the .CSV file the data is being written to and print the header info
with open(csvFileName, 'a') as csvFile:
    csvFile.write(headerRow)
    csvFile.close()


# Define the main logging function
def logging(rawSample):
    # Check if the time limit has been reached yet
    if time.time() <= t_end:

        # Get the specific pieces of info that we need and convert it to a String
        channelData = np.array(rawSample.channels_data)
        timeData = str(time.time())

        # Apply the scale factor defined in the documentation
        channelData = channelData * SCALE_FACTOR_EEG

        # Convert back to a string for formatting
        channelData = np.array2string(channelData, separator=',')

        # Format the strings
        allData = timeData + ',' + channelData
        allData = allData.replace('[', '').replace(']', '').replace(' ', '').replace('\n', '')
        allData = allData + '\n'

        # Testing printing to a .CSV
        with open(csvFileName, 'a') as csvFile:
            csvFile.write(allData)
            csvFile.close()

    # Stop the stream of raw data if the time limit has been reached 
    else:
        board.stop_stream()


# Try loop that allows for a graceful exit if needed
try:
    # If the program cannot find an OpenBCI port, try restarting the Cyton board
    board = OpenBCICyton(daisy = True)


    # This sets up the end time of the live data stream
    # Currently runs for 5 minutes, alter the 5 to change the time
    t_end = time.time() + 60 * 5


    # Start the stream of raw data
    print('Starting to Log Data!')
    board.start_stream(logging)
    print('Data Has Been Logged')

    # Make the DataFrame, read the .CSV, and skip the header and information rows
    df = pd.read_csv(csvFileName, skiprows = 5, header = None)

    # Rename the columns
    df.columns = ['Timestamp', 'Channel01', 'Channel02', 'Channel03', 'Channel04', 'Channel05', 'Channel06', 'Channel07', 'Channel08', 'Channel09', 'Channel10', 'Channel11', 'Channel12', 'Channel13', 'Channel14', 'Channel15', 'Channel16']

    # Convert DataFrame to .CSV
    df.to_csv(csvFileName, index = False)
    print('Output .CSV Saved!')

    # Plot the data
    print('Now Plotting Data!')
    x = df.Timestamp
    y01 = df.Channel01
    y02 = df.Channel02
    y03 = df.Channel03
    y04 = df.Channel04
    y05 = df.Channel05
    y06 = df.Channel06
    y07 = df.Channel07
    y08 = df.Channel08
    y09 = df.Channel09
    y10 = df.Channel10
    y11 = df.Channel11
    y12 = df.Channel12
    y13 = df.Channel13
    y14 = df.Channel14
    y15 = df.Channel15
    y16 = df.Channel16

    # Plot the data, save the data as a PDF, clear the plot, and
    # start again and run one channel at a time.

    # Channel 1 Plot and Save
    plt.title('Channel 01 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y01, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_01.pdf'), dpi = 600)
    print('Channel 01 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 2 Plot and Save
    plt.title('Channel 02 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y02, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_02.pdf'), dpi = 600)
    print('Channel 02 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 3 Plot and Save
    plt.title('Channel 03 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y03, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_03.pdf'), dpi = 600)
    print('Channel 03 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 4 Plot and Save
    plt.title('Channel 04 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y04, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_04.pdf'), dpi = 600)
    print('Channel 04 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 5 Plot and Save
    plt.title('Channel 05 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y05, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_05.pdf'), dpi = 600)
    print('Channel 05 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 6 Plot and Save
    plt.title('Channel 06 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y06, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_06.pdf'), dpi = 600)
    print('Channel 06 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 7 Plot and Save
    plt.title('Channel 07 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y07, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_07.pdf'), dpi = 600)
    print('Channel 07 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 8 Plot and Save
    plt.title('Channel 08 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y08, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_08.pdf'), dpi = 600)
    print('Channel 08 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 9 Plot and Save
    plt.title('Channel 09 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y09, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_09.pdf'), dpi = 600)
    print('Channel 09 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 10 Plot and Save
    plt.title('Channel 10 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y10, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_10.pdf'), dpi = 600)
    print('Channel 10 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 11 Plot and Save
    plt.title('Channel 11 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y11, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_11.pdf'), dpi = 600)
    print('Channel 11 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 12 Plot and Save
    plt.title('Channel 12 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y12, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_12.pdf'), dpi = 600)
    print('Channel 12 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 13 Plot and Save
    plt.title('Channel 13 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y13, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_13.pdf'), dpi = 600)
    print('Channel 13 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 14 Plot and Save
    plt.title('Channel 14 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y14, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_14.pdf'), dpi = 600)
    print('Channel 14 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 15 Plot and Save
    plt.title('Channel 15 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y15, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_15.pdf'), dpi = 600)
    print('Channel 15 Data Plot Saved as PDF!')
    plt.clf()

    # Channel 16 Plot and Save
    plt.title('Channel 16 Data')
    frame = plt.gca()
    frame.axes.get_xaxis().set_visible(False)
    plt.plot(x, y16, linewidth = 0.5, color = '#FF1B8D')
    plt.savefig((pdfFileName + '_Channel_16.pdf'), dpi = 600)
    os.chown((pdfFileName + '_Channel_16.pdf'), uid, gid)
    print('Channel 16 Data Plot Saved as PDF!')
    print('All Individual Channels Successfully Plotted and Saved as PDFs!')
    plt.clf()

    # Plot all the channels on the same PDF
    print('Now Printing All Channels to One .PDF!')

    # Sets up layout of the plots
    fig, axes = plt.subplots(16, 1, figsize=(15,15))
    fig.suptitle('Data from All 16 Channels Displayed Top to Bottom')
    
    # Plots the data
    axes[0].plot(x, y01, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[1].plot(x, y02, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[2].plot(x, y03, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[3].plot(x, y04, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[4].plot(x, y05, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[5].plot(x, y06, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[6].plot(x, y07, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[7].plot(x, y08, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[8].plot(x, y09, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[9].plot(x, y10, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[10].plot(x, y11, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[11].plot(x, y12, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[12].plot(x, y13, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[13].plot(x, y14, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[14].plot(x, y15, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')
    axes[15].plot(x, y16, label = '_nolegend_', linewidth = 0.25, color = '#FF1B8D')

    # Save and Show the Plot
    plt.setp(axes, xticks=[], yticks=[])
    plt.savefig((pdfFileName + '_AllChannels.pdf'), dpi = 1200)
    print('Plot .PDF Saved!')
    
    # Change all the permissions so the current user can use them
    os.chown((pdfFileName + '_Channel_01.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_02.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_03.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_04.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_05.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_06.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_07.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_08.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_09.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_10.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_11.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_12.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_13.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_14.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_15.pdf'), uid, gid)
    os.chown((pdfFileName + '_Channel_16.pdf'), uid, gid)
    os.chown((pdfFileName + '_AllChannels.pdf'), uid, gid)
    os.chown((os.path.dirname(os.path.abspath(__file__)) + '/Outputs/'), uid, gid)
    os.chown(csvFileName, uid, gid)
    os.chown(filePath, uid, gid)
    print('Permissions Updated!')

    
    
    # Commented out to save time, feel free to uncomment for interactive plot
    plt.show()


# Graceful exit
except (KeyboardInterrupt, SystemExit):
    print ("Exiting.")
    exit
