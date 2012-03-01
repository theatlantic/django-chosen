if (typeof(jQuery) === "undefined") {
    if (typeof(django) !== "undefined") {
        if (typeof(django.jQuery) !== "undefined") {
            jQuery = django.jQuery;
        } else {
            throw "Cannot find jQuery in django";
        }
    } else {
        throw "Cannot find jQuery or django";
    }
}
jQuery(function() {
    jQuery(".chzn-select").chosen();
});