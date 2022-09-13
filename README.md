# QueenDeathReminder
 A GroupMe bot that shares how man days since the Queen's Death

## What is it

This was made entirely as a joke.

Basically it makes a Mr. Krabs meme using whatever number is in the text file and sends it to a group on GroupMe. Note that this isn't a GroupMe Bot - it will post from your profile as if you manually sent the message.

## How to use

Download or fork or whatever the files onto your local machine. You'll need to grab the [GroupMe Library](https://pypi.org/project/GroupyAPI/) as well as [Pillow](https://pillow.readthedocs.io/en/stable/installation.html) to make it work.

```bash
pip install GroupyAPI
pip install --upgrade Pillow
```

Once you have that, head over to [GroupMe's Developer Page](https://dev.groupme.com/) and grab your auth token. Replace the <YOUR AUTH TOKEN> text with it, and do the same for the <YOUR GROUP NAME> with whichever group you want to spam with messages.

Just make sure the krabs.png file and impact.tff are in the same directory, then go ahead and run DayBotAll.py using python 3.10.x

It's best to automate this process frankly, constant daily reminders. I suggest checking out Pythonanywhere and setting up a Task to execute the script once a day. Set up a [virtual environment](https://help.pythonanywhere.com/pages/Virtualenvs/) and get GroupyAPI and Pillow installed on it, upload the files to your directory, and set the daily task to run once a day.

## Requirements

 * A GroupMe Account
 * GroupyAPI
 * Pillow
 * Python's Standard Library (specficially: DateTime)
 * DayBotAll.py and meme.py
