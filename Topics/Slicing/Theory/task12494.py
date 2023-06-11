import argparse as ap


def decode_Caesar_cipher(s, n) -> str:
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    return text


parser = ap.ArgumentParser()
parser.add_argument("--file", type=str)
args = parser.parse_args()

with open(args.file) as file:
    encoded = file.read()
    print(decode_Caesar_cipher(encoded, -13))
