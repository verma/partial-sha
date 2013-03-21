What is this?
---
You may find a need to match parts of a large file, this utility computes a hash of a part of a file.

How to use?
---

You can use this utility from the command line, all it expects is a start offset (a number or a percent), an end offset and the filename.

    ./partial-sha.py -s 10% -e 20% largefile.tbz
    
You can omit the end offset to default to end of file, or omit the start offset to default to the beginning of the file.

Why would I need this?
---
Well, this is somewhat tuned for my use case.  Slow Internet connection and large files.  

If I detect an error in a large file transfer using a `shasum` or a similar tool, I need to know exactly where the error occured.  I can compute partial shas on both ends(provided you have access) and only transfer the area of the file which was corrupted (which needs a utility of its own).

License
---
MIT
