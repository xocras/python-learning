from logging import *

COLOR_CODES = {
        'RESET': '\033[0m',
        'BOLD': '\033[1m',
        'RED': '\033[91m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'BLUE': '\033[94m',
        'MAGENTA': '\033[95m',
        'CYAN': '\033[96m'
    }

COLOR_MAP = {
    'DEBUG': COLOR_CODES['BLUE'],
    'INFO': COLOR_CODES['GREEN'],
    'WARNING': COLOR_CODES['YELLOW'],
    'ERROR': COLOR_CODES['RED'],
    'CRITICAL': COLOR_CODES['MAGENTA']
}


class ColoredFormatter(Formatter):

    def format(self, record):
        levelname = record.levelname
        message = super().format(record)
        return f"{COLOR_MAP.get(levelname, '')}{message}{COLOR_CODES['RESET']}"


# Configure logging with colored output
color_format = f"\n%(asctime)s | %(filename)s\n%(levelname)s: %(message)s"

#  Set logging level
basicConfig(level=INFO)

# Configure formatter defaults
date_format = '%Y-%m-%d %I:%M:%S %p'
formatter = ColoredFormatter(color_format, date_format)

# Replace default handler
handler = StreamHandler()
handler.setFormatter(formatter)

getLogger().handlers.clear()
getLogger().addHandler(handler)

