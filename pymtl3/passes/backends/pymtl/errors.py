#=========================================================================
# errors.py
#=========================================================================
# Author : Peitian Pan
# Date   : Dec 23, 2019
"""Exception classes for PyMTL backend."""

import inspect
import os


class PyMTLTranslationError( Exception ):
  """PyMTL translation error."""
  def __init__( self, blk, _ast, msg ):
    ast = _ast.ast
    fname = os.path.abspath( inspect.getsourcefile( blk ) )
    line = inspect.getsourcelines( blk )[1]
    col = 0
    code = ""
    try:
      line += ast.lineno - 1
      col = ast.col_offset
      code_line = inspect.getsourcelines( blk )[0][ ast.lineno-1 ]
      code = '\n  ' + code_line.strip() + \
        '\n  '+ ' ' * (col-len(code_line)+len(code_line.lstrip())) + '^'
    except AttributeError:
      # The given AST node is neither expr nor stmt
      pass
    return super().__init__(
      f"\nIn file {fname}, Line {line}, Col {col}:{code}\n- {msg}" )

class PyMTLReservedKeywordError( Exception ):
  """PyMTL reserved keyword error."""
  def __init__( self, name, msg ):
    return super().__init__(
      f"- {name} is a PyMTL reserved keyword!\n- {msg}" )
