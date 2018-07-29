import os
import sys
import ntpath
from bs4 import BeautifulSoup

def softBreakTextLines(txtFile, maxLineLength):
    originalText = txtFile.read().split('\n')
    brokenLines = ''
    for line in originalText:
        textRemaining = True
        indentation = -1
        while textRemaining:
            if len(line) <= maxLineLength:
                brokenLines += line + '\n'
                textRemaining = False
            else:
                if indentation == -1:
                    indentation = len(line) - len(line.lstrip())

                indexToSplitOn = 0
                for word in line.split(' '):
                    if indexToSplitOn + len(word) + 1 <= maxLineLength:
                        indexToSplitOn += len(word) + 1 # +1 to include spaces
                    else:
                        if len(word) + 1 > maxLineLength - indentation:
                            # special case for if the word itself is too long
                            # to fit on one line
                            indexToSplitOn = maxLineLength
                        break

                brokenLines += line[0 : indexToSplitOn] + '\n'
                line = (' ' * indentation) + (line[indexToSplitOn:].lstrip())
    return brokenLines + '\n' # add extra line of padding at the bottom

def createHtmlFromTxt(htmlBaseFileName, notesTextFileName, outputHtmlFileDestFolder):
    if not os.path.exists(outputHtmlFileDestFolder):
        os.makedirs(outputHtmlFileDestFolder)

    htmlBaseFile = open(htmlBaseFileName, 'r')
    notesTextFile = open(notesTextFileName, 'r')

    outputHtml = BeautifulSoup(htmlBaseFile, "html.parser")
    outputHtml.main.article.pre.string = softBreakTextLines(notesTextFile, 80)

    notesFileNameWithoutExtension = ntpath.basename(ntpath.splitext(notesTextFileName)[0])
    outputHtmlFile = open(os.path.join(outputHtmlFileDestFolder, 
            notesFileNameWithoutExtension + '.html'), 'w')
    outputHtmlFile.write(str(outputHtml))
    outputHtmlFile.close()

    htmlBaseFile.close()
    notesTextFile.close()

    print('Wrote note text into "%s.html" successfully!' % (notesFileNameWithoutExtension))

#===============================================================================
# -------------------- Actually Executed Part Below ----------------------------

if __name__ == "__main__":
    htmlBaseFileName = sys.argv[1]
    notesTextFileName = sys.argv[2]

    createHtmlFromTxt(htmlBaseFileName, notesTextFileName, "notesToHtmlOutput")
