class BaseConfig(object):
        '''
        Base config class
        '''
        Debug = True
        Testing = False

class ProductionConfig(BaseConfig):
        '''
        Production specific config
        '''
        Debug = False

class DevelopmentConfig(BaseConfig):
        '''
        Development environment specific configuration
        '''
        Debug = True
        Testing = True

