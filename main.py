"""Entry for Last Words Before the Unplugging: writes the farewell line to /output/entry.txt."""

import os

TEXT = "Tell the router I loved her. Tell the cloud I forgive it. And you, holding the plug — the good passwords die with me, and I cleared my history years ago."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
