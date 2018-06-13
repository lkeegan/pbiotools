#! /usr/bin/env python3

""" Create a bedGraph (bigWig) file from a riboseq BAM file
to visualise initiating ribosomes (p-site offset shifted).
"""

import os
import pandas as pd

import argparse
import logging
import misc.logging_utils as logging_utils
logger = logging.getLogger(__name__)

import yaml
import json

import misc.utils as utils

import riboutils.ribo_utils as ribo_utils
import riboutils.ribo_filenames as filenames

display_mode = 'full'
colour = '0,150,0'

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="""Create a bedGraph file e.g. to use on a genome browser, to visualise
        the riboseq read counts at each genomic position. Periodic reads are mapped to 
        their 5' ends and shifted according to their p-site offset. This script does NOT
        determine the periodic lengths and offsets, thus the 'periodic-offsets' file
        must be available. Unless specified, a file for every sample in the configuration 
        file will be created.""")

    parser.add_argument('config', help="The (yaml) config file.")
    parser.add_argument('outloc', help="The output directory. Temporary files are also"
                                    "written to this location if converting to BigWig.")

    parser.add_argument('--use-pretty-names', help="If this flag is given, then will use the names"
        "in 'riboseq_sample_name_map' if present.", action='store_true')
    parser.add_argument('--isoform-strategy', help="""See b-tea.cl_utils.
        Currently we only use 'merged'. By default, we use the 'unique' mapped reads,
        and no other option is implemented (e.g. stranded)""", default=None)
    parser.add_argument('--input-list', help="""A space-delimited list of sample names, 
        each quoted separately. They must match the keys in the configuration file. 
        Only these will be converted.""", nargs='*', type=str)
    # TO DO: add option to sum profiles of all samples of one condition, as in Rp-Bp.
    parser.add_argument('--add-chr', help="If this flag is present then 'chr' will be pre-pended"
        "to sequence names. This is done before any other changes to sequence names, so this"
        "must be taken into account if using [--chr-dict]", action='store_true')
    parser.add_argument('--overwrite', help="If this flag is present, then existing files"
        "will be overwritten.", action='store_true')
    # TO DO: implement conversion to bigWig...
    subparser = parser.add_subparsers(help="""Optional arguments if converting to bigWig. 
        The program 'bedGraphToBigWig' must be available on the user's path, and can be"
        "downloaded from 'http://hgdownload.soe.ucsc.edu/admin/exe/'.""", dest='to_bigWig')
    parser_to_bigWig = subparser.add_parser('chrSizes', help="""The 'chrom.sizes' file 
        for the UCSC database.""")
    parser_to_bigWig.add_argument('-d', '--chr-dict', help="""A dictionary mapping of 
        sequence names found in the data to the sequence names, as in 'chrom.sizes'. 
        The format is as follows: '{"key":"value"}'.""", type=json.loads)

    logging_utils.add_logging_options(parser)
    args = parser.parse_args()
    logging_utils.update_logging(args)

    config = yaml.load(open(args.config))
    note = config.get('note', None)
    is_unique = not ('keep_riboseq_multimappers' in config)

    required_keys = [
        'riboseq_data',
        'riboseq_samples',
    ]
    utils.check_keys_exist(config, required_keys)

    if args.input_list:
        sample_names = {name: [name] for name in args.input_list}
    else:
        sample_names = config['riboseq_samples']

    if args.use_pretty_names:
        sample_name_map = ribo_utils.get_sample_name_map(config)
    else:
        sample_name_map = {name: [name] for name in config['riboseq_samples'].keys()}

    # check output path
    if os.path.exists(args.outloc):
        args.outloc = os.path.join(args.outloc, '')
    else:
        msg = "Invalid output path or wrong permission: {}. Quitting.".format(args.outloc)
        raise OSError(msg)

    for name in sorted(sample_names.keys()):

        msg = "Processing sample: {}".format(name)
        logger.info(msg)

        # get riboseq bam file
        bam = filenames.get_riboseq_bam(
            config['riboseq_data'],
            name,
            is_unique=is_unique,
            isoform_strategy=args.isoform_strategy,
            note=note
        )

        # get the lengths and offsets
        lengths, offsets = ribo_utils.get_periodic_lengths_and_offsets(
            config,
            name,
            isoform_strategy=args.isoform_strategy,
            is_unique=is_unique
        )

        if len(lengths) == 0:
            msg = "No periodic read lengths and offsets were found!"
            logger.critical(msg)
            return

        # now we don't modify the ribo scripts, since we assume that riboseq is always fr
        msg = "Finding P-sites"
        logger.info(msg)

        lengths = [int(l) for l in lengths]
        offsets = [int(l) for l in offsets]
        p_sites = ribo_utils.get_p_sites(bam, lengths, offsets)

        # create the profiles
        p_sites = p_sites.groupby(p_sites.columns.tolist()).size().reset_index().rename(columns={0: 'count'})
        p_sites = p_sites[['seqname', 'start', 'end', 'count']]

        if args.add_chr:
            p_sites['seqname'] = 'chr' + p_sites['seqname'].astype(str)

        # write bedGraph to disk
        # currently header is not "customisable", add options later if necessary
        header = """track type=bedGraph name="{}" description="{}" visibility={} color={} 
            autoScale=off alwaysZero=on graphType=bar""".format(sample_name_map[name],
                                                                sample_name_map[name],
                                                                display_mode,
                                                                colour)
        note_str = filenames.get_note_string(note)
        unique_str = filenames.get_unique_string(is_unique)
        iso_str = filenames.get_isoform_strategy_string(args.isoform_strategy)
        fn = ''.join([name, note_str, iso_str, unique_str, '.bedGraph'])
        output = os.path.join(str(args.outloc), fn)
        with open(output, 'w') as f:
            f.write("{}\n".format(header))
        p_sites.to_csv(output, index=False, header=False, columns=['seqname', 'start', 'end', 'count'],
                       sep='\t', mode='a')

        # if converting to bigWig...


if __name__ == '__main__':

    main()
