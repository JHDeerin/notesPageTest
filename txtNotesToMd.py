'''
Converts my original .txt notes to Markdown
'''

import math
import sys

from htmlFromNotesDirectory import getTitleAndDateFromTitleLine

def convertNoteTextToMarkdown(noteText):
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
    for line in noteTextLines:

        # Handle code block/formulas case
        strippedLine = line.lstrip()
        indentation = len(line) - len(strippedLine)

        wasCodeBlock = isCodeBlock
        isCodeBlock = len(strippedLine) > 0 and not strippedLine.startswith('-')

        if (not wasCodeBlock and isCodeBlock) or (wasCodeBlock and not isCodeBlock):
            outputMarkdown += "```\n"

        outputMarkdown += f'{line}\n'

    return outputMarkdown

def convertTxtNoteFile(noteFilename):
    '''
    Converts the given .txt note file and saves it as a markdown file
    '''

    if not noteFilename[-4:] == '.txt':
        print(f'***{noteFilename} is not a .txt file!***')
        return

    markdownText = ''
    with open(noteFilename, 'r') as txtFile:
        markdownText = convertNoteTextToMarkdown(txtFile.read())

    outputFilename = f'{noteFilename[:-4]}.md'
    with open(outputFilename, 'w') as mdFile:
        mdFile.write(markdownText)

if __name__ == "__main__":
    notesTextFileName = sys.argv[1]

    convertTxtNoteFile(notesTextFileName)


