from .Abalone import Abalone
from .Chess import Chess
from .Cnae import Cnae

__factory = {
  'abalone':Abalone,
  'chess':Chess,
  'cnae':Cnae,
}


def create(name, *args, **kwargs):
  if name not in __factory.keys():
    raise NotImplementedError
  return __factory[name](*args, **kwargs)
