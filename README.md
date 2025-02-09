# YouTube Playlist Downloader (yt-dlp)

This Python script allows you to download an entire YouTube playlist at a selected resolution using `yt-dlp`. It ensures high-quality downloads, bypasses YouTube restrictions, and saves videos in an organized manner.

## 🚀 Features

✅ Download full YouTube playlists  
✅ Select video resolution (e.g., 720p, 1080p, 480p)  
✅ Merges video and audio automatically  
✅ Bypasses YouTube's download restrictions (No 403 Forbidden errors)  
✅ Creates a folder with the playlist name

---

## 📦 Installation

1. **Install Python** (if not installed):  
   [Download Python](https://www.python.org/downloads/)

2. **Install `yt-dlp`**:

   ```sh
   pip install yt-dlp
   ```

3. **Clone this repository**:
   ```sh
   git clone https://github.com/lvimuth/youtube-playlist-downloader.git
   cd youtube-playlist-downloader
   ```

---

## 🎬 How to Use

1. **Run the script**:

   ```sh
   python youtube_playlist_downloader.py
   ```

2. **Enter the playlist URL** when prompted.

3. **Enter the preferred resolution** (e.g., `720`, `1080`, `480`).

4. The script will create a folder with the playlist name and download all videos.

---

## 📁 Example Folder Structure

```
/YouTube_Playlist_Name
  ├── Video_1.mp4
  ├── Video_2.mp4
  ├── Video_3.mp4
```

---

## ❌ Troubleshooting

- **Getting a 403 Forbidden error?**

  - This script already bypasses common restrictions, but ensure `yt-dlp` is updated:
    ```sh
    pip install --upgrade yt-dlp
    ```

- **Download speed is slow?**

  - Use a VPN or try a different network.

- **Some videos fail to download?**
  - YouTube may restrict certain videos. Try downloading them individually.

---

## 🛠 License

This project is licensed under the MIT License.

**Happy downloading! 🎥✨**
