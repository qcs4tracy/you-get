#!/usr/bin/env python


from ..common import *

def xvideo_download(url, output_dir = '.', merge = True, info_only = False, **kwargs):
    html = get_content(url)
    matches = match1(html, r'setVideoUrlHigh\((.+)\)', r'setVideoUrlLow\((.+)\)')
    video_url = matches[0].strip("'\"") if len(matches) > 0 else None

    title = match1(html, r'<title>([^<>]+)</title>')
    heads = get_head(video_url)
    content_type = heads['Content-Type']
    size = int(heads['Content-Length'])
    print_info(site_info, title, content_type, size)

    if not info_only:
        download_urls([video_url], title, 'mp4', size, output_dir=output_dir, merge=merge)

site_info = "xvideos.com"
download = xvideo_download
download_playlist = playlist_not_supported('xvideos')
