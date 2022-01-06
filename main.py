
import client
commands = [

        ("servers", "Display your servers list (names and ids)."), 
        ("friends", "Display your dm channels (ids)"),
        ("get_server <server id>", "Display every channels (ids and names)."),
        ("get_server_users", "Display every users from a server"),
        ("get_channel <channel id>", "Display messages on channel. Also display who sent message."),
        ("save <channel_id>", "It saves everything from channel."),
        
        ("search <someone id>", "It shows everything program knows about given user."),
        ("grab_emails", "It shows messages wich propably have emails inside. (looking only for saved messages)"),

        ("send <server_id> <channel_id> <message>", "It sends message to given channel"),
        ("automatic_send <server_id> <channel_id> <messages> <time>", "It send messages automaticly with choosen brake <time> (only to servers)"),
        ("create_dm", "creates channel with friend")


]

def print_commands():
    for i in commands:
        print("command: ", i[0], " - ", "Description: ", i[1], "\n")

def main():

    print("Welcome in Illegal Discord client") #welcome message


    AUTH = input("your discord authorization TOKEN\n")

    c = client.User(AUTH)

    while True:
        command = input('type a command:\n').split(" ")

        if command[0] == "commands":
            print_commands()
        elif command[0] == "servers":
            c.servers()
        elif command[0] == "get_server":
            c.get_server(command[1])
        elif command[0] == "get_server_users":
            c.get_server_users(command[1])
        elif command[0] == "get_channel":
            c.get_channel(command[1], command[2])
        elif command[0] == "search":
            c.search(command[1])
        elif command[0] == "create_dm":
            c.create_dm(command[1])
        elif command[0] == "send":
            print(command)
            c.send(command[1], command[2])
            

    
if __name__ == "__main__":
   main()




        