pyinstaller --onefile --name powerpoint-generator-windows --add-data=assets/*:assets src/main.py --hidden-import='PIL._tkinter_finder' --noconsole
 