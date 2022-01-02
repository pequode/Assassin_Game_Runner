# Assassin_Game_Runner
A program to create a game of assassin that lets there be no designated game-master.
## Contents
## Purpose
This package was created by me when I was the president of the callbacks. There is a popular game called **Assassin** with the following rules:
* N player field can be thought of as a connected linked list.
* each player has two attributes: **target**,**pursuer**
* players "Assassinate" each other by tagging each other with a special method (i.e. using a black marker on a targets white shirt)
* when a player is killed they give their target to their pursuer.
* the game ends when the last person has eliminated their target.
The issue with this game typically is that it need a game master to create a randomized order of the linked list and then to pass out the targets to individual people. This Is a fun game a is a tradition for the Boston University Comedy Scene. As a Senior it would have been my job or one of the other presidents jobs to sit out of the game and be game master. Ehh we can do better! This program aims to automate the role of game master and allow a person to randomly and anonymously send emails to the field given a CSV of entrants. This project was an opportunity for me to finally used my coding ability for a concrete problem. It was very important that the name drawing and target distribution was done anonymously but in a way that could be recreated in an emergency to stop cheating.
## Usage
## Credit
* my co-president created the google form and group me group.
**Libraries:**
