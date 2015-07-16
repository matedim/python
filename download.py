#coding: utf8
import requests, shutil
menu = input("Ready.\n")
#if menu == "get": #режим загрузки
    #...
#if menu == "about":#о программе
    #...
#if menu == "exit": #выход
     #...

dirfile = input("Enter path to the directory with file(no \"www.\" !):")
file = input("Enter the name of the file:")


fullpath = dirfile + file

reqauthstr = input("Do you need authentification?[y/n]:")
while True:
    if reqauthstr == "y" or reqauthstr == "Y":
        reqauth = True
        break
    elif reqauthstr == "n" or reqauthstr == "N":
        reqauth = False
        break
    else:
        print("Incorrect command.")
if reqauth == True:
    user = input("Login:")
    passw = input("Password:")

    filereq = requests.get(fullpath,stream = True,auth=(user,passw))
    with open(file,"wb") as receive:
    	shutil.copyfileobj(filereq.raw,receive)
    	del filereq
elif reqauth == False:
    filereq = requests.get(fullpath,stream = True)
    with open(file,"wb") as receive:
        shutil.copyfileobj(filereq.raw,receive)
        del filereq
#if menu == "exit":
#    break
#if menu == "about":
#    print("""
#\nxfetch - v0.1.0
#Library: requests - v2.6.0
#Author: Fedor Sturov\n
#""")
#else:
#    print("Incorrect command.\n")
