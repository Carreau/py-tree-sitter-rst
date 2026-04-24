from setuptools.command.build_ext import build_ext
from setuptools import Extension, setup
from tree_sitter import Language


class BuildExtCommand(build_ext):
    """Ensure built extensions are added to the correct path in the wheel."""

    def build_extension(self, ext):
        fp = self.get_ext_fullpath(ext.name)
        Language.build_library(
            fp,
            ["tree-sitter-rst"],
        )


setup(
    ext_modules=[
        Extension(
            name="tree_sitter_rst.rst",
            sources=["rst.source"],
        ),
    ],
    zip_safe=False,
    package_data={"tree_sitter_rst": ["rst.so"]},
    cmdclass={
        "build_ext": BuildExtCommand,
    },
)
