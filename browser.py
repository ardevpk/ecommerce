

import webbrowser

# mainPath = r'D:\Desktop Data\Coding\New Python Function\new\index.py'


Weburl = 'http://127.0.0.1:8000'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
try:
    webbrowser.get(chrome_path).open_new(Weburl)
except Exception as e:
    webbrowser.open(Weburl)