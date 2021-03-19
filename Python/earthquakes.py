#Earthquakes around the globe during the past 24h. Inspired by Joe Marini's 'Learning Python: Working with JSON data' and by Marcin Bazydło 'Python Programming - Fundamentals'. 
import urllib.request
import json
import re
import datetime

def printResults(data):
    
    #Use json module to load the string data into a dictionary
    theJSON = json.loads(data)
    
    #Check if the metadata includes title of whole data and it's printout
    if "title" in theJSON["metadata"]:
        print("\n" + re.sub('\, ','\n',theJSON["metadata"]["title"]) + "\n")
        
    #Count the number of all recorded events
    count = theJSON["metadata"]["count"]
    print (str(count) + " events recorded\n")
    
    #Show magnitude and general geographical position of all events
    for element in theJSON["features"]:
        print ("Magnitude:", round(float(element["properties"]["mag"]),1), "Event time:", datetime.datetime.fromtimestamp(element["properties"]["time"] / 1000).strftime('%Y-%m-%d %H:%M:%S') , "  Epicenter:", end = '')
        if re.sub ("\D|\.|\s", "", element["properties"]["place"]) != "":
            print(" ", element["properties"]["place"])
        elif re.search ("Near", element["properties"]["place"]) != None:
            print(" ", element["properties"]["place"])            
        else:
            print("  Under", element["properties"]["place"])
        print()
    print (40 * "_" + "\n")
    
    
def main():
    #Data Source variable definition
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    
    #Open URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print ("Connecting to US Geological Survey API.\n\nChecking connection... Result code: " + str(webUrl.getcode()), end ="")
    if (webUrl.getcode() == 200):
        print (".\nIt's OK! Receiving data...")
        data = webUrl.read()
        printResults(data)
    else:
        print("[EN] Received error, cannot parse results\n[PL] Wystąpił błąd, nie można użyć wyników")
        
if __name__ == "__main__":
    main()       
