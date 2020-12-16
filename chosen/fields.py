from django import forms

from .widgets import ChosenSelect, ChosenSelectMultiple, ChosenGroupSelect

__all__ = [
    'ChosenFieldMixin', 'ChosenChoiceField', 'ChosenMultipleChoiceField',
    'ChosenModelChoiceField', 'ChosenModelMultipleChoiceField',
    'ChosenGroupChoiceField',
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


class ChosenGroupChoiceField(ChosenFieldMixin, forms.ChoiceField):
    """
    This field generate a Single Select with Groups (optgroup support).
    To render it correctly, you need to give a choice with the group title and
    the list of (id, value) for the subtitles

    A good way to do that is to add a Manager, eg::


        class MyModelManager(models.Manager):
            "Add get_group_choices to MyModel"

            def get_group_choices(self):
                '''
                Will filter the model per name and return tuples (obj.id,
                obj.rule)
                '''
                choices = []
                for name in MyModel.objects.values_list("name").distinct():
                    name = name[0]
                    name_choices = tuple((obj.id, obj.rule) for obj in
                        MyModel.objects.filter(name=name))
                    choices.append((name, name_choices))
                return choices
    """
    widget = ChosenGroupSelect
