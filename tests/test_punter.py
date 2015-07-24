from punter import api

def test_search():
    assert(api.search('www.google.com') == 'www.goeeogle.com')