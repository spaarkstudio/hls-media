from hls_media.core.hffmpeg import Ffmpeg
from hls_media.core.quality_settings import QualitySettings
import os

class HlsMedia:
    def __init__(self):
        self.__qualities__ = [
            QualitySettings(dimension=144, bitrate=500000, fps=30, time_per_segment=5),
            QualitySettings(dimension=240, bitrate=800000, fps=30, time_per_segment=5),
            QualitySettings(dimension=360, bitrate=1250000, fps=30, time_per_segment=5),
            QualitySettings(dimension=480, bitrate=2500000, fps=30, time_per_segment=5),
            QualitySettings(dimension=720, bitrate=6000000, fps=60, time_per_segment=5),
            QualitySettings(dimension=1080, bitrate=12000000, fps=60, time_per_segment=5),
        ]
    
    def apply_preset(self, qualities: list[QualitySettings]):
        self.__qualities__ = qualities
    
    def set_quality(self, index: int, quality: QualitySettings):
        self.__qualities__[index] = quality
    
    def remove_quality(self, index: int):
        del self.__qualities__[index]
    
    def render(self, input_file: str, output_path: str):
        for index in range(len(self.__qualities__)):
            self.render_only(index, input_file, output_path)
    
    def render_only(self, index: int, input_file: str, output_path: str):
        if len(self.__qualities__) < index - 1:
            raise IndexError("Selected quality index goes out of qualities length.")

        absolute_path = os.path.join(output_path, str(self.__qualities__[index].dimension))
        try:
            os.makedirs(absolute_path)
        except:
            pass

        output_file = os.path.join(absolute_path, ".m3u8")

        Ffmpeg.render(self.__qualities__[index], input_file, output_file)