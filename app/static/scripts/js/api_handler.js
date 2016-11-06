/**
 * Function that handle Event Binding.
 */

$(function() {
      $.ajax({
          url: $SCRIPT_ROOT + '/users',
          type: 'GET',
      }).then(function(data) {
          console.log(data);
          $("#result").text(data);
      });

    //GetUsers
    $('a#requestPost').bind('click', function() {
      var user_id = $('#txtUser').val();
      $.ajax({
          url: $SCRIPT_ROOT + '/users/'+user_id,
          type: 'GET',
      }).then(function(data) {
          console.log(data);
          $("#result").text(data.result);
      });
    });

    //Patch Request
    $('a#updatePost').bind('click', function() {
        var user_id = $('#txtUser').val();
        var message = {
                name: $('#txtName').val(),
                email: $('#txtEmail').val(),
                username: $('#txtUserName').val()
        }
        //Using Lodash to omit any value that isn't defined or empty
        var data = _(message).omitBy(_.isUndefined).omitBy(_.isEmpty).value();
        console.log(result);
        $.ajax({
            url: $SCRIPT_ROOT + '/users/'+user_id,
            type: 'PATCH',
            data: data,
        }).then(function(data) {
            console.log(data);
            $("#result").text(data.result);
        });
    });
});

