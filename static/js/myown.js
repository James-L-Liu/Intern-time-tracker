$(document).ready(function() {
  var currentRunningNumber = 1;

  yourLogicForCreatingACard(){
  //your normal logic will go here
  afterCreatingNewCard();
  }

  afterCreatingNewCard(){
    var newRunningNumber = currentRunningNumber + 1;
    var newModalName = "modal"+newRunningNumber;
    var newModalToggleName = "#modal"+newRunningNumber;

    $("#modal1").attr("id", newModalName);
    $("#modalToggle").attr("data-target", newModalToggleName);
    currentRunningNumber = newRunningNumber;
  }


});




$(document).ready(function()
{
	$('#edit_user').on('show.bs.modal', function (e)
	{
		var user_id = $(e.relatedTarget).data('user_id');
		$.ajax(
		{
			type : 'POST',
			url  : 'ajaxrequest/ajax_users.php?reg_id=<?= $regid ?>', //Here you will fetch records
			data    : 'user_id='+ user_id, //Pass $user_id
			success : function(result)
					{
						//alert('success'+result);
						$('.fetched_user').html(result); //Show fetched data from database
					},
			error   : function(result)
					{
						alert('error'+result);
					}
		});
	});
});