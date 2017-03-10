import re

class Note(object):

	"""
	Represents a simple note

	Attributes:
		_note -> string
		_index -> index of note in the chromatic scale
		_octave -> octave of the given note
	"""

	def __init__(self, note:str):

		validNote = True

		#Choecks notation of notes
		noteSearch = re.search("^([a-gA-G)])(#)?([1-8])?$", note)

		if self.validateNote(noteSearch):
			#Note matches the correct notation
			if noteSearch.group(2) == "#":
				#Sharp note
				self._note = noteSearch.group(1).upper() + noteSearch.group(2)
			else:
				#Flat note
				self._note = noteSearch.group(1).upper()

			#Finds the matching index
			self._setIndex()
			
			#Finds the octave
			if noteSearch.group(3) and re.search("^[1-8]$", noteSearch.group(3)):
				self._octave = int(noteSearch.group(3))
			elif noteSearch.group(2) and re.search("^[1-8]$", noteSearch.group(2)):
				self._octave = int(noteSearch.group(2))
			else:
				self._octave = 4

		else:
			#Doesn't match the correct notation
			print("Error, note doesn't match the correct notation")
			self._note = "?"
			self._noteIndex = -1
			self._octave = -1
			raise ValueError	


	def __repr__(self):

		return "Note %s, Index %d, Octave %d" %(self._note, self._index, self._octave)


	def _setIndex(self):

		"""
		Updates the index of self._note
		"""

		index = 0
		
		if len(self._note) == 2:
			index = 1

		if(self._note[0].upper() == "A"):
			self._index = index
		elif(self._note[0].upper() == "B"):
			self._index = index + 2
		elif(self._note[0].upper() == "C"):
			self._index = index + 3
		elif(self._note[0].upper() == "D"):
			self._index = index + 5
		elif(self._note[0].upper() == "E"):
			self._index = index + 7
		elif(self._note[0].upper() == "F"):
			self._index = index + 8
		elif(self._note[0].upper() == "G"):
			self._index = index + 10


	def _findNoteByIndex(self, index:int):

		"""
		Finds the note(string) corresponding to the index given
		"""

		if index > 11:
			index = index - 12

		if index == 0: 		return "A"
		elif index == 1: 	return "A#"
		elif index == 2:	return "B"
		elif index == 3:	return "C"
		elif index == 4:	return "C#"
		elif index == 5:	return "D"
		elif index == 6:	return "D#"
		elif index == 7:	return "E"
		elif index == 8:	return "F"
		elif index == 9:	return "F#"
		elif index == 10:	return "G"
		elif index == 11:	return "G#"


	def validateNote(self, noteSearch):

		if noteSearch:
			#Note matches the correct notation
			if noteSearch.group(2) == "#":
				#Sharp note
				if noteSearch.group(1).upper() == "B" or noteSearch.group(1).upper() == "E":
					return False
				else:
					return True
		else:
			return False

		return True


	def halfStep(self):
		"""Takes a half step from _note"""
		return self._findNoteByIndex(self._index+1)


	def wholeStep(self):
		"""Takes a whole step from _note"""
		return self._findNoteByIndex(self._index+2)

	@property
	def note(self):
		return self._note



"""
TODO: 
	
	- Create @note.setter
	- Integration with GitHub

"""