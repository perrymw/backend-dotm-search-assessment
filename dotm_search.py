#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Given a directory path, search all files in the path for a given text string
within the 'word/document.xml' section of a MSWord .dotm file.

The DOTM file extension is a Microsoft Word File template developed by Microsoft Corporation in its version of 2007 and 2010 document template files. The Microsoft Word program allows users to share and create various documents with the help of an extensive set of tools and aided by Microsoft’s easy to use interface. Its word processing program includes settings, macros and a default layout for documents. Macros are short programs assigned to do a set of tasks. DOTM file has two attributes namely Zip file compression and XML (Extensive Markup Language). It is identical to .DOCX and .DOCM file in which the M stands for macro and the X stands for XML. The application that can open both .DOCX and .DOCM is via Microsoft Word version 2007 or 2010. Lower versions of Microsoft Word can’t open these files unless users have a handy Word converter which allows them to see the contents of the file that was sent to them.
"""
__author__ = "perrymw ... with help from instructors"

import os
import sys
import zipfile
import argparse
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help = 'directory to search')
    parser.add_argument('text', help = 'text to search')
    return parser
def main():
    """Opens a dotm and scand for a substring"""
    parser = create_parser()
    name_space = parser.parse_args()
    search_text = name_space.text
    search_path = name_space.dir

    print("Searching directory {} for dotm files with text '{}' ...").format(search_path, search_text)

    file_list = os.listdir(search_path)
    match_count = 0
    search_count = 0

    for file in file_list:
        if not file.endswith('.dotm'):
            print("This is not the file you are looking for")
            continue
        else:
            search_count += 1

        full_path = os.path.join(search_path, file)
        if zipfile.is_zipfile(full_path):
            with zipfile.ZipFile(full_path) as z:
                name = z.namelist()
                if 'word/document.xml' in name:
                    with z.open('word/document.xml', 'r') as doc:
                        for line in doc:
                            text_location = line.find(search_text)
                            if text_location > 0:
                                print('Match found in file {}'.format(full_path))
                                print('...' + line[text_location - 40 : text_location + 41] + '...')
                                match_count += 1
    print("Total dotm files search: {}".format(search_count))
    print("total dotm files found: {}".format(match_count))
            

if __name__ == '__main__':
    main()
