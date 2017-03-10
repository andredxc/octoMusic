from classNote import Note


def main():

	chromaticScale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
	noteList = []

	for element in chromaticScale:
		noteList.append(Note(element))

	noteList.append(Note("B"))

	for element in noteList:
		print("main() - ", element)

	for element in noteList:
		print("main() - halfStep(%s) -> %s" %(element, element.wholeStep()))










if __name__ == '__main__':
	main()