import os

def setup_files(base_path):
    os.makedirs(base_path, exist_ok=True)

    sample_files = [
        "photo.jpg",
        "video.mp4",
        "document.pdf",
        "song.mp3",
        "notes.txt",
        "archive.zip"
    ]

    for file in sample_files:
        with open(os.path.join(base_path, file), "w") as f:
            f.write("Sample content")

    print("📂 Files BEFORE organizing:")
    print(os.listdir(base_path))
