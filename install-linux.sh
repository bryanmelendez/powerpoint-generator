pyinstaller --onefile --name powerpoint-generator-linux --add-data=assets/*:assets src/main.py --hidden-import='PIL._tkinter_finder'
