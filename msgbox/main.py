
from msgbox import MsgBox
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_string('''
#place kivy notation of app here

<MsgBox_ButtonsBar>:
    size_hint: 1, 0.5
    
<MsgBox_Button>:
    font_size: '20px'

''')

class MainApp(App):
    
    def callback(self):
        print "Yes, it's right descision!"
    
    def build(self):
        root = Widget()
        msg = MsgBox(text="Are you able to answer for this question?", title="Hello world",
                     type='question', yes_callback=self.callback)
        msg.open()
        return root
        

if __name__ == '__main__':
    MainApp().run()
