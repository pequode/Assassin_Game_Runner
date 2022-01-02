import csv
import random
import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
DEBUG = True
# reads CSV file three lists
def extractInputs(csvPath = "Entrants.csv" ):
    Names = []
    Emails =[]
    ImageIDs=[]
    with open(csvPath, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Names.append(row["NAME: (Please put real name first, then nickname in parenthesis)"])
            Emails.append(row["EMAIL:"])
            stringOfPP = row["PROFILE PICTURE:"]
            stringtoApp = stringOfPP[stringOfPP.find("?id")+4:]
            ImageIDs.append(stringtoApp)

    return (Names,Emails,ImageIDs)
# mixes the list up in a predictable manner(ie random but consistently random across each list)
def scrambleList(Lists,seeds):
    random.seed(seeds)
    random.shuffle(Lists)
    return Lists
# used to make a list of dictionaries with the persons name their email and their targets name and image.
def createTagetsarray(L1,L2,L3):
    seedL = len(L1) # this is so that we can recreate the list in an emergency NOT SECURE.
    Targets = []
    scrambledNames = scrambleList(L1,seedL)
    scrambledEmails = scrambleList(L2,seedL)
    scrambledImageIDs = scrambleList(L3,seedL)
    for i in range(seedL):
        if(len(scrambledEmails)!=len(scrambledNames)):
            print("size miss match error")
        if (i < seedL - 1):
            Targets.append([scrambledNames[i+1],scrambledImageIDs[i+1]])
        else:
            Targets.append([scrambledNames[0],scrambledImageIDs[0]])

    listOfDicForGame=[]
    for i in range(seedL):
        dictEntry = {"Name":scrambledNames[i],"Email":scrambledEmails[i],"Target":Targets[i][0],"ImageIDs":Targets[i][1]}
        listOfDicForGame.append(dictEntry)
    return listOfDicForGame

# gets the password for the email address shown .
def getPass(PassPath):
    f = open(PassPath)
    data = json.load(f)
    f.close()
    return data["Pass"]

# sends a single email given a target
def sendEmail(dic,extraText=""):
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    sender_email = "thebucallbacks@gmail.com"# our email address this can be any email address with dev turned on
    message = MIMEMultipart("alternative")
    message["Subject"] = "{name}'s Assassin Target".format(name=dic["Name"])
    message["From"] = sender_email
    message["To"] = dic["Email"]
    # html formated email body
    html = """\
    <html>
      <body>
        <p style="font-family: Courier New;"> <b>{Name}</b>, we have choosen you for a very special task. <em>{target}</em> has become a thorn in the side of our organization and we would like them eiliminated. Happy hunting🔪
        <br/>
        <b>{target}'s</b> last known photo:{appended}
        </p>


        <div style = "position: relative;
                          top: 0;
                          left: 0;
                          border: 10px black solid;
                          width: 500px;
                          height: 500px;
                          ">
              <div style="
                  width: 100%;
                  height: 100%;
                  overflow: hidden;

              ">
                      <img style = "  position: relative;
                                      top: 0;
                                      left: 0;
                                      width: 100%;
                                      "
                          src="https://drive.google.com/uc?export=view&amp;id={imageID}" />
              </div>
              <img style = "  position: absolute;
                              top: 0;
                              left: 0;
                              height: 100%;
                              width: 100%;"
                  src="https://www.freepnglogos.com/uploads/scope-png/image-sniper-scope-multiplayer-overlay-waw-the-30.png" />
      </div>
      </body>
    </html>
    """.format(Name=dic["Name"],target=dic["Target"],imageID=dic["ImageIDs"],appended = extraText)

    part2 = MIMEText(html, "html")
    message.attach(part2)
    # sends to smtp server
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, getPass("./Assassin_Game_Runner/critical.json"))
        server.sendmail(sender_email, dic["Email"], message.as_string())
# sends email to every dic entry
def sendEmails(ListOFDics):
    count=0
    for i in ListOFDics:
        count +=1;
        if (DEBUG==False):sendEmail(i)
        print("Sending {n}'th' email".format(n=count))
# runs all the above messages
if __name__ == "__main__":
    print(os.listdir())
    [N,E,I] = extractInputs("./Assassin_Game_Runner/ASSASSIN.csv")
    dicOfTargets = createTagetsarray(N,E,I)
    print(len(dicOfTargets))
    sendEmails(dicOfTargets)
