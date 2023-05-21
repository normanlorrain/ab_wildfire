Write-Output "Removing old venv"
Remove-Item -Recurse -errorAction ignore -Path .venv  
Write-Output "Creating new venv"
python -m venv .venv
Write-Output "Upgrading pip"
.venv\scripts\activate.ps1
python  -m pip install --upgrade pip
Write-Output "READY!"
