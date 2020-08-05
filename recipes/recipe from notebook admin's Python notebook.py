# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
api = dataiku.api_client()
project = api.get_project("FLOWCREATION")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
flow = project.get_flow()
graph = flow.get_graph()

for item in graph.get_items_in_traversal_order(as_type="object"):
    print("Next item in the graph is %s" % item.name)
print("------------")