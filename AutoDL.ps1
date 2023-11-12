# Set the path to the Python launcher shortcut
$pythonLauncherPath = "C:\Users\Yourusername\AppData\Local\Programs\Python\Launcher\py.exe"

# Set the path to your Python script
$pythonScript = "C:\Users\Yourusername\downloadorganizer.py"

# Check if the Python script exists
if (Test-Path $pythonScript) {
    # Use the Python launcher shortcut to run the script
    Start-Process -FilePath $pythonLauncherPath -ArgumentList $pythonScript -NoNewWindow -Wait
} else {
    Write-Host "Python script not found. Please check the path."
}
