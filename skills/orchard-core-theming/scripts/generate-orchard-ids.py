#!/usr/bin/env python3
import argparse
import sys
import uuid


ENCODE32_CHARS = "0123456789abcdefghjkmnpqrstvwxyz"


def _to_base32(hs, ls):
    buffer = [""] * 26

    buffer[0] = ENCODE32_CHARS[(hs >> 60) & 31]
    buffer[1] = ENCODE32_CHARS[(hs >> 55) & 31]
    buffer[2] = ENCODE32_CHARS[(hs >> 50) & 31]
    buffer[3] = ENCODE32_CHARS[(hs >> 45) & 31]
    buffer[4] = ENCODE32_CHARS[(hs >> 40) & 31]
    buffer[5] = ENCODE32_CHARS[(hs >> 35) & 31]
    buffer[6] = ENCODE32_CHARS[(hs >> 30) & 31]
    buffer[7] = ENCODE32_CHARS[(hs >> 25) & 31]
    buffer[8] = ENCODE32_CHARS[(hs >> 20) & 31]
    buffer[9] = ENCODE32_CHARS[(hs >> 15) & 31]
    buffer[10] = ENCODE32_CHARS[(hs >> 10) & 31]
    buffer[11] = ENCODE32_CHARS[(hs >> 5) & 31]
    buffer[12] = ENCODE32_CHARS[hs & 31]

    buffer[13] = ENCODE32_CHARS[(ls >> 60) & 31]
    buffer[14] = ENCODE32_CHARS[(ls >> 55) & 31]
    buffer[15] = ENCODE32_CHARS[(ls >> 50) & 31]
    buffer[16] = ENCODE32_CHARS[(ls >> 45) & 31]
    buffer[17] = ENCODE32_CHARS[(ls >> 40) & 31]
    buffer[18] = ENCODE32_CHARS[(ls >> 35) & 31]
    buffer[19] = ENCODE32_CHARS[(ls >> 30) & 31]
    buffer[20] = ENCODE32_CHARS[(ls >> 25) & 31]
    buffer[21] = ENCODE32_CHARS[(ls >> 20) & 31]
    buffer[22] = ENCODE32_CHARS[(ls >> 15) & 31]
    buffer[23] = ENCODE32_CHARS[(ls >> 10) & 31]
    buffer[24] = ENCODE32_CHARS[(ls >> 5) & 31]
    buffer[25] = ENCODE32_CHARS[ls & 31]

    return "".join(buffer)


def generate_id():
    guid_bytes = uuid.uuid4().bytes_le
    hs = int.from_bytes(guid_bytes[:8], "little", signed=True)
    ls = int.from_bytes(guid_bytes[8:], "little", signed=True)
    return _to_base32(hs, ls)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Generate Orchard Core IDs using the DefaultIdGenerator algorithm "
            "(26-char base32 with the Orchard Core alphabet)."
        )
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of IDs to generate (default: 1).",
    )
    args = parser.parse_args()
    if args.count <= 0:
        parser.error("--count must be greater than 0.")

    ids = [generate_id() for _ in range(args.count)]
    sys.stdout.write("\n".join(ids) + ("\n" if ids else ""))


if __name__ == "__main__":
    main()
