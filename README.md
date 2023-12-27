# oceandie.github.io

This is my personal Github page, created and maneged combining [Pelican](https://docs.getpelican.com/en/latest/index.html), a static site generator written in Python, with [Github Pages](https://pages.github.com/).

## Installing Pelican
(Combining instructions from these two guides: [1](https://docs.getpelican.com/en/latest/install.html) and [2](https://www.archerimagine.com/articles/pelican/python-setup-for-pelican-blog.html))

```
conda create -n pelican39 python=3.9
conda activate pelican39
pip install "pelican[markdown]"
pip install Fabric
pip install beautifulsoup4
pip install typogrify
```

## How to use it

```
pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git push  https://github.com/oceandie/oceandie.github.io.git gh-pages:master
```

