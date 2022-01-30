#!/usr/bin/env python
# coding: utf-8
import argparse, sys, os

import pandas as pd
from pytablewriter import MarkdownTableWriter

from update_pages import resolve_dir

def check_and_create(d):
    """ Turn input into an existing, absolute directory path.
    """
    if not os.path.isdir(d):
        d = resolve_dir(os.path.join(os.getcwd(), d))
        if not os.path.isdir(d):
            os.makedirs(d)
            print(f"Created directory {d}")
    return resolve_dir(d)


def check_dir(d):
    if not os.path.isdir(d):
        d = resolve_dir(os.path.join(os.getcwd(), d))
        if not os.path.isdir(d):
            raise argparse.ArgumentTypeError(d + " needs to be an existing directory")
    return resolve_dir(d)

def concat_metadata(path):
    _, folders, _ = next(os.walk(path))
    tsv_paths, keys = [], []
    for subdir in sorted(folders):
        potential = os.path.join(path, subdir, 'metadata.tsv')
        if os.path.isfile(potential):
            tsv_paths.append(potential)
            keys.append(subdir)
    if len(tsv_paths) == 0:
        return pd.DataFrame()
    dfs = [pd.read_csv(tsv_path, sep='\t', dtype='string') for tsv_path in tsv_paths]
    concatenated = pd.concat(dfs, keys=keys)
    try:
        rel_paths = [os.path.join(corpus, rel_path) for corpus, rel_path in zip(concatenated.index.get_level_values(0), concatenated.rel_paths.values)]
        concatenated.loc[:, 'rel_paths'] = rel_paths
        concatenated = concatenated.reset_index(drop=True)
    except Exception:
        print(f"Could not update rel_paths due to the following error(s):\n{sys.exc_info()[1]}")
        concatenated.index.names = ['corpus', 'i']
        concatenated = concatenated.reset_index(drop=False)
    return concatenated

def df2md(df, name=None):
    """ Turns a DataFrame into a MarkDown table. The returned writer can be converted into a string.
    """
    writer = MarkdownTableWriter()
    writer.table_name = name
    writer.header_list = list(df.columns.values)
    writer.value_matrix = df.values.tolist()
    return writer

def metadata2markdown(concatenated):
    rename4markdown = {
        'fnames': 'file_name',
        'last_mn': 'measures',
        'label_count': 'labels',
        'harmony_version': 'standard',
    }
    result = '# Overview'
    for corpus_path, df in concatenated[rename4markdown.keys()].rename(rename4markdown).groupby(concatenated.rel_paths):
        path, tail = os.path.split(corpus_path)
        heading = path if tail == 'MS3' else corpus_path
        heading = f"\n\n## {heading}\n\n"
        md = str(df2md(df.fillna('')))
        result += heading + md
    return result



def write_md(md_str, md_path):
    if os.path.isfile(md_path):
        msg = 'Updated'
        with open(md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    else:
        msg = 'Created'
        lines = []
    with open(md_path, 'w', encoding='utf-8') as f:
        for line in lines:
            if '# Overview' in line:
                break
            f.write(line)
        else:
            f.write('\n\n')
        f.write(md_str)
    print(f"{msg} {md_path}")

def write_tsv(df, tsv_path):
    if df.shape[0] > 0:
        df.to_csv(tsv_path, sep='\t', index=False)
        print(f"Concatenated metadata written to {tsv_path}.")
    else:
        print(f"No metadata found in the child directories of {directory}.")

def main(args):
    concatenated = concat_metadata(args.dir)
    tsv_path = os.path.join(args.out, 'concatenated_metadata.tsv')
    write_tsv(concatenated, tsv_path)
    md_str = metadata2markdown(concatenated)
    md_path = os.path.join(args.out, 'README.md')
    write_md(md_str, md_path)



################################################################################
#                           COMMANDLINE INTERFACE
################################################################################
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""\
-------------------------------------------------------------------
| Script for generating metadata and README for meta repositories |
-------------------------------------------------------------------

""",
    )
    parser.add_argument(
        "-d",
        "--dir",
        metavar="DIR",
        type=check_dir,
        help="Pass the root of the repository clone to gather metadata.tsv files from its child directories.",
    )
    parser.add_argument(
        "-o",
        "--out",
        metavar="OUT_DIR",
        type=check_and_create,
        help="""Output directory for TSV and MD file.""",
    )
    args = parser.parse_args()
    if args.dir is None:
        args.dir = os.getcwd()
    if args.out is None:
        args.out = os.getcwd()
    main(args)
