pip install PyQt5
pip install Ete3
pip install pyinstaller
pyinstaller initializer.py

$DesktopPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Desktop)

$SourceFileLocation = "$PSScriptRoot\dist\initializer\initializer.exe"
$ShortcutLocation = "$DesktopPath\initializer.lnk"
$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($ShortcutLocation)
$Shortcut.TargetPath = $SourceFileLocation
$Shortcut.Save()
Read-Host -Prompt "Press Enter to exit"

