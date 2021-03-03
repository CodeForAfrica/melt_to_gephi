=============
melt_to_gephi
=============


.. image:: https://img.shields.io/pypi/v/melt_to_gephi.svg
        :target: https://pypi.python.org/pypi/melt_to_gephi

.. image:: https://img.shields.io/travis/4bic/melt_to_gephi.svg
        :target: https://travis-ci.com/4bic/melt_to_gephi

.. image:: https://readthedocs.org/projects/melt-to-gephi/badge/?version=latest
        :target: https://melt-to-gephi.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A simpler way of restructituring Meltwater data to a gephi ready data file


* Free software: MIT license
* Documentation: https://melt-to-gephi.readthedocs.io.


Features
--------
 Creates a `gephi` ready file with the columns

   |source | target | tweet | url | trend | post_type
   |-------|--------|-------|-----|------ |----------
   |@s1    |@tar1   |x.x.x  |url1 |#test1 |RT
   |@s2    |@tar2   |.x.x.  |url2 |#test2 |QT


Credits
-------

This package was created with Cookiecutter_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
