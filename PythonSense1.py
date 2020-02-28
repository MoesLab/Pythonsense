import sys
import time
#import evdev
sys.path.append("../../")
from appJar import gui
#from evdev import InputDevice, categorize, ecodes
#gamepad = InputDevice('/dev/input/event5')

# some useful colours
colours = ["red", "orange", "green", "pink", "purple"]


# function to login the user
def login(btn):
    if btn == "Clear":
        app.entry("username", "")
        app.setEntryFocus("username")
        app.entry("password", "")
    elif btn == "Submit":
        app.infoBox("Success", "Access granted")
        app.setTabbedFrameDisableAllTabs("Tabs", False)
        app.setToolbarEnabled()
        app.setToolbarPinned()
        app.setToolbarButtonDisabled("LOGOUT", False)
        app.enableMenubar()

# function to confirm logout
def logoutFunction():
    return app.yesNoBox("Confirm Exit", "Are you sure you want to exit?")

# disable the tabs
def logout(btn = None):
    app.setTabbedFrameDisableAllTabs("Tabs")
    app.setTabbedFrameDisabledTab("Tabs", "Login", False)
    app.setTabbedFrameSelectedTab("Tabs", "Login")
    # disable toolbar
    app.setToolbarDisabled()
    app.setToolbarButtonEnabled("EXIT")
    app.disableMenubar()
    app.enableMenuItem("Admin", "EXIT")

# function to update the Analog
def analog():
    #val = app.meter("Meter1")[0]*100 + 1
    app.meter("Meter1", (app.meter("Meter1")[0]*100 + 1)%100)
    app.meter("Meter2", (app.meter("Meter2")[0]*100 - 1)%100)
    app.meter("Meter3", (app.meter("Meter3")[0]*100 + 1)%100)


# called by the toolbar buttons
def toolbar(btn):
    print(btn)
    if btn == "EXIT": app.stop()
    elif btn == "LOGOUT": logout()
    elif btn == "FILL": app.setTabBg("Tabs", app.getTabbedFrameSelectedTab("Tabs"), app.colourBox())
    elif btn == "ACCESS": app.showSubWindow("Access")
    elif btn == "NETWORK": app.showSubWindow("Network")
    elif btn == "MD-SOUND": app.showSubWindow("Sound")
    elif btn == "MAP": app.showSubWindow("Maps")
    elif btn == "FULL-SCREEN":
         if app.exitFullscreen():
            app.setToolbarIcon("FULL-SCREEN", "FULL-SCREEN")
         else:
            app.setSize("fullscreen")
            app.setToolbarIcon("FULL-SCREEN", "FULL-SCREEN-EXIT")


# called when scale/meters are changed
def scale(name):
    if name == "TransparencySpin":
        trans = int(app.getSpinBox(name))
        app.setTransparency(trans)
        app.setScale("TransparencyScale", trans, callFunction=False)
    elif name == "TransparencyScale":
        trans = app.getScale(name)
        app.setTransparency(trans)
        app.setSpinBox("TransparencySpin", trans, callFunction=False)
    elif name == "FontScale": app.setFont(size=app.getScale(name))


# funciton to change the selected tab - called from menu
def changeTab(tabName):
    print("Changing to: ", tabName)
    app.setTabbedFrameSelectedTab("Tabs", tabName)
    print("done")

# keypad function
def keypad():
    app.setLabel("Lpad", "No Data")
    #event = gamepad.read_one()
    #app.setLabel("Lpad", str(event))


#RGB set up
def rgbSet(btn):
    if btn == " Off ": app.setLabelFrameBg("Colour","black")
    elif btn == " Red ": app.setLabelFrameBg("Colour", "red")
    elif btn == "Green ": app.setLabelFrameBg("Colour", "green")
    elif btn == " Blue ": app.setLabelFrameBg("Colour", "blue")
    elif btn == "Custom": app.setLabelFrameBg("Colour", app.colourBox())

#Relay set up
def relaySet(rbtn):
    if rbtn == "Red Togg": RB = 0
    elif rbtn == "Green Togg": GB = 0
    elif rbtn == "Blue Togg": BB = 0

# function to get a help message on log-in page
def helpMe(nbtn):
    app.infoBox("Login Help", "Any username/password will do...")
# function to get a help message on log-in page
def helpAbout(nbtn):
    app.infoBox("About Help", "Python Sense V1.0")
# function to get a help message on log-in page
def helpHelp(nbtn):
    app.infoBox("Help", "Python Sense V1.0")


# function to update status bar with the time
def showTime():
    app.setStatusbar(time.strftime("%X"))

###########################
## GUI Code starts here ##
###########################

