class File2:
    def __init__(self, path: str):
        self.path = path
        self.contents = []

    def add_content(self, content: str):
        self.contents.append(content)

    def size(self):
        size = 0
        for content in self.contents:
            size += len(content)
        return size

    def info(self):
        var_size = self.size()
        return f"Path: {self.path} [size = {var_size}B] "





class MediaFile(File2):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int):
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duration = duration

    def info(self):
        return super().info() + f"Codec: {self.codec}, Geolocalizacion: " \
                                f"{self.geoloc}, Duracion: {self.duration}s "





class VideoFile(MediaFile):
    def __init__(self, path: str, codec: str, geoloc: tuple, duration: int,
                 dimensions: tuple):
        super().__init__(path, codec, geoloc, duration)
        self.dimensions = dimensions

    def info(self):
        return super().info() + f"Dimensions: {self.dimensions}"





videofile = VideoFile("fake/path/path.mp4", "h34d", (12345.8, 123456.9), 50,
                      (1900, 800))
videofile.add_content("audio/ogg")
videofile.add_content("video/webm")
print(videofile.info())