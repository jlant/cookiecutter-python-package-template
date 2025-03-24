{{ cookiecutter.package_name_hyphenated }}
{% for _ in cookiecutter.package_name_hyphenated %}={% endfor %}

{{ cookiecutter.package_short_description }}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   api

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
