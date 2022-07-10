#!/usr/bin/env python2.7
import sys
import textwrap
import PyPluMA

class FixMegaHitContigPlugin:
    def input(self, infile):
       self.params = dict()
       inputfile = open(infile, 'r')
       for line in inputfile:
           contents = line.strip().split('\t')
           self.params[contents[0]] = contents[1]

    def run(self):
        pass

    def output(self, outfile):
      dic={}
      tmp_contig=""
      min_len=int(self.params["minlen"])
      good=True
      for line in open(PyPluMA.prefix()+"/"+self.params["fasta"]):
        if line[0]==">": 
           if tmp_contig!="":
             if good==True: 
               dic[name]=tmp_contig
             tmp_contig=""
           cut=line.strip()[1:].split(" ")

           if int(cut[3].split("=")[1])<min_len:
             good=False
           else: 
             good=True

           name=">"+cut[0]+"_length_"+cut[3].split("=")[1]+"_cov_"+cut[2].split("=")[1]
        else: tmp_contig+=line.strip()
      dic[name]=tmp_contig

      outputfile = open(outfile, 'w')
      for k in sorted(dic, key=lambda k: len(dic[k]), reverse=True):
        outputfile.write(k)
        outputfile.write('\n')
        outputfile.write(textwrap.fill(dic[k], 100, break_on_hyphens = False))
        outputfile.write('\n')
