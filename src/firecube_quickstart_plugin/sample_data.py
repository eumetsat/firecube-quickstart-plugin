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

"""Sample source data for exercising this plugin without external input."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import xarray as xr

OBSERVATIONS = [
    ("2024-07-01T00:00:00", 19.4, 68.0),
    ("2024-07-01T06:00:00", 22.8, 61.0),
    ("2024-07-01T12:00:00", 27.3, 47.0),
    ("2024-07-01T18:00:00", 24.1, 55.0),
]


def generate_sample_data(output_dir: Path) -> list[Path]:
    """Write four time-indexed NetCDF files matching this plugin's input shape.

    Each file holds one timestamp of ``temperature_c`` and ``humidity_pct``
    on the same 2x3 latitude-longitude grid, so :func:`build_dataset` can
    concatenate them along ``timestamp``.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    paths: list[Path] = []
    for index, (timestamp, temperature, humidity) in enumerate(OBSERVATIONS, start=1):
        dataset = xr.Dataset(
            data_vars={
                "temperature_c": (
                    ("timestamp", "latitude", "longitude"),
                    np.full((1, 2, 3), temperature, dtype="float64"),
                ),
                "humidity_pct": (
                    ("timestamp", "latitude", "longitude"),
                    np.full((1, 2, 3), humidity, dtype="float64"),
                ),
            },
            coords={
                "timestamp": [np.datetime64(timestamp, "ns")],
                "latitude": [50.0, 51.0],
                "longitude": [7.0, 8.0, 9.0],
            },
            attrs={"title": "Sample Data for Quickstart Plugin"},
        )
        path = output_dir / f"sample{index:02d}.nc"
        dataset.to_netcdf(path)
        paths.append(path)

    return paths
