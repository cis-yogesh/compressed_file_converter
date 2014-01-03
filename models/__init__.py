import re
import os
EMAIL_REGEX = re.compile("([_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.(([0-9]{1,3})|([a-zA-Z]{2,3})))")
MD5_HASH = re.compile("([a-fA-F\d]{32})")
SHA1_HASH = re.compile("(/^[0-9a-f]{40}$/i)")
CURRENT_PATH = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
file_stats = []
DELETE = False




