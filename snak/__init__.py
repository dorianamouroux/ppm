from .config import Config

def main():
    conf = Config()
    conf.set('name', 'snak')
    conf.save()
