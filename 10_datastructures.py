def main():
    game = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    print(type(game))
    print_list(game)
    xmpl()

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

#dictionary
def xmpl():
    animals = {'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr'}
    print_dict(animals)

def print_dict(o):
    for key in o:
        #key
        print(key)
        #val
        print(o[key])

def print_set(o):
    print('{', end = ' ')
    for x in o: print(x, end=' ')
    print('}')

#set
def main():
    a = set('unique line')
    b = set('unique line 3')
    print_set(sorted(a))
    print_set(sorted(b))


if __name__ == '__main__': main()
