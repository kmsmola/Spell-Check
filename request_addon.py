from aqt import mw
import urllib.request
import zipfile

url = 'https://github.com/kmsmola/Spell-Check/archive/master.zip'

def downloadAddon():
    response = urllib.request.urlopen(url)
    data = response.read()
    filename = 'Spell-Check.zip'
    with open(filename, 'wb') as f:
        f.write(data)

    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(mw.addonManager.addonFolder())

downloadAddon()
