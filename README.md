# Assassin Game Runner:
A program to create a game of assassin that lets there be no designated game-master.
## Contents:
* **images**: this folder appears empty because it has all of the images of the players so I have added it to the `.gitignore` file. When a build is run this folder should be created and filled with Contestant images.
* **helper_methods**: This program runs the assassin game. It uses the Images folder and the `ASSASSIN.json` and `ASSASSIN.csv` files to get the names and emails. These folder are currently not publicly visible because they contain all of the contact information of the participants. These files should be created automatically. The program expects a CSV formated in the following manner ```Timestamp,NAME,EMAIL,GROUPME,COMEDYGROUP,PROFILEPICTURE,DEAD``` all as string variables. **The PROFILEPICTURE section is most likely to break. it uses images hosted on google drive and its is possible that this will not be supported with the same link in a few years.**
* **source.js** This and the below file are used draw every name in the field dynamically to a grid. This makes it easy to share the remaining people with the group.  
  * **tester.html**
  * **people_drawer**: an abandoned attempt to do the source.js functionality to a png with openCV

## Purpose:
This package was created by me when I was the president of the callbacks. There is a popular game called **Assassin** with the following rules:
* N player field can be thought of as a connected linked list.
* each player has two attributes: **target**,**pursuer**
* players "Assassinate" each other by tagging each other with a special method (i.e. using a black marker on a targets white shirt)
* when a player is killed they give their target to their pursuer.
* the game ends when the last person has eliminated their target.
The issue with this game typically is that it need a game master to create a randomized order of the linked list and then to pass out the targets to individual people. This Is a fun game a is a tradition for the Boston University Comedy Scene. As a Senior it would have been my job or one of the other presidents jobs to sit out of the game and be game master. Ehh we can do better! This program aims to automate the role of game master and allow a person to randomly and anonymously send emails to the field given a CSV of entrants. This project was an opportunity for me to finally used my coding ability for a concrete problem. It was very important that the name drawing and target distribution was done anonymously but in a way that could be recreated in an emergency to stop cheating.

## Usage:

 ##### Start a game of assassin:
 This should be pretty straight forward for anyone with a technical background or anyone majoring in CS or Eng but it may be a little complex for anyone unfamiliar with programming.

 **Before you start**: I have some quirks about how I write code that may be different from how you like to think. These quirks may lead to some confusing errors.
  * **Paths**: In computing there is a something called a **path**. This is how a computer keeps track of where a file is kept inside itself in an ( arguably ) human-readable way. They look like this

  `/home/username/Destop/filename.png` - Linux

  ` /Users/username/Desktop/filename.png`-MAC

  `\Users\YOURUSERNAME\Desktop\filename.png`-Windows

   As you can see they look different depending on your operating system. Worse, I run Linux and wrote the paths for this program to be intended for a Linux machine... oof. What this means is that it is possible that one reason something may break is because your computers path is different then mine was. I have tried to used relative pathing, which means that the code will try to read the file from the folder that its in. I expect that you run the code inside of the Assassin_Game_Runner folder. However, if it breaks still, try adding absolute paths in the code where ever you see a path. An absolute path is the full path to describe when your file is kept.


   * **python**: I wrote this all in python because it should be the easiest to read language that I know how to program in. However, it may be hard to get working. If you run Mac or Linux it should run straight away! However, if you are a windows user you will need to download it. This tutorial is good **[https://phoenixnap.com/kb/how-to-install-python-3-windows](https://phoenixnap.com/kb/how-to-install-python-3-windows)** but just searching **Download Python3 for windows for beginners** should get you good results too.

   * **setting up the files**: This program is designed to hide any of the files with personal info. This means that you will be missing a lot of files at the beginning of the process and you will need to recreate them. Your should take the CSV output from the survey and put it in the `Assassin_Game_Runner` folder. Make sure that its named "ASSASSIN.CSV". You will also need a file called "critical.json" in the same folder. This is used to hold the account email password. the file should look like this

   `critical.json`
   ```
    {
      "PASS":"yourpassword"
     }
    ```  


   **Running the game**: To run the game you should open a terminal in the folder with Assassin_Game_Runner. A terminal is a way of running commands for your computer with just a text based system. It may be frustrating at first but it is super useful.
   * on Mac: search in application starter thing "terminal" or press `Control + Option + Shift + T`
   * on Windows: search in programs for "powershell" or `shift + windowskey` and look for powershell
   * on Linux: you got this.

   Now you have to navigate to the correct folder. This will be different for different operating systems but searching:
   * "how to change directories in powershell(or terminal)",
   * "how to list directories in powershell(or terminal)"  
   * "how to print current directory in powershell(or terminal)"

   should get you to be able to get there. You'll know your in the right spot when the directory on the right ends with "Assassin_Game_Runner". Once there type `python3 helper_methods.py` and the program should run! Any questions. please add an issue to the github page.


##### Create a image of the field:
To run this you need to do a little more but less of it will be in the command line. First in `-Assassin_Game_Runner` create a folder called "images". Then download the images to the images folder and rename them to the corresponding person email. So "Greg" with the image "10902.jpg" and the email "gregscool@gmail.com" would have the image named "gregscool.jpg". Do that for all the players. Next make a file called `ASSASSIN.json` by using a online CSV to JSON converter. Open this file and add `ASS ='` to the beginning of the file and `';` to the end. Then open *tester.html* in a web browser by double clicking it and you should see the grid load!

## Credit:
* my co-president created the google form and group me group.

**Libraries:**
  * smtplib
  * openCV(unused currently)
  * email
