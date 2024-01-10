(function ($) {
  const toggleHeader = $('#toggle_header');

  toggleHeader.click(function () {
    const header = $('header');

    if (header.hasClass('green')) {
      header.removeClass('green').addClass('red');
    } else if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    }
  });
})(window.jQuery);
