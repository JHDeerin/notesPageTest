/**
 * Takes in a plaintext file's contents and returns the file contents as a
 * string, "soft wrapping" each line to the given maximum length (such that the
 * wrapped part matches the indentation level of the original line)
 */

function softWrapTextLines(rawText, maxLineLength) {
    const originalText = rawText.split(/[\r\n]/);    // Split at newlines
    let brokenLines = '';

    // Function to remove leading spaces from line
    function lstrip(str) {
        return str.replace(/^\s*/g, '');
    }

    originalText.forEach(function(line) {
        let textRemaining = true;
        let indentation = -1;    // -1 means indentation hasn't been set yet
        while (textRemaining) {
            if (line.length <= maxLineLength) {
                brokenLines += line + '\n';
                textRemaining = false;
            } else {
                if (indentation == -1) {
                    indentation = line.length - lstrip(line).length;
                }

                let indexToSplitOn = 0;
                line.split(' ').some(function(word) {
                    if (indexToSplitOn + word.length + 1 <= maxLineLength) {
                        indexToSplitOn += word.length + 1 // +1 to include spaces
                    } else {
                        if (word.length + 1 > maxLineLength - indentation) {
                            // special case for if the word itself is too long
                            // to fit on one line
                            indexToSplitOn = maxLineLength
                        }
                        return true; // Acts as a 'break' statement
                    }
                });
                brokenLines += line.slice(0, indexToSplitOn) + '\n';
                line = ' '.repeat(indentation) + lstrip(line.slice(indexToSplitOn));
            }
        }
    });

    return brokenLines + '\n' // add extra line of padding at the bottom
}