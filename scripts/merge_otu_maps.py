#!/usr/bin/env python
# File created on 08 Nov 2009.
from __future__ import division

__author__ = "Greg Caporaso"
__copyright__ = "Copyright 2010, The QIIME Project"
__credits__ = ["Greg Caporaso", "Dan Knights"]
__license__ = "GPL"
__version__ = "1.1.0"
__maintainer__ = "Greg Caporaso"
__email__ = "gregcaporaso@gmail.com"
__status__ = "Release"

from optparse import make_option
from qiime.pick_otus import map_otu_map_files, write_otu_map
from qiime.util import parse_command_line_parameters

script_info={}
script_info['brief_description']="""Merge OTU mapping files"""
script_info['script_description']="""This script merges OTU mapping files generated by denoise.py and/or pick_otus.py

For example, if otu_map1.txt contains:

=   ====    ====    ====
0   seq1    seq2    seq5
1   seq3    seq4    
2   seq6    seq7    seq8
=   ====    ====    ====

and otu_map2.txt contains:

=== =   =
110 0   2
221 1
=== =   =

The resulting OTU table will be:

=== ====    ====    ====    ====    ====    ====
110 seq1    seq2    seq5    seq6    seq7    seq8
221 seq3    seq4
=== ====    ====    ====    ====    ====    ====
"""
script_info['script_usage']=[]
script_info['script_usage'].append(("""Example:""","""If the seq_ids in otu_table2.txt are otu_ids in otu_table1.txt, expand the seq_ids in otu_table2.txt to be the full list of associated seq_ids from otu_table1.txt. Write the resulting otu table to otu_table.txt (-o).""","""merge_otu_maps.py -i otu_map1.txt,otu_map2.txt -o otu_table.txt"""))
script_info['output_description']="""The result of this script is an OTU mapping file."""
script_info['required_options']=[\
    make_option('-i','--otu_map_fps',\
                    help='the otu map filepaths, comma-separated and '+\
                    'ordered as the OTU pickers were run [REQUIRED]')\
]

script_info['optional_options']=[\
    make_option('-o','--output_fp',\
                help='path to write output OTU map [REQUIRED]')\
]

script_info['version'] = __version__

def main():
    option_parser, opts, args =\
       parse_command_line_parameters(**script_info)
    
    otu_files = map(open,opts.otu_map_fps.split(','))
    
    try:
        otu_map = map_otu_map_files(otu_files)
    except KeyError,e:
        print 'Some keys do not map ('+ str(e) +') -- is the order of'+\
        ' your OTU maps equivalent to the order in which the OTU pickers'+\
        ' were run?'
        exit(1)
        
    write_otu_map(otu_map,opts.output_fp)

    
if __name__ == "__main__":
    main()
