Wembedder
=========

Embedding with Wikidata.

There is a web-service available::

    python app.py

Models
------
Wembedder currently works with specially trained Gensim models. 
Pretrained models are published on Zenodo:

Wembedder wikidata-20170613-truthy-BETA-cbow-size=100-window=1-min_count=20
  Wikidata embedding Gensim CBOW trained on truthy dump with a 100-dimensional subspace, a window of 1 and a minimum count of 20.  https://zenodo.org/record/823195
  
Wembedder wikidata-20170613-truthy-BETA-cbow-size=100-window=1-min_count=20-iter=25
  Wikidata embedding Gensim CBOW trained on truthy dump with a 100-dimensional subspace, a window of 1 and a minimum count of 20. Trained with 25 iterations. https://zenodo.org/record/827339

The models need to be unpacked under `~/wembedder_data/models/`.
