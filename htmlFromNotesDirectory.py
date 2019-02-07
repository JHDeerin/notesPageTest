'''
Converts a directory of .txt note files into HTML\n
To run from the command line:\n
'python htmlFromNotesDirectory.py <path to HTML template> <path to notes directory>'
'''

from bs4 import BeautifulSoup
import sys
import ntpath
import os
import htmlFromTxtNotes
import re

def sort_naturally( l ):
    """ Sort the given list of alphanumeric strings in the way that humans expect
        (i.e. numbers in numerical order instead of by ASCII number)
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    l.sort( key=alphanum_key )

def getFilesInDir(directoryName):
    '''
    Returns the files in the given directory (sorted 'naturally' by filename)
    '''
    directoryPath = ntpath.dirname(directoryName)
    directoryFiles = os.listdir(directoryPath)
    sort_naturally(directoryFiles)
    return directoryFiles

def getTitleOfNoteFile(notesFilename):
    '''
    Returns the title written INSIDE the given file in the following format:\n
    //*****************************************//\n
    //****** <TITLE> - <OTHER INFO> **********//\n
    //***************************************//
    '''
    notesTextFile = open(notesFilename, 'r')
    titleLine = notesTextFile.read().split('\n')[1]
    notesTextFile.close()
    titleLine = titleLine.strip().strip('/').strip('*').strip()
    return titleLine.split('-')[0].strip()

def stitchHtmlSideLinksTogether(outputDirectoryName):
    '''
    Edits the previous/next links to point to the previous/next HTML note files
    for all HTML note files in the given directory
    '''
    print("Stitching HTML side links together...")

    outputHtmlFiles = getFilesInDir(outputDirectoryName)
    for i in range(0, len(outputHtmlFiles)):
        print("Linking %s..." % (outputHtmlFiles[i]))
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

    print("All side links stitched together successfully!")

def setupHtmlHeaderLinks(outputDirectoryName, noteTitles):
    '''
    Adds links to all HTML note files in the directory to the header of each
    HTML note file in the directory
    '''
    print("Setting up HTML header note links...")

    outputHtmlFiles = getFilesInDir(outputDirectoryName)
    for i in range(0, len(outputHtmlFiles)):
        print("Setting up %s..." % (outputHtmlFiles[i]))
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

    print("All header links setup successfully!")

#===============================================================================
# -------------------- Actually Executed Part Below ----------------------------

htmlBaseFileName = sys.argv[1]
directoryPath = sys.argv[2]

def createHtmlFromNotes(htmlBaseFileName, directoryPath,
        outputDirectoryName='notesToHtmlOutput/'):
    # TODO: Verify this is valid across systems
    if directoryPath[-1] != '/':
        directoryPath += '/'
    filesInDirectory = getFilesInDir(directoryPath)

    print('Found the following files in directory "%s":' % (directoryPath))
    print(filesInDirectory)
    print()
    print('Converting .txt files...')

    txtNoteTitles = []
    for filename in filesInDirectory:
        if filename.endswith('.txt'):
            notesFilename = os.path.join(directoryPath, filename)
            htmlFromTxtNotes.createHtmlFromTxt(htmlBaseFileName, notesFilename, outputDirectoryName)
            txtNoteTitles.append( getTitleOfNoteFile(notesFilename) )

    createdSomeFiles = len(txtNoteTitles) > 0
    if createdSomeFiles:
        # NOTE: ASSUMES ONLY THE JUST-CREATED FILES ARE IN THE OUTPUT DIRECTORY!
        print("Initial files all created successfully!")
        print(txtNoteTitles)
        print()

        stitchHtmlSideLinksTogether(outputDirectoryName)
        print()
        setupHtmlHeaderLinks(outputDirectoryName, txtNoteTitles)
    else:
        print("No .txt files found. Aborting operation...")

createHtmlFromNotes(htmlBaseFileName, directoryPath)