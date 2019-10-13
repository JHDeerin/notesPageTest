'''
Converts a .txt note file into an HTML file\n
To run from the command line:\n
'python htmlFromTextNotes.py <path to HTML template> <path to note file>'
'''

from bs4 import BeautifulSoup
from fileFromNotes import FileFromNotes

import os
import sys
import ntpath

class HtmlFromTxtNotes(FileFromNotes):

    def fromNotesText(noteText):
        '''
        Takes the given note's text content as a string and returns a string
        containing the new, converted text
        '''
        pass

    def fromNotesFile(notesFileName, outputFileName, baseFileName=''):
        '''
        Converts the given text file and HTML template into an HTML file with the
        .txt's content copied into any element in the template with the
        'main-note-text' class; saves the file in the given directory with 
        '''
        if not notesFileName[-4:] == '.txt':
            print(f'***{notesFileName} is not a .txt file!***')
            return

        if not outputFileName[-5:] == '.html':
            print(f'***{outputFileName} is not a .html file!***')
            return

        outputFileDestFolder = os.path.dirname(os.path.abspath(outputFileName))
        if not os.path.exists(outputFileDestFolder):
            os.makedirs(outputFileDestFolder)

        htmlBaseFile = open(baseFileName, 'r')
        notesTextFile = open(notesFileName, 'r')

        outputHtml = BeautifulSoup(htmlBaseFile, "html.parser")
        textContainers = outputHtml.find_all(class_ = "main-note-text")
        noteText = notesTextFile.read()
        for element in textContainers:
            element.string = noteText

        outputHtmlFile = open(outputFileName, 'w')
        outputHtmlFile.write(str(outputHtml))
        outputHtmlFile.close()

        htmlBaseFile.close()
        notesTextFile.close()

        print('Wrote note text into "%s" successfully!' % (outputFileName))

#===============================================================================
# -------------------- Actually Executed Part Below ----------------------------

if __name__ == "__main__":
    notesTextFileName = sys.argv[1]
    outputHtmlFileName = sys.argv[1]
    htmlBaseFileName = sys.argv[3]

    HtmlFromTxtNotes.fromNotesFile(notesTextFileName, outputHtmlFileName, htmlBaseFileName)
