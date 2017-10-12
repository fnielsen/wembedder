Wembedder
=========

Embedding with Wikidata.

There is a web-service available::

    python app.py
    
When the server is running and the model is loaded the webservice should appear at http://127.0.0.1:5000/    

Note you will need to download model(s) from Zenodo for the webservice to start.

Models
------
Wembedder currently works with specially trained Gensim models. 
Pretrained models are published on Zenodo:

Wembedder wikidata-20170613-truthy-BETA-cbow-size=100-window=1-min_count=20
  Wikidata embedding Gensim CBOW trained on truthy dump with a 100-dimensional subspace, a window of 1 and a minimum count of 20.  https://zenodo.org/record/823195
  
Wembedder wikidata-20170613-truthy-BETA-cbow-size=100-window=1-min_count=20-iter=25
  Wikidata embedding Gensim CBOW trained on truthy dump with a 100-dimensional subspace, a window of 1 and a minimum count of 20. Trained with 25 iterations. https://zenodo.org/record/827339

The models need to be unpacked under `~/wembedder_data/models/`.

Wikimedia Toolforge
-------------------
The canonical webservice runs from Wikimedia Toolforge at https://tools.wmflabs.org/wembedder/

Reference
---------
Finn Årup Nielsen, Wembedder: Wikidata entity embedding web service, `arXiv:1710.04099 <https://arxiv.org/abs/1710.04099>`_, http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/7011/pdf/imm7011.pdf
