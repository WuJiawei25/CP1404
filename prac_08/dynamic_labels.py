from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # This is your data model: a list of names
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        main_layout = self.root.ids.main

        # Dynamically create a Label for each name
        for name in self.names:
            label = Label(text=name)
            main_layout.add_widget(label)

        return self.root

DynamicLabelsApp().run()