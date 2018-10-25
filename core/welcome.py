#!/usr/bin/env python3
def banner():
    print("""

                     GitHub Repo Manager v1
                     For Linux, Mac, Windows.
                     Search, Download, and
                     Find GitHub Repos with
                     GRMv1.""")

    version = open("settings/version","r").readlines()
    print("""
                          Version Info:
    ============================================================
    """)
    print("         Version: " + version[0])
    print("""          Choose Search Type:
    ============================================================

     [1] Repository Search               [2] Username Search

     [3] Topic Search [Coming Soon]      [4] Find A Project

    ============================================================
                            Commands:

      help                               display this menu

      <number 1-4>                       run tool from above

      chkupdate                          check for update

      logout                             remove API credentials

      exit                               exit the program

    ============================================================
    """)
