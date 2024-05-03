import yt_dlp

def download_audio(url, output_path='~/Music/yt_dlp_downloads'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'writethumbnail': True,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            },
            {
                'key': 'EmbedThumbnail',
                'already_have_thumbnail': False,
            },
            {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            },
        ], 
        'outtmpl': output_path + '/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    if url == "":
        print("No URL provided")
        exit(1)

    if "&list=" in url:
        print("Detected playlist, do you want to download the whole playlist? (y/n)")
        choice = input()
        if choice.lower() == "n":
            download_audio(url)
            exit(1)
        elif choice.lower() == "y":
            playlist_info = yt_dlp.YoutubeDL().extract_info(url, download=False, process=False, extra_info={})
            download_audio(url, output_path='~/Music/yt_dlp_downloads/' + playlist_info['title'])
        else:
            print("Invalid choice, please choose 'y' or 'n', exiting...")
            exit(1)
            
    else:
        download_audio(url)

