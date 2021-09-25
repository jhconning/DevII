# Jupyter Book Build

```{contents}
:depth: 3
```

Most of the content of this site is based on Jupyter Notebooks which serve as a front-end for markdown text and scientific python (R and Stata code in a few books).

I am using [JupyterBook](https://jupyterbook.org/intro.html) which, in turn, leverages the [Sphinx](https://www.sphinx-doc.org/en/master/) documentation system, to assemble notebooks and text documents into a single site/publication. 


Some of the embedded  python code has been hidden on webpages but can be revealed via a toggle.  The output of the code will usually be displayed as a static image.  Most of the underlying notebooks can be run to interactively to reproduce or change visualizations and simulations. You can do this using a cloud server by clicking on the Binder or Colab button at the rocket icon at the top of most pages.  Alternatively, first clone the notebooks to a personal computer and run a jupyter server there. Here is one [guide](https://www.dataquest.io/blog/jupyter-notebook-tutorial/) to that process. 

I do not recommend trying to build a jupyter book site until you first get comfortable with jupyter notebooks and git and github. But for those who may be interested, read on. 


## Jupyter Book Concepts

Jupyterbook was created to assemble markdown text files, jupyter notebooks and other shareable content into publication quality output in the form of websites, late or PDF documents, etc. Jupyterbook is part of [The Executable Book Project](https://executablebooks.org/en/latest/).  Many Executable Books and Courses are being written using Jupyterbook. See the [Gallery of Jupyter Books](https://executablebooks.org/en/latest/gallery.html).  Several of the people behind the [Quantecon](https://quantecon.org/) project (which provides high-quality interactive Economics PhD Economics learning materials written mostly in scientific python and Julia), were important in the development of Jupyter Book.

The aim is to create content using easy human-readable [markdown](https://www.markdownguide.org/getting-started/) in combination with python (or other coding languages) to explore ideas and create scientific content with simulations and visualizations and to then convert this via a nice looking rendered website and/or to other intermediary or final formats such as Latex, PDF, etc.  In short, we want an easy to update and nice looking website/book for sharing reproducible research but without having to learn (too much) HTML/CSS or technical details of site hosting.

Jupyterbook extends the basic markdown syntax typically used for jupyter notebooks by adding extra [MyST Markdown](https://jupyterbook.org/content/myst.html) 'directives' and 'roles' to allow us several 'book writing' tasks including adding bibliographic citations and bibliographies, numberering equations, adding cross-references, creating tabs and dropdowns, etc. This also gives more fine control over things such as image size and positioning on a page, figure captioning, features to hide code, create warning boxes, etc.

## Setup and Build

See installation instructions on the [jupyter book](https://jupyterbook.org/) page.  We need a `_config.yml` with basic configuration settings and a `_toc.yml` file that establishes which files will be included in the navigation structure that you'll to the left of the site.

Suppose you have [cloned](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the [Econ-Teach](https://github.com/jhconning/Econ-Teach)repository that builds this site to a folder on your machine labeled `Econ-Teach` and have already installed jupyterbook.  If you then open up an Anaconda command terminal on your machine and navigate to that folder, you can then type

`jb build .`

Then jupyterbook will build a local HTML website which you can view from a browser (at the end of the build process it will tell you how to open it).  


## Github Actions and webpage

In order to build and share a website that can be reached from anywhere on the internet I use the free github pages servive. 

I've [setup a github action](https://jupyterbook.org/publish/gh-pages.html#automatically-host-your-book-with-github-actions) so that any push of new content to the Github repository will trigger a jupyter book build process on a cloud machine. The file that instructs Github actions what to do is [book.yml](https://github.com/jhconning/DevII/blob/main/.github/workflows/book.yml) in the repository. It gives instructions to trigger the creation of a virtual cloud machine that will then build the jupyterbook site using the build process just described, and host the site on [github pages](https://pages.github.com/) (free for public sites). Assuming no errors in the build process, the rendered site then displays at [jhconning.github.io/DevII](https://jhconning.github.io/DevII).  It's a neat process and it's fun to see github actions do all this work for you.  There may be a few minutes delay between a new build and the changes appearing on the site.[^1]

## Workflow

I typically develop jupyter notebook and markdown file content using [jupyterlab](https://jupyter.org/) and [Visual Studio Code](https://code.visualstudio.com/) to edit content and move files around, but I sometimes use a markdown editor such as [Typora](https://typora.io/) particularly if I'm going to type a lot of math.  You can have these different tools open at the same time, editing the same files.  VS code allows you to preview how both markdown files and jupyter notebooks will render, plus you can open up a terminal window to run local jupyterbook builds to see how they look in the browser.  

When I'm satisified that new content is ready to be shared I will then push the changes to the github repository (either via the command line, or using either VS code or the github desktop app).  I only push the 'source' files (markdown, jupyter notebooks, and relevant other files) not the locally rendered HTML because, as mentioned, a github action will build the site on a virtual machine (everything needed to make it run is in the [book.yml](https://github.com/jhconning/Econ-Teach/blob/master/.github/workflows/book.yml) configuration file).  


The following is a jupyterbook report on the build process to create this site:


[^1]: Enable Github pages in the github settings.  Also make sure that your version of the [book.yml](https://github.com/jhconning/DevII/blob/master/.github/workflows/book.yml) file points to the right branch (e.g. 'main' or 'master').
