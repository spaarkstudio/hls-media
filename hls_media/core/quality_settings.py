class QualitySettings:
    def __init__(self, dimension: int, bitrate: int, fps: int, time_per_segment: int = 3):
        self.dimension = dimension
        self.bitrate = bitrate
        self.fps = fps
        self.time_per_segment = time_per_segment