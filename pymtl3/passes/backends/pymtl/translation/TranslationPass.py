#=========================================================================
# TranslationPass.py
#=========================================================================
# Author : Peitian Pan
# Date   : Dec 23, 2019
"""Translate a PyMTL component hierarhcy into PyMTL source code."""

import filecmp
import os

from pymtl3.passes.BasePass import BasePass, PassMetadata

from .PyMTLTranslator import PyMTLTranslator


class TranslationPass( BasePass ):

  def __call__( s, top ):

    s.top = top
    s.translator = PyMTLTranslator( s.top )
    s.traverse_hierarchy( top )

  def traverse_hierarchy( s, m ):

    if hasattr(m, "pymtl_translate") and m.pymtl_translate:

      if not hasattr( m, '_pass_sverilog_translation' ):
        m._pass_sverilog_translation = PassMetadata()

      s.translator.translate( m )

      module_name = s.translator._top_module_full_name
      output_file = module_name + '.py'
      temporary_file = module_name + '.py.tmp'

      # First write the file to a temporary file
      m._pass_sverilog_translation.is_same = False
      with open( temporary_file, 'w' ) as output:
        output.write( s.translator.hierarchy.src )
        output.flush()
        os.fsync( output )
        output.close()

      # `is_same` is set if there exists a file that has the same filename as
      # `output_file`, and that file is the same as the temporary file
      if ( os.path.exists(output_file) ):
        m._pass_pymtl_translation.is_same = \
            filecmp.cmp( temporary_file, output_file )

      # Rename the temporary file to the output file
      os.rename( temporary_file, output_file )

      # Expose some attributes about the translation process
      m.translated_top_module_name = module_name
      m._translator = s.translator
      m._pass_pymtl_translation.translated = True

    else:
      for child in m.get_child_components():
        s.traverse_hierarchy( child )
