# Open-explorer-in-certain-directory-Python-
 Title

Go to the dir of file to build it.
Command : "pyinstaller --onfile customExplorer.py"

.exe in "dist" folder
Move it to where you wont accidentally delte it.

Add folder to PATH:
How to add to path: (Credit: https://windowsloop.com/how-to-add-to-windows-path/)
     Press the Start key on your keyboard.
     Search and open “Edit the system environment variables.”
     Go to the “Advanced” tab.
     Click the “Environment variables” button.
     Select the “Path” variable under “System variables.”
     Click the “Edit” button.
     Press the “New” button.
     Type the full directory path of the program. Without the program!!!! Ex.(C:\ProgramFolder)
     Press “Enter” to confirm the path.
     Click “Ok.”
     Press the “Ok” button in the Environment Variables window.
     Click “Ok” in the System Variables window.

Make a batch file that will run the .exe file.
Barch code: Include the exe in path!!! Ex.(C:\ProgramFolde\program.exe)
@echo off
echo Running My Program
"C:\Path\to\program"

Name the .bat file something simple and short, you will be using the bat file name to call it in CMD.
Now it should wokr restart cmd if you are currently running it and restart it.
I does not matter if you are using user or admin CMD.
