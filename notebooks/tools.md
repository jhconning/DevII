# The Scientific Stack

```{contents}
:depth: 3
```

This site was built mostly using open-source scientific computing tools. Here is a quick guide to what they are how they tie together to create reproducible research workflows and outputs.


## [Markdown](https://commonmark.org/)
plain text format for writing structured documents. To make materials accessible and human-readable, all text, code, and math should be written in plain text files. Markdown syntax simply indicates how to structure that text (e.g. `_italics_` produces _italics_).  We mix markdown text with [LaTex](https://en.wikipedia.org/wiki/LaTeX) syntax to render math expressions. 

There are many good markdown editors.  I recommend [Visual Studio Code](https://code.visualstudio.com) (with enhanced markdown preview extension) and [Typora](https://typora.io). VS Code also serves as powerful integrated Development Environment (IDE) for editing notebooks and keeping files organized.


## [Scientific computing with python and R](https://docs.python-guide.org/scenarios/scientific/). 

Python is a popular, easy to learn general purpose programming language. R is another open source language focused more on statistical computing. Both are popular 'glue' languages, powerful on their own but also easily extended to access and tie together powerful functionality from many powerful 'libraries' (often written in other languages such as C for speed) or huge databases hosted on remote computers). These libraries can be easily imported into python or R to greatly increase their functionality and create a powerful open-source scientific computing environment to easily match or exceed far more expensive proprietary systems.  Some popular libraries for python include:


  - [matplotlib](https://matplotlib.org/) - the most widely used of the many plotting and visualization libraries.
  - [numpy](https://numpy.org/) - vectors, matrices, and math functions. 
  - [scipy](https://docs.scipy.org/doc/scipy/reference/) - optimization, linear algebra, and other math functions.
  - [pandas](https://pandas.pydata.org/docs/getting_started/overview.html) and  [geopandas](https://geopandas.org/) (database and geospatial data manipulation))
  - [scikit-learn](https://scikit-learn.org/stable/) (machine learning)
  - [ipywidgets](https://ipywidgets.readthedocs.io/) - interactive widget control over jupyter notebooks for sliders and many other inteactive elements.

Very similar libraries exist for R. 

There is a larger 'stack' of libraries that together make up the scientific computing environment. In the early days of open-source computing it was very difficult to keep these all working together but solutions such as [anaconda](https://www.anaconda.com/products/individual) have simplified the process to one download file and a one-click installation.  

R versus python?  Try both. If your main purpose is econometrics and statistical computing, R has the more complete libraries for this purpose (although for machine learning, many people prefer python). Python might be a bit easier to learn and perhaps more versatile as a general purpose language with a wider user base, but this is a matter of opinion as R people will tell you there is very little they can't do. For building and solving general equilibrium models using numerical methods, python is a good choice,  particularly if you are coming from matlab. The  [QuantEcon](https://quantecon.org/) has good guides to scientific computing in python for economists.

  
## [Jupyter notebooks](https://jupyter.org/) 
"an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more."  Jupyter notebooks serve as a front end to document and share your code and output, whether that code be python, Julia, Stata, Matlab, etc.  Jupyter notebooks become interactive (i.e. the user can change content and see how that produces new outputs) when they are being hosted on a 'kernel server' capable of executing the content. 
  

## [git and github](https://github.com/) 

To keep your files under version control. You run git on your local machine(s) and from time to time you 'push' updates to a 'remote' repository hosted on a service such as [github](https://github.com/) to facilitate sharing and collaboration of the repository (from which you 'pull' in any changes).  

An ecosystem of services has emerged around github to allow you to share materials, collaborate, and automate useful processes.  For example, you can set things up so that any new jupyter notebooks, markdown files  or other content 'pushed' to the repository to this [DevII](https://github.com/jhconning/DevII) site will trigger a 'build' process to refresh the website which is also hosted on github.  See the [next page](how_to.md).


## [Jupyter Book](https://jupyterbook.org/) 

"an open source project for building beautiful, publication-quality books and documents from computational material."  While standalone Jupyter Notebooks can render nicely, jupyterbook is a tool for assembling a collection of jupyter notebooks and other source materials into a well structured publication, be that a website, a latex document, PDF file, etc. It allows one to add table of contents and navigation structure, cross-references, bibliographies, etc.

One way to think of these tools and workflowas is that they allow yout to produce nicely rendered HTML websites using only markdown and other relatively easy to learn skills, without having to learn HTML syntax and other technical details.

