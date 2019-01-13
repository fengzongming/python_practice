class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance
        else:
            return cls.instance

m1 = MusicPlayer()
print(m1)

m2 = MusicPlayer()
print(m2)

