`timescale 1ns/1ps;

module half_adder(
                  input a, b,
                  output c_out, s
                  );

   assign c_out = a & b;
   assign s = a ^ b;
endmodule; // half_adder


module full_adder(
                  input a, b, c_in,
                  output s, c_out
                  );


   wire                  i1, i2, i3;
   half_adder ha1 (
                   .a(a),
                   .b(b),
                   .s(i1),
                   .c_out(i2)
   );

   half_adder ha2 (
                   .a(c_in),
                   .b(i1),
                   .s(s),
                   .c_out(i3)
   );

   assign c_out = i3 | i2;

endmodule; // full_adder

module adder8(
              input [7:0] A,
              input [7:0] B,
              input c_in,
              output [7:0] S,
              output c_out
              );



   wire [7:0]        carry;

   full_adder fa1 (A[0], B[0], c_in, S[0], carry[0]);
   full_adder fa2 (A[1], B[1], carry[0], S[1], carry[1]);
   full_adder fa3 (A[2], B[2], carry[1], S[2], carry[2]);
   full_adder fa4 (A[3], B[3], carry[2], S[3], carry[3]);
   full_adder fa5 (A[4], B[4], carry[3], S[4], carry[4]);
   full_adder fa6 (A[5], B[5], carry[4], S[5], carry[5]);
   full_adder fa7 (A[6], B[6], carry[5], S[6], carry[6]);
   full_adder fa8 (A[7], B[7], carry[6], S[7], carry[7]);

   assign c_out = carry[7];

endmodule; // adder8
