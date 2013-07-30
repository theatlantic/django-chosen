django-chosen
=============

*django-chosen* is a project that makes available django FormFields that uses
the [Chosen javascript plugin](http://harvesthq.github.com/chosen/). It was
created by developers at [The Atlantic](http://www.theatlantic.com/).

Installation
------------

The recommended way to install from source is with pip:

        pip install -e "git+https://github.com/theatlantic/django-chosen.git#egg=django-chosen"

If the source is already checked out, use setuptools:

        python setup.py develop

or, you can install from pypi:

        pip install django-chosen

Usage
-----

To use the *django-chosen* in your project you need to add "chosen" to
your `INSTALLED_APPS` and include the following in the templates that
use it:

        <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}css/chosen.css"/>
 
        <script src="{{ STATIC_URL }}js/chosen.jquery.min.js"></script>
        <script src="{{ STATIC_URL }}js/chosen.jquery_ready.js"></script>

*django-chosen* makes the following fields and widget available:

__Fields:__

* `ChosenChoiceField`
* `ChosenModelChoiceField`
* `ChosenMultipleChoiceField`
* `ChosenModelMultipleChoiceField`

__Widgets:__

* `ChosenSelect`
* `ChosenSelectMultiple`


The *django-chosen* fields can be passed an optional kwarg `overlay` that
overrides the text which appears when no option is selected in the dropdown.

Example
-------

```python
from django import forms
from chosen import forms as chosenforms

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    quality = chosenforms.ChosenChoiceField(overlay="Select book quality...",
        choices=(('New', 'new'), ('Used', 'used')))
    authors = chosenforms.ChosenModelMultipleChoiceField(queryset=Author.objects.all())
```

License
-------
The django code is licensed under the
[Simplified BSD License](Simplified BSD License) and is copyright The Atlantic
Media Company. View the `LICENSE` file under the root directory for complete
license and copyright information.

The Chosen javascript library included is licensed under the
[MIT License](http://en.wikipedia.org/wiki/MIT_License). View
`chosen/media/js/chosen.LICENSE.md` for complete license and copyright
information about the Chosen javascript library.

Chosen Javascript Documentation
-------------------------------

Chosen is a library for making long, unwieldy select boxes more user friendly.

- jQuery support: 1.4+
- Prototype support: 1.7+

For documentation, usage, and examples, see
[Harvest's Chosen JS github](http://harvesthq.github.com/chosen)


### Chosen Javascript Credits

- Built by [Harvest](http://www.getharvest.com/)
- Concept and development by [Patrick Filler](http://www.patrickfiller.com/)
- Design and CSS by [Matthew Lettini](http://matthewlettini.com/)
