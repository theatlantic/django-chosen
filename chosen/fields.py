from django import forms

from widgets import ChosenSelect, ChosenSelectMultiple

class ChosenField(object):
	
	def __init__(self, *args, **kwargs):
		widget_kwargs = {}
		overlay = kwargs.pop('overlay', None)
		if overlay is not None:
			widget_kwargs['overlay'] = overlay
		widget = self.widget(**widget_kwargs)
		kwargs['widget'] = widget
		super(ChosenField, self).__init__(*args, **kwargs)
			

class ChosenChoiceField(ChosenField, forms.ChoiceField):
	
	widget = ChosenSelect

class ChosenMultipleChoiceField(ChosenField, forms.MultipleChoiceField):
	
	widget = ChosenSelectMultiple
			
