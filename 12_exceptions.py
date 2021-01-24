import sys

def main():
    try:
        x = int('foo')
    except:
        print(f'unknown_error: {sys.exc_info()}')


if __name__ == '__main__': main()