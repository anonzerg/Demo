#! /usr/bin/env python

import logging
import sys

def main() -> None:

    return None


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname)s] %(message)s",
        level=logging.INFO
    )
    log = logging.getLogger(__name__)

    try:
        main()
    except KeyboardInterrupt as e:
        log.error(e)
        sys.exit(1)
