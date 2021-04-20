"""
Kivy GUI program to square a number
Stuart Beattie
Started 20/04/2021
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Stuart Beattie'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 300)
        self.title = "Square Number 2"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
