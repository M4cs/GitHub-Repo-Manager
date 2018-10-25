import configparser, os, os.path, sys


def checkconfig():
    os.system("clear")
    print("""
GRM Requires a GitHub App Client ID and Client Secret

You can obtain these at https://github.com/settings/developers

If you don't have an app create one and use the credentials from that!
""")
    check = os.path.exists("settings/config.ini")
    if check == True:
        pass
    elif check == False:
        writeconfig()
def writeconfig():
    print("Please Login or Type Exit To Exit ")
    config = configparser.ConfigParser()
    config['DEFAULT'] = { 'client_id': '', 'client_secret': ''}
    config['DEFAULT']['client_id'] = input("Client ID: ")
    if config['DEFAULT']['client_id'] == "exit":
        exit()
    else:
        pass
    config['DEFAULT']['client_secret'] = input("Client Secret: ")
    with open('settings/config.ini', 'w') as configfile:
        config.write(configfile)

def logout():
    os.system("clear")
    os.system("rm settings/config.ini")
    writeconfig()
