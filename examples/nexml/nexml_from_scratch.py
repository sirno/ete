import sys
# Note that we import the nexml module rather than the root Nexml
#  class.  This module contains a python object for each of the
#  nexml elements declared in its XML schema.
from ete_dev import nexml

# Create an empty Nexml project 
nexml_project = nexml.Nexml()
tree_collection = nexml.Trees()

# NexMLTree is a special PhyloTree instance that is prepared to be
# added to NeXML projects. So lets populate a random tree
nexml_tree = nexml.NexMLTree()
# Random tree with 10 leaves
nexml_tree.populate(10, random_dist=True) 
# We add the tree to the collection 
tree_collection.add_tree(nexml_tree)

# Create another tree from a newick string
nexml_tree2 = nexml.NexMLTree("((hello, nexml):1.51, project):0.6;")
tree_collection.add_tree(nexml_tree2)

# Add the collection of trees to the NexML project object
nexml_project.add_trees(tree_collection)

# Now we can export the project containing our two trees 
nexml_project.export()
