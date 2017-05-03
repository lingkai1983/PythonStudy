#
# Read and write files using the built-in Python file methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
  # f = open("textfile.txt","w+")
  #
  # for i in range(10):
  #   f.write("This is line %d\r\n" %(i+1))
  #
  # f= open("textfile.txt","a+")
  #
  # for i in range(11,21):
  #   f.write("This is line %d\n" %i)
  #
  # # close the file
  # f.close()

  f = open("textfile.txt","r")

  if f.mode == 'r': #check if the file is been opened for read
   # contents = f.read()
   # print contents

   ## another way to access
   fl = f.readlines()
   for oneLine in fl:
     print oneLine


    
if __name__ == "__main__":
  main()
