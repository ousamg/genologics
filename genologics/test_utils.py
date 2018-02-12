#!/usr/bin/env python

from xml.etree import ElementTree


"""
In order to use the patched get : 
1 - import this module and set XML_DICT to your own XML dict. 
    The expected format is { "$entity_uri_1" : "$entity_xml_1",
                             "$entity_uri_2" : "$entity_xml_2",
                              ...}
2 - Set up a test case and use the Mock's library path function to patch "genologics.lims.Lims.get" with this module's "patched get"
    This will replace http calls to your lims by the XML you prepared. You can find an example of this in tests/test_example.py.

"""



XML_DICT = {}


def patched_get(*args, **kwargs):
    if 'uri' in kwargs:
        uri=kwargs['uri']
    else:
        for arg in args:
            if isinstance(arg, str) or isinstance(arg, unicode):
                uri = arg
    if not XML_DICT:
        raise Exception("You need to update genologics.test_utils.XML_DICT before using this function")
    if "?" in uri:
        uri = uri[:uri.index("?")]
    try:
        return ElementTree.fromstring(XML_DICT[uri])
    except KeyError:
        raise Exception("Cannot find mocked xml for uri {0}".format(uri))
