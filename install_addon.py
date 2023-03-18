import os
import shutil

# Get the path to the Anki add-ons folder
anki_addons_folder = os.path.join(
    os.path.expanduser("~"), ".local", "share", "Anki2", "addons"
)

# Create a new folder for the add-on
addon_folder = os.path.join(anki_addons_folder, "spellcheck_addon")
os.makedirs(addon_folder, exist_ok=True)

# Copy the add-on files to the new folder
shutil.copy("quillbot.py", addon_folder)
shutil.copy("spellcheck
