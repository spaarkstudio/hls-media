import os
from hls_media.core.hffmpeg import Ffmpeg
from hls_media.core.quality_settings import QualitySettings

class MasterHls:
    def __init__(self):
        self.__composer__ = [
            "#EXTM3U",
            "#EXT-X-VERSION:3",
        ]
    
    def add_field(self, quality: QualitySettings, absolute_path: str, hls_file: str):
        self.__composer__.extend([
            f"#EXT-X-STREAM-INF:BANDWIDTH={quality.bitrate},RESOLUTION={Ffmpeg.get_dimension(absolute_path)},FRAME-RATE={quality.fps}",
            hls_file,
        ])
    
    def save(self, output_path: str):
        with open(os.path.join(output_path, ".m3u8"), "w", encoding="utf-8") as saveMaster:
            saveMaster.write("\n".join(self.__composer__))
