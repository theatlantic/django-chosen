from django import forms

from widgets import ChosenSelect, ChosenSelectMultiple

__all__ = [
    'ChosenFieldMixin', 'ChosenChoiceField', 'ChosenMultipleChoiceField',
    'ChosenModelChoiceField', 'ChosenModelMultipleChoiceField',
]


class ChosenFieldMixin(object):

    def __init__(self, *args, **kwargs):
        widget_kwargs = "overlay" in kwargs and\
            {"overlay": kwargs.pop('overlay')} or {}
        kwargs['widget'] = self.widget(**widget_kwargs)
        super(ChosenFieldMixin, self).__init__(*args, **kwargs)


class ChosenChoiceField(ChosenFieldMixin, forms.ChoiceField):

    widget = ChosenSelect


class ChosenMultipleChoiceField(ChosenFieldMixin, forms.MultipleChoiceField):

    widget = ChosenSelectMultiple


class ChosenModelChoiceField(ChosenFieldMixin, forms.ModelChoiceField):

    widget = ChosenSelect


class ChosenModelMultipleChoiceField(ChosenFieldMixin,
        forms.ModelMultipleChoiceField):

    widget = ChosenSelectMultiple
