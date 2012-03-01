if (typeof(jQuery) === "undefined") {
    if (typeof("django") === "object" && typeof(django.jQuery) === "object") {
        jQuery = django.jQuery;
    } else {
        throw "Cannot find jQuery";
    }
}
jQuery(function() {
    jQuery(".chzn-select").chosen();
});