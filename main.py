from logger import Logger

l = Logger()


@l.logging_func
def test_func():
    [i**i for i in range(1000)]


for _ in range(3):
    test_func()


l.logging_start()
for _ in range(3):
    [i**i for i in range(1000)]
l.logging_end('cycle')

l.print_results()