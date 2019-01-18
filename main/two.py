# two.py
import one

print('Top level in two.py')

one.func()

if __name__ == "__main__":
    print("Print two.py direct")
else:
    print("two.py import")
