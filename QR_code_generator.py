import qrcode
from art import *
from termcolor import colored

def main():
    answer = input(colored("Do you want a QR code in png or jpg ? ", 'cyan'))

    if answer == str("png"):
        main_png()
    else:
        main_jpg()

def main_png():
    try:
        pic = qrcode.make(input(colored(text2art ("Please  enter your URL"),'yellow')))
        pic.save('qrcode.png')
    except ValueError as e:
        print(e)
    except:
        print("unknow error")
    print(colored('✔✔✔ The QR code is in the same directory as this one (PNG) ✔✔✔', 'green'))


def main_jpg():
    try:
        pic = qrcode.make(input(colored(text2art ("Please enter your URL"),'yellow')))
        pic.save('qrcode.jpg')
    except ValueError as e:
        print(e)
    except:
        print("unknow error")
    print(colored('✔✔✔ The QR code is in the same directory as this one (jpg) ✔✔✔', 'green'))

if __name__ == '__main__':
    main()
