import argparse
import os
import socket
import sys
import time


from klout import Klout


def run(klout_key, graphite_host, graphite_port, names, graphite_prefix):
    data = []
    client = Klout(klout_key)
    now = time.time()
    sock = _socket_for_host_port(graphite_host, graphite_port)
    for name in names:
        name = name.strip()
        identity = client.identity.klout(screenName=name).get('id')
        score = client.user.score(kloutId=identity).get('score')
        metric = '{}.{} {} {}\n'.format(graphite_prefix, name, score, now)
        sock.sendall(metric)
    sock.close()

def _socket_for_host_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((host, port))
    sock.settimeout(None)
    return sock

def get_info():
    parser = argparse.ArgumentParser(description='Send Klout scores to Graphite')
    parser.add_argument('--graphite-host', metavar='graphite-host', type=str, nargs=1, default=None, help='Host to send metrics to')
    parser.add_argument('--graphite-port', metavar='graphite-port', type=int, nargs=1, default=2003, help='Graphite port to send metrics to')
    parser.add_argument('--graphite-prefix', metavar='graphite-prefix', type=str, nargs=1, default='klout', help='Prefix for metrics')
    return parser.parse_args()


def main():
    key = os.environ.get('KLOUT_KEY')
    if key is None:
        print 'You must set your Klout key in the environment variable `KLOUT_KEY`'
        sys.exit(1)

    args = get_info()
    names = sys.stdin.readlines()
    run(
        key,
        args.graphite_host[0],
        args.graphite_port,
        names,
        args.graphite_prefix
    )

if __name__ == '__main__':
    main()
