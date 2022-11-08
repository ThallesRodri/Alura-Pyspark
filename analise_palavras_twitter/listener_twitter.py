import socket
import tweepy

HOST = 'localhost'
PORT = 9009

s = socket.socket()
s.bind((HOST, PORT))
print(f'Aguardando conexão na porta: {PORT}')

s.listen(5)
connection, address = s.accept()
print(f'Recebendo solicitação de: {address}')

token = 'AAAAAAAAAAAAAAAAAAAAAGuhigEAAAAAu%2FpbjSWNhFVvFOOqTH8WOYGrWIQ%3DFBMdk7xjJesab0MqRYHh8XeySB8OGWH8ojkaAgVCLwEMAYQwRY'

key_word = 'Luffy'

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('='*50)

        connection.send(tweet.text.encode('utf-8', 'ignore'))

printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(key_word))
printer.filter()

connection.close()