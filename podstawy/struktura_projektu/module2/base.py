from . import extras  # Explicite Relative Import (możliwy tylko wewnątrz paczki)
from .. import a
import a

licznik = extras.extra_licznik + a.licznik
