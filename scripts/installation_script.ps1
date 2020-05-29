pip install PyQt5
pip install Ete3
pip install pyinstaller
pyinstaller CompareMS2GUI.py

$DesktopPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Desktop)

$SourceFileLocation = "$PSScriptRoot\dist\CompareMS2GUI\CompareMS2GUI.exe"
$ShortcutLocation = "$DesktopPath\CompareMS2GUI.lnk"
$WScriptShell = New-Object -ComObject WScript.Shell
$Shortcut = $WScriptShell.CreateShortcut($ShortcutLocation)
$Shortcut.TargetPath = $SourceFileLocation
$Shortcut.Save()
Read-Host -Prompt "Press Enter to exit"

