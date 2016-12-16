#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'tsa'
__author__ = 'andytower'

from ConfigManager import ConfigManager
from GuiManager import GuiManager
from KeyboardStatus import keyboardStatus
from tkinter import Tk

class ThreadedClient:
    def __init__(self, master):
        self.master = master

        master.attributes('-alpha', 0.5)

        self.config=ConfigManager()
        self.keyTrainer=keyboardStatus(self.config)
        keyTrainer=self.keyTrainer

        master.protocol('WM_DELETE_WINDOW', self.kill_and_destroy)

        self.guiManager=GuiManager(master,self.config,keyTrainer.myQueue,keyTrainer)

        #keyTrainer.begin_scan()

        self.running = 1
        self.periodicCall()
        master.mainloop()

    def kill_and_destroy(self):

        self.running = 0
        #self.keyTrainer.stop_scan()
        if self.config.debug:
            print("Stopping scan...")
        self.master.destroy()


    def periodicCall(self):
        self.guiManager.processQueue()
        if not self.running:
            # import sys
            self.kill_and_destroy()
        self.master.after(20, self.periodicCall)

if __name__ == '__main__':
    root = Tk()


    app = ThreadedClient(root)
    #root.mainloop()
