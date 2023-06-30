from mal import AnimeSearch
from mal import MangaSearch
from mal import Anime
from mal import Manga
from mal import config

season=""

def risultatiAnime(n):
	info = []
	item=animeSearch.results[n]
	print(item)
	if item.type=="TV":
		id=item.mal_id
		anime = Anime(id)
		info.append(item.image_url)
		info.append(item.title)
		info.append(item.type)
		info.append(item.episodes)
		info.append(anime.aired)
		info.append(item.synopsis)
	return info

def risultatiManga(n):
	info=[]
	item = mangaSearch.results[n]
	print(item)
	if item.type=="Manga":
		id=item.mal_id
		manga = Manga(id)
		info.append(item.image_url)
		info.append(item.title)
		info.append(item.type)
		info.append(manga.volumes)
		info.append(manga.chapters)
		info.append(item.synopsis)
	return info

def setAnime(animetitle):
	global anime,season,animeSearch
	anime=animetitle
	animeSearch = AnimeSearch(str(anime))
	lunghezza=len(animeSearch.results)
	return lunghezza

def setManga(mangatitle):
	global manga,mangaSearch
	manga=mangatitle
	mangaSearch = MangaSearch(str(manga))
	lunghezza=len(mangaSearch.results)
	return lunghezza

def setSeason(seasonnumber):
	global season
	season="season "+ seasonnumber
	