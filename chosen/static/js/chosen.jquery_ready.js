(function ($) {
    $(function () {
	    $(".chzn-select").chosen();
	});
})((typeof window.jQuery == 'undefined' && typeof window.django != 'undefined')
  ? django.jQuery
  : jQuery
);