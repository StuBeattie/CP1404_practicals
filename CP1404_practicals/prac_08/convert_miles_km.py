"""
Kivy GUI program to convert Miles to Kilometers.
Stuart Beattie
Started: 21/04/21
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM_CONVERSION = 1.60934
CHANGE_VALUE = 1


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
        result = self.sort_exceptions(value) * MILES_TO_KM_CONVERSION
        self.root.ids.output_label.text = "{:,.3f}".format(result)

    def increase_increment(self, value):
        """Increase the input value by adding one then recalculate."""
        new_value = int(self.sort_exceptions(value)) + CHANGE_VALUE
        self.root.ids.input_number.text = str(new_value)
        self.handle_calculate(new_value)

    def decrease_increment(self, value):
        """Decrease the input value by subtracting one then recalculate."""

        new_value = int(self.sort_exceptions(value)) - CHANGE_VALUE
        self.root.ids.input_number.text = str(new_value)
        self.handle_calculate(new_value)

    @staticmethod
    def sort_exceptions(value):
        """Conduct error checking on inputs and button presses."""
        try:
            return float(value)
        except ValueError:
            return 0.0


MilesToKilometersApp().run()
