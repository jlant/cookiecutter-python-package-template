.. toctree::
    :glob:

API Documentation
=================

{% set num_dashes = cookiecutter.package_name_underscored|length * 2 + 1 %}
{{ cookiecutter.package_name_underscored }}.{{ cookiecutter.package_name_underscored }}
{% for char in range(num_dashes) %}-{% endfor %}

.. automodule:: {{ cookiecutter.package_name_underscored }}.{{ cookiecutter.package_name_underscored }}
   :members:
   :undoc-members:
