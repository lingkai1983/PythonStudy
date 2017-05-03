#
# Example file for working with conditional statements
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
    x = 0
    while (x < 5):
        print "x = " + str(x)
        x = x + 1

    print  "---------------"

    for x in range(5, 10):
        print "x = " + str(x)

    days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

    print  "###############"

    for i, day in enumerate(days):
        print day
        print  i

if __name__ == "__main__":
    main()
