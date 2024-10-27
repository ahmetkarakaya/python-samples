import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--old", help="Old option", deprecated=True, required=False)
parser.add_argument("--new",help="New argument", required=False)

args = parser.parse_args()