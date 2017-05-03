#
# Example file for working with filesystem shell methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

def main():
 if path.exists("textfile.txt"):
  #get the path to the file in the current directory
  src = path.realpath("textfile.txt")

  #separate the path from the file name
  (head, tail) = path.split(src)
  print "path: " + str(head)
  print "file: " + str(tail)

  #copy a backup
  dst = src + ".bak"
  shutil.copy(src,dst)
      
if __name__ == "__main__":
  main()
