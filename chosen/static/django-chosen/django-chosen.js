(function(){
    var is_django = typeof(django) !== "undefined";
    if (is_django) {
        document.write('<style>.form-row { overflow: visible }</style>');
    }
    if (typeof(window.jQuery) === "undefined") {
        if (is_django) {
            if (typeof(django.jQuery) !== "undefined") {
                window.jQuery = django.jQuery;
            } else {
                throw "Cannot find jQuery in django";
            }
        } else {
            throw "Cannot find jQuery or django";
        }
    }
    window.jQuery(function() {
        jQuery(".chzn-select").chosen();
    });
})()