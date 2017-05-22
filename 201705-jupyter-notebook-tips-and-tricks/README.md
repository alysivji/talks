# Jupyter Notebook Tricks and Tips

## Upgrade to Jupyter 5.0

Table css is worth the price of admission.

[Blog about the 5.0 release](http://blog.jupyter.org/2017/04/04/jupyter-notebook-5-0/)

## Jupyter Lab

(Just found out about this during PyCon Day 3... inspiration for this open session)

Data Science IDE! Can run multiple notebooks in 1 window!!!!

[Watch this screencast](https://www.youtube.com/watch?v=sf8PuLcijuA) and be amazed!

### Additional Resources

* [Jupyter Lab Github with installation guide](https://github.com/jupyterlab/jupyterlab)
* [Announcement blog](http://blog.jupyter.org/2016/07/14/jupyter-lab-alpha/)

## Interact

Use Jupyter notebook widgets to make exploratory data analysis interactive! [Documentation](http://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)

[Example notebook](https://github.com/alysivji/blog-notebooks/blob/master/jupyter-notebook-interact/interact-widget-timeseries-data.ipynb) (note: NOT Jupyter 5.0 compliant... yet.)

### Additional Tools

* [Altair Widgets](https://github.com/altair-viz/altair_widgets)
* [Interactive PivotTables in Jupyter](http://nicolas.kruchten.com/content/2015/09/jupyter_pivottablejs/)
* [jupyter/nbdime](https://github.com/jupyter/nbdime), a tool to allow easy git diff'ing of Jupyter Notebooks. It can be used
  as the default tool by git, and shows a nice diff in the browser.

## Jupyter + Spark (Hortonworks Sandbox)

[Instructions on how to set up](https://github.com/alysivji/talks/tree/master/201704-healthcare-big-data-analytics) the Hortonworks Sandbox with Spark 2.1 and connect it to a Jupyter notebook.

### Other ways to use Spark in a notebook

* [IBM Data Science Experience](https://datascience.ibm.com/)
* [Databricks](https://community.cloud.databricks.com)

## Jupyter and Static Site Generators (Pelican)

Blogging about data science became easier! Write up your post in a notebook and use [pelican-ipynb](https://github.com/danielfrg/pelican-ipynb) to create a Pelican post.

[What is Pelican?](http://docs.getpelican.com/)

[Great resources re: setting up pelican-ipynb](https://www.google.com/search?q=pelican+static+site&oq=pelican+static+site+&aqs=chrome..69i57j0l4.4348j0j1&sourceid=chrome&ie=UTF-8#q=pelican+static+site+jupyter)
