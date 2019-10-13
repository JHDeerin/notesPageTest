'''
Converts a directory of .txt note files into HTML\n
To run from the command line:\n
'python htmlFromNotesDirectory.py <path to HTML template> <path to notes directory>'
'''

from bs4 import BeautifulSoup
from filesFromNotesDirectory import FilesFromNotesDirectory
from htmlFromTxtNotes import HtmlFromTxtNotes
from textUtils import getTitleAndDateFromTitleLine

import ntpath
import os
import sys

class HTMLFromNotesDir(FilesFromNotesDirectory):

    @classmethod
    def _stitchHtmlSideLinksTogether(cls, outputDirectoryName):
        '''
        Edits the previous/next links to point to the previous/next HTML note files
        for all HTML note files in the given directory
        '''
        outputHtmlFiles = cls._getFilesInDir(outputDirectoryName)
        for i in range(0, len(outputHtmlFiles)):
            currentHtmlFile = open( os.path.join(outputDirectoryName, outputHtmlFiles[i]),
                    'r')
            updatedHtml = BeautifulSoup(currentHtmlFile, "html.parser")
            currentHtmlFile.close()
            sideLinks = updatedHtml.find_all("a", class_="side-link")
            prevPageName = outputHtmlFiles[max(i-1, 0)]
            nextPageName = outputHtmlFiles[min(i+1, len(outputHtmlFiles)-1)]
            sideLinks[0]['href'] = prevPageName
            sideLinks[1]['href'] = nextPageName

            currentHtmlFile = open( os.path.join(outputDirectoryName, outputHtmlFiles[i]),
                    'w')
            currentHtmlFile.write(str(updatedHtml))
            currentHtmlFile.close()

    @classmethod
    def _setupHtmlHeaderLinks(cls, outputDirectoryName, noteTitles):
        '''
        Adds links to all HTML note files in the directory to the header of each
        HTML note file in the directory
        '''
        outputHtmlFiles = cls._getFilesInDir(outputDirectoryName)
        for i in range(0, len(outputHtmlFiles)):
            currentHtmlFile = open( os.path.join(outputDirectoryName, outputHtmlFiles[i]),
                    'r')
            updatedHtml = BeautifulSoup(currentHtmlFile, "html.parser")
            currentHtmlFile.close()

            headerNoteLinks = updatedHtml.nav.find('ul', class_="note-links-slider")
            headerNoteLinks.clear()
            for j in range(0, len(outputHtmlFiles)):
                newTag = BeautifulSoup('<li><a href="#" class="is-note-link"></a></li>', "html.parser")
                newTag.a['href'] = outputHtmlFiles[j]
                newTag.a.string = "%d. %s" % (j, noteTitles[j])
                if i == j: #if this is the current file's link
                    newTag.li['class'] = 'active-note-page'
                headerNoteLinks.append(newTag)

            currentHtmlFile = open( os.path.join(outputDirectoryName, outputHtmlFiles[i]),
                    'w')
            currentHtmlFile.write(str(updatedHtml))
            currentHtmlFile.close()

    def _createNewFile(notesFileName, outputDirectoryName, baseFileName):
        '''
        Creates an HTML file from the given notes file and information
        '''
        baseNotesFileName = ntpath.basename(notesFileName)
        outputHTMLFilename = ''.join(baseNotesFileName.split('.')[:-1]) + '.html'
        outputHTMLFilename = os.path.join(outputDirectoryName, outputHTMLFilename)
        HtmlFromTxtNotes.fromNotesFile(notesFileName, outputHTMLFilename, baseFileName)

    def _filesPostProcessing(cls, inputDirectoryName, outputDirectoryName):
        '''
        Does any operations on the newly-created files after they've initially
        been created
        '''
        noteTitles = []
        filesInDirectory = cls._getFilesInDir(inputDirectoryName)
        for filename in filesInDirectory:
            if not cls._isNotesFile(filename):
                continue
            notesFilename = os.path.join(inputDirectoryName, filename)
            noteTitles.append( cls._getTitleOfNoteFile(notesFilename) )

        cls._stitchHtmlSideLinksTogether(outputDirectoryName)
        cls._setupHtmlHeaderLinks(outputDirectoryName, noteTitles)

#===============================================================================
# -------------------- Actually Executed Part Below ----------------------------

if __name__ == '__main__':
    directoryPath = sys.argv[1]
    htmlBaseFileName = sys.argv[2]
    HTMLFromNotesDir.createFiles(directoryPath, baseFileName=htmlBaseFileName)
    createHtmlFromNotesDir(htmlBaseFileName, directoryPath)