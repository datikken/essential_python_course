class Animal():
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


class Duck:
    sound = 'Quack quack'
    move = 'Walks like a duck'

    def quack(self):
        print(self.sound)

    def movement(self):
        print(self.move)


def main():
    donald = Duck()
    donald.quack()
    donald.movement()

if __name__ == '__main__': main()