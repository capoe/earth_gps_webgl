
function load_json_ajax(url) {
    var j = [];
    $.ajax({
      type: 'GET',
      url: url,
      dataType: 'json',
      success: function(data) { j = data; },
      async: false
    });
    return j;
}
