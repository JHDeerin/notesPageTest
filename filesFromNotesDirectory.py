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
    def _getTitleOfNoteFile(notesFilename):
        '''
        Returns the title written INSIDE the given file in the following format:\n
        //*****************************************//\n
        //****** <TITLE> - <OTHER INFO> **********//\n
        //***************************************//
        '''
        notesTextFile = open(notesFilename, 'r')
        titleLine = notesTextFile.read().split('\n')[1]
        notesTextFile.close()
        
        return getTitleAndDateFromTitleLine(titleLine)[0]

    @classmethod
    def _isNotesFile(cls, fileName):
        '''
        Returns True if the given file is a notes file, false otherwise
        '''
        return fileName.endswith('.txt')

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