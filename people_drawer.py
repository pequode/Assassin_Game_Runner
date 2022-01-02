import cv2 as cv
import csv
import random
import requests
# this is meant to allow people to create a png of the field. 
def extractInputs(csvPath = "Entrants.csv" ):
    Names = []
    Emails =[]
    ImageIDs=[]
    dead = []
    with open(csvPath, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)
            Names.append(row["NAME: (Please put real name first, then nickname in parenthesis)"])
            Emails.append(row["EMAIL:"])
            stringOfPP = row["PROFILE PICTURE:"]
            stringtoApp = stringOfPP[stringOfPP.find("?id")+4:]
            ImageIDs.append(stringtoApp)
            dead.append(row["DEAD"])

    return (Names,Emails,ImageIDs,dead)

[N,na,Img,Dead] = extractInputs(csvPath ="PATHTOTHECSV" )
#image = cv2.imread()
downloadToImages(Img,N)
