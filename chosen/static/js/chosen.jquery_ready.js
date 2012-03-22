(function ($) {
    $(function () {
        $(".chzn-select").each(function(i, select) {
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

            // Initialize Chosen
            $select.chosen();
        });
    });
})((typeof window.django != 'undefined') ? django.jQuery : jQuery);