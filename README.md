django-chosen
=============

*django-chosen* is a project that makes available django FormFields that uses
the [Chosen javascript plugin](http://harvesthq.github.com/chosen/). It was
created by developers at [The Atlantic](http://www.theatlantic.com/).

Note that there is a select field library with even more features available at
[https://github.com/theatlantic/django-select2-forms](https://github.com/theatlantic/django-select2-forms).
Most implementation work will go towards django-select2-forms.

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

Add `chosen` to your `INSTALLED_APPS`, then, in your template, inject your form medias to get chosen css and js :

```html
{{ form.media }}
```

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

When the selectable items represent a model with an admin change-page or similar edit-page, you can render each item as link to these pages by doing:

```python
from django import forms
from django.core.urlresolvers import reverse
from chosen import forms as chosenforms

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    quality = chosenforms.ChosenChoiceField(overlay="Select book quality...",
        choices=(('New', 'new'), ('Used', 'used')))
    authors = chosenforms.ChosenModelMultipleChoiceField(queryset=Author.objects.all())
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['authors'].widget.attrs['chosen-fk-url-base'] = reverse('admin:myapp_author_changelist')
        self.fields['authors'].widget.attrs['chosen-fk-url-target'] = '_blank'
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
