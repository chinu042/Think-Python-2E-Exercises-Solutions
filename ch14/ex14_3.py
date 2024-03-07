import os
import glob
import hashlib
import itertools

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda:f.read(4096),b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    d = {}
    rev_d = {}
    for filename in glob.glob('./**/*.py',recursive=True):
        print(os.path.abspath(filename))
        print(md5(os.path.abspath(filename)))
        d[filename] = md5(os.path.abspath(filename))

    print(set(itertools.	chain.from_iterable(values for key, values in rev_d.items() if len(values) > 1)))

if __name__ == '__main__':
	main()