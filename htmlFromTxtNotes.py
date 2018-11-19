'''
Converts a .txt note file into an HTML file\n
To run from the command line:\n
'python htmlFromTextNotes.py <path to HTML template> <path to note file>'
'''

import os
import sys
import ntpath
from bs4 import BeautifulSoup

def softWrapTextLines(txtFile, maxLineLength):
    '''
    Takes in a plaintext file and returns the file contents as a string,
    "soft wrapping" each line to the given maximum length (such that the wrapped
    part matches the indentation level of the original line)
    '''
    originalText = txtFile.read().split('\n')
    brokenLines = ''
    for line in originalText:
        textRemaining = True
        indentation = -1
        while textRemaining:
            if len(line) <= maxLineLength:
                brokenLines += line + '\n'
                textRemaining = False
            else:
                if indentation == -1:
                    indentation = len(line) - len(line.lstrip())

                indexToSplitOn = 0
                for word in line.split(' '):
                    if indexToSplitOn + len(word) + 1 <= maxLineLength:
                        indexToSplitOn += len(word) + 1 # +1 to include spaces
                    else:
                        if len(word) + 1 > maxLineLength - indentation:
                            # special case for if the word itself is too long
                            # to fit on one line
                            indexToSplitOn = maxLineLength
                        break

                brokenLines += line[0 : indexToSplitOn] + '\n'
                line = (' ' * indentation) + (line[indexToSplitOn:].lstrip())
    return brokenLines + '\n' # add extra line of padding at the bottom

def createHtmlFromTxt(htmlBaseFileName, notesTextFileName, outputHtmlFileDestFolder):
    '''
    Converts the given text file and HTML template into an HTML file with the
    .txt's content copied into any element in the template with the
    'main-note-text' class; saves the file in the given directory with 
    '''
    if not os.path.exists(outputHtmlFileDestFolder):
        os.makedirs(outputHtmlFileDestFolder)

    htmlBaseFile = open(htmlBaseFileName, 'r')
    notesTextFile = open(notesTextFileName, 'r')

    outputHtml = BeautifulSoup(htmlBaseFile, "html.parser")
    # soft wrap the notes so the output HTML matches how they look in VS Code
    textContainers = outputHtml.find_all(class_ = "main-note-text")
    noteText = softWrapTextLines(notesTextFile, 80)
    for element in textContainers:
        element.string = noteText

    notesFileNameWithoutExtension = ntpath.basename(ntpath.splitext(notesTextFileName)[0])
    outputHtmlFile = open(os.path.join(outputHtmlFileDestFolder, 
            notesFileNameWithoutExtension + '.html'), 'w')
    outputHtmlFile.write(str(outputHtml))
    outputHtmlFile.close()

    htmlBaseFile.close()
    notesTextFile.close()

    print('Wrote note text into "%s.html" successfully!' % (notesFileNameWithoutExtension))

#===============================================================================
# -------------------- Actually Executed Part Below ----------------------------

if __name__ == "__main__":
    htmlBaseFileName = sys.argv[1]
    notesTextFileName = sys.argv[2]

    createHtmlFromTxt(htmlBaseFileName, notesTextFileName, "notesToHtmlOutput")
