#!/usr/bin/env python
import pdb
import sys
import pydump
import linecache
from optparse import OptionParser

def main():

    parser = OptionParser(
        usage="%prog <filename.dump> [options]", description="pydump v%s: post-mortem debugging for Python programs" % pydump.__version__)
    parser.add_option("--pdb",  action="append_const", const="pdb",
                      dest="debuggers", help="Use builtin pdb or pdb++")
    parser.add_option("--pudb", action="append_const", const="pudb",
                      dest="debuggers", help="Use pudb visual debugger")
    parser.add_option("--ipdb", action="append_const", const="ipdb",
                      dest="debuggers", help="Use ipdb IPython debugger")
    (options, args) = parser.parse_args()

    if len(args) < 1:
        parser.print_help()
        sys.exit(1)

    if not options.debuggers:
        options.debuggers = ["pdb"]

    for debugger in options.debuggers:
        try:
            dbg = __import__(debugger)
        except ImportError as e:
            print(str(e), file=sys.stderr)
            continue
        else:
            print("Starting %s..." % debugger, file=sys.stderr)
            if debugger == "pudb":
                pydump.debug_dump(
                    args[0], lambda tb: dbg.post_mortem((None, None, tb)))
            else:
                pydump.debug_dump(args[0])
            break

			
if __name__ == '__main__':
    main()
