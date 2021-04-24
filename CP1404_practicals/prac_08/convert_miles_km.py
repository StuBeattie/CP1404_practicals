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
        result = self.convert_value(value) * MILES_TO_KM_CONVERSION
        self.root.ids.output_label.text = "{:,.3f}".format(result)

    def increment_adjustment(self, value, increment):
        """Increase the input value by adding or subtracting one on button press and recalculate."""
        new_value = int(self.convert_value(value)) + increment
        self.root.ids.input_number.text = str(new_value)
        self.handle_calculate(new_value)

    @staticmethod
    def convert_value(value):
        """Change input to float and conduct error checking."""
        try:
            return float(value)
        except ValueError:
            return 0.0


MilesToKilometersApp().run()
