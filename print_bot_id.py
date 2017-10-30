"""File to pull in your slackbot's slack ID. 

This file only needs to be run once (after the slackbot was created). 
If no slackbot was created, you will not have the bot's user ID. 
The ID will be printed in your terminal.
"""

import os
from slackclient import SlackClient

BOT_NAME = 'starterbot'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # Retrieve all users to find the bot 
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print "Bot ID for '{}' is {} .".format(user['name'], user.get('id'))
            else:
                print "could not find bot user with the name {}".format(BOT_NAME)

