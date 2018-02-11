$(document).ready(function(){
	//alert( "welcome" );
	$('#category_comment').hide();
  $('#loading_indicator').hide();
  $('#submit_completed_alert').hide();

	$('#categories').click(function(){
		$('#category_comment').toggle();
	});

	$('#submit_request').click(function(){
        $('#loading_indicator').show();
        $('#submit_completed_alert').hide();
        if ($("#categories").is(":checked")) {
            console.log("AJAX STARTED!")
            var text_form = document.getElementById("text_form").value;
            var category = $('#category_comment').val()
            $.ajax({
              url: "http://127.0.0.1:5000/niog",
              dataType: "json",
              method: "POST",
              data: {
                category: category,
                text_form: text_form
              },
              success: function(data){
              console.log("AJAX ENDED")
          	  $('#loading_indicator').hide();
          	  $('#submit_completed_alert').show();
              $("#result_text_form").val(data);
          }
    	});
    }

	});

});