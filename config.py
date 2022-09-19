import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'add-your-random-key-here'
    #S3_BUCKET = os.environ.get('S3_BUCKET')
    S3_KEY = os.environ.get('ASIA6QPPAWVULTPJ4RO4')
    S3_SECRET = os.environ.get('j1wxkmXrDnQCIg/82NmDizRCJl+Pl9MJKmruK0C8')
    awssession=os.environ.get('IQoJb3JpZ2luX2VjEJT//////////wEaCXVzLXdlc3QtMiJHMEUCIQC3qelyuXYT8hBS/rFtx/k24bFCnXE5WTkbLQxLDC7/JgIgEyPMO2gM9Sb0r8TG463iQf241SAgI56UhItsDBcxCW4qjQMIPRADGgw5OTc0NzA1NDkzNTIiDGvYmvejPFt5GD9h5yrqAhEGlXU3msWkBOOEgfYpAGsS7izpfWFesF5McsikHUwdvC/CoVHzV8X2vdx4ATRhKcqH2A5GNnraapm7EPiW1pfF4vsSPuTKbTKS7lHBCP+PDIXdzTM8ciTv5h/3lTJ5HYtYKscnlkeUJzLoSovN++VEjciP9QFDcIBFyA9+mSqYN/GjQaPPyC8PejNeXWdJLva2EVJkCVCx6457MdTOPukszi0u7qn+P3UGNcg18Zk01dCCjkhuR8omJPR2k/nI1zdPI+LpTgfw5IZleuy1tA87STBX0isr/LECVyqs7pDXA27k5vHBOIJuhlqF8F4P09eSaBz2pI9MFHskedp9gROH9EvIyk5llmkAFNaOiuQLHqVuAENbozhQ4T8fDkvzRDBdvSWBQgWYfXhE1tnmS/SYHn2iWIg2spze9kfu9r5lVoyeVPtnOI64lnGNZnI1AGt7wxqPiiLifB+vnTCpxACDbALRxPHptIArMMvUn5kGOqYBTHeMEBm/3CMgIozqx7QnhPbQJoFOyR8msXG/tEh/aJ/Q4WNHKljnkJoDO0SIADaSN52ANEgaKPdZy/lGgo24ZFNxj1T2uOBiuFGb4QM8vyh06oNwuF/DbJHtbHm2IPeSFpV8NNuVudFdv+yqIWquJTIjdAsJ7GE8ZhI9O1XfT9CHNhAr6eDqwd5WQaG2HvB7eyCG3UmdFsDgNJfT43fKq7AP6YxpRQ==')
    #S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
    ALLOWED_EXTENSIONS = set([ 'pdf', 'png', 'jpg', 'jpeg'])
    


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
