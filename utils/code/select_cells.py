#! /usr/bin/env python

import numpy as np
import argparse
import tables
from pathlib import Path
import matplotlib.pyplot as plt
import ipdb


def main():
    cwd = Path.cwd()

    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    fn = args.filename
    h5file = tables.open_file(fn, mode='r')

    cells = h5file.root.cells.read()

    hqr = getattr(h5file.root.experiments.primary.cell_anno, 'align_high_quality_read').read()
    accuracy = getattr(h5file.root.experiments.primary.cell_anno, 'align_percent_identical').read()
    accuracy = np.nan_to_num(accuracy)
    length = getattr(h5file.root.experiments.primary.cell_anno, 'align_procession_length').read()

#    ipdb.set_trace()

    cond1 = hqr == 1
    cond2 = accuracy > 60
    cond3 = length > 1000
    cond = cond1 & cond2 & cond3

    sel_cells = cells[cond]

    data = np.array([sel_cells, ['0'] * sel_cells.shape[0]])
    np.savetxt('hqr_cells.csv', data.T, fmt='%s', delimiter=',')
    h5file.close()

    print(sum(cond), 'cells are selected.')


if __name__ == '__main__':
    main()
