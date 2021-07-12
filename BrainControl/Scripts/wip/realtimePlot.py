from pyOpenBCI import OpenBCICyton
import numpy as np
import time
import tkinter as tk
import tkinter.font as tkFont
import matplotlib.figure as figure
import matplotlib.animation as animation
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Set up the scale factor provided by the pyOpenBCI documentation
SCALE_FACTOR_EEG = (4500000)/24/(2**23-1) # uV/count to convert the channels_data to uVolts_per_count



# Parameters
update_interval = 100 # Time (ms) between polling/animation updates
max_elements = 1440     # Maximum number of elements to store in plot lists

# Declare global variables
root = None
dfont = None
frame = None
canvas = None
ax = None
ay = None
eegPlotVisible = None
allData = None
times = None
EEGList = None


# Global variable to remember various states
fullscreen = False
eegPlotVisible = True


# Toggle fullscreen
def toggle_fullscreen(event=None):

    global root
    global fullscreen

    # Toggle between fullscreen and windowed modes
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)
    resize(None)   

# Return to windowed mode
def end_fullscreen(event=None):

    global root
    global fullscreen

    # Turn off fullscreen mode
    fullscreen = False
    root.attributes('-fullscreen', False)
    resize(None)

# Automatically resize font size based on window size
def resize(event=None):

    global dfont
    global frame

    # Resize font based on frame height (minimum size of 12)
    # Use negative number for "pixels" instead of "points"
    new_size = -max(12, int((frame.winfo_height() / 15)))
    dfont.configure(size=new_size)

# Toggle the EEG plot
def toggle_EEG():

    global canvas
    global ax
    global ay
    global eegPlotVisible
    global times
    global EEGList

    # Toggle plot and axis ticks/label
    eegPlotVisible= not eegPlotVisible
    ay.get_lines()[0].set_visible(eegPlotVisible)
    ay.get_yaxis().set_visible(eegPlotVisible)
    ax.get_xaxis().set_visible(False)
    canvas.draw()

# This function is called periodically from FuncAnimation
def animate(i, ax, ay):

    # Update data to display temperature and light values
    try:
        new_time = ax[0]
        new_EEGC1 = ay[0]
    except:
        pass

    # Update our labels
    #ay.set(new_ay)

    # Append timestamp to x-axis list
    #times.append(timestamp)

    # Append sensor data to lists for plotting
    #temps.append(new_temp)
    #EEGList.append(new_EEG)

    # Clear, format, and plot light values first (behind)
    #color = 'tab:red'
    #ax.clear()
    #ax.set_ylabel('Temperature (C)', color=color)
    #ax.tick_params(axis='y', labelcolor=color)
    #ax.fill_between(xs, temps, 0, linewidth=2, color=color, alpha=0.3)

    # Clear, format, and plot temperature values (in front)
    color = 'tab:blue'
    ay.clear()
    ay.set_ylabel('Heading (deg)', color=color)
    ay.tick_params(axis='y', labelcolor=color)
    ay.plot(ax, ay, linewidth=2, color=color)

    # Make sure plots stay visible or invisible as desired
    #ax.collections[0].set_visible(temp_plot_visible)
    ay.get_lines()[0].set_visible(eegPlotVisible)

# Dummy function prevents segfault
def _destroy(event):
    pass


def plotting(rawSample):
    channelData = np.array(rawSample.channels_data)
    timeData = np.array(time.time())

    channelData = channelData * SCALE_FACTOR_EEG

    ax = timeData
    ay = channelData
    allData = np.append(timeData, channelData)
    print(allData)
     
    print('Showing')

    # Call animate() function periodically
    fargs = (ax, ay)
    ani = animation.FuncAnimation(fig, animate, fargs = fargs, interval = update_interval)               

    # Start in fullscreen mode and run
    toggle_fullscreen()
    root.mainloop()
     




     
# If the program cannot find an OpenBCI port, try restarting the Cyton board
board = OpenBCICyton(daisy = True)

# Create the main window
root = tk.Tk()
root.title("Sensor Dashboard")

# Create the main container
frame = tk.Frame(root)
frame.configure(bg = 'white')

# Lay out the main container (expand to fit window)
frame.pack(fill = tk.BOTH, expand = 1)

# Create figure for plotting
fig = figure.Figure(figsize = (2, 2))
fig.subplots_adjust(left = 0.1, right = 0.8)
ax = fig.add_subplot(1, 1, 1)

# Instantiate a new set of axes that shares the same x-axis
ay = ax.twinx()

# Variables for holding temperature and light data
EEG = tk.DoubleVar()

# Create dynamic font for text
dfont = tkFont.Font(size = -24)

# Create a Tk Canvas widget out of our figure
canvas = FigureCanvasTkAgg(fig, master = frame)
canvas_plot = canvas.get_tk_widget()

# Create other supporting widgets
label_EEG = tk.Label(frame, textvariable = EEG, font = dfont, bg = 'white')
button_EEG = tk.Button(frame, text = "Toggle EEG", font = dfont, command = toggle_EEG)
button_quit = tk.Button(frame, text = "Quit", font = dfont, command = root.destroy)

# Lay out widgets in a grid in the frame
canvas_plot.grid(row = 0, column = 0, rowspan = 5, columnspan = 4)
label_EEG.grid(row = 0, column = 4, columnspan = 2)
button_quit.grid(row = 5, column = 4, columnspan = 2)

# Add a standard 5 pixel padding to all widgets
for w in frame.winfo_children():
    w.grid(padx = 5, pady = 5)

# Make it so that the grid cells expand out to fill window
for i in range(0, 5):
    frame.rowconfigure(i, weight = 1)
for i in range(0, 5):
    frame.columnconfigure(i, weight = 1)

# Bind F11 to toggle fullscreen and ESC to end fullscreen
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', end_fullscreen)

# Have the resize() function be called every time the window is resized
root.bind('<Configure>', resize)

# Call empty _destroy function on exit to prevent segmentation fault
root.bind("<Destroy>", _destroy)

board.start_stream(plotting)