'''
Creates (or recreates) all the HTML note files added as entries in this file
'''

from bs4 import BeautifulSoup
import htmlFromNotesDirectory
import os

#===============================================================================
# Configuration Information
#===============================================================================
notesToCreate = []
baseHtmlFileName = 'notesBasePage.html'

class ClassNoteEntry:
    def __init__(self, pathToNoteDirectory, pathToStylesheet, outputDirectory):
        self.pathToNoteDirectory = pathToNoteDirectory
        self.pathToStylesheet = pathToStylesheet
        self.outputDirectory = outputDirectory

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/summer2018/cs3600_introAI/lectures',
    'css/cs3600Theme.css',
    'TEST_cs3600_introAI'))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/summer2018/cs2200_systemsAndNetworks/lectures',
    'css/cs2200Theme.css',
    'TEST_cs2200_systemsNetworking'))

#===============================================================================
#===============================================================================

# Open the base notes page
baseHtmlFile = open(baseHtmlFileName, 'r')
basePageHtml = BeautifulSoup(baseHtmlFile, "html.parser")
baseHtmlFile.close()

for noteInfo in notesToCreate:
    # Setup base HTML page for the current class
    cssPathFromOutputFile = '../' + noteInfo.pathToStylesheet
    noteStylesheetTag = basePageHtml.find(id='class-theme-styles')
    noteStylesheetTag['href'] = cssPathFromOutputFile

    # Create a temporary new base file so we don't modify the original
    currentBaseFileName = noteInfo.outputDirectory + '_basePage.html'
    currentBaseFile = open(currentBaseFileName, 'w')
    currentBaseFile.write(str(basePageHtml))
    currentBaseFile.close()

    htmlFromNotesDirectory.createHtmlFromNotesDir(currentBaseFileName, noteInfo.pathToNoteDirectory, noteInfo.outputDirectory)

    # Delete the temporary base
    os.remove(currentBaseFileName)

    print('\nNotes for %s created!' % (noteInfo.outputDirectory))
    print('========================================')
