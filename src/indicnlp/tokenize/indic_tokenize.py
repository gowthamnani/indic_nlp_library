
# Copyright Anoop Kunchukuttan 2014 - present
#
# This file is part of Indic NLP Library.
# 
# Indic NLP LIbrary is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Foobar is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#        GNU General Public License for more details.
# 
#        You should have received a copy of the GNU General Public License
#        along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#

#Program for tokenizing Indian language input 
#
# @author Anoop Kunchukuttan 
#

import string, re, sys, codecs

triv_tokenizer_pat=re.compile(ur'(['+string.punctuation+ur'\u0964\u0965'+ur'])')

def trivial_tokenize(s): 
    """
    A trivial tokenizer which just tokenizes on the punctuation boundaries. This also includes punctuations for the Indian language scripts
      - the purna virama and the deergha virama
    returns a list of tokens   
    """
    tok_str=triv_tokenizer_pat.sub(r' \1 ',s.replace('\t',' '))
    return re.sub(r'[ ]+',u' ',tok_str).strip(' ').split(' ')


if __name__ == '__main__': 

    if len(sys.argv)<4:
        print "Usage: python indic_tokenize.py <infile> <outfile> <language>"
        sys.exit(1)

    with codecs.open(sys.argv[1],'r','utf-8') as ifile:
        with codecs.open(sys.argv[2],'w','utf-8') as ofile:
            for line in ifile.readlines():
                tokenized_line=string.join(trivial_tokenize(line),sep=' ')
                ofile.write(tokenized_line)
