window.MathJax = {
    tex: {
        inlineMath: [["\\(", "\\)"]],
        displayMath: [["\\[", "\\]"]],
        processEscapes: true,
        processEnvironments: true,
        // packages: {'[+]': ['color']},
        macros: {
            F: '{\\bf \\color{green} F}',
            R: '{\\bf \\color{red} R}',
            fun: '{\\color{green}f}',
            res: '{\\color{red}r}',
        }
    },
    options: {
        ignoreHtmlClass: ".*|",
        processHtmlClass: "arithmatex"
    }
};

document$.subscribe(() => {
    MathJax.typesetPromise()
})
