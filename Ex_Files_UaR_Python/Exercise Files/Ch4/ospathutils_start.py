#
# Example file for working with os.path module
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)


def main():
  import os
  from os import  path
  import datetime
  from datetime import date,time,timedelta
  import time

  #Print name of the OS
  print (os.name)

  #Check for item existence and type
  print "Item exists: " + str(path.exists("textfile.txt"))
  print "Item is a file: " + str(path.isfile("textfile.txt"))
  print "Item is a directory: " + str(path.isdir("textfile.txt"))

  print "----------------"

  #work with file paths
  print "Item's path: " + str(path.realpath("textfile.txt"))
  print "Item's path and name" + str(path.split(path.realpath("textfile.txt")))

  print "################\n"

  print "Get the modification time"
  t = time.ctime(path.getmtime("textfile.txt"))
  print (t)
  print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
  print "\n"

  print "Calculate how long ago the item was modified"
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print "It has been " + str(td) + " The file was modified"
  print "Or, " + str(td.total_seconds()) + " seconds"

  
if __name__ == "__main__":
  main()
