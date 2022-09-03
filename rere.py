#! /usr/bin/env python3
import argparse
import re
import os


def get_choice(pmt):
    rt = False
    x = input(pmt).strip()
    while x not in ["y","n",""]:
        x = input("please input y or n ")
    if x in ['y',''] :
        rt = True
    return rt

parser = argparse.ArgumentParser()
parser.add_argument("src")
parser.add_argument("dest")
parser.add_argument("-f", "--force", help="never prompt before rename",
                    action="store_true")
parser.add_argument("-r", "--recursive", help="rename files in subdirs",
                    action="store_true")
args = parser.parse_args()

basedir = os.getcwd()

files = []

for parent, dirnames, filenames in os.walk(basedir):
    
    files_path = [os.path.join(parent,file).replace(basedir + '\\',"") for file in filenames]
    files.extend(files_path)
    if not args.recursive:
        break


for file in files:
    if not re.fullmatch(args.src,file):
        continue

    file_rename = re.sub(args.src,args.dest,file)
    

    if not args.force and  not get_choice(f'Rename "{file}" to "{file_rename}"? (y/n) '):
        continue

    
    if os.path.exists(file_rename):
        if not args.force and not get_choice(f"\"{file_rename}\" already exist! replace it? (y/n)"):
            continue
        else:
            os.remove(file_rename)

    try:
        os.rename(file,file_rename)
    except Exception as e:
        print("[Error]",e)
