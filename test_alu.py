#!/usr/bin/env python3

import cocotb
from cocotb.triggers import Timer

from enum import IntEnum
from itertools import product


class INSTR(IntEnum):
    (
        INSTR_ADD,
        INSTR_SUB,
        INSTR_AND,
        INSTR_OR,
        INSTR_NAND,
        INSTR_NOR,
        INSTR_NOT,
        INSTR_XOR,
        INSTR_XNOR,
    ) = range(9)


def delay_ns(ns: int):
    """
    pyright and mypy don't like it when you assign a number to
    something that has one of the numbers.<types>.
    """
    return Timer(ns, units="ns")  # type: ignore


def dec_to_binarray(dec_in: int):
    ret = []
    while dec_in != 0:
        ret.append(dec_in % 2)
        dec_in //= 2
    return ret


reference_impls = {
    INSTR.INSTR_ADD: lambda x, y: (x + y) % 256,
    INSTR.INSTR_SUB: lambda x, y: (x - y) % 256,
    INSTR.INSTR_AND: lambda x, y: x & y,
    INSTR.INSTR_OR: lambda x, y: x | y,
    INSTR.INSTR_NAND: lambda x, y: 255 - (x & y),
    INSTR.INSTR_NOR: lambda x, y: 255 - (x | y),
    INSTR.INSTR_NOT: lambda x, _: 255 - x,
    INSTR.INSTR_XOR: lambda x, y: x ^ y,
    INSTR.INSTR_XNOR: lambda x, y: 255 - (x ^ y),
}


@cocotb.test
async def test_alu(dut):
    for a, b in product(range(2**8), range(2**8)):
        for instruction in INSTR:
            if instruction == INSTR.INSTR_SUB:
                continue
            dut.A.value = a
            dut.B.value = b
            dut.c_in.value = 0
            await delay_ns(100)
            dut.sel.value = instruction
            y = reference_impls[instruction](a, b)
            await delay_ns(200)

            assert (
                y == dut.Y.value
            ), f"In {instruction=} for {a=},{b=}, expected {y}, got {dut.Y.value}"
