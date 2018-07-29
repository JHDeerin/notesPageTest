/**
 * Based on Luigi De Rosa's tutorial for Smashing Magazine
 * (original link: https://www.smashingmagazine.com/2016/07/improving-user-flow-through-page-transitions/)
 */

var cache = {};
const main = document.querySelector('article');
let newPageLoading = false;

function loadPage(url) {
    if (cache[url]) {
        return new Promise(function(resolve) {
        resolve(cache[url]);
        });
    }

    return fetch(url, {
        method: 'GET'
    }).then(function(response) {
        cache[url] = response.text();
        return cache[url];
    });
}

function changePage() {
    if (newPageLoading === false) {
        newPageLoading = true;
        var url = window.location.href;

        loadPage(url).then(function(responseText) {
            var wrapper = document.createElement('div');
                wrapper.innerHTML = responseText;

            var oldContent = document.querySelector('pre');
            var newContent = wrapper.querySelector('pre');

            resetSideLinks(wrapper);
            changeSelectedNoteLink(wrapper);

            main.appendChild(newContent);
            animate(oldContent, newContent);
        });
    }
}

function resetSideLinks(newHtmlWrapper) {
    const currentSideLinks = document.querySelectorAll('a.side-links');
    const newSideLinks = newHtmlWrapper.querySelectorAll('a.side-links');
    
    currentSideLinks[0].setAttribute('href', newSideLinks[0].getAttribute('href'))
    currentSideLinks[1].setAttribute('href', newSideLinks[0].getAttribute('href'))
}

function changeSelectedNoteLink(newHtmlWrapper) {
    const linkListElements = document.querySelectorAll('ul.note-links-slider li');
    linkListElements[getSelectedLinkIndex(document)].className = "";
    linkListElements[getSelectedLinkIndex(newHtmlWrapper)].className = "active-note-page";
}

function getSelectedLinkIndex(htmlWrapper) {
    const linkListElements = htmlWrapper.querySelectorAll('ul.note-links-slider li');
    for (let i = 0; i < linkListElements.length; i++) {
        if (linkListElements[i].className === "active-note-page") {
            return i;
        }
    }
}

function animate(oldContent, newContent) {
    const fadeInMSLength = 100;
    oldContent.style.position = 'absolute';

    var fadeOut = oldContent.animate({
        opacity: [1, 0]
    }, fadeInMSLength);

    var fadeIn = newContent.animate({
        opacity: [0, 1]
    }, fadeInMSLength);

    fadeIn.onfinish = function() {
        oldContent.parentNode.removeChild(oldContent);
        newPageLoading = false;
    };
}

window.addEventListener('popstate', changePage);

document.addEventListener('click', function(e) {
    var el = e.target;

    while (el && !el.href) {
        el = el.parentNode;
    }

    if (el) {
        e.preventDefault();
        history.pushState({}, "", el.href);
        changePage(el.href);
        return;
    }
});