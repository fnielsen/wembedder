"""Interface to Gensim models."""


from os import listdir
from os.path import expanduser, isdir, join, split

from gensim.models import Word2Vec


MODELS_DIRECTORY = join(expanduser('~'), 'wembedder_data', 'models')


class Model(Word2Vec):

    @classmethod
    def load(cls, models_directory=MODELS_DIRECTORY):
        subdirectories = [
            join(models_directory, subdirectory)
            for subdirectory in listdir(models_directory)
            if isdir(join(models_directory, subdirectory))
        ]
        if len(subdirectories) == 0:
            model = Model()
            model.metadata = {
                'error': 'No models available'
            }
            return model

        subdirectory = subdirectories[0]
        filename = split(subdirectory)[-1]
        
        try: 
            model = super(Model, cls).load(join(subdirectory, filename))
            model.metadata = {
                'filename': filename
            }
        except FileNotFoundError:
            model = Model()
            model.metadata = {
                'error': 'File not found: {}'.format(filename)
            }
        return model
