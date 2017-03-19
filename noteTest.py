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

	testChord = Chord(noteC)
	print("1 chord: ", testChord)

	testChord.addNote(noteG)
	print("2 chord: ", testChord)
	testChord.addNote(noteE)
	print("3 chord: ", testChord)
	testChord.removeNote("E")
	print("4 chord: ", testChord)















if __name__ == '__main__':
	main()