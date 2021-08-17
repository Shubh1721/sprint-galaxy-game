from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    line=None
    def __init__(self, **kwargs):
        super(MainWidget,self).__init__(**kwargs)
        print("INIT W:"+str(self.width)+" H:"+str(self.height))
        self.init_vertical_lines()
    def on_parent(self, *args):
        pass 
    # to get window size dynamically
    def on_size(self, *args):
        # print("Size W:"+str(self.width)+" H:"+str(self.height))
        # self.perspective_point_x = self.width/2 # we can use similar in .kv file
        # self.perspective_point_y = self.height*0.75
        pass 

    def on_perspective_point_x(self, widget, value):
        # print("PX :"+str(value))
        pass
    def on_perspective_point_y(self, widget, value):
        # print("PY:"+str(value))
        pass
