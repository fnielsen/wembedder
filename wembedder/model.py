"""Interface to Gensim models."""


from os import listdir
from os.path import isdir, join, split

from gensim.models import Word2Vec

from .config import get_configuration


class Model(Word2Vec):

    @classmethod
    def load(cls, models_directory=None):
        configuration = get_configuration()
        if models_directory is None:
            models_directory = configuration.get('model', 'models_directory')

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

        default_model = configuration.get('model', 'default_model')
        if not default_model:
            subdirectory = subdirectories[0]
        else:
            subdirectory = join(models_directory, default_model)

        filename = split(subdirectory)[-1]

        try:
            model = super(Model, cls).load(join(subdirectory, filename))
            model.metadata = {
                'filename': filename
            }
        except OSError:
            model = Model()
            model.metadata = {
                'error': 'File not found: {}'.format(filename)
            }
        return model
