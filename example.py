from hls_media import HlsMedia

media = HlsMedia()

# There's already a default quality preset.
# You can go ahead and render.
media.render("video.mov", "video_folder")