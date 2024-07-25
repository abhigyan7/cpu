#!/usr/bin/env python3

import cocotb
from cocotb.triggers import Timer

from enum import IntEnum
from itertools import product

from tqdm import tqdm


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


def tc(x: int) -> int:
    return (255 - x + 1) % 256


reference_impls = {
    INSTR.INSTR_ADD: lambda x, y: ((x + y) % 256, (x + y) // 256),
    INSTR.INSTR_SUB: lambda x, y: ((x + tc(y)) % 256, (x + tc(y)) // 256),
    INSTR.INSTR_AND: lambda x, y: (x & y, 0),
    INSTR.INSTR_OR: lambda x, y: (x | y, 0),
    INSTR.INSTR_NAND: lambda x, y: (255 - (x & y), 0),
    INSTR.INSTR_NOR: lambda x, y: (255 - (x | y), 0),
    INSTR.INSTR_NOT: lambda x, _: (255 - x, 0),
    INSTR.INSTR_XOR: lambda x, y: (x ^ y, 0),
    INSTR.INSTR_XNOR: lambda x, y: (255 - (x ^ y), 0),
}


@cocotb.test
async def test_alu(dut):
    dut.sel.value = 15
    await delay_ns(1)
    for a, b in tqdm(product(range(2**8), range(2**8))):
        for instruction in INSTR:
            dut.c_in.value = 0
            dut.A.value = a
            dut.B.value = b
            dut.sel.value = instruction
            await delay_ns(1)
            y, c = reference_impls[instruction](a, b)

            assert (
                y == dut.Y.value
            ), f"In {instruction=} for {a=},{b=}, expected {y}, got {dut.Y.value}"
            assert (
                c == dut.C.value
            ), f"In {instruction=} for {a=},{b=}, expected {c}, got {dut.c.value}"
