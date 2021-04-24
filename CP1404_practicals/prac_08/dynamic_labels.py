"""
Dynamically create a GUI that displays a list
of names in separate labels.
Stuart Beattie
Started: 24/04/21
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Take a list of names and display each name in the GUI using separate labels."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Long", "Mick Stone", "Billy Bob", "Joe Slacker"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from the list and display them on the GUI"""
        pass


DynamicLabelsApp().run()
