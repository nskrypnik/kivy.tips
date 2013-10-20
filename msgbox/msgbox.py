
from kivy.app import App
from kivy.lang import Builder
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window
from kivy.properties import ListProperty, NumericProperty, StringProperty,\
                            ObjectProperty, BooleanProperty
from kivy.uix.button import Button

Builder.load_string('''
#place kivy notation of app here

<MsgBox_Separator>:
    size_hint: 1, None
    size: 0, '4dp'
    canvas:
        Color:
            rgba: self.separator_color
        Rectangle:
            size: self.size[0], self.size[1]/2.
            pos: self.pos
            
<MsgBox_Title>:
    size_hint: 1, 0.1
            
<MsgBox_Text>:
    size_hint: 1, 1
    
<MsgBox_ButtonsBar>:
    size_hint: 1, 0.5
''')


class MsgBox(ModalView):
    
    type = StringProperty('info')
    title = StringProperty('')
    text = StringProperty('')
    font_size = ObjectProperty('14dp')
    content_padding = ObjectProperty('10dp')
    buttons_padding = ObjectProperty('10dp')
    
    class MsgBox_Title(Label):
        def __init__(self, *args, **kw):
            kw.setdefault('halign', 'left')
            kw.setdefault('valign', 'middle')
            super(MsgBox.MsgBox_Title, self).__init__(*args, **kw)
            self.bind(size=self.setter('text_size'))
    
    class MsgBox_Text(Label):
        
        def __init__(self, *args, **kw):
            kw.setdefault('halign', 'center')
            kw.setdefault('valign', 'middle')
            kw.setdefault('size_hint', (1, 0.6))
            super(MsgBox.MsgBox_Text, self).__init__(*args, **kw)
            self.bind(size=self.setter('text_size'))
            
    class MsgBox_Button(Button):
        
        type = StringProperty('')
    
    class MsgBox_Separator(Widget):
        
        separator_color = ListProperty([47 / 255., 167 / 255., 212 / 255., 1.])
    
    
    class MsgBox_ButtonsBar(BoxLayout):
        pass
    
    def __init__(self, *args, **kw):
        self.title_widget = None
        self.text_widget = None
        self.separator = None
        self.yes_button = None
        self.no_button = None
        
        self._callbacks = {
                      'ok': kw.pop('ok_callback', None),
                      'yes': kw.pop('yes_callback', None),
                      'no': kw.pop('no_callback', None)}
        
        kw.setdefault('size_hint', (0.5, 0.5))
        kw.setdefault('autodismiss', False)
        super(MsgBox, self).__init__(*args, **kw)
        self.build_layout()
        
        #self.center = Window.center
        
    def build_layout(self):
        self.content = BoxLayout(orientation='vertical',
                                 padding=self.content_padding)
        # build the title
        if self.title:
            self.title_widget = self.MsgBox_Title(text=self.title, font_size=self.font_size)
            self.content.add_widget(self.title_widget)
            self.separator = self.MsgBox_Separator()
            self.content.add_widget(self.separator)
            
        self.text_widget = self.MsgBox_Text(text=self.text, font_size=self.font_size)
        self.content.add_widget(self.text_widget)
        
        self.button_bar = self.MsgBox_ButtonsBar(orientation='horizontal', 
                                    padding=self.buttons_padding,
                                    spacing=self.buttons_padding)
        # create buttons according to type of message box
        if self.type == 'info':
            self.ok_button = self.MsgBox_Button(text="OK", font_size=self.font_size, type='ok')
            self.button_bar.add_widget(self.ok_button)
            self.ok_button.bind(on_release=self.btn_release)
        if self.type == 'question':
            self.yes_button = self.MsgBox_Button(text="Yes", font_size=self.font_size, type='yes')
            self.no_button = self.MsgBox_Button(text="No", font_size=self.font_size, type='no')
            self.button_bar.add_widget(self.yes_button)
            self.button_bar.add_widget(self.no_button)
            self.yes_button.bind(on_release=self.btn_release)
            self.no_button.bind(on_release=self.btn_release)
        
        self.content.add_widget(self.button_bar)
        
        self.add_widget(self.content)
        
    def btn_release(self, btn):
        self.dismiss()
        callback = self._callbacks.get(btn.type)
        if callback:
            callback()
        

class MainApp(App):
    
    def build(self):
        msg = MsgBox(text="Are you able to answer for this question?")
        msg.open()
        return msg
        

if __name__ == '__main__':
    MainApp().run()