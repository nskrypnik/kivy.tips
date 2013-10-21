
from msgbox import MsgBox
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_string('''
#place kivy notation of app here
    
<MsgBox_Button>:
    font_size: '20px'
    
<MsgBox_Title>:
    font_size: '14dp'

''')

class MainApp(App):
    
    def build(self):
        root = Widget()
        MsgBox.question(text="Are you able to answer for this question?", title="hello world",
                        yes_callback=lambda: MsgBox.info(text='You said Yes'),
                        no_callback=lambda: MsgBox.info(text='You said No'),
                        )
        return root
        

if __name__ == '__main__':
    MainApp().run()
