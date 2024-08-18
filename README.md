<h1 align=center>
  HLS Media
</h1>
<p align=center>
  Convert any video format to web-ready m3u8 with qualities options using FFmpeg.
</p>

## Usage
```python
from hls_media import HlsMedia

media = HlsMedia()

# There's already a default qualities preset.
# You can go ahead and render.
media.render("video.mov", "video_folder")
```

Default qualities preset:
```python
[
  QualitySettings(dimension=144, bitrate=500000, fps=30, time_per_segment=5),
  QualitySettings(dimension=240, bitrate=800000, fps=30, time_per_segment=5),
  QualitySettings(dimension=360, bitrate=1250000, fps=30, time_per_segment=5),
  QualitySettings(dimension=480, bitrate=2500000, fps=30, time_per_segment=5),
  QualitySettings(dimension=720, bitrate=6000000, fps=60, time_per_segment=5),
  QualitySettings(dimension=1080, bitrate=12000000, fps=60, time_per_segment=5),
]
```

You can always render only one quality set using `.render_only()`:
```python
from hls_media import HlsMedia

media = HlsMedia()

# There's already a default qualities preset.
# You can go ahead and render.
media.render_only("video.mov", "video_folder")
```

To replace with a whole new set of preset, use `.apply_preset()`:
```python
from hls_media import HlsMedia
from hls_media.core.quality_settings import QualitySettings

media = HlsMedia()

media.apply_preset([
  QualitySettings(dimension=720, bitrate=2000000, fps=30, time_per_segment=5),
  QualitySettings(dimension=1080, bitrate=5000000, fps=30, time_per_segment=5),
])

media.render("video.mov", "video_folder")
```

To change one quality settings in preset, use `.setQuality()`:
```python
from hls_media import HlsMedia
from hls_media.core.quality_settings import QualitySettings

media = HlsMedia()

media.setQuality(index=0, quality=QualitySettings(dimension=1080, bitrate=12000000, fps=60, time_per_segment=5))

media.render("video.mov", "video_folder")
```

To delete one quality settings in preset, use `.removeQuality()`:
```python
from hls_media import HlsMedia

media = HlsMedia()

media.removeQuality(index=0)

media.render("video.mov", "video_folder")
```