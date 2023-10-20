# This is a build script to automatically pack the needed files into a single archive which can be distributed to users.
# Automatically excludes files that are not needed to run the addon in Blender.
# To build the addon, simply set the config variables down below.
# Once variables are set, run this script to build.


import os
import shutil


# CONFIG VARIABLES START

# Destination path of addon build. Always use forward slashes.
destination_path = 'C:/Users/Parallel/Desktop/'

# Version number of addon. NO trailing dot at the end. Should match bl_info in __init__.py
version_number = "0.0.0"

# Automatically pack into .zip archive. Needed for installing the addon in Blender.
pack_to_zip = True

# If true unpacked files will be removed so that only the zip archive is left in the destination folder
remove_unpacked_files_after_zip = True

# do not build files that match following patterns, to exclude development files that the end user does not need
IGNORE_PATTERNS = ('*.pyc', 'tmp*', '*__pycache__*', '.git', '.vscode', '.gitignore', '.gitattributes', 'build.py',
                   'bl-md-retopology_updater')


# CONFIG VARIABLES END


# Add root folder to path
if destination_path[-1] in ['/', '\\']:
    destination_path += "bl-md-retopology-" + version_number + "/"
else:
    destination_path += "/bl-md-retopology/" + version_number + "/"

zip_path = destination_path


# Add second layer folder (required for blender addon installation process)
if destination_path[-1] in ['/', '\\']:
    destination_path += "bl-md-retopology/"
else:
    destination_path += "/bl-md-retopology/"


dir_path = os.path.dirname(os.path.realpath(__file__))
shutil.copytree(dir_path, destination_path, ignore=shutil.ignore_patterns(*IGNORE_PATTERNS))

if pack_to_zip:
    shutil.make_archive(zip_path, "zip", zip_path)

    if remove_unpacked_files_after_zip:
        shutil.rmtree(zip_path)

print("Build script done.")
