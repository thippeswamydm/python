# main module
import sys
sys.path.append('/foo')

from print import *

def main():
    printer()
    inputprinter()

if __name__ == '__main__':
    main()