// Loads the MathJax library for rendering LaTeX in web browsers

window.MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']]
    },
    options: {
        //  HTML tags that won't be searched for math
        skipHtmlTags: [
            'script', 'noscript', 'style', 'textarea',
            'code', 'annotation', 'annotation-xml'
        ]
    }
};

(function () {
    let script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js';
    script.async = true;
    document.head.appendChild(script);
})();
