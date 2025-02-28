import requests
import argparse
import time

def readUsernames(filename):
    usernames = []
    with open(filename, "r") as file:
        for line in file:
            usernames.extend(line.split(" "))
    # removes any empty entries or newline characters
    usernames = [username.strip() for username in usernames if username.strip() not in ["", "\n"]]
    return usernames

def checkUsernames(usernames, show_progress=False):
    availableUsernames = []
    total = len(usernames)
    for i, username in enumerate(usernames, 1):
        request_data = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username)
        print(request_data.status_code)
        if request_data.status_code == 200:
            if not show_progress:
                print(f'username "{username}" is unavailable')
        else:
            availableUsernames.append(username)
        # updates progress bar if the flag is enabled
        if show_progress:
            progress = '#' * int((i / total) * 50)  # 50-character progress bar
            print(f"Progress: [{progress:<50}] {i}/{total}", end='\r')
        # rate limit is 200 requests per minute so no more than 3.33 requests per second
        time.sleep(0.35)
    if show_progress:
        print()
    return f"available usernames: {availableUsernames}"

def saveUsernames(usernames, filename):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check if Minecraft usernames are available through the Mojang API",
        add_help=False
    )
    parser.add_argument("-i", "--input", help="read usernames from a provided file")
    parser.add_argument("-u", "--usernames", nargs='+', help="directly specify one or more usernames, separated by spaces, no quotes")
    parser.add_argument("-o", "--output", help="save usernames to a provided file")
    parser.add_argument("-p", "--progress-bar", action="store_true", help="show progress bar")
    parser.add_argument("-h", "--help", action="help", help="show this help message and exit")
    args = parser.parse_args()

    if args.usernames:
        usernames = args.usernames
    elif args.input:
        usernames = readUsernames(args.input)
    else:
        usernames = input("Enter username(s): ").split(" ")
    
    availableUsernamesMsg = checkUsernames(usernames, show_progress=args.progress_bar)
    if args.output:
        saveUsernames(availableUsernamesMsg, args.output)
    else:
        print(availableUsernamesMsg)