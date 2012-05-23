from django import forms
from django.conf import settings

__all__ = ['ChosenWidgetMixin', 'ChosenSelect', 'ChosenSelectMultiple',
        'ChosenGroupSelect']


class ChosenWidgetMixin(object):

    class Media:
        js = ("%s%s?v=2" % (settings.STATIC_URL, "js/chosen.jquery.min.js"),
            "%s%s?v=3" % (settings.STATIC_URL, "js/chosen.jquery_ready.js"))
        css = {"all": ("%s%s?v=1" % (settings.STATIC_URL, "css/chosen.css"), )}

    def __init__(self, attrs={}, *args, **kwargs):

        attrs['data-placeholder'] = kwargs.pop('overlay', None)
        attrs['class'] = "class" in attrs and self.add_to_css_class(
            attrs['class'], 'chzn-select') or "chzn-select"

        super(ChosenWidgetMixin, self).__init__(attrs, *args, **kwargs)

    def add_to_css_class(self, classes, new_class):
        new_classes = classes
        try:
            classes_test = u" " + unicode(classes) + u" "
            new_class_test = u" " + unicode(new_class) + u" "
            if new_class_test not in classes_test:
                new_classes += u" " + unicode(new_class)
        except TypeError:
            pass
        return new_classes


class ChosenSelect(ChosenWidgetMixin, forms.Select):
    pass


class ChosenSelectMultiple(ChosenWidgetMixin, forms.SelectMultiple):
    pass


class ChosenGroupSelect(ChosenSelect):

    def __init__(self, attrs={}, *args, **kwargs):
        super(ChosenGroupSelect, self).__init__(attrs, *args, **kwargs)
        attrs["class"] = "chzn-single chzn-single-with-drop"

