Jinyaml
=======

Plugin for Spinx_ to use Jinja_ in Restructured Text (RST) and Markdown (md).

Installation
------------

Just use ``pip``::

    pip install sphinx-jinyaml

If you want to use markdown, it requires the ``commonmark`` plugin, but it can
be automatically installed with::

    pip install sphinx-jinyaml[markdown]

Configuration
-------------

After installing it, just add it to the extensions var in the ``conf.py`` file::

    extensions = [
        'jinyaml',                                           
    ]                     

This enables two new file extensions:

- `.jmd` or `.jmarkdown` to use Markdown (remember to install ``commonmark``).
- `.jrst` to use RestructuredText.

Any file with these extensions will be managed by Jinyaml.


Extras
------

In addition to the Jinja_ support, it is possible to add an initial Yaml with
variables that can be used in the later document. To separate both of them, just
use three hyphens. Example::

   var1: This is the value of var1
   my_list:
     - item 1
     - item 2
   my_dict:
     foo: foo 1
     bar: bar 1

   ---

   Hello!

   {{ var1 }}

   {% for item in my_list %}
   Item example: {{ item }}

   {% end %}

   {% for k, v in my_dict %}
   {{ k }} --> {{ v }}
   {% end %}

   bye!


.. _Sphinx: https://www.sphinx-doc.org/
.. _Jinja: http://jinja.pocoo.org
