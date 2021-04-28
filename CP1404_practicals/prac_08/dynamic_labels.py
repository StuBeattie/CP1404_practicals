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


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data example - list of names
        self.names = ["Bob Brown", "Mick Stone", "Cat Cyan", "Oren Ochre", "Joe Roan"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from list entries and add them to the GUI."""
        for name in self.names:
            # create a label for each name in the list.
            temp_label = Label(text=name)
            # add the label to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_label)
            # update status text
            self.status_text = "{}".format(name)


DynamicWidgetsApp().run()
