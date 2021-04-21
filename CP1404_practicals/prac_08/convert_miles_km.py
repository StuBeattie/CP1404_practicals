"""
Kivy GUI program to convert Miles to Kilometers.
Stuart Beattie
Started: 21/04/21
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM_CONVERSION = 1.60934


class MilesToKilometersApp(App):
    """Convert miles to kilometers GUI with plus or minus integer adjustment buttons"""

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) * MILES_TO_KM_CONVERSION
            self.root.ids.output_label.text = "{:,.3f}".format(result)
        except ValueError:
            self.root.ids.output_label.text = 'Must be an integer!'

    def handle_increment(self):
        """Adjust the input value by adding or subtracting one."""
        pass


MilesToKilometersApp().run()
