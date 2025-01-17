from application.models import Video


def test_video_insertion(client):
    resp = client.post('/bookmarks/video',
                       data={'header': 'test',
                             'URL': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                             'comment': 'comment'},
                       follow_redirects=True)

    assert resp.status_code == 200

    video = Video.query.one()
    assert video.header == "test"
    assert video.URL == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    assert video.comment == "comment"


def test_add_video_form(client):
    resp = client.get("/bookmarks/video")
    assert resp.status_code == 200

    data = str(resp.data)

    assert '<input type="submit" value="Add a new video"/>' in data


def test_add_video_by_url(client, mock_succesful_api_fetch):
    resp = client.post('/bookmarks/video', data={
        'URL': "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}, follow_redirects=True)

    data = str(resp.data)
    assert 'A super cool mocked video' in data


def test_add_video_by_invalid_url(client, mock_failed_api_fetch):
    resp = client.post('/bookmarks/video', data={
        'URL': "This is not an youtube url???"}, follow_redirects=True)

    data = str(resp.data)
    assert 'Check the link' in data
