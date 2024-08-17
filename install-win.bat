pyinstaller --onefile --name powerpoint-generator-v0-1-1-windows --add-data=assets/*:assets src/main.py --hidden-import='PIL._tkinter_finder' --noconsole
 