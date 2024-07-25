#!/usr/bin/env python3

import cocotb
from cocotb.triggers import Timer

from itertools import product

def delay_ns(ns: int):
    '''
    pyright and mypy don't like it when you assign a number to
    something that has one of the numbers.<types>.
    '''
    return Timer(ns, units='ns') # type: ignore


def dec_to_binarray(dec_in: int):
    ret = []
    while dec_in != 0:
        ret.append(dec_in % 2)
        dec_in //= 2
    return ret

# @cocotb.test
# async def test_full_adder(dut):
#
#     for a, b, c_in in product([0,1],[0,1],[0,1]):
#         dut.a.value = a
#         dut.b.value = b
#         dut.c_in.value = c_in
#
#         s = a+b+c_in
#         c_out = s // 2
#         s = s % 2
#         await delay_ns(1)
#         assert dut.s.value == s, f"Expected {s}, got {dut.s.value}"
#         assert dut.c_out.value == c_out, f"Expected {c_out}, got {dut.c_out.value}"



@cocotb.test
async def test_adder8(dut):

    for a, b in zip(range(2**8), range(2**8)):
        for c_in in [0,1]:
            dut.A.value = a
            dut.B.value = b
            dut.c_in.value = c_in

            # ground truths
            s = a+b+c_in
            c_out = s // (2**8)
            s = s % (2**8)

            await delay_ns(1)

            assert dut.S.value == s, f"Expected {s}, got {dut.S.value}"
            assert dut.c_out.value == c_out, f"Expected {c_out}, got {dut.c_out.value}"
