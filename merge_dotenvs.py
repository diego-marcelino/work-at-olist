import argparse
import os
from pathlib import Path
from typing import Sequence

import pytest

# flake8: noqa 103


def merge(output_file_path: str,
          merged_file_paths: Sequence[str],
          append_linesep: bool = True) -> None:
    with open(output_file_path, 'w') as output_file:
        for merged_file_path in merged_file_paths:
            with open(merged_file_path, 'r') as merged_file:
                merged_file_content = merged_file.read()
                output_file.write(merged_file_content)
                if append_linesep:
                    output_file.write(os.linesep)


def main(envs: str):
    root_dir_path = Path(__file__).parent.resolve()
    dotenv_file_path = root_dir_path / '.env'
    dotenvs_dir = root_dir_path / '.envs'
    files = [dotenvs_dir / envs / f for f in os.listdir(dotenvs_dir / envs)]
    merge(dotenv_file_path, files)


@pytest.mark.parametrize('merged_file_count', range(3))
@pytest.mark.parametrize('append_linesep', [True, False])
def test_merge(tmpdir_factory, merged_file_count: int, append_linesep: bool):
    tmp_dir_path = Path(str(tmpdir_factory.getbasetemp()))

    output_file_path = tmp_dir_path / '.env'

    expected_output_file_content = ''
    merged_file_paths = []
    for i in range(merged_file_count):
        merged_file_ord = i + 1

        merged_filename = '.service{}'.format(merged_file_ord)
        merged_file_path = tmp_dir_path / merged_filename

        merged_file_content = merged_filename * merged_file_ord

        with open(merged_file_path, 'w+') as file:
            file.write(merged_file_content)

        expected_output_file_content += merged_file_content
        if append_linesep:
            expected_output_file_content += os.linesep

        merged_file_paths.append(merged_file_path)

    merge(output_file_path, merged_file_paths, append_linesep)

    with open(output_file_path, 'r') as output_file:
        actual_output_file_content = output_file.read()

    assert actual_output_file_content == expected_output_file_content


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('envs', nargs='?', type=str, default='.local')
    args = parser.parse_args()
    main(args.envs)
