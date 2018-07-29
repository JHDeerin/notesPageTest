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
    directoryPath = ntpath.dirname(directoryName)
    directoryFiles = os.listdir(directoryPath)
    sort_naturally(directoryFiles)
    return directoryFiles

def getTitleOfNoteFile(notesFilename):
    notesTextFile = open(notesFilename, 'r')
    titleLine = notesTextFile.read().split('\n')[1]
    notesTextFile.close()
    titleLine = titleLine.strip().strip('/').strip('*').strip()
    return titleLine.split('-')[0].strip()

def stitchHtmlSideLinksTogether(outputDirectoryName):
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
            newTag = BeautifulSoup('<li><a href="#"></a></li>', "html.parser")
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

htmlBaseFileName = sys.argv[1]
directoryPath = ntpath.dirname(sys.argv[2])
filesInDirectory = getFilesInDir(sys.argv[2])

print('Found the following files in directory "%s":' % (directoryPath))
print(filesInDirectory)
print()
print('Converting .txt files...')

outputDirectoryName = "notesToHtmlOutput/"
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