#Importing all the modules necessary, including Biopython
from Bio import GenBank 
from reportlab.lib import colors 
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

#Reads the input file
genome = SeqIO.read("Genome.gb", "genbank")

#Demarks features to be added in the map
diagram = GenomeDiagram.Diagram("Tomato Curly Stunt Virus")
track = diagram.new_track(1, name="Annotated Features")
featurez = track.new_set()

#Looks at entire genome
for feature in genome.features:
	#Skips if not a gene
	if feature.type != "gene":
		continue
	#Gives the map colors!!!
	if len(featurez) % 2 == 0:
		color = colors.orange
	else:
		color = colors.green
	featurez.add_feature(feature, color=color, label = True)

#Actually draws and outputs the map
diagram.draw(format="circular", circular=True, start=0, end=len(genome), circle_core=0.7)
diagram.write("Genome_map_circular.png", "PNG")