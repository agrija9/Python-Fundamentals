'''
OOP Project to schedule dr. appointments. Program verifies if both patient and doctor are available any given date.
'''

class Person(object): # shared between doctor & patient
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.full_name = self.first_name + " " + self.last_name
		self.calendar = Calendar() # shared class for dr & patient

	def is_available(self, slot):
		return self.calendar.is_available(slot)

	def make_appointment(self, slot, record):
		return self.calendar.add_entry(slot, record)

	def get_public_record(self): # check this one
		return{
			'name': self.full_name,
			'booking_class': self.__class__.__name__

		}

#class Patient(object):
	#def __init__(self, )

class Calendar(object):
	def __init__(self):
		self.entries = {} # appointments

	def is_available(self, slot):
		return slot not in self.entries # slot is the date

	def add_entry(self, slot, record):
		if not self.is_available(slot): # case not available date
			raise DoubleBookingException # create own exception
		self.entries[slot] = record

	def __str__(self):
		return str(self.entries)

class DoubleBookingException(exception):
	pass







