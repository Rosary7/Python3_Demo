"""
If you declare a variable inside a class, but outside any method/constructor, it is a class or static variable.
We can have instance and static variable with the same name.
"""
class Fruit():
    count = 0
    def __init__(self, name, count):
        self.name = name
        self.count = count
        Fruit.count = Fruit.count + count

def main():
    apples = Fruit("apples", 3);
    pears = Fruit("pears", 4);
    print(apples.count)
    print(pears.count)
    print(Fruit.count)
    print(apples.__class__.count) # This is Fruit.count
    print(type(apples).count)     # So is this
    print(type(pears).count)      # So is this

if __name__ == '__main__':
    main()