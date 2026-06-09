from src.tagger import tag_files
from mutagen.flac import FLAC
import io

def make_flac_bytes():
    buf = io.BytesIO()
    audio = FLAC()
    audio.metadata_blocks.append(StreamInfo(
        min_blocksize=16,
        max_blocksize=65536,
        min_framesize=0,
        max_framesize=0,
        sample_rate=44100,
        channels=2,
        bits_per_sample=16,
        total_samples=0,
        md5_signature=b'\x00' * 16
    ))
    audio.save(buf)
    buf.seek(0)
    return buf.read()

mock_response = {
  "release": {
    "id": "5f86db51-2e09-4bd0-bff7-c1a77b676fde",
    "title": "Coisas estranhas",
    "status": "Official",
    "quality": "normal",
    "text-representation": {
      "language": "por"
    },
    "date": "2024-07-19",
    "country": "XW",
    "release-event-list": [
      {
        "date": "2024-07-19",
        "area": {
          "id": "525d4e18-3d00-31b9-a58b-a146a916de8f",
          "name": "[Worldwide]",
          "sort-name": "[Worldwide]",
          "iso-3166-1-code-list": [
            "XW"
          ]
        }
      }
    ],
    "release-event-count": 1,
    "cover-art-archive": {
      "artwork": "true",
      "count": "1",
      "front": "true",
      "back": "false"
    },
    "medium-list": [
      {
        "position": "1",
        "format": "Digital Media",
        "track-list": [
          {
            "id": "ccba9cce-1b41-4d65-b85c-0600810c354d",
            "position": "1",
            "number": "1",
            "length": "158000",
            "recording": {
              "id": "a67a79bf-0dc6-42a9-a2ff-3c0a11e0ca61",
              "title": "Coisas estranhas",
              "length": "158000"
            },
            "track_or_recording_length": "158000"
          },
          {
            "id": "a0464083-f3b7-4156-908f-57a88904d469",
            "position": "2",
            "number": "2",
            "length": "205000",
            "recording": {
              "id": "b9988aff-e159-416d-9b64-52e57d341246",
              "title": "AAAAAAAAA",
              "length": "205000"
            },
            "track_or_recording_length": "205000"
          },
          {
            "id": "c0d39226-b9a6-48f5-a61e-7f051864d451",
            "position": "3",
            "number": "3",
            "length": "204000",
            "recording": {
              "id": "f53abf08-0772-4307-aa7a-d27968741992",
              "title": "Lumin\u00e1ria de lava",
              "length": "204000"
            },
            "track_or_recording_length": "204000"
          },
          {
            "id": "e3a0a462-afbe-4d76-8872-92e3c47ce911",
            "position": "4",
            "number": "4",
            "length": "231000",
            "recording": {
              "id": "b91a1771-abd5-4276-958f-ef9bdbdbead7",
              "title": "Rua da lua cheia",
              "length": "231000"
            },
            "track_or_recording_length": "231000"
          },
          {
            "id": "ce3e9cf5-31fe-4a8f-b66e-1dcbb021d032",
            "position": "5",
            "number": "5",
            "length": "170000",
            "recording": {
              "id": "8d02b9c7-c5e3-4106-8c90-c57ea3394035",
              "title": "M\u00fasica para achar bruxa",
              "length": "170000"
            },
            "track_or_recording_length": "170000"
          },
          {
            "id": "f61dbd61-46ec-4ff8-8399-61fed38100a9",
            "position": "6",
            "number": "6",
            "length": "239000",
            "recording": {
              "id": "1887c9be-ced0-4a1d-9eda-46d963b2c5ff",
              "title": "Sonho estranho",
              "length": "239000"
            },
            "track_or_recording_length": "239000"
          },
          {
            "id": "67331c19-f99c-4959-9ba4-046e1a4aa937",
            "position": "7",
            "number": "7",
            "length": "211000",
            "recording": {
              "id": "001fa1fd-5951-457c-83a2-cd40dc7d7e4b",
              "title": "Pilha eletr\u00f4nica",
              "length": "211000"
            },
            "track_or_recording_length": "211000"
          },
          {
            "id": "c8ef4179-f40b-402d-8a7c-b6c453d3d5ac",
            "position": "8",
            "number": "8",
            "length": "118000",
            "recording": {
              "id": "ccac0244-6c0b-44d0-bb7d-0a2bf78bed2f",
              "title": "Lagartixa tropical",
              "length": "118000"
            },
            "track_or_recording_length": "118000"
          },
          {
            "id": "48e9c593-dbb0-4a46-a067-af98d3e4f98d",
            "position": "9",
            "number": "9",
            "length": "178000",
            "recording": {
              "id": "e4121eb1-2fb3-4d8c-ad3b-0757531329a1",
              "title": "Ver\u00e3o e brech\u00f3",
              "length": "178000"
            },
            "track_or_recording_length": "178000"
          },
          {
            "id": "c4d6c372-db32-4c18-a851-c33fc4810f51",
            "position": "10",
            "number": "10",
            "length": "187000",
            "recording": {
              "id": "72995dca-ee13-4d81-bb60-b31cc3c225ef",
              "title": "Siris paradinhos em um cantinho bem de boa",
              "length": "187000"
            },
            "track_or_recording_length": "187000"
          }
        ],
        "track-count": 10
      }
    ],
    "medium-count": 1
  }
}

def test_no_file_match(mocker):
  mocker.patch("src.tagger.musicbrainzngs.get_release_by_id", return_value=mock_response)
  tagged_files = tag_files([("Benzin", make_flac_bytes())], "id")
  assert tagged_files == []

def test_correctly_tagged_files(mocker):
	mocker.patch("src.tagger.musicbrainzngs.get_release_by_id", return_value=mock_response)
	files_to_tag = [("Pilha eletrônica", make_flac_bytes()), ("Luminária de lava", make_flac_bytes())]
	tagged_files = tag_files(files_to_tag, "id")

	resultado1 = tagged_files[0][1]
	resultado2 = tagged_files[1][1]

	audio1 = FLAC(io.BytesIO(resultado1))
	audio2 = FLAC(io.BytesIO(resultado2))

	assert audio1["title"][0] == "Pilha eletrônica"
	assert audio1["tracknumber"][0] == "7"
	assert audio2["title"][0] == "Luminária de lava"
	assert audio2["tracknumber"][0] == "3"

def test_partial_tagged_files(mocker):
	mocker.patch("src.tagger.musicbrainzngs.get_release_by_id", return_value=mock_response)
	files_to_tag = [("Pilha eletrônica", make_flac_bytes()), ("Luminária de lava", make_flac_bytes()), ("Benzin", make_flac_bytes())]
	tagged_files = tag_files(files_to_tag, "id")
	assert len(tagged_files) == 2

def test_corrupted_file(mocker):
	mocker.patch("src.tagger.musicbrainzngs.get_release_by_id", return_value=mock_response)
	files_to_tag = [("Pilha eletrônica", make_flac_bytes()), ("Arquivo", b'Corrupted bytes')]
	tagged_files = tag_files(files_to_tag, "id")
	assert len(tagged_files) == 1

def test_empty_file_list(mocker):
	mocker.patch("src.tagger.musicbrainzngs.get_release_by_id", return_value=mock_response)
	files_to_tag = []
	tagged_files = tag_files(files_to_tag, "id")
	assert tagged_files == []
