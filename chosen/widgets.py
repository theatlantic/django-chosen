import os
import re

from chosen import settings

from django import forms
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string

class ChosenWidget(object):
	
	def __init__(self, attrs=None, *args, **kwargs):
		if attrs is not None:
			attrs = attrs.copy()
		else:
			attrs = {}
		
		overlay = kwargs.pop('overlay', None)
		if overlay is not None:
			attrs['data-placeholder'] = overlay
		
		if 'class' in attrs:
			attrs['class'] = self.add_to_css_class(attrs['class'], 'chzn-select')
		else:
			attrs['class'] = 'chzn-select'
		
		super(ChosenWidget, self).__init__(attrs, *args, **kwargs)
	
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
		
	
	def get_media(self):
		"""
		A method used to dynamically generate the media property,
		since we may not have the urls ready at the time of import,
		and then the reverse() call would fail.
		"""
		from django.forms.widgets import Media as _Media
		
		if settings.CHOSEN_MEDIA_URL is not None:
			media_url = settings.CHOSEN_MEDIA_URL + '/'
		else:
			media_url = reverse('chosen-static', kwargs={'path':''})
		
		media_cls = type('Media', (_Media,), {
			'css': {
				'all': (
					os.path.join(media_url, 'css/chosen.css?v=1'),
				)
			},
			'js': (
				os.path.join(media_url, 'js/chosen.jquery.js?v=1'),
			)
		})
		return _Media(media_cls)
	
	media = property(get_media)
	

class ChosenSelect(ChosenWidget, forms.Select):
	pass

class ChosenSelectMultiple(ChosenWidget, forms.SelectMultiple):
	pass