import pandas as pd
import json, os, math
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime

# Code from Marcel Champagne

def generate_graphs():
    # get the filepath names
    fpath = "C:/Users/marce/Documents/CU Course Folders/CCSS dev/SSI Hackathon/Dragino DDS75-LB Ultrasonic Distance Sensor/a84041bbbf5946fc"
    json_file_names = [filename for filename in os.listdir(fpath) if os.path.isfile(os.path.join(fpath, filename))]
    # timestamp x axis, altitude y axis, distance z axis, RSSI color axis
    xlist = []
    ylist = [] 
    zlist = []
    clist = []

    # loop through JSON data to get what we need
    for filename in json_file_names:
        with open(os.path.join(fpath, filename), 'r') as json_file:
            curr_file = json.load(json_file)
            if curr_file.get("rxInfo") == None:
                continue
            data = curr_file.get("object").get("distance")
            # uncomment if you want to remove outliers (5 points with significantly higher distance)
            #if data > 1000:
            #    continue
            ylist.append(data)
            data = curr_file.get("rxInfo")[0].get("nsTime")
            data = data[:19]           
            data = data.replace("T", " ")
            xlist.append(data)
            data = curr_file.get("rxInfo")[0].get("location").get("altitude")
            zlist.append(data)
            data = curr_file.get("rxInfo")[0].get("rssi")
            clist.append(data)

    # create figures
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection="3d")
    datetimes = dates.date2num(xlist)
    sc = ax.scatter3D(datetimes, ylist, zlist, marker='o', c=clist, cmap='rainbow')
    plt.colorbar(sc, label='Signal Strength (RSSI)')
    ax.set_xlabel('Time')
    ax.set_ylabel('Distance')
    ax.set_zlabel('Altitude')
    ax.set_title('Dragino DDS75-LB Ultrasonic Distance Sensor Data')
    plt.show()
    
def generate_map():
    print("this was not implemented (because of time and also that the location data was too close together)")

def main():
    print("Welcome to my SSI hackathon project!! \n\nThis is a CLI application which will allow the user to create a 3D graph to plot the data given from the Dragino Ultrasonic Distance Sensor.")
    print("If more time were to be alloted, the graph could be customizable with what data you want to put on what axis.")
    print("If also I had more time with this project in the future/on another day, this could also be charted on an interactive map using leaflet.js in a more scalable webapp, using the coordinate data provided.")
    option = 0
    while(option!=3):
        option = int(input("Below you can select an option: \n1: Create Graph\n2: Create Map (not implemented)\n3: Exit\n"))
        match(option):
            case 1:
                generate_graphs()
            case 2:
                generate_map()
            case 3:
                break
            case _:
                print("invalid input")

main()
