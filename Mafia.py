# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))