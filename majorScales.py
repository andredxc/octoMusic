from abjad import *

chromaticScale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

def singleStep():

def halfStep():

def createMajor(note):

	"""
	Returns the major scale of the specified note

	Format of the major scale:
	I   II   III     IV   V   VI   VII     VIII
      1    1	 1/2    1   1    1     1/2

	"""

	if not(type(note) == string):

		print("%s is not a string" %note)
		return false

	for index, chromaticNote in enumerate(chromaticScale):
		
		print("Index: %d, Note: %d" %(index, note))

		if note.upper() == chromaticNote:

			noteIndex = index

	majorScale.append(chromaticScale[index])
	majorScale.appen(chromaticScale[index + ])
		




if __name__ == '__main__':
	
	createMajor()