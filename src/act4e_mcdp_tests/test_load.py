from glob import glob
from os.path import join
from typing import Any, Callable, Iterator
import yaml

from act4e_mcdp import load_repr1


def test_loading_all() -> Iterator[tuple[Callable[[str, dict[str, Any]], None], str, dict[str, Any]]]:
    directory = "assets/test-data/downloaded"
    # find all *yaml file there

    files = glob(join(directory, "*.mcdpr1.yaml"))
    for filename in files:
        if "queries" in filename:
            continue
        with open(filename) as f:
            content = f.read()

        data = yaml.load(content, Loader=yaml.SafeLoader)
        yield check_one, filename, data
        # ob = load_repr1(data)
        # print(ob)
        # logger.info(f'loaded {filename}')


def check_one(filename: str, data: dict[str, Any]) -> None:
    try:
        ob: Any = load_repr1(data)
    except Exception as e:
        raise Exception(f"Error while loading {filename}") from e
    print(ob)
