from hls_media.core.hffmpeg import Ffmpeg
from hls_media.core.quality_settings import QualitySettings
from hls_media.core.master_hls import MasterHls
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
        hls_master = MasterHls()

        for quality in self.__qualities__:
            self.render_custom(quality, input_file, output_path)
            hls_master.add_field(quality, os.path.join(output_path, str(quality.dimension), ".m3u8"), f"{quality.dimension}/.m3u8")
        
        hls_master.save(output_path)
    
    def render_only(self, index: int, input_file: str, output_path: str):
        if len(self.__qualities__) < index - 1:
            raise IndexError("Selected quality index goes out of qualities length preset.")

        self.render_custom(self.__qualities__[index], input_file, output_path)
    
    def render_custom(self, quality: QualitySettings, input_file: str, output_path: str):
        absolute_path = os.path.join(output_path, str(quality.dimension))
        try:
            os.makedirs(absolute_path)
        except:
            pass

        output_file = os.path.join(absolute_path, ".m3u8")

        Ffmpeg.render(quality, input_file, output_file)