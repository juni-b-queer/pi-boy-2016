import pypboy
import config

from pypboy.modules.data import entities

class Module(pypboy.SubModule):

	label = "Radio"

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		self.stations = [
			entities.GalaxyNewsRadio(), entities.RadioNewVegas(), entities.DiamondCityRadio(), entities.PopRadio()
		]
		for station in self.stations:
			self.add(station)
		self.active_station = None
		config.radio = self
		self.menu = pypboy.ui.Menu(170, ["Galaxy News Radio", "Radio New Vegas", "Diamond City Radio", "Pop Radio"], [self.show_gnr, self.show_rnv, self.show_dcr, self.show_pop], 0)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 50
		self.add(self.menu)

	def handle_resume(self):
		self.parent.pypboy.header.headline = "DATA"
		self.parent.pypboy.header.title = " RADIO STATIONS "
		super(Module, self).handle_resume()

	def show_gnr(self):
		self.select_station(0)
		print "Galaxy News Radio"

	def show_rnv(self):
		self.select_station(1)
		print "Radio New Vegas"

	def show_dcr(self):
		self.select_station(2)
		print "Diamond City Radio"
		
	def show_pop(self):
		self.select_station(3)
		print "Pop Radio"
		


		

	def select_station(self, station):
		if hasattr(self, 'active_station') and self.active_station:
			self.active_station.stop()
		self.active_station = self.stations[station]
		self.active_station.play_random()


	def handle_event(self, event):
		if event.type == config.EVENTS['SONG_END']:
			if hasattr(self, 'active_station') and self.active_station:
				self.active_station.play_random()
