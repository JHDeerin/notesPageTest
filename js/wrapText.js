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

    function softWrapString(line) {
        let textRemaining = true;
        let indentation = line.length - lstrip(line).length;

        line = lstrip(line);

        while (textRemaining) {
            if (line.length <= maxLineLength - indentation) {
                brokenLines += ' '.repeat(indentation) + line + '\n';
                textRemaining = false;
                break;
            }

            // determine which index to break the line on by iterating through
            // each word and adding its length
            let indexToSplitOn = 0;
            line.split(' ').some(function(word) {
                if (indexToSplitOn + word.length + 1 <= maxLineLength - indentation) {
                    indexToSplitOn += word.length + 1 // +1 to include spaces
                } else {
                    // special case for if the word itself is too long to fit on
                    // one line
                    if (word.length + 1 > maxLineLength - indentation) {
                        indexToSplitOn = maxLineLength
                    }
                    return true; // Acts as a 'break' statement
                }
            });

            // break line, saving the broken-off part
            brokenLines += ' '.repeat(indentation) + line.slice(0, indexToSplitOn) + '\n';
            line =  lstrip(line.slice(indexToSplitOn));
        }
    }

    originalText.forEach(softWrapString);

    return brokenLines + '\n' // add extra line of padding at the bottom
}