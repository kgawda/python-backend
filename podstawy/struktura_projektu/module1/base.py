print("zaimportowano module1/base.py")
import a
import module1.extras  # Absolute Import

licznik = a.licznik + module1.extras.extra_licznik
