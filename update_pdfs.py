#!/usr/bin/env python3
import argparse
import os
import shutil
import re


def update_pdf(src, case_id):
    """Copy the source PDF to its new location, based on Case ID."""
    dest = 'casestudies/{}/casestudy/files/global/{}/'.format(
        case_id, case_id)
    print('Copying {} to {}...'.format(src, dest))
    shutil.copy(src, dest)


def update_pdfs(pdf_dir):
    print(pdf_dir)
    root_re = pdf_dir.replace('/', '\/')
    for root, dirs, files in os.walk(pdf_dir):
        m = re.match(root_re + r'\/(?P<case_id>[0-9]+)', root)
        if m is None:
            continue
        else:
            case_id = m.group('case_id')

        path = root.split(os.sep)
        for f in files:
            if f.endswith('.pdf'):
                update_pdf(os.path.join(root, f), case_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--pdf-dir', help='location of the new PDF files')
    args = parser.parse_args()

    update_pdfs(args.pdf_dir)
