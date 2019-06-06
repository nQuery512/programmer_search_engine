function redirect(route, argument_id = "search-field")
{
    var arguments = "?q="+document.getElementById(argument_id).value;
    window.location = "http://localhost:5000/"+route+arguments;
}


function alt_redirect(route)
{
    window.location = "http://localhost:5000/"+route;
}

function generate_color()
{
    return "#"+((1<<24)*Math.random()|0).toString(16)
}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function addEnterEvent(button_id)
{
    $("body").keyup(function(event) {
        if (event.keyCode === 13) {
            $(button_id).click();
        }
    });
}

function getRandomString(char_count) {
  var text = "";
  var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

  for (var i = 0; i < char_count; i++)
    text += possible.charAt(Math.floor(Math.random() * possible.length));

  return text;
}