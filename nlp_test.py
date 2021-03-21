#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : test1.py
# @Author: gaofzhan
# @Email: gaofeng.a.zhang@ericssoin.com
# @Date  : 2021/3/20 18:58
# @Desc  : 
class StrNode(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = StrNode(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None


STR_CONST_LIST = ['(', ')', '{', '}', '[', ']']

POP_FLAG = {
    ')': '(',
    ']': '[',
    '}': '{'
}


def main(str_text):
    stack = Stack()
    for i in str_text:
        if i in ['(', '[', '{']:
            push_node = StrNode(i)
            stack.push(push_node)
        elif i in POP_FLAG.keys():  # if i not in [), ], }]
            # case1 nothing to pop, so the character can not match
            # input : ')[]'
            if stack.is_empty():
                return False
            pop_node = stack.pop()
            str_character = pop_node.data
            # case2 the poped character can not match
            # input : '([)'
            if str_character != POP_FLAG[i]:
                return False
        else:
            raise RuntimeError('unexecpted character')
    # case3: the input has a single character
    # input : '()[]{'
    if not stack.is_empty():
        return False
    return True


if __name__ == "__main__":
    print(main('()'))
    print(main("()[]{}"))
    print(main("(]"))
    print(main("([)]"))
    print(main("{[]}"))
