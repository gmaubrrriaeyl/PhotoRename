"""
Reads file attribute and renames photos based on the
creation date in the following format:
YYYY-MM-DD HH-MM-SS.jpg

This script renames ALL FILES in the source folder. YOU CANNOT
UNDO THIS OPERATION
"""

import os
import datetime
from pathlib import Path
import wx

class Frame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size = (400,450))

        self.panel = wx.Panel(self, -1) # First panel

        #Labels
        self.exit = wx.StaticText(self.panel, label = '', pos=(100,100))
        self.warn2 = wx.StaticText(self.panel, label = 'Currently wipes metadata on completion which is a huge problem.', pos=(20,40))
        self.warn3 = wx.StaticText(self.panel, label = 'Need to use shutil instead of os', pos=(20,60))

        self.linux = wx.RadioButton(self.panel, label = 'Linux/Mac', pos = (30, 140))
        self.windows = wx.RadioButton(self.panel, label = 'Windows', pos = (30, 160))

        #Checkbox
        #self.backup = wx.CheckBox(self.panel, -1, label = 'Backup file names?', pos = (30,230))
        #self.newdir = wx.CheckBox(self.panel, -1, label = 'Copy and rename photos to new directory?', pos = (30,250))
        
        #Buttons
        self.rename = wx.Button(self.panel, label = "Select Directory", pos = (60,300))
        self.clear = wx.Button(self.panel, label="Clear Form", pos=(180, 300))
        self.close = wx.Button(self.panel, label = "Close", pos = (280, 300))
        self.rename.Bind(wx.EVT_BUTTON, self.rename_photos)
        self.clear.Bind(wx.EVT_BUTTON, self.clear_form)
        self.close.Bind(wx.EVT_BUTTON, self.close_frame)


        ##Functions
    def rename_photos(self, event):
        with wx.DirDialog(self, "File Explorer", style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dirDialog:
            if dirDialog.ShowModal() == wx.ID_CANCEL:
                return
        path = dirDialog.GetPath()
        with os.scandir(path) as loc:
            x = 0
            for i in loc:
                info = i.stat()
                src = i
                dst = str(datetime.datetime.fromtimestamp(info.st_ctime))
                dst = dst.replace(':', '-')
                sep = '.'
                dst = dst.split(sep, 1)[0]
                if self.linux.GetValue():                    
                    dst = str(path) + '/' + dst + ".jpg"
                    os.rename(src, dst)
                    x += 1
                if self.windows.GetValue():
                    dst = str(path) + '\\' + dst + ".jpg"
                    os.rename(src, dst)
                    x += 1
            print("Operation completed on " + str(x) + " files.")


    def clear_form(self, event):
        self.exit.SetLabel('')
        self.txtctrl1.SetValue('')

        
    def close_frame(self, event):
        self.Close()
        
"""
        label: program description
        button: program description long
        
        text entry: Pathway
        label: text entry

        Checkbox: item type
        
        Button: rename func
        Button: clear
        Button: close
        
"""

if __name__ == "__main__":
    app = wx.App()
    fr = Frame(None, 'Photo Renamer')
    fr.Show()
    app.MainLoop()
