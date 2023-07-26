#!/usr/bin/env python3


class FoundTokens:
    def __init__(self, tokens_cheker, tokens_normalizer):
        self.tokens_cheker = tokens_cheker
        self.tokens_normalizer = tokens_normalizer
        self.data = []

    def update(self, new_token, line):
        if self.tokens_cheker(new_token):
            self.data.append((self.tokens_normalizer(new_token), line))

    def __str__(self):
        return str(self.data)

    def sort(self):
        self.data.sort(key=lambda pair: pair[1])

    def print_sorted(self):
        for token, line in sorted(self.data, key=lambda pair: pair[1]):
            print(f"{token}, line {line}")
