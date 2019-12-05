import re

from flask import abort, redirect, render_template, request, url_for
from sqlalchemy_filters import apply_filters, apply_pagination

from application.app import app, db
from application.models import Bookmark


@app.route("/")
def index():
    return redirect(url_for("bookmarks_list"))


@app.route("/list", methods=["GET"])
def bookmarks_list():
    page = request.args.get('page', 1, type=int)
    filter_type = request.args.get('type', type=int)

    bookmarks = Bookmark.query
    types = list({(b.__class__.__name__, b.type) for b in bookmarks})

    if filter_type:
        filter_spec = [{'field': 'type', 'op': '==', 'value': filter_type}]
        bookmarks = apply_filters(bookmarks, filter_spec)

    bookmarks, pagination = apply_pagination(bookmarks, page_number=page,
                                             page_size=5)

    page = pagination.page_number
    next_url = url_for('bookmarks_list', page=page + 1) \
        if page < pagination.num_pages else None
    prev_url = url_for('bookmarks_list', page=page - 1) \
        if page > 1 else None

    return render_template("list.html", bookmarks=bookmarks, types=types,
                           next_url=next_url, prev_url=prev_url, current=page)


@app.route("/bookmark/<bookmark_id>", methods=["GET"])
def get_bookmark(bookmark_id):
    try:
        int(bookmark_id)
        assert Bookmark.query.get(bookmark_id)
    except (ValueError, AssertionError):
        abort(404)
    bookmark = db.session.query(Bookmark).get(bookmark_id)

    if bookmark.type == Bookmark.TYPE_BOOK:
        return render_template("bookmarks/book/details.html", book=bookmark)
    elif bookmark.type == Bookmark.TYPE_VIDEO:
        yt = "https://www.youtube-nocookie.com/embed/"
        timestamp = request.args.get('timestamp')
        # substitute non-ID part with embed-URL
        embed = re.sub(r'http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)' +
                       r'(&(amp;)?[\w\?=]*)?', yt, bookmark.URL)
        timestamp = request.args.get('timestamp')
        print("timestamp: ", timestamp)
        if timestamp:
            embed += '?start=' + str(timestamp)
        print(embed)
        return render_template("bookmarks/video/details.html", video=bookmark,
                               embed=embed)

    abort(404)


@app.route("/bookmark/delete/<bookmark_id>", methods=["GET"])
def delete_bookmark(bookmark_id):
    Bookmark.query.get_or_404(bookmark_id)  # To check if bookmark is found on db

    db.session.query(Bookmark).filter(Bookmark.id == bookmark_id).delete()
    db.session.commit()

    return redirect(url_for("bookmarks_list"))


@app.route("/bookmarks/edit/<bookmark_id>", methods=["GET"])
def bookmarks_edit(bookmark_id):
    bookmark = Bookmark.query.get_or_404(bookmark_id)

    if bookmark.type == Bookmark.TYPE_BOOK:
        return redirect(url_for("book_update", book_id=bookmark_id, bookmark=bookmark))
    elif bookmark.type == Bookmark.TYPE_VIDEO:
        return redirect(url_for("video_update", video_id=bookmark_id, bookmark=bookmark))

    abort(404)