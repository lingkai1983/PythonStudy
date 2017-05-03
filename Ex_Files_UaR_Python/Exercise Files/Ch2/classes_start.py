#
# Example file for working with classes
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
class MyClass():
  def method1(self):
    print("MyClass method1")

  def method2(self, someString):
    print("MyClass method2: " + someString)

class AnotherClass(MyClass):
  def method2(self):
    print("Another Class Method2")

  def method1(self):
    MyClass.method1(self)
    print("AnotherClass Method1")

def main():
  c1 = MyClass()
  c1.method1()
  c1.method2("Lingkai Zuo")
  print("--------------------")
  c2 = AnotherClass()
  c2.method2()
  c2.method1()
  
if __name__ == "__main__":
  main()
