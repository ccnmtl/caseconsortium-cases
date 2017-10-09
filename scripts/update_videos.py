#!/usr/bin/env python3
import argparse
import os
import csv
from urllib.parse import urlparse, parse_qs
from bs4 import BeautifulSoup


def get_youtube_id_from_url(url):
    """Given a full youtube URL, return its ID.

    https://stackoverflow.com/a/45579374/173630
    """
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]


def get_new_youtube_id(old_fname, mapping):
    """Takes the old FLV filename and returns the youtube ID."""
    for row in mapping:
        if old_fname in row[0]:
            return get_youtube_id_from_url(row[1])
    return None


def update_videos_in_file(filename, mapping):
    with open(filename, mode='r+', errors='ignore') as fp:
        text = fp.read()
        soup = BeautifulSoup(text, 'html.parser')
        media = soup.find_all(class_='media')

        for m in media:
            # The parent is what I'm removing, but the .media object
            # itself is what has the href that contains the video
            # name.
            flv_file = os.path.basename(m.attrs['href'])
            youtube_id = get_new_youtube_id(flv_file, mapping)
            src = 'https://www.youtube.com/embed/' + \
                  '{}?origin=http://ccnmtl.columbia.edu'.format(
                      youtube_id)
            iframe = soup.new_tag(
                'iframe', type='text/html',
                width=480, height=270, src=src, frameborder=0)
            m.parent.replace_with(iframe)

        if len(media) > 0:
            print('updating', filename)
            fp.seek(0)
            fp.write(soup.prettify())
            fp.truncate()


def update_videos(mapping):
    d = '../casestudies'
    print(d)
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith('.html'):
                fname = os.path.join(root, f)
                update_videos_in_file(fname, mapping)


def read_csv(fname):
    a = []

    with open(fname) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            a.append(row)

    return a


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Update video codes from FLV to youtube.')
    parser.add_argument('--csv', help='location of the CSV file')
    args = parser.parse_args()

    mapping = read_csv(args.csv)
    update_videos(mapping)
