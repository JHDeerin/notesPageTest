/**
 * Based on Luigi De Rosa's tutorial for Smashing Magazine
 * (original link: https://www.smashingmagazine.com/2016/07/improving-user-flow-through-page-transitions/)
 */

const main = document.querySelector('article');
let maxLineLength = 80; // Max length in characters

let cache = {};
let newPageLoading = false;

// When our 1st page is loaded, wrap its text
wrapElementText(document.querySelector('.main-note-text'));

async function loadPage(url) {
    if (cache[url]) {
        return new Promise(function(resolve) {
            resolve(cache[url]);
        });
    }

    const response = await fetch(url, {
        method: 'GET'
    });
    cache[url] = response.text();
    return cache[url];
}

function changePage(isLinkToAnotherNote) {
    if (newPageLoading === false) {
        var url = window.location.href;
        
        if (isLinkToAnotherNote) {
            newPageLoading = true;

            loadPage(url).then(function(responseText) {
                var wrapper = document.createElement('div');
                wrapper.innerHTML = responseText;
            
                var oldContent = document.querySelector('.main-note-text');
                var newContent = wrapper.querySelector('.main-note-text');

                // Wrap new lines
                wrapElementText(newContent);

                resetSideLinks(wrapper);
                changeSelectedNoteLink(wrapper);

                main.appendChild(newContent);
                animate(oldContent, newContent);
            });
        } else {
            //for now, just load non-note links like normal without any effects
            window.location.href = url;
        }
    }
}

function wrapElementText(element) {
    element.innerText = softWrapTextLines(element.innerText, maxLineLength);
}

function resetSideLinks(newHtmlWrapper) {
    const currentSideLinks = document.querySelectorAll('a.side-link');
    const newSideLinks = newHtmlWrapper.querySelectorAll('a.side-link');
    
    currentSideLinks[0].setAttribute('href', newSideLinks[0].getAttribute('href'))
    currentSideLinks[1].setAttribute('href', newSideLinks[1].getAttribute('href'))
}

function changeSelectedNoteLink(newHtmlWrapper) {
    const linkListElements = document.querySelectorAll('ul.note-links-slider li');
    linkListElements[getSelectedLinkIndex(document)].classList.remove("active-note-page");
    
    const newSelectedPageIndex = getSelectedLinkIndex(newHtmlWrapper);
    linkListElements[newSelectedPageIndex].classList.add("active-note-page");
    linkListElements[newSelectedPageIndex].scrollIntoView({behavior: "smooth"});
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

document.addEventListener('click', function(e) {
    var el = e.target;

    //go up the DOM tree until we find something with a link
    while (el && !el.href) { 
        el = el.parentNode;
    }

    if (el) {
        e.preventDefault();
        history.pushState({}, "", el.href);

        isLinkToAnotherNotePage = el.classList.contains("is-note-link")
        changePage(isLinkToAnotherNotePage);
        return;
    }
});