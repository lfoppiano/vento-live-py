# Vento Live py - Live sentiment analysis using twitter (Python)

This is a re-implementation, using python, NLTK and Bottle of https://github.com/lfoppiano/vento-live

## What do you need:

- [TBD] A mongoDB instance running somewhere, for setting up quickly a local database:
```
    mkdir ~/mongodb
    mongod --dbpath mongodb
```
(By default mongodb will be found on localhost:27017)

- A twitter account and the set up for the API (https://apps.twitter.com/), enabling access key and secret key. See https://dev.twitter.com/rest/public

## How to run it:
Just type:
```
python controller.py
```
Connect to http://localhost:8080/vento-live/index.html, type in the textbox one or multiple keywords and wait :)


## Note
- The web application doesn't give any feedback and any error :)