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

"""Generic Zarr ingestor for quickstart_plugin."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

import xarray as xr

from firecube.ingestor.api import (
    GenericZarrIngestor,
    PluginConfig,
    PluginContext,
    register_ingestor,
)


@dataclass
class QuickstartPluginIngestorConfig(PluginConfig):
    """Plugin configuration.

    To accept ``--option key=value`` flags, add dataclass fields here.
    See docs/concepts/plugins/create-a-plugin.md.
    """

    pass


@register_ingestor("quickstart_plugin")
class QuickstartPluginIngestor(GenericZarrIngestor):
    PRODUCT_NAME: ClassVar[str] = "quickstart_plugin"
    plugin_config_class = QuickstartPluginIngestorConfig

    def build_dataset(
        self,
        group: str,
        items: list[Any],
        ctx: PluginContext,
    ) -> xr.Dataset | None:
        _ = group
        if not items:
            return None

        datasets: list[xr.Dataset] = []
        for item in items:
            path = ctx.materialize(item)
            with xr.open_dataset(path) as source:
                datasets.append(source.load())

        return xr.concat(datasets, dim="timestamp").sortby("timestamp")
