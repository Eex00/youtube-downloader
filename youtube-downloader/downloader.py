import yt_dlp

def download_video(url, save_path='.'):
    try:
        # Set up download options
        ydl_opts = {
            'outtmpl': save_path + '/%(title)s.%(ext)s',  # Save video with title as filename
        }
        
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
        
        print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask user for YouTube link
    url = input("Enter the YouTube video URL: ")
    # Ask for the path where you want to save the video
    save_path = input("Enter the directory to save the video (or press Enter to save in the current directory): ")
    if not save_path:
        save_path = '.'

    download_video(url, save_path)
