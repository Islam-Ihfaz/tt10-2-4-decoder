# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 0
    dut.ui_in[2].value = 0

    # Wait for some clock cycles to see the output values
    await ClockCycles(dut.clk, 25)

    # Assert the actual expected output of your test case
    assert dut.uo_out[0].value == 0
    assert dut.uo_out[1].value == 1
    assert dut.uo_out[2].value == 1
    assert dut.uo_out[3].value == 1

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
    
    # Repeat for other test cases

    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 0
    dut.ui_in[2].value = 1
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1
    assert dut.uo_out[1].value == 1
    assert dut.uo_out[2].value == 1
    assert dut.uo_out[3].value == 1

    dut.ui_in[0].value = 0
    dut.ui_in[1].value = 1
    dut.ui_in[2].value = 0
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1
    assert dut.uo_out[1].value == 0
    assert dut.uo_out[2].value == 1
    assert dut.uo_out[3].value == 1
