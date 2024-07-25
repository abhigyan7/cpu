`timescale 1ns/1ps;

module half_adder(a, b, c_out, s);
   input a, b;
   output c_out, s;

   assign c_out = a & b;
   assign s = a ^ b;
endmodule; // half_adder


module full_adder(a, b, c_in, c_out, s);
   input a, b, c_in;
   output c_out, s;
   wire   i1, i2, i3;

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


