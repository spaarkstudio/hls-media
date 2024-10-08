import subprocess
import re
from hls_media.core.quality_settings import QualitySettings

class Ffmpeg:
    @classmethod
    def render(cls, quality: QualitySettings, input_file: str, output_file: str):
        subprocess.Popen([
            "ffmpeg",
            "-i", input_file,
            "-c:v", "libx264",
            "-c:a", "aac",
            "-vf", f"scale=-1:{quality.dimension},fps={quality.fps},pad=ceil(iw/2)*2:ceil(ih/2)*2",
            "-b:v", str(quality.bitrate),
            "-hls_time", str(quality.time_per_segment),
            "-hls_list_size", "0",
            "-f", "hls",
            output_file,
        ]).wait()

    @classmethod
    def get_dimension(cls, input_file: str):
        result = subprocess.run([
            "ffmpeg", "-i", input_file
        ], capture_output = True)

        dimension = re.search(r'\b\d+x\d+\b', result.stderr.decode()).group() # type: ignore

        return dimension
