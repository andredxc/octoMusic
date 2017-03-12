import re


class Note(object):
    """
	Represents a simple note

	Attributes:
		_note -> string
		_index -> index of note in the chromatic scale
		_octave -> octave of the given note
	"""

    # -----------------------------------------------------------------------------------------PRIVATE FUNCTIONS
    def __init__(self, note: str):

        # Choecks notation of notes
        noteSearch = re.search("^([a-gA-G)])(#)?([1-8])?$", note)

        if self._validateNote(noteSearch):
            # Note matches the correct notation
            if noteSearch.group(2) == "#":
                # Sharp note
                self._note = noteSearch.group(1).upper() + noteSearch.group(2)
            else:
                # Flat note
                self._note = noteSearch.group(1).upper()

            # Finds the matching index
            self._setIndex()

            # Finds the octave
            if noteSearch.group(3) and re.search("^[1-8]$", noteSearch.group(3)):
                self._octave = int(noteSearch.group(3))
            elif noteSearch.group(2) and re.search("^[1-8]$", noteSearch.group(2)):
                self._octave = int(noteSearch.group(2))
            else:
                self._octave = 4

        else:
            # Doesn't match the correct notation
            print("Error, note doesn't match the correct notation")
            self._note = "?"
            self._noteIndex = -1
            self._octave = -1
            raise ValueError

    def __repr__(self):

        return "Note %s, Index %d, Octave %d" % (self._note, self._index, self._octave)

    def _setIndex(self):

        """
		Updates the index of self._note
		"""

        index = 0

        if len(self._note) == 2:
            index = 1

        if self._note[0].upper() == "A":
            self._index = index
        elif self._note[0].upper() == "B":
            self._index = index + 2
        elif self._note[0].upper() == "C":
            self._index = index + 3
        elif self._note[0].upper() == "D":
            self._index = index + 5
        elif self._note[0].upper() == "E":
            self._index = index + 7
        elif self._note[0].upper() == "F":
            self._index = index + 8
        elif self._note[0].upper() == "G":
            self._index = index + 10

    @staticmethod
    def _findNoteByIndex(index: int):

        """
		Finds the note(string) corresponding to the index given
		"""

        if index > 11:
            index -= 12

        if index == 0:
            return "A"
        elif index == 1:
            return "A#"
        elif index == 2:
            return "B"
        elif index == 3:
            return "C"
        elif index == 4:
            return "C#"
        elif index == 5:
            return "D"
        elif index == 6:
            return "D#"
        elif index == 7:
            return "E"
        elif index == 8:
            return "F"
        elif index == 9:
            return "F#"
        elif index == 10:
            return "G"
        elif index == 11:
            return "G#"

    @staticmethod
    def _validateNote(noteSearch):
        """
        Validates a note according to the notation <note><sharp?><octave?>
        """
        if noteSearch:
            # Note matches the correct notation
            if noteSearch.group(2) == "#":
                # Sharp note
                if noteSearch.group(1).upper() == "B" or noteSearch.group(1).upper() == "E":
                    return False
                else:
                    return True
        else:
            return False

        return True

    @staticmethod
    def _validateInterval(intervalSearch):
        """
        Validates a note according to the notation <number><perfect, minor or major>
        """
        if intervalSearch:
            #Interval matches the correct notation
            if intervalSearch.group(1) == "1" or intervalSearch.group(1) == "4" or intervalSearch.group(1) == "5" or intervalSearch.group(1) == "8":
                #Perfect intervals
                if intervalSearch.group(2) == "p":
                    return True
                else:
                    return False
            else:
                #Minor or major intervals
                if intervalSearch.group(2) == "m" or intervalSearch.group(2) == "M":
                    return True
                else:
                    return False
        else:
            return False

    # -----------------------------------------------------------------------------------------PUBLIC FUNCTIONS
    def halfStep(self, stepCount: int):
        """Takes a half step from self._note"""
        if self._note == "G#":
            self._octave += 1
        return self._findNoteByIndex(self._index + stepCount * 1)

    def wholeStep(self, stepCount: int):
        """Takes a whole step from self._note"""
        if self._note == "G":
            self._octave += 1
        return self._findNoteByIndex(self._index + stepCount * 2)

    def primitiveMajorScale(self):
        """
		Returns a list containing the primitive major scale of self._note
		I   II   III     IV   V   VI   VII     VIII
		  1    1     1/2    1   1    1     1/2
		"""
        majorScale = [self._note]

        for count in range(1, 8):
            if count == 3 or count == 7:
                #Takes a halfstep from the last element
                majorScale.append(Note(majorScale[len(majorScale)-1]).halfStep(1))
            else:
                #Takes a wholestep from the last element
                majorScale.append(Note(majorScale[len(majorScale)-1]).wholeStep(1))

        return majorScale

    def harmonicMajorScale(self):
        """
        Returns a list containing the harmonic major scale of self._note
        I   II   III     IV   V   VI     VII     VIII
          1    1     1/2    1   1    1/2     1/2
        """
        majorScale = [self._note]

        for count in range(1, 8):
            if count == 3 or count == 6 or count == 7:
                # Takes a halfstep from the last element
                majorScale.append(Note(majorScale[len(majorScale) - 1]).halfStep(1))
            else:
                # Takes a wholestep from the last element
                majorScale.append(Note(majorScale[len(majorScale) - 1]).wholeStep(1))

        return majorScale

    def primitiveMinorScale(self):
        """
        Returns a list containing the primitive minor scale of self._note
        I   II     III   IV   V     VI   VII   VIII
          1    1/2     1    1   1/2    1     1
        """
        minorScale = [self._note]

        for count in range(1, 8):
            if count == 2 or count == 5:
                # Takes a halfstep from the last element
                minorScale.append(Note(minorScale[len(minorScale) - 1]).halfStep(1))
            else:
                # Takes a wholestep from the last element
                minorScale.append(Note(minorScale[len(minorScale) - 1]).wholeStep(1))

        return minorScale

    def harmonicMinorScale(self):
        """
        Returns a list containing the harmonic minor scale of self._note
        I   II     III   IV   V     VI     VII     VIII
          1    1/2     1    1   1/2    3/2     1/2
        """
        minorScale = [self._note]

        for count in range(1, 8):
            if count == 2 or count == 5 or count == 7:
                # Takes a halfstep from the last element
                minorScale.append(Note(minorScale[len(minorScale) - 1]).halfStep(1))
            elif count == 6:
                #Taies 3 halfsteps from the last element
                minorScale.append(Note(minorScale[len(minorScale) - 1]).halfStep(3))
            else:
                # Takes a wholestep from the last element
                minorScale.append(Note(minorScale[len(minorScale) - 1]).wholeStep(1))

        return minorScale

    def interval(self, interval:str):
        """
        Returns the note resulting from taking an interval from self._note
        """
        # Choecks notation of the interval
        intervalSearch= re.search("^([1-8])([pmM])$", interval)
        if self._validateInterval(intervalSearch):
            #Interval matches the correct notation
            if intervalSearch.group(1) == "1":
                #0t 0st
                return self._note
            elif intervalSearch.group(1) == "2":
                # 0t 1st or 1t 0st
                if intervalSearch.group(2) == "m":
                    return self.halfStep(1)
                elif intervalSearch.group(3) == "M":
                    return self.halfStep(2)
            elif intervalSearch.group(1) == "3":
                # 1t 1st or 2t 0st
                if intervalSearch.group(2) == "m":
                    return self.halfStep(3)
                elif intervalSearch.group(3) == "M":
                    return self.halfStep(4)
            elif intervalSearch.group(1) == "4":
                # 2t 1st
                return self.halfStep(5)
            elif intervalSearch.group(1) == "5":
                # 3t 1st
                return self.halfStep(7)
            elif intervalSearch.group(1) == "6":
                # 3t 2st or 4t 1st
                if intervalSearch.group(2) == "m":
                    return self.halfStep(8)
                elif intervalSearch.group(3) == "M":
                    return self.halfStep(9)
            elif intervalSearch.group(1) == "7":
                # 4t 2st or 5t 1st
                if intervalSearch.group(2) == "m":
                    return self.halfStep(10)
                elif intervalSearch.group(3) == "M":
                    return self.halfStep(11)
            elif intervalSearch.group(1) == "8":
                # 5t 2st
                return self.halfStep(12)

    #-----------------------------------------------------------------------------------------GETTERS & SETTERS
    @property
    def note(self):
        return self._note


"""
TODO: 
	
	- Create @note.setter
	- Integration with GitHub

"""
