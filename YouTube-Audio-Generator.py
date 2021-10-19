from __future__ import unicode_literals
import argparse
import os
import shutil
import sys
import youtube_dl

DOWNLOAD_ARCHIVE_FILE = 'download_archive.txt'
NEW_FILE_DIR = './new'
DARKSTREAM_URL = 'https://www.youtube.com/channel/UCGJNdaSwFeP3pLd1MhN0dRg'

class MyLogger(object):
    def debug(self, msg):
        print('[DEBUG]: ', msg)

    def warning(self, msg):
        print('[WARN ]: ', msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def process_command_line(argv):
    """
    Returns a Namespace object with the argument names as attributes.
    `argv`` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """

    if argv is None:
        argv = sys.argv[1:]

    # initialize the parse object
    desc = 'Download the Darkstream videos from YouTube and extract audio to MP3 format'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--all', action='store_false',
                        dest='use_archive_file',
                        help='All videos for the entire channel')
    parser.add_argument('--next', action='store_true',
                        dest='use_archive_file',
                        default=True,
                        help='The next ste of videos since the last download')
    parser.add_argument('-n', action='store',
                        dest='channel_url',
                        default=DARKSTREAM_URL,
                        help='The YouTube channel url')

    return parser.parse_args()


def download_videos(channel_url, use_download_archive=True):
    ydl_opts = {
        #'simulate': True,
        'outtmpl': '%(upload_date)s_%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'writethumbnail': True,
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'ignoreerrors': True,
        'nooverwrites': True,
        'writeinfojson': True
    }

    if use_download_archive:
        ydl_opts['download_archive'] = DOWNLOAD_ARCHIVE_FILE

    old_file_set = get_file_set('.')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])

    if not os.path.exists(NEW_FILE_DIR):
        os.makedirs(NEW_FILE_DIR)
    
    new_file_set = get_file_set('.')
    files_to_move = list(new_file_set - old_file_set)

    print("Downloaded {} new files. Moving to the 'new' directory.".format(len(files_to_move)))
    for file in files_to_move:
        new_file_path = os.path.join('new', file)
        print('Moving {} ...'.format(file))
        shutil.move(file, new_file_path)


def get_file_set(path):
    return set([f for f in os.listdir('.') if os.path.isfile(f)])


def _main():
    args = process_command_line(sys.argv)
    channel_url = args.channel_url
    use_archive_file = args.use_archive_file
    download_videos(channel_url, use_archive_file)


if __name__ == '__main__':
    status = _main()
    sys.exit(status)
