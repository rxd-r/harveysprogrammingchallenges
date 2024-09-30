class Picture:
    description: str
    width: int
    height: int
    frameColour: str

    def __init__(self, desc: str, w: int, h: int, col: str):
        self.description = desc
        self.width = w
        self.height = h
        self.frameColour = col

    @property
    def string_rep (self) -> str:
        return f"{{description: \"{self.description}\", width: {self.width}, height: {self.height}, frame_colour: \"{self.frameColour}\"}}"

    @staticmethod
    def read_in ():
        pics = []
        try:
            with open('pictures.txt', 'r') as file:
                desc = None
                width = -1
                height = -1
                col = None

                for line in file:
                    if desc is None:
                        desc = line.strip()
                    elif width == -1:
                        width = int(line)
                    elif height == -1:
                        height = int(line)
                    elif col is None:
                        col = line.strip()

                        pics.append(Picture(desc, width, height, col))
                        desc = None
                        width = -1
                        height = -1
                        col = None
        except:
            print("Error")

        print("Read in pics")
        for pic in pics:
            print(pic.string_rep)