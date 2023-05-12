Setting up python on windows 10:

Install python 9 on windows store if you haven't yet.  Make sure your environment paths are set up.
search environment variables in windows search. 
- Click environment variables.
- Click Path -> Edit
- C:\Users\(your user here)\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages
- C:\Users\(your user here)\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts
Search cmd in windows search
type the following:
python -m pip install keyboard
python -m pip install pyautogui
python -m pip install opencv-python
python -m pip install pillow

Open e7, enter the lobby and open the shop.  Full screen your emulator.

You can try to use my screenshots, but I recommend creating your own. (Refresh shop until you see a mystic/cov bookmark and screenshot them and save them as PNG files with the exact same name as mine.

Windows search "idle" and open the program.  Open the "curosr location.py" file in the folder you downloaded.
Click Run and Run Module.  This will give you coordinates for your cursor location when it is on the screen.
Place your cursor over the center of an item and look at the number/remember it.
Now place your cursor on the center of the buy button for that item.  You will need to subtract the X and Y values of those coordinates and edit the script accordingly.
Open Auto Refresh.py in a notepad file or in Idle.
Scroll down and look for line 42 and 60 
These lines contain the X and Y coordinate differences you just calculated.  I have +1050 and +40 because of my monitor resolution.  Change them to work for yours.

Save the .py file, full screen your emulator, and run the file just like you ran the cursor location file.  It should refresh your shop and buy all mystics for you.