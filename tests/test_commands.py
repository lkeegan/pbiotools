import pytest
import subprocess


@pytest.fixture
def list_commands():
    return [
        "bam-to-wiggle",
        "bedx-to-bedy",
        "bed-to-bigBed",
        "bed12-to-gtf",
        "calculate-bed-overlap",
        "convert-ccds-to-bed",
        "count-aligned-reads",
        "count-reads",
        "create-aligned-read-count-bar-chart",
        "create-mygene-report",
        "create-init-ribo-track",
        "dna-to-aa",
        "download-srr-files",
        "extract-bed-sequences",
        "extract-cds-coordinates",
        "fasta-to-fastq",
        "fastq-pe-dedupe",
        "filter-bam-by-ids",
        "fix-all-bed-files",
        "get-all-utrs",
        "get-read-length-distribution",
        "gtf-to-bed12",
        "join-long-chromosomes",
        "merge-isoforms",
        "parse-meme-names",
        "plot-read-length-distribution",
        "remove-duplicate-bed-entries",
        "remove-duplicate-sequences",
        "remove-multimapping-reads",
        "reorder-fasta",
        "run-bowtie",
        "run-signalp",
        "run-tmhmm",
        "split-bed12-blocks",
        "split-long-chromosomes",
        "subtract-bed",
        "extract-metagene-profiles",
        "estimate-metagene-profile-bayes-factors",
        "select-periodic-offsets",
        "pickle-stan",
    ]


def test_commands_help_arg(list_commands):
    for command in list_commands:
        assert subprocess.run([command, "--help"]).returncode == 0


# def test_pickle_stan_command_help_arg():
#     try:
#         import pystan
#         have_pystan2 = True
#     except:
#         have_pystan2 = False
#     if have_pystan2:
#         assert subprocess.run(["pickle-stan", "--help"]).returncode == 0
#     else:
#         pytest.skip("pystan2 not found")