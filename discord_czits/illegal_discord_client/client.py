
from headers import Header
import requests, json, time, os


LANG = "pl"
API_VERSION = "https://discord.com/api/v9/"

class User:
    def __init__(self, AUTH):
        self.token = AUTH
        self.name = None
        self.current_path = None
        
        self.guild_in = None
        self.channel_in = None

        self.get = Header(self.token, "GET", LANG )

        self.post = Header(self.token, "POST", LANG )

    def make_get_header(self, path):
        self.get.create_header(API_VERSION + path)
        header = self.get.header
        return header

    def make_post_header(self, path):
        self.post.create_post_header(API_VERSION + path)
        header = self.post.header
        return header

    def servers(self):
        self.current_path = "users/@me/guilds"
        header = self.make_get_header(self.current_path)

        res = requests.get( API_VERSION + self.current_path, headers=header, params={"limit" : 200} )
        res = json.loads(res.text)
        for i in res:
            print("server id: ", i['id'], "server name: ", i['name'])

        self.get.refresh_ua()
        
    def get_server(self, id):
        self.current_path = f"guilds/{id}/channels"
        header = self.make_get_header(self.current_path)

        res = requests.get(API_VERSION + self.current_path, headers=header).text

        res = json.loads(res)

        for i in res:
            print("channel id: ", i['id'], "channel name: ", i['name'])
    
        self.guild_in = id

        self.get.refresh_ua()

    def get_channel(self, id, num = 10):

        self.channel_in = id

        num = int(num)

        if num > 100:
            num = 100

        self.current_path = f"/channels/{id}/messages"
        header = self.make_get_header(self.current_path)

        res = requests.get(API_VERSION + self.current_path, headers=header, params={'limit' : num}).text

        res = json.loads(res)

        print("")
        for i in res:
            user = i['author']
            message_id = i['id']
            content = i['content']
            print(message_id + ': ', content, "  user: ", user["username"], ":" ,user["id"], "\n")

        self.get.refresh_ua()

    def get_server_users(self, id):
        self.current_path = f"guilds/{id}/members"
        self.guild_in = id

        list_of_users_id = []
        after = ''

        header = self.make_get_header(self.current_path)

        r = requests.get(API_VERSION + self.current_path, headers=header, params={'limit' : 1000})
        
        list_of_users = json.loads(r.text)

        print(list_of_users)

        for i in list_of_users:
            i = i['user']
            i = ( i['id'], i['username'] )
            list_of_users_id.append(i)
        
        after = list_of_users_id[-1][0]

        while True:
            
            r = requests.get(API_VERSION + self.current_path, headers=header, params={'limit' : 1000, 'after' : after})
            

            list_of_users = json.loads(r.text)

            if len(list_of_users_id) < 1000:
                break

            for i in list_of_users:
                i = i['user']
                i = (i['id'], i['username'])
                list_of_users_id.append(i)

            after = list_of_users_id[-1][0]
        for i in list_of_users_id:
            print("name: ", i[0], "id: ", i[1], "\n")

        

    def search(self, id):

        self.current_path = f'users/{id}/'
        header = self.make_get_header(self.current_path)

        res = requests.get(API_VERSION + self.current_path, headers=header, params={"with_mutual_guilds" : "true", "guild_id" : self.guild_in}).text

        res = json.loads(res)

        print(res)

    def create_dm(self, id):

        self.current_path = '/users/@me/channels'

        header = self.make_get_header(self.current_path)

        response = requests.post(API_VERSION + self.current_path, headers=header, json={"recipients" : [id]} )
        response = json.loads(response.text)

        print(response['id'])

    def send(self, channel_id, message):
        
        self.current_path = f'/channels/{channel_id}/messages'

        header = self.make_post_header(self.current_path)

        requests.post(API_VERSION + self.current_path, headers=header, json={"content" : message} )

        




            
            




        

