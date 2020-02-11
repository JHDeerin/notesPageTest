'''
A general purpose class for converting a directory of my .txt notes into some
other format
'''

from abc import ABC, abstractmethod
from textUtils import getTitleAndDateFromTitleLine, sort_naturally

import ntpath
import os
import shutil

class FilesFromNotesDirectory(ABC):

    @staticmethod
    def _getFilesInDir(directoryName):
        '''
        Returns the files in the given directory (sorted 'naturally' by filename)
        '''
        directoryPath = ntpath.dirname(directoryName)
        directoryFiles = os.listdir(directoryPath)
        sort_naturally(directoryFiles)
        return directoryFiles

    @staticmethod
    def _getTitleOfTxtNoteFile(notesFilename):
        '''
        Returns the title and date string written INSIDE the given .txt file\n
        in the following format:\n

        //*****************************************//\n
        //*********** <TITLE> - <DATE> ***********//\n
        //***************************************//
        '''
        notesTextFile = open(notesFilename, 'r', encoding='utf8')
        titleLine = notesTextFile.read().split('\n')[1]
        notesTextFile.close()

        return getTitleAndDateFromTitleLine(titleLine)[0]

    @staticmethod
    def _getTitleOfMdNoteFile(notesFilename):
        '''
        Returns the title string written INSIDE the given .md Markdown file\n
        in the following format:\n

        # <TITLE>\n
        \n
        # <DATE>
        '''
        notesTextFile = open(notesFilename, 'r', encoding='utf8')
        titleLines = notesTextFile.read().split('\n')[:3]
        notesTextFile.close()

        # Ignore first character to ignore Markdown heading hash
        titleString = titleLines[0].strip('#')[1:].strip()
        dateString = titleLines[2].strip('#')[1:].strip()

        # TODO: Currently, date is ignored
        return titleString


    @staticmethod
    def _getTitleOfNoteFile(notesFilename):
        '''
        Returns the title string written INSIDE the given file in the\n
        following format:\n

        .txt:\n
        //*****************************************//\n
        //*********** <TITLE> - <DATE> ***********//\n
        //***************************************//
        \n
        .md:\n
        # <TITLE>\n
        \n
        # <DATE>

        Returns an empty string if no title/date could be found
        '''
        if notesFilename[-4:] == '.txt':
            return FilesFromNotesDirectory._getTitleOfTxtNoteFile(notesFilename)
        if notesFilename[-3:] == '.md':
            return FilesFromNotesDirectory._getTitleOfMdNoteFile(notesFilename)

        return ''

    @classmethod
    def _isNotesFile(cls, fileName):
        '''
        Returns True if the given file is a notes file, false otherwise
        '''
        return fileName.endswith('.txt') or fileName.endswith('.md')

    @staticmethod
    @abstractmethod
    def _createNewFile(notesFileName, outputDirectoryName, baseFileName):
        '''
        Creates a converted file from the given notes file and information
        '''
        pass

    @classmethod
    @abstractmethod
    def _filesPostProcessing(cls, inputDirectoryName, outputDirectoryName):
        '''
        Does any operations on the newly-created files after they've initially
        been created
        '''
        pass

    @classmethod
    def createFiles(cls,
                    notesDirectoryName,
                    outputDirectoryName='notesToHtmlOutput',
                    rawNotesDirectoryName='rawNotes',
                    baseFileName=''):
        '''
        Creates files based on the notes files found in the given
        directoryPath, using the base file as a template; all output files
        placed in the given output directory. Creates a backup copy of the
        original notes in the rawNotesDirectory.
        '''

        # TODO: Find a more robust way of making sure it's a directory
        if notesDirectoryName[-1] != '/':
            notesDirectoryName += '/'
        filesInDirectory = cls._getFilesInDir(notesDirectoryName)

        print('Converting notes files in "%s"...' % (notesDirectoryName))

        # Setup directories for final output and copying raw notes
        if not os.path.exists(outputDirectoryName):
            os.makedirs(outputDirectoryName)
        rawNotesDirectoryName += '/' + ntpath.basename(outputDirectoryName)
        if not os.path.exists(rawNotesDirectoryName):
            os.makedirs(rawNotesDirectoryName)
        outputDirectoryName += '/'
        rawNotesDirectoryName += '/'

        filesConverted = 0
        for filename in filesInDirectory:
            # Check if file is an actual notes file
            if not cls._isNotesFile(filename):
                continue

            notesFilename = os.path.join(notesDirectoryName, filename)

            # Create copy of the raw notes for GitHub
            shutil.copy2(notesFilename, rawNotesDirectoryName)

            # Create converted file
            cls._createNewFile(notesFilename, outputDirectoryName, baseFileName)
            filesConverted += 1

        createdSomeFiles = filesConverted > 0
        if createdSomeFiles:
            # NOTE: ASSUMES ONLY THE JUST-CREATED FILES ARE IN THE OUTPUT DIRECTORY!
            cls._filesPostProcessing(cls, notesDirectoryName, outputDirectoryName)
            print('Converted %d files successfully!' % (filesConverted))
        else:
            print("No .txt files found. Aborting operation...")
