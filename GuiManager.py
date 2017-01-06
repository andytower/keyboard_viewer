#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'tsa'
__author__ = 'andytower'

import queue
from tkinter import *
from tkinter import font


class GuiManager:

    def __init__(
        self,
        master,
        config,
        keyTrainer,
        currentLang
        ):
        self.master = master

        master.title('Keyboard')
        master.attributes('-topmost', 1)
        master.resizable(width=FALSE, height=FALSE)

        self.shift_key_codes = config.shift_keys
        self.config = config
        self.currentLang = currentLang
        self.keyTrainer = keyTrainer
        self.block_resizing = False

        self.gui_all_buttons = dict()
        self.gui_rows = dict()
        self.gui_row_buttons = dict()
        self.sticky_key_behaviour = self.config.sticky_key_behaviour

        self.buttonFont = font.Font(family=config.font_name,
                                    size=config.font_size)
        self.boldUnderscoredButtonFont = font.Font(family=config.font_name, size=config.font_size,
                      weight='bold', underline=1)

        for row_index in range(1, config.getNumOfRows() + 1):
            self.gui_rows[int(row_index)] = Frame(master)
            self.gui_row_buttons[int(row_index)] = []
            for button_num in range(1,
                                    config.getNumOfKeysInRow(row_index)
                                    + 1):
                newButton = Button(self.gui_rows[int(row_index)])
                if self.config.padx != -1:
                    newButton.config(padx=self.config.padx)
                if self.config.pady != -1:
                    newButton.config(pady=self.config.pady)
                if (row_index, int(button_num)) \
                    in config.key_pos_to_index:
                    self.gui_all_buttons[config.key_pos_to_index[(row_index,
                            int(button_num))]] = newButton
                self.gui_row_buttons[int(row_index)].append(newButton)
                newButton.pack(side=LEFT)

            self.gui_rows[int(row_index)].pack()
        self.reconfigure_text_on_buttons(config, shift_pressed=0,
                lang=self.currentLang)

        if len(self.config.colored_keys) != 0:
            for button_index in self.config.colored_keys:
                if button_index in self.gui_all_buttons:
                    self.gui_all_buttons[button_index].configure(bg=self.config.colored_keys[button_index])

        master.update_idletasks()

        self.default_geometry = self.parse_geometry(master.geometry())

    def resize_window_back(self):
        self.block_resizing = False
        self.resize_y_of_window(self.default_geometry[1])

    def parse_geometry(self, in_geometry):
        geometry_x_y = in_geometry[:in_geometry.find('+')]
        geometry_x_y = geometry_x_y.split('x')
        window_size = (int(geometry_x_y[0]), int(geometry_x_y[1]))
        return window_size

    def resize_y_of_window(self, y):
        y = 0
        if y < 0:
            y = 0
        self.master.geometry(str(self.default_geometry[0]) + 'x'
                             + str(y))
        self.master.update_idletasks()


    def reconfigure_text_on_buttons(
        self,
        config,
        shift_pressed,
        lang,
        ):
        for row_index in range(1, config.getNumOfRows() + 1):
            configured_buttons = dict((k, v) for (k, v) in config.key_pos_to_index.items() if k[0] == row_index)
            for configured_button_pos in configured_buttons:
                key_index = configured_buttons[configured_button_pos]
                self.gui_all_buttons[key_index]['font'] = \
                    self.buttonFont
                self.gui_all_buttons[key_index].configure(text=config.getKeyName(key_index,
                        shift_pressed, lang))
        for key_index in config.bold_underscored_keys:
            if key_index in self.gui_all_buttons:
                self.gui_all_buttons[key_index]['font'] = \
                    self.boldUnderscoredButtonFont

    def start(self):
        self.mainloop()
