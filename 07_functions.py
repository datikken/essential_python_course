# def main():
#     kitten('meow', 'grrr', 'purrr')
#
# def kitten(*args):
#     if len(args):
#         for s in args:
#             print(s)
#     else: print('Meow.')

def main():
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__' : main()