#
# First, we create a file containing only tweet ids. We extract data from June 2020 as an example:
#
# $> cd twitter/2020
# $> gunzip 2020-06.csv.gz
# $> cut -d, -f1 2020-06.csv > 2020-06.txt
#
#
#
#
# This script will walk through the tweet id file and
# hydrate with twarc. The line oriented JSON files will
# be placed right next to the tweet id file.
#
# Note: you will need to install twarc, tqdm, and run twarc configure
# from the command line to tell it your Twitter API keys.
#
# Reference: https://github.com/sjgiorgi/blm_twitter_corpus/blob/master/hydrate.py
#

import gzip
import json
import os

from tqdm import tqdm
from twarc import Twarc
from pathlib import Path


consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_SECRET_KEY')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

twarc = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)
data_dirs = ['.']


def main():
    for data_dir in data_dirs:
        for path in Path(data_dir).iterdir():
            if path.name.endswith('.txt'):
                hydrate(path)


def _reader_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)


def raw_newline_count(fname):
    """
    Counts number of lines in file
    """
    f = open(fname, 'rb')
    f_gen = _reader_generator(f.raw.read)
    return sum(buf.count(b'\n') for buf in f_gen)


def hydrate(id_file):
    print('hydrating {}'.format(id_file))

    gzip_path = id_file.with_suffix('.jsonl.gz')
    if gzip_path.is_file():
        print('skipping json file already exists: {}'.format(gzip_path))
        return

    num_ids = raw_newline_count(id_file)

    with gzip.open(gzip_path, 'w') as output:
        with tqdm(total=num_ids) as pbar:
            for tweet in twarc.hydrate(id_file.open()):
                output.write(json.dumps(tweet).encode('utf8') + b"\n")
                pbar.update(1)


if __name__ == "__main__":
    main()
