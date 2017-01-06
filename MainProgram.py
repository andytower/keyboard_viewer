#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'tsa'
__author__ = 'andytower'

from ConfigManager import ConfigManager
from GuiManager import GuiManager
from KeyboardStatus import keyboardStatus
from tkinter import Tk
from tkinter import Toplevel


class ThreadedClient:
    english = Tk()
    russian = Toplevel(english)

    def __init__(self):
        self.russian.attributes('-alpha', 0.5)
        self.english.attributes('-alpha', 0.5)

        self.config = ConfigManager()
        self.keyTrainer = keyboardStatus(self.config)
        keyTrainer = self.keyTrainer

        self.russian.protocol('WM_DELETE_WINDOW', self.kill_and_destroy)
        self.english.protocol('WM_DELETE_WINDOW', self.kill_and_destroy)

        self.guiManager = GuiManager(self.english, self.config,
                                     self.keyTrainer, 0)
        self.guiManager2 = GuiManager(self.russian, self.config,
                                      self.keyTrainer, 1)

        print(self.english.winfo_screenheight())
        self.running = 1
        self.english.mainloop()

    def kill_and_destroy(self):
        self.running = 0
        self.russian.destroy()
        self.english.destroy()

if __name__ == '__main__':
    app = ThreadedClient()
