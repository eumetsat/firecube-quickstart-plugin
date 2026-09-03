# Copyright 2026 EUMETSAT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Prepare source data for this plugin.

Run with the dev environment active:

    uv run python scripts/generate_sample_data.py [output_dir]

``output_dir`` defaults to ``sample_data`` under the
current directory, matching what ``--input-data`` expects.
"""

from __future__ import annotations

import sys
from pathlib import Path

from firecube_quickstart_plugin.sample_data import generate_sample_data


def main() -> None:
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("sample_data")
    paths = generate_sample_data(output_dir)
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
