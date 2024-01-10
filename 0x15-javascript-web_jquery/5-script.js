(function ($) {
  const addItem = $('#add_item');

  addItem.click(function () {
    const ul = $('ul');

    if (ul.hasClass('my_list')) {
      ul.append('<li>Item</li>');
    }
  });
})(window.jQuery);
