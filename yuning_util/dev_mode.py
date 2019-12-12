
class DevMode:

    def __init__(self, pkg, auto_on=True):
        from pathlib import Path
        
        pkgs = {
            'k-seq': '/home/yuning/research/k-seq/src/',
            'skin-mb': '/home/yuning/research/skin_microbiome/src/'
        }
        
        if pkg in pkgs.keys():
            self.pkg_path = pkgs[pkg]
        elif Path(pkg).is_dir():
            self.pkg_path = pkg
        else:
            raise ValueError('Package {} is not built-in or valid path')
        if auto_on:
            self.on()
    
    def on(self, get_log_handler=False):
        """Turn on the dev mode"""
        import sys
        
        # prioritize the dev package location
        if self.pkg_path not in sys.path:
            sys.path.insert(0, self.pkg_path)
        elif sys.path.index(self.pkg_path) !=0:
            sys.path.remove(self.pkg_path)
            sys.path.insert(0, self.pkg_path)

        # redirect logging info to standard output
        import logging
        root = logging.getLogger()
        handler = logging.StreamHandler(sys.stdout)
        root.addHandler(handler)
        if get_log_handler:
            return handler
    
    def off(self):
        if self.pkg_path in sys.path:
            sys.path.remove(self.pkg_path)
