import os, json, subprocess, requests, ctypes

try:
    with open(os.path.join(os.getcwd(), 'portapp.json'), 'r') as f:
        version = json.load(f)
        version = version['version'] + '-' + version['release']
        f.close()
except:
    i = ctypes.windll.user32.MessageBoxW(0, "No installed Brave Portable detected. New install?", "Brave Startup", 4)
    if i == 6:
        version = 'New install'
    else:
        os._exit(0)

fetch = json.loads(requests.get('https://api.github.com/repos/portapps/brave-portable/releases/latest').text)
link = fetch['assets'][0]['browser_download_url']
if version == 'New install':
    subprocess.Popen(['C:\\Windows\\System32\\cmd.exe', '/c', 'start', '', link])
elif str(fetch['tag_name']) != str(version) and version != 'New install':
    i = ctypes.windll.user32.MessageBoxW(0, "There is a new version!\nUpdated version: "+ str(fetch['tag_name']) +"\nCurrent version: " + str(version) + "\nWould you like to update?", "Brave Startup", 4)
    if i == 7:
        os._exit(0)
    subprocess.Popen('"brave-portable.exe" "' + link + '"')
else:
    subprocess.Popen("brave-portable.exe --no-startup-window")
os._exit(0)