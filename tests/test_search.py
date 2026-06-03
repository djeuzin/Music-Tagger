from src.search import get_albums

def test_get_right_amout_of_albums(mocker):
    mock_response = {
	    "recording-list": [
	        {
	            "release-list": [
	                {"title": "Manual", "date": "2015", "id": "abc123"},
	            ]
	        },
	        {
	            "release-list": [
	                {"title": "Manual", "date": "2015", "id": "abc123"},  # duplicata
	            ]
	        },
	        {
	            "release-list": [
	                {"title": "Levitation Sessions", "date": "2020", "id": "def456"},
	            ]
	        },
	        {
	            "release-list": [
	                {"title": "Paste Sampler", "date": "2016", "id": "ghi789"},
	            ]
	        },
	    ]
	}
    mocker.patch("src.search.musicbrainzngs.search_recordings", return_value=mock_response)
    assert len(get_albums("Benzin")) == 3

def test_no_duplicate_releases(mocker):
	mock_response = {
	    "recording-list": [
	        {
	            "release-list": [
	                {"title": "Manual", "date": "2015", "id": "abc123"},
	            ]
	        },
	        {
	            "release-list": [
	                {"title": "Manual", "date": "2015", "id": "abc123"},  # duplicata
	            ]
	        },
	        {
	            "release-list": [
	                {"title": "Levitation Sessions", "date": "2020", "id": "def456"},
	            ]
	        },
	        {
	            "release-list": [
	                {"title": "Paste Sampler", "date": "2016", "id": "ghi789"},
	            ]
	        },
	    ]
	}
	mocker.patch("src.search.musicbrainzngs.search_recordings", return_value=mock_response)
	albums = get_albums("Benzin")
	assert albums[0] != albums[1] and albums[1] != albums[2] and albums[0] != albums[2]

def test_empty_release_list(mocker):
	mock_response = { "recording-list": [ ] }
	mocker.patch("src.search.musicbrainzngs.search_recordings", return_value=mock_response)
	albums = get_albums("Benzin")
	assert len(albums) == 0

def test_no_release_list(mocker):
	mock_response = {"recording-list": [{"release-list": []}]}
	mocker.patch("src.search.musicbrainzngs.search_recordings", return_value=mock_response)
	albums = get_albums("Benzin")
	assert len(albums) == 0

def test_no_date_release(mocker):
	mock_response = {
	    "recording-list": [
	        {
	            "release-list": [
	                {"title": "Manual", "id": "abc123"},
	            ]
	        },
	        {
	            "release-list": [
	                {"title": "Manual", "id": "abc123"},  # duplicata
	            ]
	        },
	        {
	            "release-list": [
	                {"title": "Levitation Sessions", "id": "def456"},
	            ]
	        },
	        {
	            "release-list": [
	                {"title": "Paste Sampler", "id": "ghi789"},
	            ]
	        },
	    ]
	}
	mocker.patch("src.search.musicbrainzngs.search_recordings", return_value=mock_response)
	albums = get_albums("Benzin")
	assert all(album[1] is None for album in albums)