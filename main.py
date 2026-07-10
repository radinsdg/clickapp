from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)
        
        self.label = Label(text='0', font_size=100)
        
        btn = Button(text='click', font_size=40)
        btn.bind(on_press=self.increment)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout
    
    def increment(self, instance):
        current = int(self.label.text)
        self.label.text = str(current + 1)

if __name__ == '__main__':
    MyApp().run()
