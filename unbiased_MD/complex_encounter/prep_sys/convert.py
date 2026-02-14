import parmed as pmd
parm = pmd.load_file("leap.top", "leap.rst")
parm.save("topol.top") # .top saves to GROMACS topology file format
parm.save("input.gro")
