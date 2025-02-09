import os
import yt_dlp

def download_single_video(video_url, resolution="720"):
    """Downloads a single YouTube video at the specified resolution."""
    output_folder = "Downloaded_Videos"
    os.makedirs(output_folder, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Save video in the folder
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

if __name__ == "__main__":
    video_url = input("Enter YouTube Video URL: ").strip()
    resolution = input("Enter preferred resolution (e.g., 720, 1080, 480): ").strip()

    if not resolution.isdigit():
        print("Invalid resolution! Defaulting to 720p.")
        resolution = "720"

    download_single_video(video_url, resolution)
