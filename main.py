import os
import os.path
from os import path
import sys
from pathlib import Path

def main():
    rawAlias = sys.argv[1:]
    home = str(Path.home())
    os.chdir(home+"/.oh-my-zsh/custom")
    customAlias = "aliases.zsh"
    path.exists(customAlias)
    if not path.exists(customAlias): #Checks if file exist
        with open('aliases.zsh', 'a') as zsh:
            pass
    else:
        with open('aliases.zsh', 'a') as zsh:
            zsh.write(createAlias(rawAlias)+"\n")
            zsh.close
            print("New Alias Created")

def createAlias(rawAlias):
    newAlias = rawAlias[0] + " " + rawAlias[1] + rawAlias[2] + '"' + rawAlias[3] + '"'
    return newAlias

main()