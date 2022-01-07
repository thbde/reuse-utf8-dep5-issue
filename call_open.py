import locale
import logging  # better expection printing
import sys
from pathlib import Path

dep5_path: Path = Path(__file__).parent / ".reuse" / "dep5"

print(f"{dep5_path=} exists? {dep5_path.exists()}")
print(f"{locale.getpreferredencoding()=}")
print(f"{sys.getfilesystemencoding()=}")




try:
    print("call dep5_path.open()")
    with dep5_path.open() as fd:
        print("start reading")
        for line in fd:
            print("print(line)")
            print(line, end="")
except Exception as e:
    logging.exception(e)
    #print(repr(e))

print("")
print("")
print("")

print("call dep5_path.open(encoding='utf-8')")
with dep5_path.open(encoding="utf-8") as fd:
    print("start reading")
    for line in fd:
        print("print(line)")
        print(line, end="")

# output (local paths truncated):
# dep5_path=WindowsPath('/reuse-utf8-dep5-issue/.reuse/dep5') exists? True
# locale.getpreferredencoding()='cp1252'
# sys.getfilesystemencoding()='utf-8'
# call dep5_path.open()
# start reading
# ERROR:root:'charmap' codec can't decode byte 0x90 in position 321: character maps to <undefined>
# Traceback (most recent call last):
#   File "\reuse-utf8-dep5-issue\call_open.py", line 12, in <module>
#     for line in fd:
#   File "<some-path>\Python\Python310\lib\encodings\cp1252.py", line 23, in decode
#     return codecs.charmap_decode(input,self.errors,decoding_table)[0]
# UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 321: character maps to <undefined>



# call dep5_path.open(encoding='utf-8')
# start reading
# print(line)
# Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
# print(line)
# Upstream-Name: Project
# print(line)
# Upstream-Contact: Jane Doe <jane@example.com>
# print(line)
# Source: https://example.com/jane/project
# print(line)
# # this line and the next line contain only ascii characters
# print(line)
# # the line next however contains some utf-8 characters
# print(line)
# # a penguin: 🐧 and a panda face: 🐼
# print(line)
# # this is again an ascii line. all lines in this file expect the previous line contain only ascii characters
# print(line)

# print(line)
# Files: /*
# print(line)
# Copyright: none
# print(line)
# License: MIT
