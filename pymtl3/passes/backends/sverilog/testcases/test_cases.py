"""
=========================================================================
test_cases.py
=========================================================================
Centralized test case repository for the SystemVerilog backend.

Author : Peitian Pan
Date   : Dec 16, 2019
"""

from textwrap import dedent

from pymtl3 import *
from pymtl3.testcases import add_attributes, \
      CasePassThroughComp, CaseSequentialPassThroughComp, \
      CaseBits32x2ConcatComp, CaseBits32x2ConcatConstComp, \
      CaseBits32x2ConcatMixedComp, CaseBits64SextInComp, \
      CaseBits64ZextInComp, CaseBits32x2ConcatFreeVarComp, \
      CaseBits32x2ConcatUnpackedSignalComp, CaseBits32BitSelUpblkComp, \
      CaseBits64PartSelUpblkComp, CaseSVerilogReservedComp, \
      CaseReducesInx3OutComp, CaseIfBasicComp, CaseIfDanglingElseInnerComp, \
      CaseIfDanglingElseOutterComp, CaseElifBranchComp, CaseNestedIfComp, \
      CaseForRangeLowerUpperStepPassThroughComp, CaseIfExpInForStmtComp, \
      CaseIfBoolOpInForStmtComp, CaseIfTmpVarInForStmtComp, CaseFixedSizeSliceComp, \
      CaseIfExpUnaryOpInForStmtComp, Bits32Foo, NestedStructPackedPlusScalar, \
      CaseBits32FooInBits32OutComp, CaseConstStructInstComp, \
      CaseStructPackedArrayUpblkComp, CaseNestedStructPackedArrayUpblkComp, \
      Bits32x5Foo, CaseConnectValRdyIfcUpblkComp, CaseArrayBits32IfcInUpblkComp, \
      CaseInterfaceArrayNonStaticIndexComp, \
      CaseBits32SubCompAttrUpblkComp, CaseBits32ArraySubCompAttrUpblkComp, \
      CaseConnectInToWireComp, CaseConnectBitsConstToOutComp, \
      CaseConnectConstToOutComp, CaseConnectBitSelToOutComp, \
      CaseConnectSliceToOutComp, CaseConnectConstStructAttrToOutComp, \
      CaseConnectArrayStructAttrToOutComp, CaseConnectNestedStructPackedArrayComp, \
      CaseConnectValRdyIfcComp, CaseConnectArrayNestedIfcComp, \
      CaseBits32ConnectSubCompAttrComp, CaseBits32ArrayConnectSubCompAttrComp, \
      CaseConnectLiteralStructComp, CaseConnectPassThroughLongNameComp, \
      CaseLambdaConnectComp, ThisIsABitStructWithSuperLongName

import pymtl3.passes.rtlir.rtype.RTLIRDataType as rdt

CasePassThroughComp = add_attributes( CasePassThroughComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = in_;
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = in_;
          end

        endmodule
    '''
)

CaseSequentialPassThroughComp = add_attributes( CaseSequentialPassThroughComp,
    'REF_UPBLK',
    '''\
        always_ff @(posedge clk) begin : upblk
          out <= in_;
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          always_ff @(posedge clk) begin : upblk
            out <= in_;
          end

        endmodule
    '''
)

CaseConnectPassThroughLongNameComp = add_attributes( CaseConnectPassThroughLongNameComp,
    'REF_PORT',
    '''\
        input logic [0:0] clk,
        input logic [31:0] in_,
        output logic [31:0] out,
        input logic [0:0] reset
    ''',
    'REF_WIRE',
    '''\
    ''',
    'REF_CONN',
    '''\
        assign out = in_;
    ''',
    'REF_SRC',
    '''\
        module DUT__a840bd1c84c05ea2
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          assign out = in_;

        endmodule
    ''',
    'REF_STRUCT',
    '''\
    ''',
)

CaseLambdaConnectComp = add_attributes( CaseLambdaConnectComp,
    'REF_UPBLK',
    '''\
        always_comb begin : _lambda__s_out
          out = in_ + 32'd42;
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          always_comb begin : _lambda__s_out
            out = in_ + 32'd42;
          end

        endmodule
    '''
)

CaseBits32x2ConcatComp = add_attributes( CaseBits32x2ConcatComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = { in_1, in_2 };
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_1,
          input logic [31:0] in_2,
          output logic [63:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = { in_1, in_2 };
          end

        endmodule
    '''
)

