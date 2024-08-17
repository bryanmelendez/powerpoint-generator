pyinstaller --name powerpoint-generator --distpath powerpoint-generator --add-data=assets/*:assets src/main.py --hidden-import='PIL._tkinter_finder'
