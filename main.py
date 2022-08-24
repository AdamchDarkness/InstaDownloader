import instaloader
import os

if not os.path.exists('InstaScrap'):
 os.mkdir('InstaScrap')

os.chdir('InstaScrap/')

instagram = instaloader.Instaloader()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
print('\n')
print('\n')
print(""
" ___ _   _ ____ _____  _        ________   _____        ___   _ _     ___    _    ____  _____ ____  "
"|_ _| \ | / ___|_   _|/ \      / / /  _ \ / _ \ \      / / \ | | |   / _ \  / \  |  _ \| ____|  _ \ "
" | ||  \| \___ \ | | / _ \    / / /| | | | | | \ \ /\ / /|  \| | |  | | | |/ _ \ | | | |  _| | |_) |"
" | || |\  |___) || |/ ___ \  / / / | |_| | |_| |\ V  V / | |\  | |__| |_| / ___ \| |_| | |___|  _ < "
"|___|_| \_|____/ |_/_/   \_\/_/_/  |____/ \___/  \_/\_/  |_| \_|_____\___/_/   \_\____/|_____|_| \_\      ")
print('\n')
print("                              ___________________BY DARKNESSUUUU___________________              ")
print('\n')
print('\n')

username = input("Type your username : ")
mdp = input("Type your password : ")

print("!! Connecting ...")

try:
    instagram.login(username,mdp)
except:
    print("Username or password are wrong")
    exit()

user = input("Type the instagram you want :  ")
print("!! Connecting ...")

if not os.path.exists(user):
 os.mkdir(user)

os.chdir(user + '/')

user_id = instagram.check_profile_id(user)
while(True):
    clear()
    print('\n')
    print('\n')
    print("____________________INSTA DOWNLOADER____________________")
    print('\n')
    print('\n')
    print(" 1 - To download profil picture ")
    print('\n')
    print(" 2 - To download stories ")
    print('\n')
    print(" 3 - To download hilights ")
    print('\n')
    print(" 4 - To download posts ")
    print('\n')
    print(" 5 - To download igtv ")
    print('\n')
    print(" 6 - To download posts where the user is tagged ")
    print('\n')
    print(" 9 - To exit")
    print('\n')

    w = int(input("Choice : "))

    if(w==1):
        if not os.path.exists('profil picture'):
            print("!! Downloading ...")
            try:
                instagram.download_profilepic(user_id)
                os.rename(user,'profil picture')
            except:
                print("User does not have profil picture")
        else:
            print("The directory already exists please delete it")
    elif(w==2):
        if not os.path.exists('stories'):
            print("!! Downloading ...")
            try:
                instagram.download_stories(userids={user_id})
                os.rename('：stories','stories')
            except:
                print("User does not have stories")
        else:
            print("The directory already exists please delete it")
    elif(w==3):
        if not os.path.exists('highlights'):
            print("!! Downloading ...")
            try:
                instagram.download_highlights(user_id)
                os.rename(user,'highlights')
            except:
                print("User does not have highlights")
        else:
            print("The directory already exists please delete it")
    elif(w==4):
        if not os.path.exists('posts'):
            print("!! Downloading ...")
            try:
                instagram.download_profile(user_id)
                os.rename(user,'posts')
            except:
                print("User does not have posts")
        else:
            print("The directory already exists please delete it")
    elif(w==5):
        if not os.path.exists('igtv'):
            print("!! Downloading ...")
            try:
                instagram.download_igtv(user_id)
                os.rename(user,'igtv')
            except:
                print("User does not have IGTV")
        else:
            print("The directory already exists please delete it")
    elif(w==6):
        if not os.path.exists('tagged'):
            print("!! Downloading ...")
            try:
                instagram.download_tagged(user_id)
                os.rename(user,'tagged')
            except:
                print("User does not have tagged")
        else:
            print("The directory already exists please delete it")
    else:
        exit() 

