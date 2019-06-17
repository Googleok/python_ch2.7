
# 1. Local
# 2. Enclosing Function(내포한 함수)
# 3. Global
# 4. Built-in

a = 1  # Global

b = 300
def f():
    b = 200     # Enclosing Variable
    def g():
        # b = 100     # Local
        print(b)
        print(__name__)     # Built-in
    g()

if __name__ == '__main__':
    f()

