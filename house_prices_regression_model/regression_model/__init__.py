import logging

from regression_model.config.core import PACKAGE_ROOT, config

logging.getLogger(config.app_config.package_name).addFilter(logging.NullHandler())


with open(PACKAGE_ROOT / "VERSION") as version_file:
    __version__ = version_file.read().strip()
