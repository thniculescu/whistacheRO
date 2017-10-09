from kivy.base import runTouchApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.pagelayout import PageLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
import time
from datetime import datetime

Builder.load_string('''
<Pagina>:
    playerup: _id_player_up
    apas: _de_apasat_
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: 1
            Label:
                id: _id_player_up
                text: 'toplay'
                font_size: 40
                size_hint_x: 2
            Button:
                text: 'Undo'
                font_size: 30
                size_hint_x: 1
        GridLayout:
            cols: 3
            size_hint_y: 10
            Button:
                id: _de_apasat_
                text:'0'
            Button:
                text:'1'
            Button:
                text:'2'
            Button:
                text:'3'
            Button:
                text:'4'
            Button:
                text:'5'
            Button:
                text:'6'
            Button:
                text:'7'
            Button:
                text:'8'

    BoxLayout:
        canvas:
            Color:
                rgba: 0/255., 8/255., 57/255., 1
            Rectangle:
                pos: self.pos
                size: self.size

        orientation: 'vertical'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'gay1'
            Label:
                text: 'scor1'
            Label:
                text: 'strk1'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'gay2'
            Label:
                text: 'scor2'
            Label:
                text: 'strk2'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'gay3'
            Label:
                text: 'scor3'
            Label:
                text: 'strk3'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'gay4'
            Label:
                text: 'scor4'
            Label:
                text: 'strk4'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'gay5'
            Label:
                text: 'scor5'
            Label:
                text: 'strk5'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                text: 'gay6'
            Label:
                text: 'scor6'
            Label:
                text: 'strk6'
''')


class Pagina(PageLayout):
    def schimba(self):
        self.playerup.text = 'ESTI GAY BAAA!!!'
        

    
class ScreenManagerApp(App):

    def build(self):
        self.principala = Pagina()
        return self.principala

    def on_start(self):
        self.principala.ids._de_apasat_.on_press = self.principala.schimba


ScreenManagerApp().run()


#if __name__ == '__main__':
 #   runTouchApp(Builder.load_string(kv))
