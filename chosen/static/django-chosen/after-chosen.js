(function ($) {
    $(function () {
        $(".chzn-select").each(function(i, select) {
            var options, $select = $(select);

            // Set overflow:visible on parent .form-row for django admin
            $select.parents('.form-row').css('overflow', 'visible');

            if (typeof grappelli === 'object') {
                // Set overflow:visible on grappelli fieldset.module .row
                $select.parents('.row').filter(function(i) {
                    return $(this).parent('fieldset.module').length;
                }).css('overflow', 'visible');
                // Set overflow:visible on grappelli tabular module
                $select.parents('td').filter(function(i) {
                    return $(this).parent('.module.table').length;
                }).css('overflow', 'visible');
            }

            // Initialize Chosen, read options from data-chosen attribute
            try {
                options = $.parseJSON($select.attr('data-chosen'));
            } catch (e) {
                options = {};
            }
            // Set i18n options
            if (typeof gettext !== 'undefined') {
                options = $.extend({
                    no_results_text: gettext('No results match')
                }, options);
            }
            $select.chosen(options);
        });
    });
})(window.jQuery);

window.jQuery = window.prevjQuery;
