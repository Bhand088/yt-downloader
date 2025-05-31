from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"\n📥 Downloading: {yt.title}")
        stream.download()
        print("✅ Download complete!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    download_video(video_url)
