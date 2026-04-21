
# 🎵 Billboard to Spotify Playlist Generator

This Python project allows you to **travel back in time musically** 🎶 by scraping the *Billboard Hot 100* chart for any given date and automatically creating (or updating) a Spotify playlist with those songs.

---

## 📌 Features

* Scrapes **Billboard Hot 100** songs for a specific date
* Searches each song on Spotify
* Adds songs to a Spotify playlist automatically
* Handles missing songs gracefully
* Uses environment variables for security

---

## 🛠️ Technologies Used

* Python
* `requests` – for HTTP requests
* `BeautifulSoup` – for web scraping
* `spotipy` – Spotify API wrapper
* `python-dotenv` – for environment variable management

---

## 📂 Project Structure

```
.
├── main.py
├── .env
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/billboard-spotify-playlist.git
cd billboard-spotify-playlist
```

---

### 2. Install Dependencies

```bash
pip install requests spotipy beautifulsoup4 python-dotenv
```

---

### 3. Spotify Developer Setup

1. Go to Spotify Developer Dashboard
2. Create a new app
3. Get:

   * `CLIENT_ID`
   * `CLIENT_SECRET`
4. Set Redirect URI to:

   ```
   http://127.0.0.1:8080
   ```

---

### 4. Create `.env` File

```env
CLIENTID=your_client_id
CLIENTSECRET=your_client_secret
PLAYLIST_ID=your_playlist_id
```

---

## ▶️ How to Run

```bash
python main.py
```

Enter a date when prompted:

```
Which year do you want to travel to? Type the date in the format YYYY-MM-DD:
```

Example:

```
2005-08-13
```

---

## 🔄 How It Works

1. Takes user input (date)
2. Scrapes Billboard Hot 100 songs for that date
3. Searches each song on Spotify
4. Collects track URIs
5. Adds them to the specified playlist

---

## ⚠️ Notes

* Some songs may not be available on Spotify and will be skipped
* Ensure your Spotify account has permission to modify the playlist
* Keep your `.env` file private 

---

## 🚀 Future Improvements

* Automatically create a new playlist instead of using an existing one
* Add better error handling
* Improve song matching accuracy
* Add a GUI interface

---

## 🙌 Acknowledgements

* Billboard for chart data
* Spotify Web API
* Spotipy library

