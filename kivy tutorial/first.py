import kivy
from kivy.app import App 
#kivy.require("1.10.0")

from kivy.uix.label import Label

class KivyClass(App):
	def build(self):
		return Label(text="HElLo WOrlD!!")
KivyClass().run()		