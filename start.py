#!/usr/bin/env python3
import requests, json, time, os, time, configparser
from settings import config
from core import welcome

config.checkconfig()
print("Logged In Successfully!")
time.sleep(1)
os.system("clear")
welcome.banner()

terminalname = "[GRM]>> "

def main():
    terminal = input(terminalname)
    if terminal[0:4] == "help":
        welcome.banner()
        main()
    elif terminal[0:1] == "1":
        reposearch()
        main()
    elif terminal[0:1] == "2":
        usersearch()
        main()
    elif terminal[0:1] == "3":
        topicsearch()
        main()
    elif terminal[0:1] == "4":
        findaproject()
        main()
    elif terminal[0:9] == "chkupdate":
        version = open("settings/version","r").readlines()
        if version[0] == "1.0.0":
            main()
        else:
            print("Needs Updating!")
            main()
    elif terminal[0:6] == "logout":
        config.logout()
        main()
    elif terminal[0:4] == "exit":
        print("Exiting..")
        exit()
    else:
        print("Unknown Command..")
        main()

api = "https://api.github.com/"
config = configparser.ConfigParser()
config.read('settings/config.ini')
client_id = config['DEFAULT']['client_id']
client_secret = config['DEFAULT']['client_secret']
auth = "?client_id=" + client_id + "&client_secret=" + client_secret

def reposearch():
    print("Search Repositories By A Keyword\nYou Can Download A Repo From This Search\nDownloads To /clonedrepos/")
    print("")
    query = input("\nEnter Keyword To Search For: ").replace(" ","+")
    r = requests.get(api + "search/repositories?q=" + query + "&sort=stars" + auth).text
    resp = json.loads(r)
    print("\nDisplaying Top Results: ")
    try:
        for i in range(100):
            fullname = resp['items'][i]['full_name']
            print(fullname)
    except IndexError:
        pass
    print("Which Repo Would You Like To Download?")
    ans2 = input(terminalname)
    repo = "https://github.com/" + ans2 + ".git"
    os.system("git clone %s clonedrepos/%s" % (repo,ans2.replace("/","-")))
    welcome.banner()

def usersearch():
    print("Search Users On GitHub\nDisplay Info On User\nCan Log Info To /userinfo/")
    print("")
    query = input("\nEnter Username: ")
    r = requests.get(api + "search/users?q=" + query + "&sort=followers" + auth).text
    resp = json.loads(r)
    try:
        for i in range(100):
            name = resp['items'][i]['login']
            id = resp['items'][i]['id']
            url = resp['items'][i]['html_url']
            print("Name: " + str(name) + "\nID: " + str(id) + "\nURL: " + str(url) + "\n")
    except IndexError:
        pass

def findaproject():
    print("Search Through Issues For Help Wanted\nDisplay Repos in a Topic w Help Wanted/")
    print("")
    time.sleep(2)
    print("Finding Recent Issues")
    r = requests.get(api + "search/issues?q=help+wanted").text
    resp = json.loads(r)
    print(resp)
    try:
        for i in range(100):
            title = resp['items'][i]['title']
            url = resp['items'][i]['url']
            print("Title: " + title + "\nURL: " + url + "\n")
    except IndexError:
        pass





















main()
