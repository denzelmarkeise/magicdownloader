# downloadorganizer
This GitHub project automates the organization of files in the Downloads folder.
Overview

Download Organizer is a script designed for Windows users to automate the organization of files in the Downloads folder. It employs a PowerShell script coupled with a FileSystemWatcher to trigger a Python file organization script whenever a new file is added, providing a streamlined solution to maintain a well-organized Downloads directory.

Features

    Automatic Organization: Files in the Downloads folder are automatically sorted into subdirectories based on their types (e.g., documents, images, videos) for a neat and structured file organization.
    Continuous Monitoring: The script runs in the background, utilizing the FileSystemWatcher class to monitor the Downloads folder and respond to new file additions promptly.
    Customizable: Users can easily customize the Python file organization script and adapt it to their specific preferences and directory structures.

    Usage

    Configure Paths: Update the paths in the PowerShell script (WatchDownloads.ps1) to specify the location of your Downloads folder and the Python executable along with the organization script.

    powershell

$folder = "C:\Users\YourUsername\Downloads"
$script = "C:\Path\To\python.exe C:\Path\To\Your\Script.py"

Run the PowerShell Script: Open a PowerShell console with administrator privileges and run the script as a background job.

powershell

Start-Job -FilePath .\WatchDownloads.ps1

Customize Python Script (Optional): Modify the Python script (YourScript.py) as needed to tailor the file organization logic to your preferences.

Dependencies

    Python: Ensure Python is installed on your system, and the path to the Python executable is correctly specified in the PowerShell script.
    PowerShell: The script utilizes PowerShell for continuous monitoring.

    License

This project is licensed under the MIT License - see the LICENSE file for details. Feel free to fork and adapt it to suit your needs!