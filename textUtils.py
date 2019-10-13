'''
Contains general-purpose methods for operating on strings of text related to my
.txt notes
'''

def getTitleAndDateFromTitleLine(notesTitleLine):
    '''
    Returns the title and date from the given line in the following format:\n

    //****** <TITLE> - <DATE STRING> **********//\n

    Returns them as a tuple: (titleString, dateString)
    '''
    titleLine = notesTitleLine.strip().strip('/').strip('*').strip()

    # Assume everything after the last '-' is a date, and everything before is
    # part of the title
    titleLinePieces = titleLine.split('-')
    titleString = '-'.join(titleLinePieces[:-1]).strip()
    dateString = titleLinePieces[-1].strip()

    return (titleString, dateString)

def softWrapTextLine(line, indentation, maxLineLength=80):
    '''
    "Soft wraps" a line to the given maximum length (such that the wrapped part
    matches the given indentation level)
    '''
    outputLine = ''
    textRemaining = True
    isFirstLine = True
    while textRemaining:
        if len(line) <= maxLineLength:
            outputLine += line
            textRemaining = False
        else:
            indexToSplitOn = 0
            for word in line.split(' '):
                newLineLength = indexToSplitOn + len(word) + 1
                if isFirstLine:
                    newLineLength += indentation
                if newLineLength <= maxLineLength:
                    indexToSplitOn += len(word) + 1 # +1 to include spaces
                else:
                    if len(word) + 1 > maxLineLength - indentation:
                        # special case for if the word itself is too long
                        # to fit on one line
                        indexToSplitOn = maxLineLength
                    break

            isFirstLine = False
            outputLine += line[0 : indexToSplitOn] + '\n'
            # add padding to the beginning of the new line
            line = (' ' * indentation) + (line[indexToSplitOn:].lstrip())
    return outputLine