from classNote import Note


def main():

	chromaticScale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
	noteList = []

	for element in chromaticScale:
		noteList.append(Note(element))

	scalesFile = open("primitiveMajorScales.txt", "w")

	scalesFile.write("HARMONIC MAJOR SCALE\n")

	#HARMONIC MAJOR
	for note in noteList:

		majorScaleIter = note.harmonicMajorScale()
		scalesFile.write("\n%s -> " % note)
		for element in majorScaleIter:
			scalesFile.write("%s, " % element)

	scalesFile.write("PRIMITIVE MINOR SCALE\n")

	#PRIMITIVE MINOR
	for note in noteList:

		majorScaleIter = note.primitiveMinorScale()
		scalesFile.write("\n%s -> " % note)
		for element in majorScaleIter:
			scalesFile.write("%s, " % element)

	scalesFile.write("HARMONIC MAJOR SCALE\n")

	#HARMONIC MINOR
	for note in noteList:

		majorScaleIter = note.harmonicMinorScale()
		scalesFile.write("\n%s -> " % note)
		for element in majorScaleIter:
			scalesFile.write("%s, " % element)













if __name__ == '__main__':
	main()