/**
 * Based on Luigi De Rosa's tutorial for Smashing Magazine
 * (original link: https://www.smashingmagazine.com/2016/07/improving-user-flow-through-page-transitions/)
 */

const main = document.querySelector('article');
const maxLineLength = 80; // Max length in characters
const linePixelWidths = getAllPossibleLineWidths(maxLineLength);

let currentOriginalText = main.querySelector('.main-note-text').innerText;

let cache = {};
let newPageLoading = false;

// When our 1st page is loaded, wrap its text and go to the
wrapElementText(main.querySelector('.main-note-text'));
changeSelectedNoteLink(document.body, scrollBehavior='auto');

async function loadPage(url) {
    if (cache[url]) {
        return new Promise(function(resolve) {
            resolve(cache[url]);
        });
    }

    const response = await fetch(url, { method: 'GET' });
    cache[url] = response.text();
    return cache[url];
}

function isLocalPage() {
    return location.hostname === "localhost" || location.hostname === "127.0.0.1" || location.hostname === "";
}

function changePage(isLinkToAnotherNote) {
    if (newPageLoading) {
        return;
    }

    var url = window.location.href;
    if (!isLinkToAnotherNote) {
        //for now, just load non-note links like normal without any effects
        window.location.href = url;
        return;
    }

    newPageLoading = true;

    loadPage(url).then(function(responseText) {
        var wrapper = document.createElement('div');
        wrapper.innerHTML = responseText;

        var oldContent = document.querySelector('.main-note-text');
        var newContent = wrapper.querySelector('.main-note-text');

        // Wrap new lines
        currentOriginalText = newContent.innerText;
        wrapElementText(newContent);

        resetSideLinks(wrapper);
        changeSelectedNoteLink(wrapper);

        main.appendChild(newContent);
        animate(oldContent, newContent);
    });
}

function wrapElementText(element) {
    const currentMaxWidth = main.querySelector('.main-note-text').offsetWidth;

    let lineLengthChars = 0;
    // Find the first line width that can fit on-screen
    for (let numChars = maxLineLength; numChars >= 0; numChars--) {
        if (linePixelWidths[numChars] <= currentMaxWidth) {
            lineLengthChars = numChars;
            break;
        }
    }
    element.innerText = softWrapTextLines(element.innerText, lineLengthChars);
    reloadMathJax(); // MathJax needs to be updated after content change
}

function getAllPossibleLineWidths(maxLineWidthInChars) {
    const possibleWidths = new Array(maxLineWidthInChars + 1);
    const ruler = document.getElementById('text-width-ruler')

    possibleWidths[0] = 0.0;
    let currentString = '';
    for (let numChars = 1; numChars <= maxLineWidthInChars; numChars++) {
        currentString += '#';
        // TODO: Find if there's a way to do this without re-adding entire
        // string each time?
        ruler.innerText = currentString;
        possibleWidths[numChars] = ruler.offsetWidth;
    }
    return possibleWidths;
}

function resetSideLinks(newHtmlWrapper) {
    const currentSideLinks = document.querySelectorAll('a.side-link');
    const newSideLinks = newHtmlWrapper.querySelectorAll('a.side-link');

    currentSideLinks[0].setAttribute('href', newSideLinks[0].getAttribute('href'))
    currentSideLinks[1].setAttribute('href', newSideLinks[1].getAttribute('href'))
}

function changeSelectedNoteLink(newHtmlWrapper, scrollBehavior='smooth') {
    const linkListElements = document.querySelectorAll('ul.note-links-slider li');
    const newSelectedPageIndex = getSelectedLinkIndex(newHtmlWrapper);

    linkListElements[getSelectedLinkIndex(document)].classList.remove("active-note-page");
    linkListElements[newSelectedPageIndex].classList.add("active-note-page");
    linkListElements[newSelectedPageIndex].scrollIntoView({behavior: scrollBehavior});
}

function getSelectedLinkIndex(htmlWrapper) {
    const linkListElements = htmlWrapper.querySelectorAll('ul.note-links-slider li');
    for (let i = 0; i < linkListElements.length; i++) {
        if (linkListElements[i].classList.contains("active-note-page")) {
            return i;
        }
    }
}

function animate(oldContent, newContent) {
    const fadeInMSLength = 100;
    oldContent.style.position = 'absolute';
    oldContent.style.opacity = 1;
    oldContent.style.transition = `${fadeInMSLength / 1000.0}s opacity`;
    oldContent.style.opacity = 0;

    newContent.style.opacity = 0;
    newContent.style.transition = `${fadeInMSLength / 1000.0}s opacity`;
    newContent.style.opacity = 1;

    window.setTimeout(function() {
        oldContent.parentNode.removeChild(oldContent);
        newPageLoading = false;
    }, fadeInMSLength);
}

window.addEventListener('popstate', changePage);
window.addEventListener('resize', function(){
    document.querySelector('.main-note-text').innerText = currentOriginalText
    wrapElementText(document.querySelector('.main-note-text'));
});

document.addEventListener('click', function(e) {
    var el = e.target;

    //go up the DOM tree until we find something with a link
    while (el && !el.href) {
        el = el.parentNode;
    }

    if (el) {
        e.preventDefault();
        if (isLocalPage()) {
            // Since fetch doesn't work offline, just load page normally
            window.location.href = el.href;
            return;
        }

        history.pushState({}, "", el.href);
        isLinkToAnotherNotePage = el.classList.contains("is-note-link")
        changePage(isLinkToAnotherNotePage);
        return;
    }
});