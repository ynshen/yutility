"""Develope Mode
"""

import sys


class DevMode:
    """Class to control development environment
    """

    def __init__(self, pkg, auto_on=True):
        from pathlib import Path

        pkgs = {
            'k-seq': ['/home/yuning/research/k-seq/src/',
                      '/Users/yuning/research/k-seq/src/'],
            'skin-mb': '/home/yuning/research/skin_microbiome/src/'
        }
        if pkg in pkgs.keys():
            self.pkg_path = pkgs[pkg]
        elif Path(pkg).is_dir():
            self.pkg_path = pkg
        else:
            raise ValueError('Package {} is not built-in or valid path')
        if not isinstance(self.pkg_path, list):
            self.pkg_path = [self.pkg_path]
        if auto_on:
            self.on()

    def on(self):
        """Turn on the dev mode"""

        # prioritize the dev package location
        for p in self.pkg_path:
            if p not in sys.path:
                sys.path.insert(0, p)
            elif sys.path.index(p) != 0:
                sys.path.remove(p)
                sys.path.insert(0, p)

        # redirect logging info to standard output
        import logging
        root = logging.getLogger()
        if root.handlers != [] and any(
            [handler.name is not None and 'stdout' in handler.name
             for handler in root.handlers]
        ):
            pass
        else:
            handler = logging.StreamHandler(sys.stdout)
            handler.name = 'stdout'
            root.addHandler(handler)
        root.setLevel(logging.INFO)

    def off(self):
        for p in self.pkg_path:
            if p in sys.path:
                sys.path.remove(p)
