# Python Wordle OSX Message Tracking
A cobbled together python script that queries the local sqlite db and runs a regex on messages for a specific group chat, looking for wordle scores and collating those into a google sheets row for that date

## Usage
`Config.py` holds config for sheet id, names of friends and their phone numbers

To run:

`pip install -r requirements.txt`

`python WordleScoreFromChat.py` 
