import sys

sys.stderr.write(" This is stderr text\n")
sys.stderr.flush()
sys.stdout.write("this is stdout text\n")

print(sys.argv) #gives file name
print("********\n\n")
if len(sys.argv) >1:
    #print(sys.argv[-1])
    print(sys.argv[1] * 5)


def main(arg):
    print(arg)

main(sys.argv[1])
