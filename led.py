import os
import requests

DISPLAY_TEXT='send_text'
CLEAR_TEXT='clear_text'

DISPLAY_TEXT_CMD  = """LedDisplayControllerGui.exe -NoServer -NoGui -SetBrightness 0.1 -SetSpeed 0.1 -SendText "%s" """
CLEAR_TEXT_CMD = """LedDisplayControllerGui.exe -NoServer -NoGui -DeleteRegex "" -SendText "" """

def run_display_command(command, message=None):
  cwd = os.getcwd()
  os.chdir("..")
  if command == DISPLAY_TEXT:
    cmd_string = DISPLAY_TEXT_CMD % message
    #print("sending command %s" % cmd_string)
    os.system(cmd_string)
  elif command == CLEAR_TEXT:
    #print("sending command %s" % CLEAR_TEXT_CMD)
    os.system(CLEAR_TEXT_CMD)
  os.chdir(cwd)