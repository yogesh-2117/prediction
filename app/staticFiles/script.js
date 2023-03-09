function ConvertFormToJSON(form){
    var array = jQuery(form).serializeArray();
    var json = {};

    jQuery.each(array, function() {
        json[this.name] = this.value || '';
       });

    return json;
}
    $(function() {
$('button').click(function(e) {
    e.preventDefault()
    var json = ConvertFormToJSON($('form'));
    console.log(json)
    $.ajax({
        url: '/predict',
        data: JSON.stringify(json),
          dataType: "json",
        type: 'POST',
        contentType: "application/json",
        success: function(response) {
            console.log(response);
            alert("Accident Severity is predicted as:"+response.result)
        },
        error: function(error) {
            console.log(error);
        }
    });
});
});