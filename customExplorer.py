import os
import subprocess
import sys
from time import sleep



userDisk = int(input("Drive C:\ = 1, Drive D:\ = 2: "))

def main1():
    if userDisk == 1:
        initial_directory = 'C:\\'
        while True:
            os.chdir(initial_directory)  # Ensure the script starts in the desired directory

            # Always run the 'dir' command
            subprocess.run('dir', shell=True)

            dirShowCase = input("Do you want to display the contents of the Directory (y/n): ")

            if dirShowCase == "y":
                userFolderDisplay = input("Input DIR PATH to display: ")
                userFolderDisplayNEW = userFolderDisplay.replace('/', "\\")
                subprocess.run(fr'dir {userFolderDisplayNEW}', shell=True)

            userFolder = input("Enter the PATH of folder/file: ")
            userFolderNEW = userFolder.replace('/', "\\")
            subprocess.Popen(fr'explorer "C:\{userFolderNEW}"')
            print("done")
            sleep(2)

            userQuit = input("Do you want to quit? (y/n): ").lower()

            if userQuit == "y":
                break
            else:
                print("\n")
                pass
    else:
        pass

    if userDisk == 2:
        initial_directory = 'D:\\'
        while True:
            os.chdir(initial_directory)  # Ensure the script starts in the desired directory

            # Always run the 'dir' command
            subprocess.run('dir', shell=True)

            dirShowCase = input("Do you want to display the contents of the Directory (y/n): ")

            if dirShowCase == "y":
                userFolderDisplay = input("Input DIR PATH to display: ")
                userFolderDisplayNEW = userFolderDisplay.replace('/', "\\")
                subprocess.run(fr'dir {userFolderDisplayNEW}', shell=True)

            userFolder = input("Enter the PATH of folder/file: ")
            userFolderNEW = userFolder.replace('/', "\\")
            subprocess.Popen(fr'explorer "D:\{userFolderNEW}"')
            print("done")
            sleep(2)

            userQuit = input("Do you want to quit? (y/n): ").lower()

            if userQuit == "y":
                break
            else:
                print("\n")
                pass
    else:
        pass


if __name__ == "__main__":
        main1()
