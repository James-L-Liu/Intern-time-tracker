import music.adapters.repository as repo
import music.adapters.services as services

def extract_track_by_album(album_id):
    tracks_by_album, album_selected = [], None
    tracks = services.get_tracks(repo.repo_instance)
    for track in tracks:
        if track.album is not None:
            if track.album.album_id == album_id:
                tracks_by_album.append(track)
                album_selected = track.album.title
    return tracks_by_album, album_selected


def get_all_albums():
    return services.get_albums(repo.repo_instance)