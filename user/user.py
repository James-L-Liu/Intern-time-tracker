from flask import Blueprint, render_template, url_for, request
import music.album.services as utilities

user_blueprint = Blueprint('user_bp', __name__)


@user_blueprint.route('/users', methods=['GET'])
def get_album_by_id(album_id):
    tracks_by_album, album_selected = utilities.extract_track_by_album(album_id)
    number_of_tracks = len(tracks_by_album)
    tracks_per_page = 80
    pages = ceil(number_of_tracks / tracks_per_page)
    page_number = request.args.get('page_number')
    if page_number is not None:
        page_number = int(page_number)
    else:
        page_number = 1

    return render_template('album/album.html',
                           tracks=tracks_by_album,
                           album=album_selected,
                           pages=pages,
                           page_num=int(page_number),
                           tracks_per_page=tracks_per_page,
                           id=album_id)

@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    all_users = Data.query.all()
    return render_template('crud_users.html', all_users)

@album_blueprint.route('/album', methods=['GET'])
def get_all_album():
    return render_template('album/album1.html', albums=utilities.get_all_albums())

