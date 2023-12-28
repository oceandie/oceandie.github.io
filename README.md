# oceandie.github.io

This is my personal Github page, created and maneged combining [Pelican](https://docs.getpelican.com/en/latest/index.html), a static site generator written in Python, with [Github Pages](https://pages.github.com/).

## 1. How to install Pelican
(Combining instructions from these two guides: [1](https://docs.getpelican.com/en/latest/install.html) and [2](https://www.archerimagine.com/articles/pelican/python-setup-for-pelican-blog.html))

```
conda create -n pelican39 python=3.9
conda activate pelican39
pip install "pelican[markdown]"
pip install Fabric
pip install beautifulsoup4
pip install typogrify
```

## 2. How to use Pelican
This guide is adapted from [here](https://github.com/getpelican/pelican/blob/master/docs/tips.rst)

a) Cloning the repository
```
git clone https://github.com/oceandie/oceandie.github.io.git
```

b) Modifying / updating the content of the web page in `oceandie.github.io.git/pelican/content`

c) Creating the html pages to be published
```
cd oceandie.github.io.git/pelican
conda activate pelican39
pelican content -o ../docs -s pelicanconf.py
git add *
git commit -m 'your message ofr the commit'
git push  orgin main
```

