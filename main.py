import os
import re
import yt_dlp

def sanitize_filename(filename):
    """Removes invalid characters for Windows/Linux/macOS file system."""
    return re.sub(r'[\/:*?"<>|]', '_', filename)

def download_video(video_url, resolution, output_folder):
    """Downloads a YouTube video with the specified resolution."""
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Save videos in the playlist folder
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'merge_output_format': 'mp4',  # Ensures proper format
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Downloading: {video_url} at {resolution}p resolution...")
            ydl.download([video_url])
            print(f"Downloaded successfully!\n")
        except Exception as e:
            print(f"Error downloading {video_url}: {e}")

def download_playlist(playlist_url, resolution="720"):
    """Downloads all videos from a YouTube playlist with the given resolution."""
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
    
    playlist_title = sanitize_filename(info_dict['title']) if 'title' in info_dict else "YouTube_Playlist"
    output_folder = os.path.join(os.getcwd(), playlist_title)
    os.makedirs(output_folder, exist_ok=True)

    print(f"Downloading playlist: {playlist_title}")

    for entry in info_dict.get('entries', []):
        if entry and 'url' in entry:
            download_video(entry['url'], resolution, output_folder)

    print("Playlist download complete!")

if __name__ == "__main__":
    playlist_url = input("Enter YouTube Playlist URL: ").strip()
    resolution = input("Enter preferred resolution (e.g., 720, 1080, 480): ").strip()
    
    if not resolution.isdigit():
        print("Invalid resolution! Defaulting to 720p.")
        resolution = "720"
    
    download_playlist(playlist_url, resolution)
