'''
Converts my original .txt notes to Markdown
'''

from fileFromNotes import FileFromNotes
from htmlFromNotesDirectory import getTitleAndDateFromTitleLine
from textUtils import softWrapTextLine

import math
import sys

class MarkdownFromTxtFile(FileFromNotes):
    @staticmethod
    def _isPossibleCodeLine(line):
        '''
        Returns true if the given line should go in a Markdown code block because it
        it's a formula/line of code/ASCII diagram/etc.
        '''
        strippedLine = line.lstrip()
        return len(strippedLine) > 0 and not strippedLine.startswith('-')

    @staticmethod
    def _convertLineToGoogleMarkdownStyle(line):
        '''
        Format the given line into Google's Markdown style for lists
        '''
        if MarkdownFromTxtFile._isPossibleCodeLine(line) or len(line.strip('-')) == 0:
            # Don't try to format it if it isn't a list-style line
            return line
        if len(line.strip()) == 0:
            return ''

        strippedLine = line.lstrip()

        indentation = len(line) - len(strippedLine)
        roundedIndentation = math.ceil(indentation / 4) * 4

        # Indent 1 level more than beginning bullet
        indentedLine = softWrapTextLine(strippedLine[1:].strip(), roundedIndentation + 4)
        spacedLine = f'-   {indentedLine}'
        tabbedLine = (' ' * roundedIndentation) + spacedLine
        return tabbedLine

    def fromNotesText(noteText):
        '''
        Takes the given .txt note text as a string and returns a string containing
        the new text as Markdown
        '''

        outputMarkdown = ''

        noteTextLines = noteText.split('\n')

        # Assumes title is always on the 2nd line, header is first 3 lines
        titleString, dateString = getTitleAndDateFromTitleLine(noteTextLines[1])
        noteTextLines = noteTextLines[3:]

        outputMarkdown += f'# {titleString}\n\n## {dateString}\n\n'
        isCodeBlock = False
        codeBlockIndentation = 0
        for line in noteTextLines:

            # Handle code block/formulas case
            strippedLine = line.lstrip()
            indentation = len(line) - len(strippedLine)

            wasCodeBlock = isCodeBlock
            isCodeBlock = MarkdownFromTxtFile._isPossibleCodeLine(line)

            if (not wasCodeBlock and isCodeBlock) or (wasCodeBlock and not isCodeBlock):
                if isCodeBlock:
                    codeBlockIndentation = indentation
                outputMarkdown += f"{' '*codeBlockIndentation}```\n"

            tabbedLine = MarkdownFromTxtFile._convertLineToGoogleMarkdownStyle(line)
            outputMarkdown += f'{tabbedLine}\n'

        return outputMarkdown

    def fromNotesFile(notesFileName, outputFileName, baseFileName=''):
        '''
        Converts the given .txt note file and saves it as a markdown file
        '''

        if not notesFileName[-4:] == '.txt':
            print(f'***{notesFileName} is not a .txt file!***')
            return

        if not outputFileName[-3:] == '.md':
            print(f'***{outputFileName} is not a .md file!***')
            return

        markdownText = ''
        with open(notesFileName, 'r', encoding='utf8') as txtFile:
            markdownText = MarkdownFromTxtFile.fromNotesText(txtFile.read())

        with open(outputFileName, 'w', encoding='utf8') as mdFile:
            mdFile.write(markdownText)

if __name__ == "__main__":
    notesTextFileName = sys.argv[1]
    outputFileName = f'{notesTextFileName[:-4]}.md'

    MarkdownFromTxtFile.fromNotesFile(notesTextFileName, outputFileName)
