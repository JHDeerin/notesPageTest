// Loads the MathJax library for rendering LaTeX in web browsers

window.MathJax = {
  options: {
    skipHtmlTags: [            //  HTML tags that won't be searched for math
        'script', 'noscript', 'style', 'textarea',
        'code', 'annotation', 'annotation-xml'
    ]
  }
};

(function () {
  var script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js';
  script.async = true;
  document.head.appendChild(script);
})();