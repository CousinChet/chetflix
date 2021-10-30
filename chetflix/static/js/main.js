// const date = new Date();
// document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);


// spinner
$('.loading').on('click',function(){
	var $btn = $(this);
		$btn.button('loading');
		setTimeout(function(){
   		$btn.button('reset');
	},2000);
});
