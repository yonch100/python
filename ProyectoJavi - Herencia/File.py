import self as self

class File:

    def __init__(self, path:str):
        """
        :param path: String
        """
        self.path = path
        self.size = 0.0
        self.info = ""
        self.contents = []


    def add_content(self, content:str):
        """
        :param content: se recibe un string para que se agrege a la lista contents
        :return:
        """
        #self.content = content
        self.contents.append(content)


#Analisar este metodo
    def size(self, size):
        """
        :param size:
        :return:
        """
        size = 0
        for content in self.contents:
            size += len(content)
        return size


    def info(self):
        """
        :return: regresa ""
        """
        var_size = self.size()
        return f"path {self.path} [size = {var_size}B]"

#--------------------------------------------------------------------------------------------------

class MediaFile(File):

    def __init__(self,path:str, codec:str, geoloc:tuple, duracion: int):
        """
        :param path: (heredadod de file)
        :param codec: (heredadod de file)
        :param geoloc: (heredadod de file)

        :param duracion: atributo de clase, duracion de Mediafile
        """
        super().__init__(path)
        self.codec = codec
        self.geoloc = geoloc
        self.duracion = duracion

        def info(self):
            return super().info() + f"codec: {self.codec} Geolocalizacion: {self.geoloc} Duracion: {self.duracion}"

# --------------------------------------------------------------------------------------------------

class VideoFile(MediaFile):

    def __init__(self, path:str, codec:str, geoloc:tuple, duracion: int, dimension: tuple):
        """
        :param dimension: Tuple
        """
        super().__init__(path, codec, geoloc, duracion)
        self.dimension = dimension

    def info(self):
        return super().info() + f"Dimensiones: {self.dimension}"

# --------------------------------------------------------------------------------------------------


File = VideoFile("/home/python/video.mp4", "codec x10", (25.5454, 31.4343), 487, (1920, 1080) )

