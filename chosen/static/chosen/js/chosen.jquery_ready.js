(function ($) {

    // Extend django admin function `dismissAddAnotherPopup` to
    // call $.fn.trigger('liszt:updated') on the chosen <select> element
    var _dismissAddAnotherPopup = window.dismissAddAnotherPopup;
    window.dismissAddAnotherPopup = function(win, newId, newRepr) {
        var $elem = $('#' + windowname_to_id(win.name));
        if (typeof _dismissAddAnotherPopup === 'function') {
            _dismissAddAnotherPopup(win, newId, newRepr);
        }
        if ($elem.hasClass('chosen-select')) {
            $elem.trigger('liszt:updated');
        }
    };

	$(document).ready(function($){
        $(".chosen-select").each(function(i, select) {
            var $select = $(select);

            // Set overflow:visible on parent .form-row for django admin
            $select.parents('.form-row').css('overflow', 'visible');

            if (typeof grappelli == 'object') {
                // Set overflow:visible on grappelli fieldset.module .row
                $select.parents('.row').filter(function(i) {
                    return $(this).parent('fieldset.module').length;
                }).css('overflow', 'visible');
                // Set overflow:visible on grappelli tabular module
                $select.parents('td').filter(function(i) {
                    return $(this).parent('.module.table').length;
                }).css('overflow', 'visible');
            }

            options = {};
            if ($select.attr('data-optional')) {
                options['allow_single_deselect'] = true;
            }

            // Initialize Chosen
            $select.chosen(options).change(function(){
            	// If a foreign-key URL defined, convert Chosen selections to links.
            	var fk_url_base = $select.attr('chosen-fk-url-base');
            	var fk_url_target = $select.attr('chosen-fk-url-target') || '_blank';
            	if(fk_url_base){
	            	var chosen_el = $('#'+$select.attr('id')+'_chosen');
	            	$('.chosen-choices .search-choice span', chosen_el).replaceWith(function(){
	            		var el = $(this);
	            		// Lookup object id from the close button.
	            		var index = parseInt($('.search-choice-close', el.parent()).attr('data-option-array-index'));
	            		var id = $select.data('chosen').results_data[index].value;
	            		// Construct link to page for the foreign key object.
	            		var fk_url = fk_url_base + id;
	            	    return '<a class="search-choice-fk-link" href="' + fk_url + '" target="' + fk_url_target + '">' + $.trim(el.text()) + '</a>';
	            	});
	            	// Allow the links to be clicked normally.
            		$('.search-choice-fk-link', chosen_el).parent().parent().unbind('click');
            	}
            }).trigger("change");
            
        });
    });
})((typeof window.django != 'undefined' && typeof django.jQuery.fn.chosen != 'undefined') ? django.jQuery : jQuery);
