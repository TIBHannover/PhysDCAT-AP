"""PhysDCAT-AP.

Development of PhysDCAT-AP - A metadata schema for physics derived from DCAT-AP+.
"""

try:
    from physdcat_ap._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
