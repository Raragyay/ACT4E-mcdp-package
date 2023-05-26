from glob import glob
from os.path import join

import yaml

from act4e_mcdp import load_repr1
from . import logger


def test_loading_all() -> None:
    directory = 'assets/test-data/downloaded'
    # find all *yaml file there

    files = glob(join(directory, '*.yaml'))
    for filename in files:
        with open(filename) as f:
            content = f.read()

        data = yaml.load(content, Loader=yaml.SafeLoader)
        yield check_one, filename, data
        # ob = load_repr1(data)
        # print(ob)
        # logger.info(f'loaded {filename}')


def check_one(filename, data: dict) -> None:
    ob = load_repr1(data)
    print(ob)
