#!/usr/bin/python

from graph import *

def main():
    q = (int(raw_input().strip()))
    assert 1 <= q <= 10
    for i in range(q):
        n, m = raw_input().strip().split(' ')
        assert 2 <= n <= 1000
        assert 1 <= m <= ((n * (n - 1)) / 2)

        g = Graph()
        
        for j in range(m):
            u, v = raw_input().strip().split(' ')
            assert 1 <= u <= n
            assert 1 <= v <= n
            g.add_edge((str(u), str(v)))

        s = (int(raw_input().strip()))
        assert 1 <= s <= n


if __name__ == '__main__':
    main()
