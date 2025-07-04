# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from airflow.providers.google.cloud.links.base import BaseGoogleLink

BIGTABLE_BASE_LINK = "/bigtable"
BIGTABLE_INSTANCE_LINK = BIGTABLE_BASE_LINK + "/instances/{instance_id}/overview?project={project_id}"
BIGTABLE_CLUSTER_LINK = (
    BIGTABLE_BASE_LINK + "/instances/{instance_id}/clusters/{cluster_id}?project={project_id}"
)
BIGTABLE_TABLES_LINK = BIGTABLE_BASE_LINK + "/instances/{instance_id}/tables?project={project_id}"


class BigtableInstanceLink(BaseGoogleLink):
    """Helper class for constructing Bigtable Instance link."""

    name = "Bigtable Instance"
    key = "instance_key"
    format_str = BIGTABLE_INSTANCE_LINK


class BigtableClusterLink(BaseGoogleLink):
    """Helper class for constructing Bigtable Cluster link."""

    name = "Bigtable Cluster"
    key = "cluster_key"
    format_str = BIGTABLE_CLUSTER_LINK


class BigtableTablesLink(BaseGoogleLink):
    """Helper class for constructing Bigtable Tables link."""

    name = "Bigtable Tables"
    key = "tables_key"
    format_str = BIGTABLE_TABLES_LINK
