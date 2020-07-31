from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class PagesConfig(AppConfig):
    name = 'pages'
    path = os.path.join(settings.MODELS, 'models.p')
 
    with open(path, 'rb') as pickled:
       data = pickle.load(pickled)
    classifier = data['classifier']
    work_encoder = data['work_encoder']
    spec_encoder = data['spec_encoder']
    deg_encoder = data['degree_encoder']
    gen_encoder = data['gender_encoder']