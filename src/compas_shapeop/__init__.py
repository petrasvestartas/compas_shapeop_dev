__version__ = "0.1.1"

try:
    from . import _shapeop
except ImportError:
    pass

from .shapeop import Solver
from .meshsolver import MeshSolver

__all__ = ["Solver", "MeshSolver"]