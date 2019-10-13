'''
General class for converting my .txt or other notes files into a different
format
'''

from abc import ABC, abstractmethod

class FileFromNotes(ABC):

    @staticmethod
    @abstractmethod
    def fromNotesText(noteText):
        '''
        Takes the given note's text content as a string and returns a string
        containing the new, converted text
        '''
        pass

    @staticmethod
    @abstractmethod
    def fromNotesFile(notesFileName, outputFileName, baseFileName=''):
        '''
        Converts the given notes file into an output file
        '''
        pass

