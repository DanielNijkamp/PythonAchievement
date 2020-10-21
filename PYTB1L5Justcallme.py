import sys

def callMe(name, number):
    print("hallo")
    print("wie is daar? ")
    print("ik ben het "+ name)
    print("hoi "+ name+ " ik ben nu even bezig kan ik je later terugbellen?")
    print("is goed")
    print("wat is je nummer?")
    print("het is: "+ number)
    print("is goed ik bel je later terug!")
    print("is goed doei doei")
    print("later")
    print("EINDE GESPREK")

callMe(sys.argv[1], sys.argv[2])
