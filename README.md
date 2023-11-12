# downloadorganizer
This GitHub project automates the organization of files in the Downloads folder.
Overview

Download Organizer is a script designed for users to automate the organization of files in the Downloads folder. 

Features

    Automatic Organization: Files in the Downloads folder are automatically sorted into subdirectories based on their types (e.g., documents, images, videos) for a neat and structured file organization.
    Continuous Monitoring: The script can run in the background depending on yor OS.
    Customizable: Users can easily customize the Python file organization script and adapt it to their specific preferences and directory structures.


Powershell Included Script

This script is written in PowerShell and is intended to automate the execution of a Python script using the Python launcher shortcut (py.exe). 

Make sure to replace "Yourusername" with your actual Windows username and adjust the paths accordingly. Also, ensure that the specified Python launcher path and script path are correct for your system.


To schedule the execution of your PowerShell script using Task Manager at regular intervals, you can follow these steps:

    Open Task Scheduler:
        Press Win + X and select "Task Scheduler" from the menu.

    Create a New Task:
        In the Actions pane on the right, click on "Create Basic Task..."

    Set Name and Description:
        Provide a name and description for your task, then click "Next."

    Trigger Configuration:
        Choose "Daily" and click "Next."

    Set Daily Options:
        Set the start date and time to the current date and time.
        Set the recurrence to "Every 1 days" and "Repeat task every" to "1 minutes."
        Set the duration to "Indefinitely" if you want the task to repeat indefinitely.

    Action Configuration:
        Choose "Start a Program" and click "Next."

    Program/Script and Add Arguments:
        In the "Program/script" field, browse and select the PowerShell executable (powershell.exe). Typically, this is located at C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe.
        In the "Add arguments" field, enter the full path to your PowerShell script:

        arduino

    -File "C:\Path\To\Your\Script.ps1"

    Make sure to replace "C:\Path\To\Your\Script.ps1" with the actual path to your PowerShell script.

Start In (Optional):

    In the "Start in (optional)" field, enter the directory where your script is located.

Finish:

    Review your settings and click "Finish."

Enter User Credentials (Optional):

    If your script requires specific user permissions, you might need to enter the appropriate credentials on the "General" tab.

Run the Task:

    To test the task, right-click on it in Task Scheduler and select "Run."