with gui("Demo") as app:
    app.setLogLevel("ERROR")
    app.showSplash("PYTHONSENSE\nBy:Moe Azizi")

    # add a simple toolbar
    app.addToolbar(["EXIT", "LOGOUT", "FILL", "ACCESS", "NETWORK", "MD-SOUND", "MAP", "FULL-SCREEN"], toolbar, findIcon=True)

    #app.createMenu("Admin") with the name toolbar

    app.addMenuPreferences(toolbar)

    app.addMenuItem("Admin", "EXIT", toolbar, shortcut="Option-Control-Shift-Alt-Command-B", underline=2)
    app.addMenuItem("Admin", "LOGOUT", toolbar, shortcut="Shift-Command-B", underline=3)
    app.addMenuItem("Admin", "FILL", toolbar, shortcut="Control-Shift-C", underline=1)
    app.addMenuList("Tabs", ["Login", "Candles", "RGB LED", "Analog", "Relays", "Keypad", "Map", "Configs"], changeTab)
 
    app.addMenuCheckBox("Settings", "Box 1", toolbar, "Command-1")
    app.addMenuCheckBox("Settings", "Box 2", toolbar, "Command-2")
    app.addMenuCheckBox("Settings", "Box 3", toolbar, "Command-3")
    app.addMenuCheckBox("Settings", "Box 4", toolbar, "Command-4")
    app.addMenuCheckBox("Settings", "Box 5", toolbar, "Command-5")

    app.addMenuRadioButton("Settings", "r1", "Radio 6", toolbar, "Command-6", 7)
    app.addMenuRadioButton("Settings", "r1", "Radio 7", toolbar, "Command-7", 7)
    app.addMenuRadioButton("Settings", "r1", "Radio 8", toolbar, "Command-8", 7)
    app.addMenuRadioButton("Settings", "r1", "Radio 9", toolbar, "Command-9", 7)
    app.addMenuRadioButton("Settings", "r1", "Radio 0", toolbar, "Command-0", 7)

    app.addMenuList("List Items", ["Item 1", "Item 2", "-", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7"], toolbar)
    app.addMenuList("List Items", ["-", "aaa", "-", "bbb", "-", "ccc", "-", "ddd", "-"], toolbar)


    #app.addMenuWindow()
    #app.addMenuHelp(toolbar)
    #app.addMenuItem("WIN_SYS", "About", helpHelp)
    app.addMenuList("Help", ["Help", "About"], [helpHelp, helpAbout])

    try:
        app.setMenuIcon("Admin", "EXIT", "EXIT", "left")
        app.setMenuIcon("Admin", "LOGOUT", "LOGOUT", "left")
        app.setMenuIcon("Admin", "FILL", "FILL", "left")
    except:
        pass
     
    #app.addCanvas("c1")

    app.disableMenubar()

    # add a statusbar to show the time
    app.addStatusbar(side="RIGHT")
    #app.addStatusbar(side="LEFT")
    app.registerEvent(showTime)
    app.stopFunction = logoutFunction

    with app.tabbedFrame("Tabs"):
        with app.tab("Login", bg="slategrey", sticky="new"):
            with app.labelFrame("Login Form"):
                app.label("username", "Username", sticky="ew")
                app.entry("username", pos=('p', 1), focus=True)
                app.label("password", "Password")
                app.entry("password", pos=('p', 1), secret=True)
                app.buttons(["Submit", "Clear"], login, colspan=2)
                app.link("help", helpMe, column=1, sticky="e")

        with app.tab("Candles"):
             app.startFrame("LEFT",row=0, column=0)
             app.addImage("Cand1", "candle1.gif")
             app.shrinkImage("Cand1",1)
             app.button("Sensor1")
             app.stopFrame()
             
             app.startFrame("RIGHT", row=0, column=1)
             app.addImage("Cand2", "candle1.gif")
             app.shrinkImage("Cand2",1)
             app.button("Sensor2")
             app.stopFrame()

        with app.tab("RGB LED"):
            with app.labelFrame("Colour", sticky="news"):
                 app.setBg("red")

            app.buttons([" Off "," Red ","Green "," Blue ","Custom"], rgbSet)    
  
        with app.tab("Analog"):
            app.meter("Meter1", fill="red")
            app.meter("Meter2", fill="green")
            app.meter("Meter3", fill="blue")
            app.registerEvent(analog)

        with app.tab("Relays"):
            with app.labelFrame("Relay", sticky="news"):
                 app.addImage("Rl1", "Relay1.gif")
                 app.shrinkImage("Rl1",1)

            app.buttons(["Blue Togg","green Togg","Red Togg"], relaySet)    


        with app.tab("Keypad", inPadding = (4,4)):
             app.startLabelFrame("Nyko BLE", 0, 0, sticky = "news")
             app.addImage("Nyko BLE", "Nyko2.gif")
             app.stopLabelFrame()
             app.addLabel("Lpad",text = None)
             app.registerEvent(keypad)
             app.getFocus()


        with app.tab("Map"):
             #app.addGoogleMap("m1")
             #app.setGoogleMapSize("m1","300x300")
             app.getFocus()

        with app.tab("Configs", sticky = "news"):
             app.slider("FontScale", 12, show=True, change=scale, range=(6,40))
             app.slider("TransparencyScale", 100, change=scale, interval=25)
             app.spin("TransparencySpin", value=0, endValue=100, item='100', change=scale)

    with app.subWindow("Access", sticky="news"):
         app.getFocus()

    with app.subWindow("Network", sticky="news"):
         app.getFocus()

    with app.subWindow("Sound", sticky="news"):
         app.getFocus()

    with app.subWindow("Maps", sticky="news"):
        #app.addGoogleMap("g1")
        app.getFocus()

    # start logged out
    logout()
