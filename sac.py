import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
from colorama import Fore, Back, Style
import logging

import argparse
 


def create1():
        logging.info("Selected option 1")
        print(Fore.BLUE + '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) Creating video... ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)'+ Style.RESET_ALL)
        try:
            create = os.system('ffmpeg -i content/background.mp4 -i content/image1.jpg -i content/image2.jpg -i content/image3.jpg -i assets/text.png -i assets/name.png -filter_complex "[0:v]scale=2275:1280[bg];[bg]crop=720:1280:0:0[bg];[bg][1:v] overlay=150:200 [tmp1]; [tmp1][2:v] overlay=300:600 [tmp2]; [tmp2][3:v] overlay=200:900 [tmp2];  [tmp2][4:v] overlay=100:60[tmp2];  [tmp2][5:v] overlay=300:1150" temp/withoutoutro.mp4')
        except:
            logging.error("Unknown error")

        try:
            video_1 = VideoFileClip("temp/withoutoutro.mp4")
            video_2 = VideoFileClip("assets/outro.mp4")
            print(Fore.BLUE + '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) Concatenating outro... ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)'+ Style.RESET_ALL)
            final_video= concatenate_videoclips([video_1, video_2])
            final_video.write_videofile("output.mp4")
            logging.info("Outro added successfully")
        except Exception  as e:
            logging.error(e)

        try:
            print(Fore.BLUE + '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) Removing temp files... ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)'+ Style.RESET_ALL)
            os.remove('temp/withoutoutro.mp4')
            logging.info("Removed temp files successfully")

        except Exception  as e:
            logging.error(e)
        print(Fore.GREEN + 'Video created successfully!'+ Style.RESET_ALL)
        logging.info("Video created successfully")

def create2():
        logging.info("Selected option 2")
        print(Fore.BLUE + '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) Creating video... ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)'+ Style.RESET_ALL)
        try:
            create = os.system('ffmpeg -i content/background.mp4 -i content/image1.jpg -i content/image2.jpg -i content/image3.jpg -i assets/text.png -i assets/name.png -filter_complex "[0:v]scale=2275:1280[bg];[bg]crop=720:1280:0:0[bg];[bg][1:v] overlay=150:100 [tmp1]; [tmp1][2:v] overlay=300:500 [tmp2]; [tmp2][3:v] overlay=200:800 [tmp2];  [tmp2][4:v] overlay=100:1000[tmp2];  [tmp2][5:v] overlay=300:10 " temp/withoutoutro.mp4')
        except:
            logging.error("Unknown error")
        try:
            video_1 = VideoFileClip("temp/withoutoutro.mp4")
            video_2 = VideoFileClip("assets/outro.mp4")
            print(Fore.BLUE + '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) Concatenating outro... ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)'+ Style.RESET_ALL)
            final_video= concatenate_videoclips([video_1, video_2])
            final_video.write_videofile("output.mp4")
            logging.info("Outro added successfully")
        except Exception  as e:
            logging.error(e)

        try:
            print(Fore.BLUE + '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) Removing temp files... ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)'+ Style.RESET_ALL)
            os.remove('temp/withoutoutro.mp4')
            logging.info("Removed temp files successfully")

        except Exception  as e:
            logging.error(e)
        print(Fore.GREEN + 'Video created successfully!'+ Style.RESET_ALL)
        logging.info("Video created successfully")

def check():
   print(Fore.GREEN + "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) Folder Check ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)" + Style.RESET_ALL)
   if os.path.exists("assets") and os.path.exists("content") and os.path.exists("temp"):
        print("Checking assets folder...")
        if os.path.exists("assets/name.png") and os.path.exists("assets/outro.mp4") and os.path.exists("assets/text.png"):
            print("Assets folder is all correct")
        else:
            print("Possibly you forgot to put one of these files: name.png outro.mp4 text.png in the assets folder")
            exit()
        if os.path.exists("content/image1.jpg") and os.path.exists("content/background.mp4") and os.path.exists("content/image2.jpg") and os.path.exists("content/image3.jpg"):
            print("Content folder is all correct")
        else:
            print("Possibly you forgot to put one of these files: background.mp4 image1.jpg image2.jpg image3.jpg in the content folder")
            exit()
        print("All folders are correct!")
   else:
        logging.warning("Folders not created!")
        print(Fore.YELLOW +"Folders not created!" + Style.RESET_ALL)
        print("Creating folders...")
        os.mkdir("assets")
        os.mkdir("content")
        os.mkdir("temp")
        logging.info("Created successfully")
        print("Created successfully")
        print("Now you need to put the content in those folders, visit the documentation at github.com/itroeix/ShortsAutoCreator")
        exit()

# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-p", "--Position", help = "Possible positions: up, down")
 
# Read arguments from command line
args = parser.parse_args()


# Create and configure logger
logging.basicConfig(filename="sac.log",
                    format='[%(asctime)s]: [%(levelname)s, line: %(lineno)d]  %(message)s',
                    filemode='w')
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
 
if __name__=="__main__":
    check()
    print(Fore.GREEN + "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) ShortsAutoCreator ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)" + Style.RESET_ALL)
    if args.Position:
        if args.Position == "up":
            print(Fore.YELLOW + "There may be some errors, log file is created in sac.log" + Style.RESET_ALL)
            create1()
        elif args.Position == "down":
            print(Fore.YELLOW + "There may be some errors, log file is created in sac.log" + Style.RESET_ALL)
            create2()
        else:
            logging.error("Position is incorrect! Possible positions: up, down")
            print("Position is incorrect! Possible positions: up, down ")
    else:
        logging.warning("Unspecified parameters, menu is used")
        print(Fore.YELLOW + "Unspecified parameters, menu is used" + Style.RESET_ALL)
        print(Fore.YELLOW + "There may be some errors, log file is created in sac.log" + Style.RESET_ALL)
        print("Text position:")
        print("1. Up")
        print("2. Down")

        choice = input("> ")

        if choice == '1':
            create1()
        elif choice == '2':
            create2()
        else:
            logging.error('Invalid choice.')
            print("Invalid choice.")
   # test
