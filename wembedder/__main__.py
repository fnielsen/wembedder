"""Handle command-line input.

Usage:
  wembedder most-similar <q>

"""


from __future__ import print_function

from .model import Model

from docopt import docopt


arguments = docopt(__doc__)
q = arguments['<q>']

# Load model
model = Model.load()

# Compute similarities
results = model.most_similar(q)

# Report results
for result in results:
    print(result[0])
