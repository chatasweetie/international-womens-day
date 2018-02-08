var $mediaElements = $('.link-card-pad');

$('.filter_link').click(function(e){
    e.preventDefault();
    console.log("active")
    // get the category from the attribute
    var filterVal = $(this).data('filter');

    if(filterVal === 'all'){
      $mediaElements.show();
    }else{
       // hide all then filter the ones to show
       $mediaElements.hide().filter('.' + filterVal).show();
    }
});

