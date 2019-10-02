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
basePageTitle = "Jake's CS Notes - "

class ClassNoteEntry:
    def __init__(self, pathToNoteDirectory, pathToStylesheet, outputDirectory,
            pageTitle="Jake's CS Notes"):
        self.pathToNoteDirectory = pathToNoteDirectory
        self.pathToStylesheet = pathToStylesheet
        self.outputDirectory = outputDirectory
        self.pageTitle = pageTitle

# Freshman Year
notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2016/cs1331_objectOriented/theBigCollectionOfAllFullNotesInOrder',
    'css/cs1331Theme.css',
    'cs1331_oop',
    "OOP"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/spring2017/cs1332_dataStructuresAlgorithms/allLectureNotesCombined',
    'css/cs1332Theme.css',
    'cs1332_dataAlgos',
    "Data Structures / Algorithms"))

# Sophomore Year
notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2017/cs2110/lectures',
    'css/cs2110Theme.css',
    'cs2110',
    "CS 2110"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2017/cs2340/lectures',
    'css/cs2340Theme.css',
    'cs2340_objectsDesign',
    "Objects and Design"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/summer2018/cs2200_systemsAndNetworks/lectures',
    'css/cs2200Theme.css',
    'cs2200_systemsNetworking',
    "Systems and Networks"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/summer2018/cs3600_introAI/lectures',
    'css/cs3600Theme.css',
    'cs3600_introAI',
    "Intro. to AI"))

# Junior Year
notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/spring2019/cs3451_compGraphics/notes',
    'css/cs3451Theme.css',
    'cs3451_compGraphics',
    "Computer Graphics"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/spring2019/cs4731_gameAI/notes',
    'css/cs4731Theme.css',
    'cs4731_gameAI',
    "Game AI"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/spring2019/cx4230/notes',
    'css/cx4230Theme.css',
    'cx4230',
    "Intro. Modeling/Simulation"))

# Senior Year
notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2019/cs4476_computerVision/notes',
    'css/cs4476Theme.css',
    'cs4476_compVision',
    "Computer Vision"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2019/cs4635_knowledgeAI/notes',
    'css/cs4635Theme.css',
    'cs4635_knowledgeAI',
    "Knowledge-Based AI"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2019/cs4646_MLforTrading/notes',
    'css/cs4646Theme.css',
    'cs4646_MLforTrading',
    "Machine Learning for Trading"))

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
    pageTitleTag = basePageHtml.find('title')
    pageTitleTag.string = basePageTitle + noteInfo.pageTitle
    titleLink = basePageHtml.find(id='class-title-link')
    titleLink.string = noteInfo.pageTitle

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
