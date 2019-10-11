'''
Converts my original .txt notes to Markdown
'''

import math
import sys

from htmlFromNotesDirectory import getTitleAndDateFromTitleLine

def isPossibleCodeLine(line):
    '''
    Returns true if the given line should go in a Markdown code block because it
    it's a formula/line of code/ASCII diagram/etc.
    '''
    strippedLine = line.lstrip()
    return len(strippedLine) > 0 and not strippedLine.startswith('-')

def softWrapTextLine(line, indentation, maxLineLength=80):
    '''
    "Soft wraps" a line to the given maximum length (such that the wrapped part
    matches the given indentation level)
    '''
    outputLine = ''
    textRemaining = True
    isFirstLine = True
    while textRemaining:
        if len(line) <= maxLineLength:
            outputLine += line
            textRemaining = False
        else:
            indexToSplitOn = 0
            for word in line.split(' '):
                newLineLength = indexToSplitOn + len(word) + 1
                if isFirstLine:
                    newLineLength += indentation
                if newLineLength <= maxLineLength:
                    indexToSplitOn += len(word) + 1 # +1 to include spaces
                else:
                    if len(word) + 1 > maxLineLength - indentation:
                        # special case for if the word itself is too long
                        # to fit on one line
                        indexToSplitOn = maxLineLength
                    break

            isFirstLine = False
            outputLine += line[0 : indexToSplitOn] + '\n'
            # add padding to the beginning of the new line
            line = (' ' * indentation) + (line[indexToSplitOn:].lstrip())
    return outputLine

def convertLineToGoogleMarkdownStyle(line):
    '''
    Format the given line into Google's Markdown style for lists
    '''
    if isPossibleCodeLine(line) or len(line.strip('-')) == 0:
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
    codeBlockIndentation = 0
    for line in noteTextLines:

        # Handle code block/formulas case
        strippedLine = line.lstrip()
        indentation = len(line) - len(strippedLine)

        wasCodeBlock = isCodeBlock
        isCodeBlock = isPossibleCodeLine(line)

        if (not wasCodeBlock and isCodeBlock) or (wasCodeBlock and not isCodeBlock):
            if isCodeBlock:
                codeBlockIndentation = indentation
            outputMarkdown += f"{' '*codeBlockIndentation}```\n"

        tabbedLine = convertLineToGoogleMarkdownStyle(line)
        outputMarkdown += f'{tabbedLine}\n'

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


