from .Abalone import Abalone


__factory = {
  'abalone':Abalone
}


def create(name, *args, **kwargs):
  if name not in __factory.keys():
    raise NotImplementedError
  return __factory[name](*args, **kwargs)
