from classNote import Note

class Chord(object):
	"""
	Represents a chord

	Attributes:
	_name -> string
	_notes -> list containing Notes(object)

	"""
	def __init__(self, note):
		#'note' can be either a string or a classNote.Note
		if type(note) == str:
			self._notes = [Note(note)]

		elif isinstance(note, Note):
			self._notes = [note]

		else:
			print("Parameter \'note\' can't be a %s" %type(note))
			raise TypeError

	def __repr__(self):

		return "Chord %s" %self._notes

	# -----------------------------------------------------------------------------------------PRIVATE FUNCTIONS

	# -----------------------------------------------------------------------------------------PUBLIC FUNCTIONS
	def addNote(self, note):
		#'note' can be either a string or a classNote.Note
		if type(note) == str:
			self._notes.append(Note(note))

		elif isinstance(note, Note):
			self._notes.append(note)

		else:
			print("Parameter \'note\' can't be a %s" %type(note))
			raise TypeError
			return False

		return True

	def removeNote(self, note):
		#'note' can be either a string or a classNote.Note
		if type(note) == str:
			self._notes.remove(Note(note))

		elif isinstance(note, Note):
			self._notes.remove(note)

		else:
			print("Parameter \'note\' can't be a %s" %type(note))
			raise TypeError
			return False

		return True



