'''
Creates (or recreates) all the HTML note files added as entries in this file
'''

from bs4 import BeautifulSoup
from htmlFromNotesDirectory import HTMLFromNotesDir

import multiprocessing
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
    'htmlNotes/cs1331_oop',
    "OOP"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/spring2017/cs1332_dataStructuresAlgorithms/allLectureNotesCombined',
    'css/cs1332Theme.css',
    'htmlNotes/cs1332_dataAlgos',
    "Data Structures / Algorithms"))

# Sophomore Year
notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2017/cs2110/lectures',
    'css/cs2110Theme.css',
    'htmlNotes/cs2110',
    "CS 2110"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2017/cs2340/lectures',
    'css/cs2340Theme.css',
    'htmlNotes/cs2340_objectsDesign',
    "Objects and Design"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/summer2018/cs2200_systemsAndNetworks/lectures',
    'css/cs2200Theme.css',
    'htmlNotes/cs2200_systemsNetworking',
    "Systems and Networks"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/summer2018/cs3600_introAI/lectures',
    'css/cs3600Theme.css',
    'htmlNotes/cs3600_introAI',
    "Intro. to AI"))

# Junior Year
notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/spring2019/cs3451_compGraphics/notes',
    'css/cs3451Theme.css',
    'htmlNotes/cs3451_compGraphics',
    "Computer Graphics"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/spring2019/cs4731_gameAI/notes',
    'css/cs4731Theme.css',
    'htmlNotes/cs4731_gameAI',
    "Game AI"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/spring2019/cx4230/notes',
    'css/cx4230Theme.css',
    'htmlNotes/cx4230',
    "Intro. Modeling/Simulation"))

# Senior Year
notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2019/cs4476_computerVision/notes',
    'css/cs4476Theme.css',
    'htmlNotes/cs4476_compVision',
    "Computer Vision"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2019/cs4635_knowledgeAI/notes',
    'css/cs4635Theme.css',
    'htmlNotes/cs4635_knowledgeAI',
    "Knowledge-Based AI"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2019/cs4646_MLforTrading/notes',
    'css/cs4646Theme.css',
    'htmlNotes/cs4646_MLforTrading',
    "Machine Learning for Trading"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2019/phil3109_engineeringEthics/notes',
    'css/phil3109Theme.css',
    'htmlNotes/phil3109_engineeringEthics',
    "Engineering Ethics"))

notesToCreate.append(ClassNoteEntry(
    '../../../Class Materials/fall2019/phil3115_philScience/notes',
    'css/phil3115Theme.css',
    'htmlNotes/phil3115_philScience',
    "Philosophy of Science"))

#===============================================================================
#===============================================================================


# Open the base notes page
baseHtmlFile = open(baseHtmlFileName, 'r')
basePageHtml = BeautifulSoup(baseHtmlFile, "html.parser")
baseHtmlFile.close()

def convertNoteDirectory(classNotesInfo):
    # Setup base HTML page for the current class
    cssPathFromOutputFile = '../../' + classNotesInfo.pathToStylesheet
    noteStylesheetTag = basePageHtml.find(id='class-theme-styles')
    noteStylesheetTag['href'] = cssPathFromOutputFile
    pageTitleTag = basePageHtml.find('title')
    pageTitleTag.string = basePageTitle + classNotesInfo.pageTitle
    titleLink = basePageHtml.find(id='class-title-link')
    titleLink.string = classNotesInfo.pageTitle

    # Create a temporary new base file so we don't modify the original
    if not os.path.exists(classNotesInfo.outputDirectory):
        os.makedirs(classNotesInfo.outputDirectory)
    currentBaseFileName = classNotesInfo.outputDirectory + '_basePage.html'
    currentBaseFile = open(currentBaseFileName, 'w')
    currentBaseFile.write(str(basePageHtml))
    currentBaseFile.close()

    HTMLFromNotesDir.createFiles(classNotesInfo.pathToNoteDirectory,
                                outputDirectoryName=classNotesInfo.outputDirectory,
                                baseFileName=currentBaseFileName)

    # Delete the temporary base
    os.remove(currentBaseFileName)

    print('\nNotes for %s created!' % (classNotesInfo.outputDirectory))
    print('========================================')

if __name__ == "__main__":
    with multiprocessing.Pool() as process_pool:
        process_pool.map(convertNoteDirectory, notesToCreate)
