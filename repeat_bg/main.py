
from kivy.app import App
from kivy.lang import Builder
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget 
from kivy.uix.scatter import ScatterPlane
from kivy.graphics import Rectangle
from kivy.core.image import Image 

Builder.load_string('''
#place kivy notation of app here
''')


class RootWidget(ScatterPlane):
    
    def __init__(self, *args, **kw):
        super(RootWidget, self).__init__(*args, **kw)
        texture = Image('wood.png').texture
        texture.wrap = 'repeat'
        texture.uvsize = (8, 8)
        with self.canvas:
            Rectangle(size=(2048, 2048), texture=texture)


class MainApp(App):
    
    def build(self):
        root = RootWidget()
        return root
        

if __name__ == '__main__':
    MainApp().run()