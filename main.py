import os
from sys import stdout
from time import sleep
from getpass import getpass
import instaloader
from colorama import Fore


def main():
    if not os.path.exists('Result'):
        os.mkdir('Result')
    os.chdir('Result/')

    home_terminal()

    instagram = instaloader.Instaloader()

    instgram_osint(instagram)

    return


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
    return


def log(log_type, content):
    if log_type == "success":
        return Fore.GREEN + f'\n  - {content}' + Fore.RESET
    if log_type == "info":
        return Fore.BLUE + f'\n  -- {content}' + Fore.RESET
    if log_type == "warning":
        return Fore.YELLOW + f'\n * {content}' + Fore.RESET
    if log_type == "error":
        return Fore.RED + f'\n ** {content}' + Fore.RESET


def home_terminal():
    clear()
    app_logo = [
        "\n",
        Fore.LIGHTBLUE_EX +
        " ___ _   _ ____ _____  _        ________   _____        ___   _ _     ___    _    ____  _____ ____  ",
        "|_ _| \ | / ___|_   _|/ \      / / /  _ \ / _ \ \      / / \ | | |   / _ \  / \  |  _ \| ____|  _ \ ",
        " | ||  \| \___ \ | | / _ \    / / /| | | | | | \ \ /\ / /|  \| | |  | | | |/ _ \ | | | |  _| | |_) |",
        " | || |\  |___) || |/ ___ \  / / / | |_| | |_| |\ V  V / | |\  | |__| |_| / ___ \| |_| | |___|  _ < ",
        "|___|_| \_|____/ |_/_/   \_\/_/_/  |____/ \___/  \_/\_/  |_| \_|_____\___/_/   \_\____/|_____|_| \_\      ",
        Fore.RESET +
        "\n"
    ]

    app_credits = [
        "DARKNESSUUUU",
        "Lilian"
    ]

    for e in app_logo:
        print(e)
    for author in app_credits:
        print(f' Thank {author}\n')


def selection_terminal():
    clear()
    app_content = [
        "",
        "____________________INSTA DOWNLOADER____________________",
        " 1 - To download profil picture ",
        " 2 - To download stories ",
        " 3 - To download hilights",
        " 4 - To download posts",
        " 5 - To download igtv",
        " 6 - To download posts where the user is tagged",
        " 9 - To exit"
        "\n"
    ]
    for line in app_content:
        print(f'\n{line}')
    return


def selection_redirect(seconds):
    print(log("warning", "You gonna be redirect to selection in few seconds"))
    sleep(seconds)
    return


def instgram_osint(instagram):
    username = input("Type your username: ")
    password = getpass("\nType your password: ")

    print(log("info", "Connecting..."))

    try:
        instagram.login(username, password)
        print(log("success", "Conneted !"))
    except Exception as e:
        print(log("error", f'error: {e}'))
        selection_redirect(5)
        main()

    user = input("\nTarget username: ")

    user_id = instagram.check_profile_id(user)

    print(log("info", "Creating the target directory"))
    if not os.path.exists(user):
        os.mkdir(user)
    os.chdir(user + '/')
    print(log("success", "Directory created"))
    sleep(2)

    while 1:

        selection_terminal()

        choice = int(input("Choice: "))

        if choice == 1:
            print(log("info", "Downloading profile picture..."))
            try:
                instagram.download_profilepic(user_id)
                os.rename(user, 'profile picture')
                print(log("success", "Profile picture downloaded"))
            except Exception as e:
                print(log("error", f'{e}'))

        elif choice == 2:
            print(log("info", "Downloading stories..."))
            try:
                instagram.download_stories(userids={user_id})
                os.rename('：stories', 'stories')
                print(log("success", "Stories downloaded"))
            except Exception as e:
                print(log("error", f'{e}'))
        elif choice == 3:
            print(log("info", "Downloading Highlights..."))
            try:
                instagram.download_highlights(user_id)
                os.rename(user, 'highlights')
                print(log("success", "Highlights downloaded"))
            except Exception as e:
                print(log("error", f'{e}'))
        elif choice == 4:
            print(log("info", "Downloading Posts"))
            try:
                instagram.download_profile(user_id)
                os.rename(user, 'posts')
                print(log("success", "Posts downloaded"))
            except Exception as e:
                print(log("error", f'{e}'))
        elif choice == 5:
            print(log("info", "Downloading IGTV"))
            try:
                instagram.download_igtv(user_id)
                os.rename(user, 'igtv')
                print(log("success", "IGTV downloaded"))
            except Exception as e:
                print(log("error", f'{e}'))
        elif choice == 6:
            print(log("info", "Downloading posts where user has been tagged"))
            try:
                instagram.download_tagged(user_id)
                os.rename(user, 'tagged')
                print(log("success", "posts where user has been tagged downloaded"))
            except Exception as e:
                print(log("error", f'{e}'))
        selection_redirect(5)
        continue


if __name__ == '__main__':
    main()
