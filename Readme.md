# Steam game list

## Introduction
- Display special game list which sort by discount on [Steam](https://store.steampowered.com/search/?specials=1)

## Requirements
If you want run this project, the requirements are as follows:
- Python 3
- MySQL
- Django

## Usage
1. Use [SteamGameListCrawler](https://github.com/youmu257/SteamGameListCrawler) to get the game list and write to database.
Run the command ```python SteamGameListCrawler.py --db```
2. Start the Django server.
Run the command ```python manage.py runserver 0.0.0.0:8000```
3. Open the browser and go to "http://localhost:8000".
You can see the special game list.