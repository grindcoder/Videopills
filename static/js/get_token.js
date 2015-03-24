jQuery(document).ready(function(){
    jQuery('#submit_get_token').click(function(){
       alert('ciao');
        jQuery.ajax({
                url: '/api-token-auth/',
                type : "POST",
                data: {
                    username: jQuery('#user').val(),
                    password: jQuery('#pass').val()
                }
            }
        ).done(function( data ) {
            resp = JSON.parse(data) || jQuery.parseJSON(data);
            jQuery('#result').html(resp['token']);
  });
    });
});