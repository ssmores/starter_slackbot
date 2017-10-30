# Starter Slackbot
--------------------------

**Description**
A bot integrated into slack. When an action isn't recognized, it will respond accordingly. 


Learn more about the developer on [LinkedIn](www.linkedin.com/in/stefaniemoy). 

**How it works**
In a Slack Group where you have API access, create a bot [here](https://api.slack.com/bot-users). Run the starterbot.py file to get the bot's ID (in your terminal), and put the bot's ID and bot token into your secrets file. Source your secrets, run the starterbot.py file, and start chatting at it in your slack channel.


### Technology Stack

* Back-End: Python
* APIs: Slack


### How to run locally

Create a virtual environment 

```
>>> virtualenv env
>>> source env/bin/activate
```

Install the dependencies

```
>>> pip install -r requirements.txt
```

Ensure your keys are in your secrets.sh file and run them.
```
>>> source secrets.sh
```