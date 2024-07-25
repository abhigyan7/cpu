module and8(
            input [0:7] A,
            input [0:7] B,
            output [0:7] Y
            );
   assign Y = A & B;
endmodule; // and8

module or8(
            input [0:7] A,
            input [0:7] B,
            output [0:7] Y
            );
   assign Y = A | B;
endmodule; // or8

module nand8(
            input [0:7] A,
            input [0:7] B,
            output [0:7] Y
            );
   assign Y = ~(A & B);
endmodule; // nand8

module nor8(
            input [0:7] A,
            input [0:7] B,
            output [0:7] Y
            );
   assign Y = ~(A | B);
endmodule; // nor8

module not8(
            input [0:7] A,
            output [0:7] Y
            );
   assign Y = ~A;
endmodule; // not8

module xor8(
            input [0:7] A,
            input [0:7] B,
            output [0:7] Y
            );
   assign Y = A ^ B;
endmodule; // xor8


module xnor8(
            input [0:7] A,
            input [0:7] B,
            output [0:7] Y
            );
   assign Y = ~(A ^ B);
endmodule; // xnor8
