django-chosen
=============

*django-chosen* is a project that makes available django FormFields that
uses the `Chosen javascript plugin`_. It was created by developers at
`The Atlantic`_.

Installation
------------

The recommended way to install from source is with pip::

    $ pip install -e git+git://github.com/theatlantic/django-chosen.git#egg=django-chosen

If the source is already checked out, use setuptools::

    $ python setup.py install


Usage
-----

*django-chosen* makes available the following fields and widget:

Fields::

    - ``ChosenChoiceField``
    - ``ChosenModelChoiceField``
    - ``ChosenMultipleChoiceField``
    - ``ChosenModelMultipleChoiceField``

Widgets::

    - ``ChosenSelect``
    - ``ChosenSelectMultiple``


The *django-chosen* fields can be passed an optional kwarg ``overlay`` that
overrides the text which appears when no option is selected in the dropdown.

Example
-------

::

    from django import forms
    from chosen import forms as chosenforms

    class BookForm(forms.Form):
        name = forms.CharField(max_length=100)
        quality = chosenforms.ChosenChoiceField(overlay="Select book quality...",
            choices=(('New', 'new'), ('Used', 'used')))
        authors = chosenforms.ChosenModelMultipleChoiceField(queryset=Author.objects.all())

License
-------
The django code is licensed under the `Simplified BSD License`_ and is
copyright The Atlantic Media Company. View the LICENSE file under the root
directory for complete license and copyright information.

The Chosen javascript library included is licensed under the `MIT License`_.
View ``chosen/media/js/chosen.LICENSE.md`` for complete license and copyright
information about the Chosen javascript library.

Chosen javascript documentation
-------------------------------

Chosen is a library for making long, unwieldy select boxes more user friendly.

- jQuery support: 1.4+
- Prototype support: 1.7+

For documentation, usage, and examples, see:
http://harvesthq.github.com/chosen

Chosen Credits
..............

- Built by Harvest_
- Concept and development by `Patrick Filler`_
- Design and CSS by `Matthew Lettini`_

.. _The Atlantic: http://www.theatlantic.com/
.. _Simplified BSD License: http://www.opensource.org/licenses/bsd-license.php
.. _MIT License: http://en.wikipedia.org/wiki/MIT_License
.. _Chosen javascript plugin: http://harvesthq.github.com/chosen/
.. _Harvest: http://www.getharvest.com/
.. _Patrick Filler: http://www.patrickfiller.com/
.. _Matthew Lettini: http://matthewlettini.com/
