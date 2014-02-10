from irc.client import SimpleIRCClient, ServerConnectionError

from irclogs.core import create_app, db
from irclogs.models import Message

import argparse
import sys

# The following is needed for flask-sqlalchemy
# To use f-sa derived models, an app context is needed
# NOTE: is there a better way to do this?
app = create_app()

class LoggerBot(SimpleIRCClient):
    def __init__(self, target):
        super().__init__()
        self.target = target

    def on_welcome(self, connection, event):
        connection.join(self.target)

    def on_pubmsg(self, connection, event):
        with app.app_context():
            nick = event.source.split('!')[0] # the source is of the format nick!~user@host
            message = Message(nick=nick, body=event.arguments[0])
            db.session.add(message)
            db.session.commit()
            print('{}: {}'.format(message.nick, message.body))

    def on_disconnect(self, connection, event):
        sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description='Logging bot for IRC channels')
    parser.add_argument('-s', '--server', default='irc.freenode.net', help='The IRC server to connect to with (default: irc.freenode.net)', required=True)
    parser.add_argument('-p', '--port', type=int, default=6667, help='Server port (default: 6667)')
    parser.add_argument('-n', '--nickname', help='Nickname for the bot to login with', required=True)
    parser.add_argument('-c', '--channel', help='Channel to log', required=True)
    parser.add_argument('-P', '--password', help='Optional password (freenode takes this in the form of nickname:password)')

    args = parser.parse_args()

    list_args = [args.server, args.port, args.nickname]
    if args.password:
        list_args.append(args.password)

    bot = LoggerBot(args.channel)
    try:
        bot.connect(*list_args)
    except ServerConnectionError as e:
        print(e)
        sys.exit(1)
    bot.start()

if __name__ == '__main__':
    main()
