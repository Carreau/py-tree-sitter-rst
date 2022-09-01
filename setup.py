import pathlib
import re
import setuptools


from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
from setuptools.command.build_ext import build_ext
from setuptools import Extension, setup




class BdistWheel(_bdist_wheel):
    def finalize_options(self):
        _bdist_wheel.finalize_options(self)
        self.root_is_pure = False


class BuildExtCommand(build_ext):
    """Ensure built extensions are added to the correct path in the wheel."""

    #def run(self):
    #    breakpoint()
    #    super().run()
        #self.build_extension()
        #pass

    #def _get_inplace_equivalent(self, build_py, ext):
        #    print('INPLACE', build_py, ext)
    #    super()._get_inplace_equivalent(build_py, ext)


    #def copy_extensions_to_source(self):
    #    #breakpoint()
    #    super().copy_extensions_to_source()

    def build_extension(self, ext):
        """I think link ext object to ext_path that is given by

        self.get_ext_fullpath(ext.name)

        Which itself rely on

        build_py = self.get_finalized_command('build_py')
        package_dir = os.path.abspath(build_py.get_package_dir(package))
        build_py = self.get_finalized_command('build_py')
        package_dir = os.path.abspath(build_py.get_package_dir(package))
        """
        from tree_sitter import Language, Parser
        from pathlib import Path
        #breakpoint()
        fp  = self.get_ext_fullpath(ext.name)
        print('Put it in ', fp)
        #build_py = self.get_finalized_command('build_py')
        #package_dir = os.path.abspath(build_py.get_package_dir(package))
        Language.build_library(
            # Store the library in the `build` directory
            fp,
            # Include one or more languages
            [
                "tree-sitter-rst",
            ],
        )
        pass


setuptools.setup(
    name="tree_sitter_rst",
    ext_modules=[
        Extension(
            name="tree_sitter_rst.rst",  # as it would be imported
                               # may include packages/namespaces separated by `.`

            sources=["rst.source"], # all sources are compiled into a single binary file
        ),
    ],
    version="0.0.1",
    description="Binary Python wheels for tree_sitter_rst parser.",
    long_description="",
    author="Matthias Bussonnier",
    author_email="bussonniermatthias@gmail.com",
    zip_safe=False,
    url="",
    license="BSD",
    packages=["tree_sitter_rst"],
    package_data={"tree_sitter_rst": ["rst.so"]},
    install_requires=["tree-sitter"],
    cmdclass={
        "bdist_wheel": BdistWheel,
        "build_ext": BuildExtCommand,
    },
)
