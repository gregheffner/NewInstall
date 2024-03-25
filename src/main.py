#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys

try:
    from loguru import logger
except ImportError:
    print("Please pip install loguru")
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    logger.error("Please pip install python-dotenv")
    sys.exit(1)


def parse_args():
    """
    Parses debug and folder arguments.

    Variables:
    debug (bool): If True, debug logging will be enabled. Default = False

    Returns: (argparse.Namespace): Parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        required=False,
        help="Enable debug logging",
    )
    return parser.parse_args()


def setup_logging(debug: bool):
    """
    Setup loguru logging.

    Variables:
    debug (bool): If True, debug logging will be enabled. Default = False

    Returns:
    logger (loguru.logger): Loguru logger object.
    """
    # Remove all built in handlers
    logger.remove()
    # Set custom loguru format
    fmt = (
        "<level>{time:YYYY-MM-DD hh:mm:ss A}</level> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{"
        "function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level> "
    )
    # Set Debug level if --debug is passed
    if debug:
        logger.add(sys.stderr, format=fmt, level="DEBUG")
    else:
        logger.add(sys.stderr, format=fmt, level="INFO")
    return logger


def create():
    os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
    os.system('brew install python')
    os.system('sudo easy_install pip')
    os.system('pip install virtualenv')
    os.system("brew bundle --file /NewInstall/brewbundle/Brewfile")
    os.system("sudo apt install zsh")
    os.system("chsh -s $(which zsh)")
    os.system("sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"")
    os.system("cp /zshrc_files/zshrc ~/.zshrc")
    os.system("pip install cookiecutter")
    os.system("git clone git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k")
    os.system("cp /NewInstall/p10k.zsh ~/.p10k.zsh")


if __name__ == "__main__":
    # Parse the arguments
    args = parse_args()
    # setup logger
    logger = setup_logging(args.debug)
    # Load .env file
    logger.debug("Loading .env file")
    load_dotenv()
    create()
    logger.info("Script Finished")
