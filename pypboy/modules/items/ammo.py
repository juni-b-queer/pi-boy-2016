import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

	label = "Ammo"

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		self.menu = pypboy.ui.Menu(100, ["STAY ON", "TURN OFF"], [self.show_On, self.show_Off], 0)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		self.add(self.menu)
		
	def handle_resume(self):
		self.parent.pypboy.header.headline = "ITEMS"
		self.parent.pypboy.header.title = " TURN OFF "
		super(Module, self).handle_resume()
		
	def show_On(self):
		print "On"

	def show_Off(self):
		pygame.mixer.quit()
