#!/usr/bin/python
# -*- coding: utf-8 -*-


class BitList:

    def __init__(self, bits=0, length=0):
        self.bits = abs(int(bits))
        self.length = abs(int(length))
        actual_length = self.get_length(True)
        if actual_length > self.length:
            self.length = actual_length

    def get_length(self, recompute=False):
        if not recompute:
            return self.length
        length = 0
        bits = self.bits
        while bits > 0:
            length += 1
            bits //= 2
        return length

    def get_bit(self, key):
        if key < 0:
            key += self.length
        if key < 0 or key >= self.length:
            raise IndexError()
        return self.bits % 2 ** (key + 1) // 2 ** key

    def get_slice(
        self,
        start=0,
        stop=-1,
        step=1,
        ):
        if stop is None:
            stop = -1
        if step is None:
            step = 1
        if start < 0:
            start += self.length
        if stop < 0:
            stop += self.length
        bits = 0
        current = start
        while current != stop and current > 0 and current < self.length:
            bits += self[current] * 2 ** ((current - min(start, stop))
                    // step)
            current += step
        return BitList(bits)

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.get_bit(key)
        elif isinstance(key, slice):
            return self.get_slice(key.start, key.stop, key.step)
        raise IndexError()

    def __setitem__(self, key, value):
        if key < 0:
            key += self.length
        if key < 0 or key >= self.length:
            raise IndexError()
        if value is True:
            value = 1
        elif value is False:
            value = 0
        if value == 0:
            if self[key]:
                self.bits -= 2 ** key
        elif value == 1:
            if not self[key]:
                self.bits += 2 ** key
        else:
            raise ValueError('0, 1, False, True are only allowed values for BitList'
                             )

    def __str__(self):
        return str(bin(self.bits))[2:]


# Example
# Creating a list of bits with length=10

bl = BitList(length=10)
bl[9] = 1
bl[1] = 1
bl[3] = 1

# Prints: 100000101 11

print (bl, bl[1:5:2])
