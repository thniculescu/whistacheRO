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
	sID: [_s1_, _s2_, _s3_, _s4_, _s5_, _s6_]
	trkID: [_trk1_, _trk2_, _trk3_, _trk4_, _trk5_, _trk6_]
	bID: [_b0_, _b1_, _b2_, _b3_, _b4_, _b5_, _b6_, _b7_, _b8_]
	playerup: _id_player_up
	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			orientation: 'horizontal'
			size_hint_y: 1
			Label:
				id: _id_player_up
				font_size: 20
				text: 'nicualwayswins'
				size_hint_x: 2
			Button:
				text: 'Undo'
				id: _undo_
				font_size: 30
				size_hint_x: 1
		BoxLayout:
			orientation: 'horizontal'
			size_hint_y: 1
			Label:
				text: 'Game of:'
				size_hint_x: 2
			Label:
				id: _gameof_
				text: '-'
				size_hint_x: 2
			Label:
				text: 'Bids untill now:'
				size_hint_x: 3
			Label:
				id: _buntinow_
				text: '-'
				size_hint_x: 1

		GridLayout:
			cols: 3
			size_hint_y: 10
			Button:
				text:'0'
				font_size: 80
				id: _b0_
			Button:
				font_size: 80
				text:'1'
				id: _b1_
			Button:
				font_size: 80
				text:'2'
				id: _b2_
			Button:
				font_size: 80
				text:'3'
				id: _b3_
			Button:
				font_size: 80
				text:'4'
				id: _b4_
			Button:
				font_size: 80
				text:'5'
				id: _b5_
			Button:
				font_size: 80
				text:'6'
				id: _b6_
			Button:
				font_size: 80
				text:'7'
				id: _b7_
			Button:
				font_size: 80
				text:'8'
				id: _b8_

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
				id: _s1_
				text: 'scor1'
			Label:
				id: _trk1_
				text: 'strk1'
		BoxLayout:
			orientation: 'horizontal'
			Label:
				id: _p2_
				text: 'gay2'
			Label:
				id: _s2_
				text: 'scor2'
			Label:
				id: _trk2_
				text: 'strk2'
		BoxLayout:
			orientation: 'horizontal'
			Label:
				id: _p3_
				text: 'gay3'
			Label:
				id: _s3_
				text: 'scor3'
			Label:
				id: _trk3_
				text: 'strk3'
		BoxLayout:
			orientation: 'horizontal'
			Label:
				id: _p4_
				text: 'gay4'
			Label:
				id: _s4_
				text: 'scor4'
			Label:
				id: _trk4_
				text: 'strk4'
		BoxLayout:
			orientation: 'horizontal'
			Label:
				id: _p5_
				text: 'gay5'
			Label:
				id: _s5_
				text: 'scor5'
			Label:
				id: _trk5_
				text: 'strk5'
		BoxLayout:
			orientation: 'horizontal'
			Label:
				id: _p6_
				text: 'gay6'
			Label:
				id: _s6_
				text: 'scor6'
			Label:
				id: _trk6_
				text: 'strk6'
