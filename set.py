#!usr/bin/env python
import sys

def main():
    if len(sys.argv) != 2:
        print 'Usage: %s <input-file>' % sys.argv[0]
        sys.exit(-1)

    with open(sys.argv[1]) as f:
        unified_set = set([])
        for line in f.readlines():
            unified_set.add(line.strip())

        for item in unified_set:
            print item

if __name__ == '__main__':
    main()
