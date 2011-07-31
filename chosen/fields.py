from django import forms

from widgets import ChosenSelect, ChosenSelectMultiple

__all__ = [
	'ChosenFieldMixin', 'ChosenChoiceField', 'ChosenMultipleChoiceField',
	'ChosenModelChoiceField', 'ChosenModelMultipleChoiceField',
]

class ChosenFieldMixin(object):
	
	def __init__(self, *args, **kwargs):
		widget_kwargs = {}
		overlay = kwargs.pop('overlay', None)
		if overlay is not None:
			widget_kwargs['overlay'] = overlay
		widget = self.widget(**widget_kwargs)
		kwargs['widget'] = widget
		super(ChosenFieldMixin, self).__init__(*args, **kwargs)
			

class ChosenChoiceField(ChosenFieldMixin, forms.ChoiceField):
	
	widget = ChosenSelect

class ChosenMultipleChoiceField(ChosenFieldMixin, forms.MultipleChoiceField):
	
	widget = ChosenSelectMultiple
			
class ChosenModelChoiceField(ChosenFieldMixin, forms.ModelChoiceField):

	widget = ChosenSelect

class ChosenModelMultipleChoiceField(ChosenFieldMixin, forms.ModelMultipleChoiceField):
	
	widget = ChosenSelectMultiple
	