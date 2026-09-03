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

"""Tests for QuickstartPluginIngestor.

This file is intentionally empty. The firecube scaffold cannot guess what your
plugin does, so it does not generate placeholder tests that might give false
confidence in coverage. ``pytest`` will collect zero tests from this file
until you add them.

Test ideas to consider once your hooks are implemented:

  1. Registration check: import firecube_quickstart_plugin, then assert QuickstartPluginIngestor is
     present in firecube's AVAILABLE_INGESTORS registry (proves the
     @register_ingestor decorator fired correctly).
  2. PRODUCT_NAME assertion: verify QuickstartPluginIngestor.PRODUCT_NAME equals
     "quickstart_plugin".
  3. Hook contract: instantiate QuickstartPluginIngestor, invoke your hook(s) with a
     known input fixture, assert the returned shape / dtype / row count
     matches expectations.
  4. Edge cases specific to your input format: empty input, partial input,
     malformed input.

See docs/concepts/plugins/create-a-plugin.md for full testing guidance.
"""
