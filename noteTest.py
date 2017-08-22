from classNote import Note


def main():

	chromaticScale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
	noteList = []

	for element in chromaticScale:
		noteList.append(Note(element))

	scalesFile = open("primitiveMajorScales.txt", "w")

	scalesFile.write("INTERVALS\n")

	for element in noteList:
		scalesFile.write("%s 1p -> %s\n" %())














if __name__ == '__main__':
	main()