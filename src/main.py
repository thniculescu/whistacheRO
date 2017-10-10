from kivy.base import runTouchApp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.pagelayout import PageLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
import time
from datetime import datetime
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput


Builder.load_string('''
<Pagina>:
    numPlayer: 6
    playerNames: ['-', '-', '-', '-', '-', '-']
    pID: [_p1_, _p2_, _p3_, _p4_, _p5_, _p6_]
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
                id: _p1_
                text: 'gay1'
            Label:
                text: 'scor1'
            Label:
                text: 'strk1'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                id: _p2_
                text: 'gay2'
            Label:
                text: 'scor2'
            Label:
                text: 'strk2'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                id: _p3_
                text: 'gay3'
            Label:
                text: 'scor3'
            Label:
                text: 'strk3'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                id: _p4_
                text: 'gay4'
            Label:
                text: 'scor4'
            Label:
                text: 'strk4'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                id: _p5_
                text: 'gay5'
            Label:
                text: 'scor5'
            Label:
                text: 'strk5'
        BoxLayout:
            orientation: 'horizontal'
            Label:
                id: _p6_
                text: 'gay6'
            Label:
                text: 'scor6'
            Label:
                text: 'strk6'
''')

butoane = [0, 0, 0, 0, 0, 0]
tin = [0, 0, 0, 0, 0, 0]


class Pagina(PageLayout):
    #def setNames(self):
       #for i in range(self.numPlayer):
           #self.pID[i].text = self.playerNames[i]

    def schimba(self):
        self.playerup.text = 'ESTI GAY BAAA!!!'

    def scotpopup(self, pp, bb, tt):
        if bb.text[0] != 'N':
            self.numPlayer = int(bb.text[0])
            for i in range(self.numPlayer):
                #print tt[i].text
                #print self.playerNames[i]
                self.pID[i].text = tt[i].text
                #print self.playerNames[i] + 'dupa'
                pp.dismiss()




    def getNames(self):

        droptop = DropDown(height = 44, width = 10)
        gigi = BoxLayout()
        gigi.orientation = 'vertical'
        popup = Popup(title='New Game',
                      content=gigi,
                      auto_dismiss=False)


        dropbut = Button(text = 'Number of players:', size_hint=(1, 1))
        for i in range(2, 6):
            butoane[i] = Button(text = '%s Players' % (i + 1), size_hint_y=None, height = 50)
            butoane[i].bind(on_release=lambda btn: droptop.select(btn.text))
            droptop.add_widget(butoane[i])


        dropbut.bind(on_release = droptop.open)
        #droptop.bind(on_select=lambda instance, x: setattr(dropbut, 'text', x))
        droptop.bind(on_select=lambda instance, x: setattr(dropbut, 'text', x))
        gigi.add_widget(dropbut)




        b1 = Button(text='OK')
        #b1.on_press=popup.dismiss
        b1.bind(on_release = lambda instance: self.scotpopup(popup, dropbut, tin))
        #b1.bind(on_press = lambda instance: popup.dismiss())

        #b1.on_press = self.scotpopup(popup, dropbut)
        b2 =  Label(text = 'girl from ipanema')
        gigi.add_widget(b1)
        gigi.add_widget(b2)


        for i in range(6):
            tin[i] = TextInput(multiline = False)
            gigi.add_widget(tin[i])

        popup.open()


class ScreenManagerApp(App):

    def build(self):
        self.principala = Pagina()
        return self.principala

    def on_start(self):
        self.principala.getNames()
        self.principala.ids._de_apasat_.on_press = self.principala.schimba


ScreenManagerApp().run()


#if __name__ == '__main__':
 #   runTouchApp(Builder.load_string(kv))
