# imgurbackups

Imgur is removing old content https://help.imgur.com/hc/en-us/articles/14415587638029/
> We will be focused on removing old, unused, and inactive content that is not tied to a user account 

before the days of Giphy, I had organized bookmarks for all of my gif reactions. Wanted to try to save whatever was left (found that a lot of the links actually died already)

Here are the steps:

0) get an Imgur API Client ID: https://api.imgur.com/oauth2/addclient (use `https://www.getpostman.com/oauth2/callback` as callback URL)
1) Export your Chrome Bookmarks from Bookmarks Manager. name the file `bookmarks.html`
2) `python bookmarkconvert.py` (requires `pip install beautifulsoup4`)
3) Check your `bookmarks.csv` file for any errors
4) add your Imgur Client ID to the `imgurdownload.py` script
5) `python imgurdownload.py`

![Thumbs Up](https://i.imgur.com/FSGvo.gif)