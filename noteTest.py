from classNote import Note


def main():

	chromaticScale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
	noteList = []

	for element in chromaticScale:
		noteList.append(Note(element))

	scalesFile = open("primitiveMajorScales.txt", "w")

	scalesFile.write("INTERVALS\n")

	noteC = Note("C")

	scalesFile.write("%s -> \n" %noteC)
	scalesFile.write("1j: %s\n" %noteC.interval("1j"))
	scalesFile.write("2m: %s - 2M: %s\n" %(noteC.interval("2m"), noteC.interval("2M")))
	scalesFile.write("3m: %s - 3M: %s\n" % (noteC.interval("3m"), noteC.interval("3M")))
	scalesFile.write("4j: %s\n" % noteC.interval("4j"))
	scalesFile.write("5j: %s\n" % noteC.interval("5j"))
	scalesFile.write("6m: %s - 6M: %s\n" % (noteC.interval("6m"), noteC.interval("6M")))
	scalesFile.write("7m: %s - 7M: %s\n" % (noteC.interval("7m"), noteC.interval("7M")))
	scalesFile.write("8j: %s\n" % noteC.interval("8j"))


	noteG = Note("G")

	scalesFile.write("%s -> \n" %noteG)
	scalesFile.write("1j: %s\n" %noteG.interval("1j"))
	scalesFile.write("2m: %s - 2M: %s\n" %(noteG.interval("2m"), noteG.interval("2M")))
	scalesFile.write("3m: %s - 3M: %s\n" % (noteG.interval("3m"), noteG.interval("3M")))
	scalesFile.write("4j: %s\n" % noteG.interval("4j"))
	scalesFile.write("5j: %s\n" % noteG.interval("5j"))
	scalesFile.write("6m: %s - 6M: %s\n" % (noteG.interval("6m"), noteG.interval("6M")))
	scalesFile.write("7m: %s - 7M: %s\n" % (noteG.interval("7m"), noteG.interval("7M")))
	scalesFile.write("8j: %s\n" % noteG.interval("8j"))















if __name__ == '__main__':
	main()