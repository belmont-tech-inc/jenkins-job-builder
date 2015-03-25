# Copyright (C) 2013 eNovance SAS <licensing@enovance.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""
The Workflow Project module handles creating Jenkins workflow projects.
You may specify ``workflow`` in the ``project-type`` attribute of
the :ref:`Job` definition.

Requires the Jenkins `Workflow Aggregator Plugin.
<https://github.com/jenkinsci/workflow-plugin>`_

Example::

  job:
    name: test_job
    project-type: workflow
    script: |
      stuff
"""

import xml.etree.ElementTree as XML
import jenkins_jobs.modules.base

class Workflow(jenkins_jobs.modules.base.Base):
    sequence = 0

    def root_xml(self, data):
        xml_parent = XML.Element('flow-definition')
        definition_root = XML.SubElement(xml_parent,
                                         'definition',
                                         {'class': 'org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition',
                                          'plugin': 'workflow-cps'})

        if 'script' in data:
            XML.SubElement(definition_root, 'script').text = data['script']
        else:
            XML.SubElement(definition_root, 'script').text = ''

        return xml_parent
