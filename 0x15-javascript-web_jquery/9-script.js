(function ($) {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      const hello = $('#hello');
      hello.text(data.hello);
    }
  });
})(window.jQuery);
