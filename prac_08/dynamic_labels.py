from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class DynamicLabelsApp(App):
    def build(self):
        # Create the root layout
        root = BoxLayout(orientation='vertical')

        # Sample list of names
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

        # Create labels for each name and add them to the root layout
        for name in names:
            label = Label(text=name)
            root.add_widget(label)

        return root

if __name__ == '__main__':
    DynamicLabelsApp().run()
