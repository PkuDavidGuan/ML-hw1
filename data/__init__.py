from .Abalone import Abalone
from .Chess import Chess
from .Cnae import Cnae
from .Dota2 import Dota2
from .Seismic import Seismic
from .Iris import Iris
__factory = {
  'abalone':Abalone,
  'chess':Chess,
  'cnae':Cnae,
  'dota2':Dota2,
  'seismic':Seismic,
  'iris': Iris,
}


def create(name, *args, **kwargs):
  if name not in __factory.keys():
    raise NotImplementedError
  return __factory[name](*args, **kwargs)