''')

butoane = [0, 0, 0, 0, 0, 0]
tin = [0, 0, 0, 0, 0, 0]
scor = [0, 0, 0, 0, 0, 0]
streak = [0, 0, 0, 0, 0, 0]
licitate = [-1, -1, -1, -1, -1, -1]
ture = 0
tcur = 0
gameof = []
playerof = []
totolit = 0
totomade = 0

grey = 0

cbutoane = [0, 0, 0, 0, 0, 0]
ctin = [0, 0, 0, 0, 0, 0]
cscor = [0, 0, 0, 0, 0, 0]
cstreak = [0, 0, 0, 0, 0, 0]
clicitate = [-1, -1, -1, -1, -1, -1]
cture = 0
ctcur = 0
ctotolit = 0
ctotomade = 0


class Tinput(TextInput):
#def chfocus(self, parent, i):
	def chfocus(self, tin, poz):
		#global tin
		tin = tin[0]
		if poz < 5:
			tin[poz + 1].focus = True


class Pagina(PageLayout):
#def setNames(self):
   #for i in range(self.numPlayer):
	   #self.pID[i].text = self.playerNames[i]


	def schimbaAfis(self):
		global tcur
		global gameof
		global ture
		global totolit
		global scor
		global licitate
		global streak
		if(tcur == ture):
			winners = ''
			maxim = 0
			winners = self.pID[0].text
			for i in range(1, self.numPlayer):
				if scor[i] > scor[maxim]:
					maxim = i
					winners = self.pID[i].text
					ding = ' wins!!'
				elif scor[i] == scor[maxim]:
					winners += ' and ' + self.pID[i].text
					ding = ' win!!'
			self.playerup.text = winners + ding
			return
		else:
			if(tcur % (self.numPlayer * 2) == 0):
				for i in range(9):
					self.bID[i].disabled = False
				for i in range(int(gameof[tcur / (self.numPlayer * 2)][0]) + 1, 9):
					self.bID[i].disabled = True
					
			self.ids._buntinow_.text = str(totolit)
			self.ids._gameof_.text = str(gameof[tcur / (self.numPlayer * 2)])
			prefi = tcur / self.numPlayer
			if(prefi % 2 == 0):
				self.playerup.text = self.playerNames[(tcur % self.numPlayer + (tcur / (2 * self.numPlayer))) % self.numPlayer] + ' bids'
			else:
				self.playerup.text = self.playerNames[(tcur % self.numPlayer + (tcur / (2 * self.numPlayer))) % self.numPlayer] + ' made'

	def update(self):
		global scor, streak, cscor, cstreak, ctotolit, totolit, licitate, clicitate, ctcur, tcur, totomade
		for i in range(self.numPlayer):
			self.sID[i].text = str(scor[i])
			self.trkID[i].text = str(streak[i])
		
	def savestate(self):
		global scor, streak, cscor, cstreak, ctotolit, totolit, licitate, clicitate, ctcur, tcur, totomade
		for i in range(self.numPlayer):
			cscor[i] = scor[i]
			cstreak[i] = streak[i]
			clicitate[i] = licitate[i]	
		ctcur = tcur
		ctotolit = totolit
		ctotomade = totomade

	def onundo(self):
		global scor, streak, cscor, cstreak, ctotolit, totolit, licitate, clicitate, ctcur, tcur, totomade
		for i in range(self.numPlayer):
			scor[i] = cscor[i]
			streak[i] = cstreak[i]
			licitate[i] = clicitate[i]
		#print 'tcur = %s ctcur = %s' % (tcur, ctcur)
		tcur = ctcur
		
		totolit = ctotolit
		totomade = ctotomade
		#print 'UNDO BA'
		self.update()
		self.schimbaAfis()
			
	def lici(self, nrb):
		global licitate, scor, streak, totolit, tcur, totomade, gameof, grey
		curpl = (tcur % self.numPlayer + (tcur / (2 * self.numPlayer))) % self.numPlayer
		rund = tcur % (self.numPlayer * 2)
		joc = int(gameof[tcur / (self.numPlayer * 2)][0])
		self.savestate()
		if rund < self.numPlayer:
			totomade = 0
			joc = int(gameof[tcur / (self.numPlayer * 2)][0])
			
			if tcur % self.numPlayer == self.numPlayer - 1:
				if totolit <= joc:
					self.bID[joc - totolit].disabled = False

			licitate[curpl] = nrb
			totolit += nrb
			
			if tcur % self.numPlayer == self.numPlayer - 2:
				if totolit <= joc:
					self.bID[joc - totolit].disabled = True	
					
		else:
			
			if tcur % self.numPlayer == self.numPlayer - 1:
				if totomade <= joc:
					self.bID[joc - totomade].background_color = grey
					self.bID[joc - totomade].color = (1, 1, 1, 1)
				
			totomade += nrb
			totolit = 0
			if licitate[curpl] == nrb:
				scor[curpl] += 5 + nrb
				if streak[curpl] < 0:
					streak[curpl] = 0
				streak[curpl] += 1
			else:
				scor[curpl] -= abs(nrb - licitate[curpl])
				if streak[curpl] > 0:
					streak[curpl] = 0
				streak[curpl] -= 1

			if abs(streak[curpl]) == 5:
				scor[curpl] += streak[curpl] * 2
				streak[curpl] = 0
			
			if tcur % self.numPlayer == self.numPlayer - 2:
				if totomade <= joc:
					grey = self.bID[joc - totomade].background_color
					self.bID[joc - totomade].background_color = (0, 255, 0, 255)
					self.bID[joc - totomade].color = (0, 0, 0, 1)
			
			
			
		self.update()
		tcur += 1
		self.schimbaAfis()
		
	def scotpopup(self, pp, bb, tt):
		global gameof
		global ture
		global tcur
		if bb.text[0] != 'N':
			self.numPlayer = int(bb.text[0])
			ture = (self.numPlayer * 3 + 12) * self.numPlayer * 2
			tcur = 0
			#print ture
			for i in range(self.numPlayer * 3 + 12):
				playerof.append(i % self.numPlayer)
				#print playerof[i]
			for i in range(self.numPlayer):
				gameof.append('1.' + str(i))
			for i in range(2, 8):
				gameof.append(str(i))
			for i in range(self.numPlayer):
				gameof.append('8.' + str(i))
			for i in range(-7, -1):
				gameof.append(str(-i))
			for i in range(self.numPlayer):
				gameof.append('1.' + str(i))


			for i in range(self.numPlayer):
				#print tt[i].text
				#print self.playerNames[i]
				self.pID[i].text = tt[i].text
				self.playerNames[i] = tt[i].text
				#print self.playerNames[i] + 'dupa'
				pp.dismiss()
			for i in range(self.numPlayer, 6):
				self.pID[i].text = ''
				self.sID[i].text = ''
				self.trkID[i].text = ''
			
			self.schimbaAfis()

	def getNames(self):
		global tin

		droptop = DropDown(height = 80, width = 10)
		gigi = BoxLayout()
		gigi.orientation = 'vertical'
		popup = Popup(title='New Game',
					  content=gigi,
					  auto_dismiss=False)


		dropbut = Button(text = 'Number of players:', font_size = 20, size_hint=(1, 1))
		for i in range(2, 6):
			butoane[i] = Button(text = '%s Players' % (i + 1), size_hint_y=None, height_hint = 1, font_size = 20)
			butoane[i].bind(on_release=lambda btn: droptop.select(btn.text))
			droptop.add_widget(butoane[i])


		dropbut.bind(on_release = droptop.open)
		#droptop.bind(on_select=lambda instance, x: setattr(dropbut, 'text', x))
		droptop.bind(on_select=lambda instance, x: setattr(dropbut, 'text', x))
		gigi.add_widget(dropbut)




		b1 = Button(text='OK', font_size = 40)
		#b1.on_press=popup.dismiss
		b1.bind(on_release = lambda instance: self.scotpopup(popup, dropbut, tin))
		#b1.bind(on_press = lambda instance: popup.dismiss())

		#b1.on_press = self.scotpopup(popup, dropbut)
		b2 =  Label(text = 'girl from ipanema')
		gigi.add_widget(b1)


		for i in range(6):
			tin[i] = Tinput(text = '', hint_text = 'Player %s' % (i + 1), multiline = False, font_size = 40)
			#tin[i].inend(tin[i], self, i)
			tinref = [tin]
			#j = i
			#tin[i].on_text_validate = lambda: tin[i].chfocus(tinref, j)
			gigi.add_widget(tin[i])

		tin[0].on_text_validate = lambda: tin[i].chfocus(tinref, 0)
		tin[1].on_text_validate = lambda: tin[i].chfocus(tinref, 1)
		tin[2].on_text_validate = lambda: tin[i].chfocus(tinref, 2)
		tin[3].on_text_validate = lambda: tin[i].chfocus(tinref, 3)
		tin[4].on_text_validate = lambda: tin[i].chfocus(tinref, 4)
		tin[5].on_text_validate = lambda: tin[i].chfocus(tinref, 5)
		#for i in range(6)

		popup.open()


class ScreenManagerApp(App):
	global ture
	global tcur
	global gameof

	def build(self):
		self.principala = Pagina()
		return self.principala


	def on_start(self):
		self.principala.getNames()

		self.principala.bID[0].on_release = lambda: self.principala.lici(0)
		self.principala.bID[1].on_release = lambda: self.principala.lici(1)
		self.principala.bID[2].on_release = lambda: self.principala.lici(2)
		self.principala.bID[3].on_release = lambda: self.principala.lici(3)
		self.principala.bID[4].on_release = lambda: self.principala.lici(4)
		self.principala.bID[5].on_release = lambda: self.principala.lici(5)
		self.principala.bID[6].on_release = lambda: self.principala.lici(6)
		self.principala.bID[7].on_release = lambda: self.principala.lici(7)
		self.principala.bID[8].on_release = lambda: self.principala.lici(8)
		self.principala.ids._undo_.on_release = lambda : self.principala.onundo()


ScreenManagerApp().run()


#if __name__ == '__main__':
#   runTouchApp(Builder.load_string(kv))
