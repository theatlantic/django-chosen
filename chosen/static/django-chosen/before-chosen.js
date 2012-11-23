window.prevjQuery = window.jQuery;
window.jQuery = (typeof window.django != 'undefined') ? django.jQuery : window.prevjQuery;
