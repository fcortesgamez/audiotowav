#!/usr/bin/env python3

import json
# import librosa
import subprocess
import sys
import tempfile


def main():
    if len(sys.argv) != 2:
        sys.exit('Usage:  {} <sound-file>'.format(sys.argv[0]))
    filename = sys.argv[1]

    print('Loading file ...')
    soundfile = load_soundfile(filename)

    print('Extrating data ...', )
    data = extract_data(soundfile)

    # Pretty print
    pretty_print(data)


def pretty_print(data):
    print(json.dumps(data, indent=4))
    # f = tempfile.NamedTemporaryFile(delete=False)
    # f.write(json.dumps(data).encode('ascii'))
    # print("jq '.' {}".format(f.name))
    # subprocess.call("jq '.' {}".format(f.name), shell=True)


def extract_data(sound):
    # TODO
    databytes = b'{"tests":{"net.wifi":{"result":1,"resultText":"SSID"},"net.gateway":{"result":1,"resultText":"ping 1.2.3.4 ok"},"net.inet":{"result":1,"resultText":"ping 8.8.8.8 ok"},"net.dns":{"result":1,"resultText":"vpn.eneco.toon.eu: 63.35.124.51"},"net.time":{"result":1,"resultText":"2019-05-16T09:16:08+0000"}}}'
    return json.loads(databytes)


def load_soundfile(filepath):
    # return librosa.load(filepath)
    pass

if __name__ == '__main__':
    main()
