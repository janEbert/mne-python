"""
===========================
Reading an inverse operator
===========================
"""
# Author: Alexandre Gramfort <gramfort@nmr.mgh.harvard.edu>
#
# License: BSD (3-clause)

print __doc__

import mne
from mne.datasets import sample

data_path = sample.data_path('.')
fname = data_path
fname += 'MNE-sample-data/MEG/sample/sample_audvis-meg-oct-6-meg-inv.fif'

inv = mne.read_inverse_operator(fname)

print "Method: %s" % inv['methods']
print "fMRI prior: %s" % inv['fmri_prior']
print "Number of sources: %s" % inv['nsource']
print "Number of channels: %s" % inv['nchan']

###############################################################################
# Show result

# 3D source space
import numpy as np
lh_points = inv['src'][0]['rr']
lh_faces = inv['src'][0]['use_tris']
rh_points = inv['src'][1]['rr']
rh_faces = inv['src'][1]['use_tris']
from enthought.mayavi import mlab
mlab.triangular_mesh(lh_points[:,0], lh_points[:,1], lh_points[:,2], lh_faces)
mlab.triangular_mesh(rh_points[:,0], rh_points[:,1], rh_points[:,2], rh_faces)
mlab.show()
