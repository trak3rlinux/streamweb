function search_func()
{
    var query=document.getElementById('search_text').value;
    document.getElementById('form_search').action='/search/'+query;
    return false;
}