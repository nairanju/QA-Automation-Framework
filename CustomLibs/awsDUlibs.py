import xml.etree.ElementTree as ET
import os
from configparser import ConfigParser
import pathlib
config = ConfigParser()
config.sections()
Path_= pathlib.Path.cwd().parent

xml_path=str(Path_)+"\Config\DU_config.xml"

"""
this function fetches name attribute of procress tag in DU_config.xml by giving file_path, tag & id as arguments"""
#
# def configData_xml(file_path,tag,id):
#     tree = ET.parse(file_path)
#     root = tree.getroot()
#     dictresult = {}
#     for child in root.findall(f".//{tag}[@id='{id}']"):
#         for child1 in child:
#             dictresult.update({child1.tag:child1.text})
#
#     return dictresult['mgmt_ip'], dictresult['username'], dictresult['password']
#
#     # for child in root.findall(f".//{tag}[@id='{id}']"):
#     #     for child1 in child.findall(".//Process[@name]"):
#     #         print(child1.attrib['name'])
#     # print(dictresult)
#
# configData_xml(xml_path,"gnb_CU","AWS_CU_SETUP3")

def xml_tagValues(file_path,element, attribute, tag, text ):
    """
        This function fetches tag values of  attribute of procress tag in DU_config.xml by giving file_path, element, attribute, tag & text as
        arguments
        :param element for xml file
        :param attribute value
        :param tag value
    """
    tree = ET.parse(file_path)
    root = tree.getroot()
    tagResults = []
    for attribute in root.findall(f".//{element}[@id='{attribute}']"):
        for tagValue in attribute.findall(".//" + tag + f"[@{text}]"):
            tagResults.append(tagValue.attrib[f'{text}'])
    return tagResults


# xml_tagValues(xml_path,"gnb_CU", "AWS_CU_SETUP3", "Process","name")

def xml_DUconfig(file_path, element,attribute,tagvalue):
    """
            This function fetches text of given tag
            in DU_config.xml by giving file_path,
             element , attribute & tag
    """

    tree = ET.parse(file_path)
    root = tree.getroot()
    for element_ in root.findall(f".//{element}[@id='{attribute}']" ):
        for sub_element in element_.findall(f".//{tagvalue}"):
            return sub_element.text

# s=xml_DUconfig(xml_path,"gnb_DU", "AWS_DU_SETUP3", "mgmt_ip")
# print(s)
