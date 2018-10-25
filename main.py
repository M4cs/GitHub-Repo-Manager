#!/usr/bin/env python3
import requests, json, time, os, sys
from prettytable import PrettyTable

print("Search Query: ")
search = input("[>] ").replace(" ", "+")
print("[Optional] Username Specific: ")
user = input("[>] ")
print("[Optional] Language Specific: ")
lang = input("[>] ")
print("Sorting Method [Stars, Forks, Updated]")
sort = input("[>] ")
api = "https://api.github.com/"
auth = "?client_id=a16deb7ee8737b442b49&client_secret=703cc2f532087b508954934280a83dde1b0852f2"
r = requests.get(api + "search/repositories?q=" + search + "&sort=" + "?user=" + user + auth)
re = r.text
resp = json.loads(re)
try:
    print("=== Start Results ===")
    for i in range(10000):
        name = resp['items'][i]['name']
        print(name)
except IndexError:
    print("=== End Results ===")
