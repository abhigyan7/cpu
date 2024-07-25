#!/usr/bin/env python3

import cocotb
from cocotb.triggers import Timer

from itertools import product

@cocotb.test
async def test_full_adder(dut):

    for a, b, c_in in product([0,1],[0,1],[0,1]):
        dut.a.value = a
        dut.b.value = b
        dut.c_in.value = c_in

        s = a+b+c_in
        c_out = s // 2
        s = s % 2
        await Timer(1, units="ns")
        assert dut.s.value == s, f"Expected {s}, got {dut.s.value}"
        assert dut.c_out.value == c_out, f"Expected {c_out}, got {dut.c_out.value}"

