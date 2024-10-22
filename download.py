import yt_dlp

# Function to download the latest 10 videos from a channel
def download_latest_videos_from_channel(channel_url, output_path='.'):
    try:
        # Options for downloading the best video quality
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Best video and audio
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Output path and filename
            'noplaylist': False,  # Ensure that we download the playlist (all videos)
            'yes-playlist': True,  # Enable downloading all videos from the channel
            'merge_output_format': 'mp4',  # Merged output format
            'max_downloads': 20,  # Limit to the latest 10 videos
        }

        # Download the latest videos
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([channel_url])
        print("Download complete! Latest 10 videos downloaded.")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
channel_url = input("Enter the YouTube channel URL: ")
output_path = input("Enter output path (or press Enter for current directory): ")
download_latest_videos_from_channel(channel_url, output_path if output_path else '.')
