# Ableton_Live_Unique_Note_IDs_fix
Python script for solving the issue when you can't open up an Ableton Live session and it says "Non-unique Note IDs".

*Please make a copy of your .als file before putting it in this tool!*
*I am not liable for anything that happens to the file, so a copy is always a good idea!*

How to use (tried to give some instructions for folks new to terminal and technical things):

0. You'll need to download the Python file or copy the code into a Python file.
1. Make sure you have Python installed.  I used version 3.10.10 to create this, but in theory any python that's newer could work too. If you're new to Python versioning, be aware that this can be a spot of trouble.  [Download Python](https://www.python.org/downloads)
2. Once Python is installed (if you haven't already), open up a new Terminal window (I am using macOS).  To do so you can press CMD+Spacebar and enter "Terminal" in the search.
4. Copy the .als file you want to fix and paste that copy somewhere safe (Just in case, you don't want to actually mess anything up).
5. Navigate to the path of the Python file in Terminal using `cd` which stands for Change Directory.  I've already made it an executable, so you can just do this:
    $ ./als_xml_fix.py /Users/YOURUSERNAMEHERE/Music/Albeton/User\ Library/Projects/COPYOFYOURABLETONFILE.ALS
6. Your resulting file should be in the fix folder named "output_file_fixed.als". 
7. Try it out!
8. If that doesn't work, e-mail contact@ableton.com with your project file (the .als file) and let them know what the error message is, and hopefully they will get it back to you fixed.
