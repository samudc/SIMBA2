import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set input/output paths
outdir  =
pdb     =
trj     =

# load trajectory with topology, stride reduces number of frames
traj = md.load(trj, top=pdb, stride=10)

# center coordinates to remove translation
traj.center_coordinates()

# basic trajectory info
top = traj.topology
first_frame = 0
last_frame = traj.n_frames
n_frames = traj.n_frames

# select atoms belonging to chain A and chain B
atoms_chain_A = traj.topology.select("chainid 0")  # chain A
atoms_chain_B = traj.topology.select("chainid 1")  # chain B

# get residue indices for each chain
res_chain_A = [res.index for res in traj.topology.chain(0).residues]
res_chain_B = [res.index for res in traj.topology.chain(1).residues]

# initialize data struct for contact frequencies and distances
contact_maps = []
contact_distances = []

# loop over residue pairs between chain A and chain B
for i in res_chain_A:
    contact_map = []
    contact_distance = []
    for j in res_chain_B:
        if i == j:
            contacts = 0  # skip self-contact
        else:
            dist = md.compute_contacts(trj, [[i, j]])
            array = np.asarray(dist[0]).astype(float)
            distance = np.average(array)
            contact_distance.append(distance)
            contact = np.where(array < 1.2, 1, 0)
            contacts = np.average(contact)
        contact_map.append(contacts)

    contact_maps.append(contact_map)
    contact_distances.append(contact_distance)

final_map = np.asarray(contact_maps).astype(float)
final_distance = np.asarray(contact_distances).astype(float)

# load precomputed contact map (for plotting only)
contact_map = np.loadtxt(outdir + 'contactmap_m.dat')

# plot heatmap
cmap = 'turbo'
fig = plt.figure(figsize=(12, 2))
ax = fig.add_subplot(111)

im = sns.heatmap(contact_map.T, cmap=cmap, ax=ax)
ax.grid(which='both', alpha=0.5)
cbar = im.collections[0].colorbar
cbar.ax.tick_params(labelsize=22)
# invert y-axis for residue numbering orientation
ax.invert_yaxis()
ax.axvline(x=3, color='white', ls='--')
ax.axvline(x=67, color='white', ls='--')

# save and show 
plt.savefig(outdir + 'contact_map.png', bbox_inches='tight', dpi=300)
plt.show()

