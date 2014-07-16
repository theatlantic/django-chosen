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

    $(function () {
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
            $select.chosen(options);
        });
    });
})((typeof window.django != 'undefined') ? django.jQuery : jQuery);
