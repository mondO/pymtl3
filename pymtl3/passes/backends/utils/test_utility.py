#=========================================================================
# test_utility.py
#=========================================================================
# Author : Peitian Pan
# Date   : Jun 5, 2019
"""Provide utility methods for testing."""

def trim( s ):
  string = []
  lines = s.split( '\n' )
  for line in lines:
    _line = line.split()
    _string = "".join( _line )
    if _string and not _string.startswith( '//' ):
      string.append( "".join( line.split() ) )
  return "\n".join( string )

def check_eq( s, t ):
  if isinstance( s, list ) and isinstance( t, list ):
    for _s, _t in zip( s, t ):
      assert trim(_s) == trim(_t)
  else:
    assert trim(s) == trim(t)
