class kStacks:

    def __init__(self, n, k):
        self.n = n
        self.k = k

        self.arr = [0] * n
        self.top = [-1] * k

        self.next = [i + 1 for i in range(n)]
        self.next[n - 1] = -1

        self.free = 0

    def push(self, x, m):

        if self.free == -1:
            return False

        i = self.free

        self.free = self.next[i]

        self.next[i] = self.top[m]

        self.top[m] = i

        self.arr[i] = x

        return True

    def pop(self, m):

        if self.top[m] == -1:
            return -1

        i = self.top[m]

        self.top[m] = self.next[i]

        self.next[i] = self.free

        self.free = i

        return self.arr[i]