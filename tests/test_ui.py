from time import sleep


def test_open_url(browser):
    assert "Bookmarks" in browser.title
