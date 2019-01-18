# one.py
def func():
    print("fun in one.py")


print("top level in one.py")

if __name__ == "__main__":
    print("Print one.py direct")
else:
    print("one.py import")
