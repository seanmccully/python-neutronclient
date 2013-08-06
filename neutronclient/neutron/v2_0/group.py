# Copyright 2012 OpenStack LLC.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# vim: tabstop=4 shiftwidth=4 softtabstop=4



import argparse
import logging

from neutronclient.common import exceptions
from neutronclient.neutron import v2_0 as neutronV20




class CreateGroup(neutronV20.CreateCommand):
    """Create a group for a given tenant"""

    resource = 'group'
    api = 'group'
    extra_values = False
    log = logging.getLogger(__name__ + '.CreateGroup')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'description', metavar='description',
            help='description of group to create')
        parser.add_argument(
            'name', metavar='name',
            help='name of group to create')


    def args2body(self, parsed_args):

        body = {'group': {
            'name': parsed_args.name,
            'description' : parsed_args.description }}
        if parsed_args.tenant_id:
            body['group'].update({'tenant_id': parsed_args.tenant_id})
        return body



class ListGroup(neutronV20.ListCommand):
    """List networks that belong to a given tenant."""

    # Length of a query filter on subnet id
    # id=<uuid>& (with len(uuid)=36)
    subnet_id_filter_len = 40
    api = 'group'
    resource = 'group'

    log = logging.getLogger(__name__ + '.ListGroup')

    list_columns = ['id', 'name', 'description']
    pagination_support = True
    sorting_support = True


class ShowGroup(neutronV20.ShowCommand):
    """Show information of a given group"""

    resource = 'group'
    log = logging.getLogger(__name__ + '.ShowGroup')


class DeleteGroup(neutronV20.DeleteCommand):
    """Delete a given group."""

    log = logging.getLogger(__name__ + '.DeleteGroup')
    resource = 'group'


class UpdateGroup(neutronV20.UpdateCommand):
    """Update group's information."""

    log = logging.getLogger(__name__ + '.UpdateGroup')
    resource = 'group'

