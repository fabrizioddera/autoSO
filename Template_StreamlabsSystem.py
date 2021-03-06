#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class
from AutoSO_Module import AutoSOSettings
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "AutoSO script"
Website = "https://www.streamlabs.com"
Description = "Auto shutout for raid and host"
Creator = "Fabrizio"
Version = "1.1.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
global SettingsFile
SettingsFile = ""
global ScriptSettings
ScriptSettings = AutoSOSettings()

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():

    Log("INIT DELLO SCRIPT")
    #   Create Settings Directory
    directory = os.path.join(os.path.dirname(__file__), "Settings")
    if not os.path.exists(directory):
        os.makedirs(directory)

    #   Load settings
    SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\\settings.json")
    ScriptSettings = AutoSOSettings(SettingsFile)
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    if data.IsChatMessage() and data.Message.find(ScriptSettings.Message) > -1 and getUserName(data.RawData) == ScriptSettings.BotName :
        Parent.SendStreamMessage("!" + ScriptSettings.Command + " " + getRaider(data.Message))
   
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

# Get username from message
def getUserName(rawMessage):
    array=rawMessage.split(";")
    for data in array:
        if data.find("display-name") > -1:
            arrayOfData=data.split("=")
            return arrayOfData[1]

def getRaider(message):
    array=message.split(" ")
    return array[0]

#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
#---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    
    if "$myparameter" in parseString:
        return parseString.replace("$myparameter","I am a cat!")
    
    return parseString

#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return

#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return

#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return

def Log(message):
    Parent.Log("AutoSO", message)
    return
