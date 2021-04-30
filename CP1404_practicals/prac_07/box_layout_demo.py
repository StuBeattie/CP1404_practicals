"""User greeting GUI"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Greet the user by name using a GUI."""

    def build(self):
        """Build box layout."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Connect buttons with GUI to allow user interaction."""
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_text(self):
        """Clear text from Label and TextInput."""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
