"""
Very basic document storage DB using SQLAlchemy - REST client

Example::

    >>> client = DocStoreRestClient('localhost', 5000)
    >>> client.get_doc('test_doc_1').json()
    {'value': 200, '_id': 'test_doc_1', 'last_modified': 1525050671, '_rev': 8}
    >>> client.update_doc('test_doc_1', {'value':12345})
    <Response [200]>
    >>> client.get_doc('test_doc_1').json()
    {'value': 12345, '_id': 'test_doc_1', 'last_modified': 1525050743, '_rev': 9}
    >>> client.get_doc('test_doc_1', rev=2).json()
    {'_id': 'test_doc_1', 'last_modified': 1525048183, 'value': 1, '_rev': 2}

:author: Doug Skrypa
"""

import logging

from requests_client import RequestsClient

__all__ = ['DocStoreRestClient']
log = logging.getLogger(__name__)


class DocStoreRestClient(RequestsClient):
    def get_doc(self, doc_id, rev=None):
        return self.get('doc/{}'.format(doc_id), params={'rev': rev})

    def update_doc(self, doc_id, content):
        return self.post('doc/{}'.format(doc_id), json=content)

    create_doc = update_doc
