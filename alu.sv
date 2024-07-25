`timescale 1ns/1ps;


typedef enum bit [3:0] {
              INSTR_ADD = 4'b0000,
              INSTR_SUB = 4'b0001,
              INSTR_AND = 4'b0010,
              INSTR_OR = 4'b0011,
              INSTR_NAND = 4'b0100,
              INSTR_NOR = 4'b0101,
              INSTR_NOT = 4'b0110,
              INSTR_XOR = 4'b0111,
              INSTR_XNOR = 4'b1000
              } INSTR;

module alu8(
            input [0:7]        A,
            input [0:7]        B,
            input [0:3]        sel,
            input              c_in,
            output reg [0:7]   Y,
            output reg         C
            );

   wire [7:0]            sum;
   wire                  carry;
   adder8 adder(
                .A(A),
                .B(B),
                .c_in(c_in),
                .S(sum),
                .c_out(carry)
                );


   wire [7:0]            difference;
   wire                  burrow;
   adder8 subtractor(
                .A(A),
                .B(~B),
                .c_in(1'b1),
                .S(difference),
                .c_out(borrow)
                );


   wire [7:0]            and_value;
   and8 _and(
             .A(A),
             .B(B),
             .Y(and_value));

    wire [7:0] or_value;
    or8 _or(A,B,or_value);

    wire [7:0] xor_value;
    xor8 _xor(A,B,xor_value);

    wire [7:0] not_value;
    not8 _xnot(A,not_value);

    wire [7:0] nand_value;
    nand8 _nand(A,B,nand_value);

    wire[7:0] nor_value;
    nor8 _nor(A,B,nor_value);

    wire [7:0] xnor_value;
    xnor8 _xnor(A,B,xnor_value);

   always @* begin

      case (sel)

        INSTR_ADD: begin
           Y = sum;
           C = carry;
        end

        INSTR_SUB: begin
           Y = difference;
           C = borrow;
        end

        INSTR_AND: begin
           Y = and_value;
        end

        INSTR_OR: begin
           Y = or_value;
        end

        INSTR_XOR: begin
           Y = xor_value;
        end

        INSTR_NOT: begin
           Y = not_value;
        end

        INSTR_NAND: begin
           Y = nand_value;
        end

        INSTR_NOR: begin
           Y = nor_value;
        end

        INSTR_XNOR: begin
           Y = xnor_value;
        end

        default: begin
           Y = 0;
        end
      endcase; // case (sel)
   end
endmodule; // alu8
