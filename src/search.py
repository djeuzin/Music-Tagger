import musicbrainzngs

musicbrainzngs.set_useragent("test", "0.1", "seu@email.com")

def get_albums(track: str) -> list[(str, str)] | None:
	query = musicbrainzngs.search_recordings(query=track)

	result = []
	ids = []
	i = 0

	recording = query['recording-list']

	for release in recording:
		if not release.get('release-list'):
			continue	

		if i == 3: break

		release_title = release['release-list'][0]['title']
		release_year = release['release-list'][0].get('date')


		if release['release-list'][0]['id'] not in ids:
			result.append((release_title, release_year))
			ids.append(release['release-list'][0]["id"])
			i += 1
	
	return result