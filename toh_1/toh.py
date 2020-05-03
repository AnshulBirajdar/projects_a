import sys
import time

print("Welcome to Towers of Hanoi")
print("There are 3 towers ie. a , b , c")
print("You Have to say:")
print("Source:a\nDestination:b")


class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            popped_item = self.stack[-1]
            del (self.stack[-1])
            return popped_item

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[(len(self.stack) - 1)]
        else:
            return None

    def prints(self):
        return str(self.stack)


name = input("What is your name ").title()
a = Stack()
b = Stack()
c = Stack()
level = int(input("LEVEL:"))
levelz = str(level)
level += 3
for i in range(level-1, 0, -1):
    a.push(i)

winner_stack = a.stack
moves = 0

height = len(a.stack) - 1


def main_loop(source: Stack, destination: Stack):
    source_pop = source.pop()
    destination_peek = destination.peek()
    if True:
        try:
            if source_pop < destination_peek:
                destination.push(source_pop)
            else:
                source.push(source_pop)
                print("Wrong move, not accepting it")
        except TypeError:
            destination.push(source_pop)

    return source, destination


# print('a', a.prints(), '\nb', b.prints(), '\nc', c.prints())

def draw_disks(a, b, c, position, width=2 * int(max(a.stack))):
    # width parameter defaults to double of the largest sized disk in the initial tower.
    if position >= 0:
        # If A has a value in the list at the given position, create a disk at its position (height)
        valueInA = " " if position >= len(a.stack) else create_disk(a.stack[position])
        # Same for B and C
        valueInB = " " if position >= len(b.stack) else create_disk(b.stack[position])
        valueInC = " " if position >= len(c.stack) else create_disk(c.stack[position])

        # Print each row
        print("{0:^{width}}{1:^{width}}{2:^{width}}".format(valueInA, valueInB, valueInC, width=width))

        # Recursively call this method again to the next position (height)
        draw_disks(a, b, c, position - 1, width)
    else:
        # When done with recursive, print column labels
        print("{0:^{width}}{1:^{width}}{2:^{width}}".format("A", "B", "C", width=width))


def create_disk(size):
    if size == 1:
        return "/\\"
    else:
        return "/" + create_disk(size - 1) + "\\"



running = True

while running:
    draw_disks(a, b, c, height)
    moves += 1
    x = input("Enter the source").lower()
    y = input("Enter the destination").lower()

    if x == y:
        print("You have entered the same thing")
    elif x == 'a' and y == 'b':
        a, b = main_loop(a, b)
    elif x == 'a' and y == 'c':
        a, c = main_loop(a, c)
    elif x == 'b' and y == 'a':
        b, a = main_loop(b, a)
    elif x == 'b' and y == 'c':
        b, c = main_loop(b, c)
    elif x == 'c' and y == 'a':
        c, a = main_loop(c, a)
    elif x == 'c' and y == 'b':
        c, b = main_loop(c, b)
    if c.stack == winner_stack or b.stack == winner_stack:
        print("You are the winner")
        file_write = open("results.txt", 'a')
        file_write.write(name)
        file_write.write(' has completed the tower of hanoi  ')
        file_write.write(' of level')
        file_write.write(levelz)
        file_write.write('in')
        file_write.write(str(moves))
        file_write.write(' moves')
        file_write.write('\n')
        print("Closing in 3 seconds")
        #print('a', a.prints(), '\nb', b.prints(), '\nc', c.prints())
        draw_disks(a, b, c, height)
        time.sleep(3)
        file_write.close()
        sys.exit()


    # print('a', a.prints(), '\nb', b.prints(), '\nc', c.prints())

