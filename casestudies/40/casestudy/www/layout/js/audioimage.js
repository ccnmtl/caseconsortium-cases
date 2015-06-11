// this snipped of jQuery replaces image elements w/ the audiofile class id 
// with the proper code for inline playing
//

// I can't get replaceWith or replaceAll to work, so here is the equivalent
$.fn.replace = function(o) { return this.after(o).remove(); }; 

$(function() {
    PLAYER_PATH = './players/1pixelout.swf';

    $(".audiofile").each(function() {

	original_src = $(this).attr('src');
	
	audio_player = '<object type="application/x-shockwave-flash"' +
	               'data="' + PLAYER_PATH + '" height="24" width="290">' +
	    '<param name="movie" value="' + PLAYER_PATH + '">' +
	    '<param name="wmode" value="transparent"> <param name="menu" value="false"> <param name="quality" value="high">' +
	    '<param name="FlashVars" value="soundFile=' + original_src + '">' +
	    '<embed src="' + PLAYER_PATH + '" flashvars="soundFile=' + original_src  + '" height="24" width="290">' +
	    '</object>';

	$(this).replace(audio_player);

	/* use 'this' as the dom object, so $(this).attr('class') */
    })
});