CaseBits32x2ConcatConstComp = add_attributes( CaseBits32x2ConcatConstComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = { 32'd42, 32'd0 };
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          output logic [63:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = { 32'd42, 32'd0 };
          end

        endmodule
    '''
)

CaseBits32x2ConcatMixedComp = add_attributes( CaseBits32x2ConcatMixedComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = { in_, 32'd0 };
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [63:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = { in_, 32'd0 };
          end

        endmodule
    '''
)

CaseBits64SextInComp = add_attributes( CaseBits64SextInComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = { { 32 { in_[31] } }, in_ };
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [63:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = { { 32 { in_[31] } }, in_ };
          end

        endmodule
    '''
)

CaseBits64ZextInComp = add_attributes( CaseBits64ZextInComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = { { 32 { 1'b0 } }, in_ };
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [63:0] out,
          input logic [0:0] reset
        );

          // @s.update
          // def upblk():
          //   s.out = zext( s.in_, 64 )

          always_comb begin : upblk
            out = { { 32 { 1'b0 } }, in_ };
          end

        endmodule
    '''
)

CaseBits32x2ConcatFreeVarComp = add_attributes( CaseBits32x2ConcatFreeVarComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = { in_, __const__STATE_IDLE };
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [63:0] out,
          input logic [0:0] reset
        );
          localparam [31:0] __const__STATE_IDLE = 32'd0;

          always_comb begin : upblk
            out = { in_, __const__STATE_IDLE };
          end

        endmodule
    '''
)

CaseBits32x2ConcatUnpackedSignalComp = add_attributes( CaseBits32x2ConcatUnpackedSignalComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = { in_[0], in_[1] };
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_ [0:1],
          output logic [63:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = { in_[0], in_[1] };
          end

        endmodule
    '''
)

CaseBits32BitSelUpblkComp = add_attributes( CaseBits32BitSelUpblkComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = in_[1];
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [0:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = in_[1];
          end

        endmodule
    '''
)

CaseBits64PartSelUpblkComp = add_attributes( CaseBits64PartSelUpblkComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = in_[35:4];
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [63:0] in_,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = in_[35:4];
          end

        endmodule
    '''
)

CaseReducesInx3OutComp = add_attributes( CaseReducesInx3OutComp,
    'REF_UPBLK',
    '''\
        always_comb begin : v_reduce
          out = ( ( & in_1 ) & ( | in_2 ) ) | ( ^ in_3 );
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_1,
          input logic [31:0] in_2,
          input logic [31:0] in_3,
          output logic [0:0] out,
          input logic [0:0] reset
        );

          always_comb begin : v_reduce
            out = ( ( & in_1 ) & ( | in_2 ) ) | ( ^ in_3 );
          end

        endmodule
    '''
)

CaseIfBasicComp = add_attributes( CaseIfBasicComp,
    'REF_UPBLK',
    '''\
        always_comb begin : if_basic
          if ( in_[7:0] == 8'd255 ) begin
            out = in_[15:8];
          end
          else
            out = 8'd0;
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [15:0] in_,
          output logic [7:0] out,
          input logic [0:0] reset
        );

          always_comb begin : if_basic
            if ( in_[7:0] == 8'd255 ) begin
              out = in_[15:8];
            end
            else
              out = 8'd0;
          end

        endmodule
    '''
)

CaseIfDanglingElseInnerComp = add_attributes( CaseIfDanglingElseInnerComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          if ( 1'd1 ) begin
            if ( 1'd0 ) begin
              out = in_1;
            end
            else
              out = in_2;
          end
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_1,
          input logic [31:0] in_2,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            if ( 1'd1 ) begin
              if ( 1'd0 ) begin
                out = in_1;
              end
              else
                out = in_2;
            end
          end

        endmodule
    '''
)

CaseIfDanglingElseOutterComp = add_attributes( CaseIfDanglingElseOutterComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          if ( 1'd1 ) begin
            if ( 1'd0 ) begin
              out = in_1;
            end
          end
          else
            out = in_2;
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_1,
          input logic [31:0] in_2,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            if ( 1'd1 ) begin
              if ( 1'd0 ) begin
                out = in_1;
              end
            end
            else
              out = in_2;
          end

        endmodule
    '''
)

CaseElifBranchComp = add_attributes( CaseElifBranchComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          if ( 1'd1 ) begin
            out = in_1;
          end
          else if ( 1'd0 ) begin
            out = in_2;
          end
          else
            out = in_3;
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_1,
          input logic [31:0] in_2,
          input logic [31:0] in_3,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            if ( 1'd1 ) begin
              out = in_1;
            end
            else if ( 1'd0 ) begin
              out = in_2;
            end
            else
              out = in_3;
          end

        endmodule
    '''
)

CaseNestedIfComp = add_attributes( CaseNestedIfComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          if ( 1'd1 ) begin
            if ( 1'd0 ) begin
              out = in_1;
            end
            else
              out = in_2;
          end
          else if ( 1'd0 ) begin
            if ( 1'd1 ) begin
              out = in_2;
            end
            else
              out = in_3;
          end
          else if ( 1'd1 ) begin
            out = in_3;
          end
          else
            out = in_1;
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_1,
          input logic [31:0] in_2,
          input logic [31:0] in_3,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            if ( 1'd1 ) begin
              if ( 1'd0 ) begin
                out = in_1;
              end
              else
                out = in_2;
            end
            else if ( 1'd0 ) begin
              if ( 1'd1 ) begin
                out = in_2;
              end
              else
                out = in_3;
            end
            else if ( 1'd1 ) begin
              out = in_3;
            end
            else
              out = in_1;
          end

        endmodule
    '''
)

CaseForRangeLowerUpperStepPassThroughComp = add_attributes( CaseForRangeLowerUpperStepPassThroughComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          for ( int i = 0; i < 5; i += 2 )
            out[i] = in_[i];
          for ( int i = 1; i < 5; i += 2 )
            out[i] = in_[i];
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_ [0:4],
          output logic [31:0] out [0:4],
          input logic [0:0] reset
        );

          always_comb begin : upblk
            for ( int i = 0; i < 5; i += 2 )
              out[i] = in_[i];
            for ( int i = 1; i < 5; i += 2 )
              out[i] = in_[i];
          end

        endmodule
    '''
)

CaseIfExpInForStmtComp = add_attributes( CaseIfExpInForStmtComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          for ( int i = 0; i < 5; i += 1 )
            out[i] = ( i == 1 ) ? in_[i] : in_[0];
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_ [0:4],
          output logic [31:0] out [0:4],
          input logic [0:0] reset
        );

          always_comb begin : upblk
            for ( int i = 0; i < 5; i += 1 )
              out[i] = ( i == 1 ) ? in_[i] : in_[0];
          end

        endmodule
    '''
)

CaseIfExpUnaryOpInForStmtComp = add_attributes( CaseIfExpUnaryOpInForStmtComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          for ( int i = 0; i < 5; i += 1 )
            out[i] = ( i == 1 ) ? ~in_[i] : in_[0];
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_ [0:4],
          output logic [31:0] out [0:4],
          input logic [0:0] reset
        );

          always_comb begin : upblk
            for ( int i = 0; i < 5; i += 1 )
              out[i] = ( i == 1 ) ? ~in_[i] : in_[0];
          end

        endmodule
    '''
)

CaseIfBoolOpInForStmtComp = add_attributes( CaseIfBoolOpInForStmtComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          for ( int i = 0; i < 5; i += 1 )
            if ( ( in_[i] != 32'd0 ) && ( ( i < 4 ) ? in_[i + 1] != 32'd0 : in_[4] != 32'd0 ) ) begin
              out[i] = in_[i];
            end
            else
              out[i] = 32'd0;
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_ [0:4],
          output logic [31:0] out [0:4],
          input logic [0:0] reset
        );

          always_comb begin : upblk
            for ( int i = 0; i < 5; i += 1 )
              if ( ( in_[i] != 32'd0 ) && ( ( i < 4 ) ? in_[i + 1] != 32'd0 : in_[4] != 32'd0 ) ) begin
                out[i] = in_[i];
              end
              else
                out[i] = 32'd0;
          end

        endmodule
    '''
)

CaseIfTmpVarInForStmtComp = add_attributes( CaseIfTmpVarInForStmtComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          for ( int i = 0; i < 5; i += 1 ) begin
            if ( ( in_[i] != 32'd0 ) && ( ( i < 4 ) ? in_[i + 1] != 32'd0 : in_[4] != 32'd0 ) ) begin
              __tmpvar__upblk_tmpvar = in_[i];
            end
            else
              __tmpvar__upblk_tmpvar = 32'd0;
            out[i] = __tmpvar__upblk_tmpvar;
          end
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_ [0:4],
          output logic [31:0] out [0:4],
          input logic [0:0] reset
        );
          logic [31:0] __tmpvar__upblk_tmpvar;

          always_comb begin : upblk
            for ( int i = 0; i < 5; i += 1 ) begin
              if ( ( in_[i] != 32'd0 ) && ( ( i < 4 ) ? in_[i + 1] != 32'd0 : in_[4] != 32'd0 ) ) begin
                __tmpvar__upblk_tmpvar = in_[i];
              end
              else
                __tmpvar__upblk_tmpvar = 32'd0;
              out[i] = __tmpvar__upblk_tmpvar;
            end
          end

        endmodule
    '''
)

CaseFixedSizeSliceComp = add_attributes( CaseFixedSizeSliceComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          for ( int i = 0; i < 2; i += 1 )
            out[i] = in_[i * 8 +: 8];
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [15:0] in_,
          output logic [7:0] out [0:1],
          input logic [0:0] reset
        );

          always_comb begin : upblk
            for ( int i = 0; i < 2; i += 1 )
              out[i] = in_[i * 8 +: 8];
          end

        endmodule
    '''
)

CaseBits32FooInBits32OutComp = add_attributes( CaseBits32FooInBits32OutComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = in_.foo;
        end
    ''',
    'REF_SRC',
    '''\
        typedef struct packed {
          logic [31:0] foo;
        } Bits32Foo;

        module DUT
        (
          input logic [0:0] clk,
          input Bits32Foo in_,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = in_.foo;
          end

        endmodule
    '''
)

CaseConstStructInstComp = add_attributes( CaseConstStructInstComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = in_.foo;
        end
    ''',
    'REF_SRC',
    '''\
        typedef struct packed {
          logic [31:0] foo;
        } Bits32Foo;

        module DUT
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );
          localparam Bits32Foo in_ = { 32'd0 };

          always_comb begin : upblk
            out = in_.foo;
          end

        endmodule
    '''
)

CaseStructPackedArrayUpblkComp = add_attributes( CaseStructPackedArrayUpblkComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = { in_.foo[0], in_.foo[1], in_.foo[2] };
        end
    ''',
    'REF_SRC',
    '''\
        typedef struct packed {
          logic [4:0][31:0] foo;
        } Bits32x5Foo;

        module DUT
        (
          input logic [0:0] clk,
          input Bits32x5Foo in_,
          output logic [95:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = { in_.foo[0], in_.foo[1], in_.foo[2] };
          end

        endmodule
    '''
)

CaseNestedStructPackedArrayUpblkComp = add_attributes( CaseNestedStructPackedArrayUpblkComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = { in_.bar[0], in_.woo.foo, in_.foo };
        end
    ''',
    'REF_SRC',
    '''\
        typedef struct packed {
          logic [31:0] foo;
        } Bits32Foo;

        typedef struct packed {
          logic [31:0] foo;
          logic [1:0][31:0] bar;
          Bits32Foo woo;
        } NestedStructPackedPlusScalar;

        module DUT
        (
          input logic [0:0] clk,
          input NestedStructPackedPlusScalar in_,
          output logic [95:0] out,
          input logic [0:0] reset
        );

          always_comb begin : upblk
            out = { in_.bar[0], in_.woo.foo, in_.foo };
          end

        endmodule
    '''
)

CaseConnectValRdyIfcUpblkComp = add_attributes( CaseConnectValRdyIfcUpblkComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out__val = in___val;
          out__msg = in___msg;
          in___rdy = out__rdy;
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [0:0] reset,
          input logic [31:0] in___msg,
          output logic [0:0] in___rdy,
          input logic [0:0] in___val,
          output logic [31:0] out__msg,
          input logic [0:0] out__rdy,
          output logic [0:0] out__val
        );

          always_comb begin : upblk
            out__val = in___val;
            out__msg = in___msg;
            in___rdy = out__rdy;
          end

        endmodule
    '''
)

CaseArrayBits32IfcInUpblkComp = add_attributes( CaseArrayBits32IfcInUpblkComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = in___1__foo;
        end
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset,
          input logic [31:0] in___0__foo,
          input logic [31:0] in___1__foo,
          input logic [31:0] in___2__foo,
          input logic [31:0] in___3__foo,
          input logic [31:0] in___4__foo
        );

          always_comb begin : upblk
            out = in___1__foo;
          end

        endmodule
    '''
)

CaseBits32SubCompAttrUpblkComp = add_attributes( CaseBits32SubCompAttrUpblkComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = b__out;
        end
    ''',
    'REF_SRC',
    '''\
        module Bits32OutDrivenComp
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          assign out = 32'd42;

        endmodule

        module DUT
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );
          logic [0:0] b__clk;
          logic [31:0] b__out;
          logic [0:0] b__reset;

          Bits32OutDrivenComp b
          (
            .clk( b__clk ),
            .out( b__out ),
            .reset( b__reset )
          );

          always_comb begin : upblk
            out = b__out;
          end

          assign b__clk = clk;
          assign b__reset = reset;

        endmodule
    '''
)

CaseBits32ArraySubCompAttrUpblkComp = add_attributes( CaseBits32ArraySubCompAttrUpblkComp,
    'REF_UPBLK',
    '''\
        always_comb begin : upblk
          out = b__1__out;
        end
    ''',
    'REF_SRC',
    '''\
        module Bits32OutDrivenComp
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          assign out = 32'd42;

        endmodule

        module DUT
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );
          logic [0:0] b__0__clk;
          logic [31:0] b__0__out;
          logic [0:0] b__0__reset;

          Bits32OutDrivenComp b__0
          (
            .clk( b__0__clk ),
            .out( b__0__out ),
            .reset( b__0__reset )
          );

          logic [0:0] b__1__clk;
          logic [31:0] b__1__out;
          logic [0:0] b__1__reset;

          Bits32OutDrivenComp b__1
          (
            .clk( b__1__clk ),
            .out( b__1__out ),
            .reset( b__1__reset )
          );

          logic [0:0] b__2__clk;
          logic [31:0] b__2__out;
          logic [0:0] b__2__reset;

          Bits32OutDrivenComp b__2
          (
            .clk( b__2__clk ),
            .out( b__2__out ),
            .reset( b__2__reset )
          );

          logic [0:0] b__3__clk;
          logic [31:0] b__3__out;
          logic [0:0] b__3__reset;

          Bits32OutDrivenComp b__3
          (
            .clk( b__3__clk ),
            .out( b__3__out ),
            .reset( b__3__reset )
          );

          logic [0:0] b__4__clk;
          logic [31:0] b__4__out;
          logic [0:0] b__4__reset;

          Bits32OutDrivenComp b__4
          (
            .clk( b__4__clk ),
            .out( b__4__out ),
            .reset( b__4__reset )
          );

          always_comb begin : upblk
            out = b__1__out;
          end

          assign b__0__clk = clk;
          assign b__0__reset = reset;
          assign b__1__clk = clk;
          assign b__1__reset = reset;
          assign b__2__clk = clk;
          assign b__2__reset = reset;
          assign b__3__clk = clk;
          assign b__3__reset = reset;
          assign b__4__clk = clk;
          assign b__4__reset = reset;

        endmodule
    '''
)

CaseConnectInToWireComp = add_attributes( CaseConnectInToWireComp,
    'REF_PORT',
    '''\
        input logic [0:0] clk,
        input logic [31:0] in_ [0:4],
        output logic [31:0] out,
        input logic [0:0] reset
    ''',
    'REF_WIRE',
    '''\
        logic [31:0] wire_ [0:4];
    ''',
    'REF_CONST',
    '',
    'REF_CONN',
    '''\
        assign out = wire_[2];
        assign wire_[0] = in_[0];
        assign wire_[1] = in_[1];
        assign wire_[2] = in_[2];
        assign wire_[3] = in_[3];
        assign wire_[4] = in_[4];
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_ [0:4],
          output logic [31:0] out,
          input logic [0:0] reset
        );
          logic [31:0] wire_ [0:4];

          assign out = wire_[2];
          assign wire_[0] = in_[0];
          assign wire_[1] = in_[1];
          assign wire_[2] = in_[2];
          assign wire_[3] = in_[3];
          assign wire_[4] = in_[4];

        endmodule
    '''
)

CaseConnectBitsConstToOutComp = add_attributes( CaseConnectBitsConstToOutComp,
    'REF_PORT',
    '''\
        input logic [0:0] clk,
        output logic [31:0] out,
        input logic [0:0] reset
    ''',
    'REF_WIRE',
    '',
    'REF_CONST',
    '',
    'REF_CONN',
    '''\
        assign out = 32'd0;
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          assign out = 32'd0;

        endmodule
    '''
)

CaseConnectConstToOutComp = add_attributes( CaseConnectConstToOutComp,
    'REF_PORT',
    '''\
        input logic [0:0] clk,
        output logic [31:0] out,
        input logic [0:0] reset
    ''',
    'REF_WIRE',
    '',
    'REF_CONST',
    '''\
        localparam [31:0] const_ [0:4] = '{ 32'd42, 32'd42, 32'd42, 32'd42, 32'd42 };
    ''',
    'REF_CONN',
    '''\
        assign out = 32'd42;
    ''',
    'REF_SRC',
    # const_ is not used in upblks so will be optimized away
    '''\
        module DUT
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          assign out = 32'd42;

        endmodule
    '''
)

CaseConnectBitSelToOutComp = add_attributes( CaseConnectBitSelToOutComp,
    'REF_PORT',
    '''\
        input logic [0:0] clk,
        input logic [31:0] in_,
        output logic [0:0] out,
        input logic [0:0] reset
    ''',
    'REF_WIRE',
    '',
    'REF_CONST',
    '',
    'REF_CONN',
    '''\
        assign out = in_[0:0];
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [0:0] out,
          input logic [0:0] reset
        );

          assign out = in_[0:0];

        endmodule
    '''
)

CaseConnectSliceToOutComp = add_attributes( CaseConnectSliceToOutComp,
    'REF_PORT',
    '''\
        input logic [0:0] clk,
        input logic [31:0] in_,
        output logic [3:0] out,
        input logic [0:0] reset
    ''',
    'REF_WIRE',
    '',
    'REF_CONST',
    '',
    'REF_CONN',
    '''\
        assign out = in_[7:4];
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [31:0] in_,
          output logic [3:0] out,
          input logic [0:0] reset
        );

          assign out = in_[7:4];

        endmodule
    '''
)

CaseConnectConstStructAttrToOutComp = add_attributes( CaseConnectConstStructAttrToOutComp,
    'REF_PORT',
    '''\
        input logic [0:0] clk,
        output logic [31:0] out,
        input logic [0:0] reset
    ''',
    'REF_WIRE',
    '',
    'REF_CONN',
    '''\
        assign out = 32'd42;
    ''',
    'REF_STRUCT',
    (
        rdt.Struct('Bits32Foo', {'foo':rdt.Vector(32)}),
        dedent('''\
                  typedef struct packed {
                    logic [31:0] foo;
                  } Bits32Foo;
               ''')
    ),
    'REF_SRC',
    # struct definition will be eliminated because it's not used 
    # in an upblk
    '''\
        module DUT
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          assign out = 32'd42;

        endmodule
    '''
)

CaseConnectLiteralStructComp = add_attributes( CaseConnectLiteralStructComp,
    'REF_PORT',
    '''\
        input logic [0:0] clk,
        output NestedStructPackedPlusScalar out,
        input logic [0:0] reset
    ''',
    'REF_WIRE',
    '',
    'REF_CONN',
    '''\
        assign out = { 32'd42, { 32'd1, 32'd2 }, { 32'd3 } };
    ''',
    'REF_STRUCT',
    (
        rdt.Struct('NestedStructPackedPlusScalar', {
          'foo':rdt.Vector(32),
          'bar':rdt.PackedArray([2], rdt.Vector(32)),
          'woo':rdt.Struct('Bits32Foo', {'foo':rdt.Vector(32)}),
        }),
        dedent('''\
                  typedef struct packed {
                    logic [31:0] foo;
                    logic [1:0][31:0] bar;
                    Bits32Foo woo;
                  } NestedStructPackedPlusScalar;
               ''')
    ),
    'REF_SRC',
    '''\
        typedef struct packed {
          logic [31:0] foo;
        } Bits32Foo;

        typedef struct packed {
          logic [31:0] foo;
          logic [1:0][31:0] bar;
          Bits32Foo woo;
        } NestedStructPackedPlusScalar;

        module DUT
        (
          input logic [0:0] clk,
          output NestedStructPackedPlusScalar out,
          input logic [0:0] reset
        );

          assign out = { 32'd42, { { 32'd2, 32'd1 } }, { 32'd3 } };

        endmodule
    '''
)

CaseConnectArrayStructAttrToOutComp = add_attributes( CaseConnectArrayStructAttrToOutComp,
    'REF_PORT',
    '''\
        input logic [0:0] clk,
        input Bits32x5Foo in_,
        output logic [31:0] out,
        input logic [0:0] reset
    ''',
    'REF_WIRE',
    '',
    'REF_CONN',
    '''\
        assign out = in_.foo[1];
    ''',
    'REF_STRUCT',
    (
        rdt.Struct('Bits32x5Foo', {'foo':rdt.PackedArray([5], rdt.Vector(32))}),
        dedent('''\
                  typedef struct packed {
                    logic [4:0][31:0] foo;
                  } Bits32x5Foo;
               ''')
    ),
    'REF_SRC',
    '''\
        typedef struct packed {
          logic [4:0][31:0] foo;
        } Bits32x5Foo;

        module DUT
        (
          input logic [0:0] clk,
          input Bits32x5Foo in_,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          assign out = in_.foo[1];

        endmodule
    '''
)

CaseConnectNestedStructPackedArrayComp = add_attributes( CaseConnectNestedStructPackedArrayComp,
    'REF_PORT',
    '''\
        input logic [0:0] clk,
        input NestedStructPackedPlusScalar in_,
        output logic [95:0] out,
        input logic [0:0] reset
    ''',
    'REF_WIRE',
    '',
    'REF_CONN',
    '''\
        assign out[31:0] = in_.foo;
        assign out[63:32] = in_.woo.foo;
        assign out[95:64] = in_.bar[0];
    ''',
    'REF_STRUCT',
    (
        rdt.Struct('NestedStructPackedPlusScalar', {
          'foo':rdt.Vector(32),
          'bar':rdt.PackedArray([2], rdt.Vector(32)),
          'woo':rdt.Struct('Bits32Foo', {'foo':rdt.Vector(32)}),
        }),
        dedent('''\
                  typedef struct packed {
                    logic [31:0] foo;
                    logic [1:0][31:0] bar;
                    Bits32Foo woo;
                  } NestedStructPackedPlusScalar;
               ''')
    ),
    'REF_SRC',
    '''\
        typedef struct packed {
          logic [31:0] foo;
        } Bits32Foo;

        typedef struct packed {
          logic [31:0] foo;
          logic [1:0][31:0] bar;
          Bits32Foo woo;
        } NestedStructPackedPlusScalar;

        module DUT
        (
          input logic [0:0] clk,
          input NestedStructPackedPlusScalar in_,
          output logic [95:0] out,
          input logic [0:0] reset
        );

          assign out[31:0] = in_.foo;
          assign out[63:32] = in_.woo.foo;
          assign out[95:64] = in_.bar[0];

        endmodule
    '''
)

CaseConnectValRdyIfcComp = add_attributes( CaseConnectValRdyIfcComp,
    'REF_IFC',
    '''\
        input  logic [31:0] in___msg,
        output logic [0:0]  in___rdy,
        input  logic [0:0]  in___val,
        output logic [31:0] out__msg,
        input  logic [0:0]  out__rdy,
        output logic [0:0]  out__val
    ''',
    'REF_CONN',
    '''\
        assign out__msg = in___msg;
        assign in___rdy = out__rdy;
        assign out__val = in___val;
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [0:0] reset,
          input logic [31:0] in___msg,
          output logic [0:0] in___rdy,
          input logic [0:0] in___val,
          output logic [31:0] out__msg,
          input logic [0:0] out__rdy,
          output logic [0:0] out__val
        );

          assign out__msg = in___msg;
          assign in___rdy = out__rdy;
          assign out__val = in___val;

        endmodule
    '''
)

CaseConnectArrayNestedIfcComp = add_attributes( CaseConnectArrayNestedIfcComp,
    'REF_IFC',
    '''\
        input  logic [0:0]  in___0__ctrl_foo,
        input  logic [31:0] in___0__memifc__msg,
        output logic [0:0]  in___0__memifc__rdy,
        input  logic [0:0]  in___0__memifc__val,
        input  logic [0:0]  in___1__ctrl_foo,
        input  logic [31:0] in___1__memifc__msg,
        output logic [0:0]  in___1__memifc__rdy,
        input  logic [0:0]  in___1__memifc__val,

        output  logic [0:0]  out__0__ctrl_foo,
        output  logic [31:0] out__0__memifc__msg,
        input   logic [0:0]  out__0__memifc__rdy,
        output  logic [0:0]  out__0__memifc__val,
        output  logic [0:0]  out__1__ctrl_foo,
        output  logic [31:0] out__1__memifc__msg,
        input   logic [0:0]  out__1__memifc__rdy,
        output  logic [0:0]  out__1__memifc__val
    ''',
    'REF_CONN',
    '''\
        assign out__0__ctrl_foo = in___0__ctrl_foo;
        assign out__0__memifc__msg = in___0__memifc__msg;
        assign in___0__memifc__rdy = out__0__memifc__rdy;
        assign out__0__memifc__val = in___0__memifc__val;
        assign out__1__ctrl_foo = in___1__ctrl_foo;
        assign out__1__memifc__msg = in___1__memifc__msg;
        assign in___1__memifc__rdy = out__1__memifc__rdy;
        assign out__1__memifc__val = in___1__memifc__val;
    ''',
    'REF_SRC',
    '''\
        module DUT
        (
          input logic [0:0] clk,
          input logic [0:0] reset,
          input logic [0:0] in___0__ctrl_foo,
          input logic [31:0] in___0__memifc__msg,
          output logic [0:0] in___0__memifc__rdy,
          input logic [0:0] in___0__memifc__val,
          input logic [0:0] in___1__ctrl_foo,
          input logic [31:0] in___1__memifc__msg,
          output logic [0:0] in___1__memifc__rdy,
          input logic [0:0] in___1__memifc__val,
          output logic [0:0] out__0__ctrl_foo,
          output logic [31:0] out__0__memifc__msg,
          input logic [0:0] out__0__memifc__rdy,
          output logic [0:0] out__0__memifc__val,
          output logic [0:0] out__1__ctrl_foo,
          output logic [31:0] out__1__memifc__msg,
          input logic [0:0] out__1__memifc__rdy,
          output logic [0:0] out__1__memifc__val
        );

          assign out__0__ctrl_foo = in___0__ctrl_foo;
          assign out__0__memifc__msg = in___0__memifc__msg;
          assign in___0__memifc__rdy = out__0__memifc__rdy;
          assign out__0__memifc__val = in___0__memifc__val;
          assign out__1__ctrl_foo = in___1__ctrl_foo;
          assign out__1__memifc__msg = in___1__memifc__msg;
          assign in___1__memifc__rdy = out__1__memifc__rdy;
          assign out__1__memifc__val = in___1__memifc__val;

        endmodule
    '''
)

CaseBits32ConnectSubCompAttrComp = add_attributes( CaseBits32ConnectSubCompAttrComp,
    'REF_COMP',
    '''\
        logic [0:0] b__clk;
        logic [31:0] b__out;
        logic [0:0] b__reset;

        Bits32OutDrivenComp b
        (
          .clk( b__clk ),
          .out( b__out ),
          .reset( b__reset )
        );
    ''',
    'REF_SRC',
    '''\
        module Bits32OutDrivenComp
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          assign out = 32'd42;

        endmodule

        module DUT
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );
          logic [0:0] b__clk;
          logic [31:0] b__out;
          logic [0:0] b__reset;

          Bits32OutDrivenComp b
          (
            .clk( b__clk ),
            .out( b__out ),
            .reset( b__reset )
          );

          assign b__clk = clk;
          assign b__reset = reset;
          assign out = b__out;

        endmodule
    '''
)

CaseBits32ArrayConnectSubCompAttrComp = add_attributes( CaseBits32ArrayConnectSubCompAttrComp,
    'REF_COMP',
    '''\
        logic [0:0] b__0__clk;
        logic [31:0] b__0__out;
        logic [0:0] b__0__reset;

        Bits32OutDrivenComp b__0
        (
          .clk( b__0__clk ),
          .out( b__0__out ),
          .reset( b__0__reset )
        );

        logic [0:0] b__1__clk;
        logic [31:0] b__1__out;
        logic [0:0] b__1__reset;

        Bits32OutDrivenComp b__1
        (
          .clk( b__1__clk ),
          .out( b__1__out ),
          .reset( b__1__reset )
        );

        logic [0:0] b__2__clk;
        logic [31:0] b__2__out;
        logic [0:0] b__2__reset;

        Bits32OutDrivenComp b__2
        (
          .clk( b__2__clk ),
          .out( b__2__out ),
          .reset( b__2__reset )
        );

        logic [0:0] b__3__clk;
        logic [31:0] b__3__out;
        logic [0:0] b__3__reset;

        Bits32OutDrivenComp b__3
        (
          .clk( b__3__clk ),
          .out( b__3__out ),
          .reset( b__3__reset )
        );

        logic [0:0] b__4__clk;
        logic [31:0] b__4__out;
        logic [0:0] b__4__reset;

        Bits32OutDrivenComp b__4
        (
          .clk( b__4__clk ),
          .out( b__4__out ),
          .reset( b__4__reset )
        );
    ''',
    'REF_SRC',
    '''\
        module Bits32OutDrivenComp
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );

          assign out = 32'd42;

        endmodule

        module DUT
        (
          input logic [0:0] clk,
          output logic [31:0] out,
          input logic [0:0] reset
        );
          logic [0:0] b__0__clk;
          logic [31:0] b__0__out;
          logic [0:0] b__0__reset;

          Bits32OutDrivenComp b__0
          (
            .clk( b__0__clk ),
            .out( b__0__out ),
            .reset( b__0__reset )
          );

          logic [0:0] b__1__clk;
          logic [31:0] b__1__out;
          logic [0:0] b__1__reset;

          Bits32OutDrivenComp b__1
          (
            .clk( b__1__clk ),
            .out( b__1__out ),
            .reset( b__1__reset )
          );

          logic [0:0] b__2__clk;
          logic [31:0] b__2__out;
          logic [0:0] b__2__reset;

          Bits32OutDrivenComp b__2
          (
            .clk( b__2__clk ),
            .out( b__2__out ),
            .reset( b__2__reset )
          );

          logic [0:0] b__3__clk;
          logic [31:0] b__3__out;
          logic [0:0] b__3__reset;

          Bits32OutDrivenComp b__3
          (
            .clk( b__3__clk ),
            .out( b__3__out ),
            .reset( b__3__reset )
          );

          logic [0:0] b__4__clk;
          logic [31:0] b__4__out;
          logic [0:0] b__4__reset;

          Bits32OutDrivenComp b__4
          (
            .clk( b__4__clk ),
            .out( b__4__out ),
            .reset( b__4__reset )
          );

          assign b__0__clk = clk;
          assign b__0__reset = reset;
          assign b__1__clk = clk;
          assign b__1__reset = reset;
          assign b__2__clk = clk;
          assign b__2__reset = reset;
          assign b__3__clk = clk;
          assign b__3__reset = reset;
          assign b__4__clk = clk;
          assign b__4__reset = reset;
          assign out = b__1__out;

        endmodule
    '''
)