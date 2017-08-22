from classNote import Note
from classChord import Chord


def main():

	chromaticScale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
	noteList = []

	for element in chromaticScale:
		noteList.append(Note(element))

	noteC = Note("C")
	noteG = Note("G")
	noteE = Note("E")

<<<<<<< HEAD
	scalesFile.write("INTERVALS\n")

	for element in noteList:
		scalesFile.write("%s 1p -> %s\n" %())

=======
	testChord = Chord(noteC)
	print("1 chord: ", testChord)

	testChord.addNote(noteG)
	print("2 chord: ", testChord)
	testChord.addNote(noteE)
	print("3 chord: ", testChord)
	testChord.removeNote("E")
	print("4 chord: ", testChord)


>>>>>>> 751acaa36c5b9a5e3cdb1993ff8560d8df4ba418













if __name__ == '__main__':
	main()