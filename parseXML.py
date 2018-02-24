#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax
import sys

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.author = ""


    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "article":
            print("This is article"+attributes["key"])

    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "type":
            self.CurrentData = ""

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "author":
            self.author = content

# class CHandler(xml.sax.handler.ContentHandler):
#     def startElement(self, name, attrs):
#         print ()
#     def characters(self, ch):
#         print ()
#
# class EResolver(xml.sax.handler.EntityResolver):
#     def resolveEntity(self,publicId,systemId):
#         print (" resolveEntity  ",publicId,systemId)
#         sys.exit()
# class DHandler(xml.sax.handler.DTDHandler):
#     def notationDecl(name, publicId, systemId):
#         print (" notationDecl ",publicId,systemId)
#         sys.exit()
#     def unparsedEntityDecl(name, publicId, systemId, ndata):
#         print (" unparsedEntityDecl ",publicId,systemId,ndata)
#         sys.exit()

if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    # parser.setContentHandler(CHandler())
    # parser.setEntityResolver(EResolver())
    # parser.setDTDHandler(DHandler())

    parser.parse("dblp.xml")