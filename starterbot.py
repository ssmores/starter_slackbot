import os
import time
from slackclient import SlackClient

# starterbot's ID 
BOT_ID = os.environ['BOT_ID']

# constants
AT_BOT = '<@{}>'.format(BOT_ID)
EXAMPLE_COMMAND = 'do'

slack_client = SlackClient(os.environ['SLACK_BOT_TOKEN'])


def handle_command(command, channel):
    """Receives command directed at bot to determine if valid commands."""

    response = 'Not sure what you mean. Use the *{}* command with numbers, delimited by spaces.'.format(EXAMPLE_COMMAND)
    if command.startswith(EXAMPLE_COMMAND):
        response = 'Sure...write some more code then I can do that!'
    slack_client.api_call('chat.postMessage', channel=channel, text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """The Slact RTM API is an event firehose. Returns None unless commands directed to Bot."""

    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), output['channel']

    return None, None







if __name__ == "__main__":
    # 1 second delay between reading from firehose
    READ_WEBSOCKET_DELAY = 1

    if slack_client.rtm_connect():
        print 'Starterbot connected and running!'
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print 'Connection failed. Invalid Slack token or bot ID?'