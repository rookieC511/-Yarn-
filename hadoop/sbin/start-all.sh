#!/usr/bin/env bash

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

HDFS_DATANODE_USER=root
HDFS_DATANODE_SECURE_USER=hdfs
HDFS_NAMENODE_USER=root
HDFS_SECONDARYNAMENODE_USER=root
YARN_RESOURCEMANAGER_USER=root
HADOOP_SECURE_DN_USER=yarn
YARN_NODEMANAGER_USER=root

## @description  catch the ctrl-c
## @audience     private
## @stability    evolving
## @replaceable  no
function hadoop_abort_startall()
{
  exit 1
}

# let's locate libexec...
if [[ -n "${HADOOP_HOME}" ]]; then
  HADOOP_DEFAULT_LIBEXEC_DIR="${HADOOP_HOME}/libexec"
else
  this="${BASH_SOURCE-$0}"
  bin=$(cd -P -- "$(dirname -- "${this}")" >/dev/null && pwd -P)
  HADOOP_DEFAULT_LIBEXEC_DIR="${bin}/../libexec"
fi

HADOOP_LIBEXEC_DIR="${HADOOP_LIBEXEC_DIR:-$HADOOP_DEFAULT_LIBEXEC_DIR}"
# shellcheck disable=SC2034
HADOOP_NEW_CONFIG=true
if [[ -f "${HADOOP_LIBEXEC_DIR}/hadoop-config.sh" ]]; then
  . "${HADOOP_LIBEXEC_DIR}/hadoop-config.sh"
else
  echo "ERROR: Cannot execute ${HADOOP_LIBEXEC_DIR}/hadoop-config.sh." 2>&1
  exit 1
fi

if ! hadoop_privilege_check; then
  trap hadoop_abort_startall INT
  hadoop_error "WARNING: Attempting to start all Apache Hadoop daemons as ${USER} in 10 seconds."
  hadoop_error "WARNING: This is not a recommended production deployment configuration."
  hadoop_error "WARNING: Use CTRL-C to abort."
  sleep 10
  trap - INT
fi

# start hdfs daemons if hdfs is present
if [[ -f "${HADOOP_HDFS_HOME}/sbin/start-dfs.sh" ]]; then
  "${HADOOP_HDFS_HOME}/sbin/start-dfs.sh" --config "${HADOOP_CONF_DIR}"
fi

# start yarn daemons if yarn is present
if [[ -f "${HADOOP_YARN_HOME}/sbin/start-yarn.sh" ]]; then
  "${HADOOP_YARN_HOME}/sbin/start-yarn.sh" --config "${HADOOP_CONF_DIR}"
fi


