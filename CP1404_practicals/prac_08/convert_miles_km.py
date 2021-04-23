"""
Kivy GUI program to convert Miles to Kilometers.
Stuart Beattie
Started: 21/04/21
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM_CONVERSION = 1.60934
INCREASE_VALUE = 1
DECREASE_VALUE = -1


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
            # If error occurs reset input number to zero
            self.root.ids.output_label.text = str(0.0)

    def increase_increment(self, value):
        """Increase the input value by adding one then recalculate."""
        try:
            new_value = int(value) + INCREASE_VALUE
            self.root.ids.input_number.text = str(new_value)
            self.handle_calculate(new_value)
        except ValueError:
            self.root.ids.input_number.text = str(0)

    def decrease_increment(self, value):
        """Decrease the input value by subtracting one then recalculate."""
        try:
            new_value = int(value) - INCREASE_VALUE
            self.root.ids.input_number.text = str(new_value)
            self.handle_calculate(new_value)
        except ValueError:
            self.root.ids.input_number.text = str(0)


MilesToKilometersApp().run()
