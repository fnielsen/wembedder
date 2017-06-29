"""Interface to Gensim models."""


from gensim.models import Word2Vec


# TODO: Make canonical data directory
MODEL_FILENAME = (
    '/home/faan/data/wikidata/'
    'wikidata-20170613-truthy-BETA-size=100-window=1-min_count=20'
)


class Model(Word2Vec):

    @classmethod
    def load(cls, filename=MODEL_FILENAME):
        model = super(Model, cls).load(filename)
        model.metadata = {
            'filename': filename
        }
        return model
