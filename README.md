# firecube-quickstart-plugin

A minimal [firecube](https://github.com/eumetsat/firecube) ingestor plugin used
as a worked example: it reads a set of time-indexed NetCDF files and converts
them into a Zarr product. It ships its own sample-data generator, so it can be
tried end to end without sourcing external data.

## Copyright and License

Copyright © EUMETSAT 2025-2026
The provided code and instructions are licensed under [Apache License, Version 2.0](LICENSE).
Contact EUMETSAT for details on the usage and distribution terms.

## Authors

See [AUTHORS](AUTHORS).

## Development

```bash
uv sync
uv run pytest
```

## Install into firecube

```bash
uv run firecube plugins install --editable .
uv run firecube plugins describe quickstart_plugin
```

`firecube plugins describe` should list `[ENGINE]` options. If you add plugin-specific options via a `PluginConfig` subclass, they will appear under `[PLUGIN]`.

## Prepare source data

This plugin expects time-indexed NetCDF files (see `build_dataset()`). It
ships a helper that writes four example files with that shape, so you don't
need to source real data to try it out:

```bash
uv run python scripts/generate_sample_data.py
```

This writes `sample01.nc` .. `sample04.nc` into `sample_data/` (pass a
different path as an argument to change that). Each file holds one timestamp
of `temperature_c` and `humidity_pct` on the same 2x3 latitude-longitude grid.

## Run the ingestion


```bash
uv run firecube ingest quickstart_plugin \
  --input-data sample_data \
  --target file:///sample_data/quickstart_plugin_out.zarr \
  --product-name quickstart_plugin \
  --storage-type local \
  --storage-driver fsspec \
  --output-format zarr \
  --write-mode staged
```

For S3 targets, swap `--storage-type local` for `--storage-type s3` and use an `s3://bucket/key.zarr` URI.

## SW Bill of Materials (SBoM)


### Dependencies

The following dependencies are not included in the package but are required and will be downloaded at build or runtime:

| dependency | version | license | copyright | home_url | comments |
| --- | --- | --- | --- | --- | --- |
| firecube | >=0.1.0 (installed: 0.1.4.post1) | Apache-2.0 | EUMETSAT | https://github.com/eumetsat/firecube | Host ingestion engine this plugin registers into |
| xarray | (installed: 2026.7.0) | Apache-2.0 | xarray developers | https://github.com/pydata/xarray | |

`firecube` and `xarray` pull in further transitive dependencies (e.g. `numpy`, `dask`, `fsspec`) not enumerated here; see the generated `.reports/dependency-licenses.json` for the full resolved tree.

### Build/Edit/Test dependencies

The following dependencies are only required for building, editing, or testing the software:

| dependency | version | sw type | license | copyright | home_url | comments |
| --- | --- | --- | --- | --- | --- | --- |
| hatchling | (installed: 1.18) | Build tools | MIT | PyPA | https://hatch.pypa.io/latest/ | |
| pytest | (installed: 9.1.1) | Development tools | MIT | pytest developers | https://github.com/pytest-dev/pytest | |
| ruff | (installed: 0.16.4) | Development tools | MIT | Astral Software Inc. | https://github.com/astral-sh/ruff | |
| mypy | (installed: 2.3.1) | Development tools | MIT | mypy developers | https://github.com/python/mypy | |
