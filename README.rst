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
 
 .. list-table:: Gephi File Structure
   :widths: 25 25 50 25 25 25
   :header-rows: 1

   * - source
     - target
     - tweet
     - trend
     - url
     - post_type
   * - @s1
     - @tar1
     - some tweet text
     - #tag1
     - Tweet 1 url 
     - RT
   * - @s2
     - @tar2
     - Another tweet text
     - #tag2
     - Tweet 2 url 
     - QT




Credits
-------

This package was created with Cookiecutter_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter


