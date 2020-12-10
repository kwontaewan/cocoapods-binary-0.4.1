import os
import sys

def wrapper(content):
    return """
platform :ios, '9.0'
use_frameworks!
plugin "cocoapods-binary"

target 'Binary' do
%s
end
    """ % content

def save_to_podfile(text):
    path = os.path.dirname(os.path.abspath(__file__))
    path += "/Podfile"
    file = open(path, "w+")
    file.write(text[0])
    file.close()

    path = os.path.dirname(os.path.abspath(__file__))
    path += "/Binary/import.swift"
    file = open(path, "w+")
    file.write(text[1])
    file.close()



def initial():
    return (wrapper(
"""
keep_source_code_for_prebuilt_frameworks!

pod "Masonry"
"""), 
"""
import Masonry
""")

def addSwiftPod():
    return (wrapper(
"""
keep_source_code_for_prebuilt_frameworks!

pod "RxCocoa", :binary => true
pod "Literal", :binary => true
"""), 
"""
import RxCocoa
import Literal
""")

def revertToSourceCode():
    return (wrapper(
"""
keep_source_code_for_prebuilt_frameworks!

pod "RxCocoa", :binary => true
pod "Literal"
"""), 
"""
import RxCocoa
import Literal
""") 

def addDifferentNamePod():
    return (wrapper(
"""
enable_bitcode_for_prebuilt_frameworks!

pod "Masonry", :binary => true
pod "Literal", :binary => true
pod "lottie-ios", :binary => true
"""), 
"""
import Masonry
import Literal
import Lottie
""") 


def addSubPod():
    return (wrapper(
"""
pod "Masonry", :binary => true
pod "Literal", :binary => true
pod "lottie-ios", :binary => true
pod "AFNetworking/Reachability", :binary => true
""") , 
"""
import Masonry
import Literal
import Lottie
import AFNetworking
""") 

def addVendoredLibPod():
    return (wrapper(
"""
pod "Literal", :binary => true
pod "AFNetworking/Reachability", :binary => true
pod "Instabug", :binary => true
pod "GrowingIO", :binary => true
""") , 
"""
import Literal
import AFNetworking
import Instabug
""") 

def deleteAPod():
    return (wrapper(
"""
pod "Literal", :binary => true
pod "AFNetworking/Reachability", :binary => true
""") , 
"""
import Literal
import AFNetworking
""") 

def universalFlag():
    return (wrapper(
"""
all_binary!

pod "Literal"
pod "AFNetworking/Reachability"
""") , 
"""
import Literal
import AFNetworking
""") 
    



if __name__ == "__main__":
    arg = sys.argv[1]
    print("===================\nchange Podfile to: " + arg + "\n")
    save_to_podfile(globals()[arg]())