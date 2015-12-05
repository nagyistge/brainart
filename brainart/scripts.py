#!/usr/bin/python

'''
script.py: 
Runtime executable

'''

from brainart.utils import get_avg_rgb, get_color_lookup, generate_matching_df
from brainart.db import get_data
from brainart.mosaic import generate
from glob import glob
import numpy as np
import argparse
import pandas
import sys
import os


def main():
    parser = argparse.ArgumentParser(
    description="make images out of brain imaging data")
    parser.add_argument("--input", dest='image', help="full path to jpg image", type=str, default=None,required=True)
    parser.add_argument("--db", dest='db', help="path to folder for png images for database", type=str, default=None)
    parser.add_argument("--threshold", dest='threshold', help="threshold value to match pixels to brain images", type=float, default=0.9)
    parser.add_argument('--update', dest='update', help="regenerate png database", default=False, action='store_true')
    parser.add_argument("--background-color", dest='bgcolor', help="background color", type=str, default="black")
    parser.add_argument("--color-lookup", dest='lookup', help="color lookup (white, black, greyblack, greywhite)", type=str, default="white")
    parser.add_argument("--output-folder", dest='output', help="output folder for html file", type=str, default=None)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)
    
    # Regenerate database of png images
    if args.update == True:
        if args.db is not None:
            get_data(args.folder)
        else:
            print "Please specify location for png images for database with --db argument"
    else:        
        if args.image == None:
            print "Please specify input jpg image with --input argument."

        # Check background color
        if args.lookup not in ["black","white","greyblack","greywhite"]:
            print "Unrecognized lookup table! Setting to white."
            args.lookup = "white"
            
        generate(template=args.image,
                 output_folder=args.output,
                 color_lookup=args.lookup,
                 bgcolor=args.bgcolor,
                 threshold=args.threshold)
