function redirect(route)
{
    var arguments = "?q="+document.getElementById('search_field').value;
    window.location = "http://localhost:5000/"+route+arguments;
}

function alt_redirect(route)
{
    window.location = "http://localhost:5000/"+route;
}