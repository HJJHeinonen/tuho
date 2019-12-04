def test_book_insertion(client):
    rv = client.post('/bookmarks',
                     data=dict(
                         header='test',
                         writer='writer',
                         ISBN=123,
                         comment='comment'
                     ),
                     follow_redirects=True)
    assert b'test' in rv.data


def test_nonuniq_isbn_not_added(client):
    bookData = dict(header='test',
                    writer='writer',
                    ISBN=1234,
                    comment='comment')
    client.post('/bookmarks', data=bookData, follow_redirects=True)
    rv = client.post('/bookmarks', data=bookData, follow_redirects=True)
    print(str(rv.data))
    assert b'Book with given ISBN is already in the database' in rv.data


def test_add_video_form(client):
    resp = client.get("/bookmarks/new")
    assert resp.status_code == 200

    data = str(resp.data)

    assert '<input type="submit" value="Add a new book"/>' in data