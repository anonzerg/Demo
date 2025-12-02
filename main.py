#! /usr/bin/env python

import logging
import sys
import tkinter as tk

from tkinter import ttk

from app import Connect

def main() -> None:
    root = tk.Tk()
    app = Connect(root)
    root.mainloop()

    return None


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname)s] %(message)s",
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    try:
        main()
    except KeyboardInterrupt as e:
        logger.error(e)
        sys.exit(1)
