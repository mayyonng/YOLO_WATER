import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets = ['train', 'test', 'val']
wd = getcwd()
print(wd)
# for image_set in sets:
#     if not os.path.exists('D:/rovision_project/datasets/sandRiver/labels/'):
#         os.makedirs('D:/rovision_project/datasets/sandRiver/labels/')
#
#     image_ids = open('D:/rovision_project/datasets/sandRiver/labels/%s.txt' % (image_set)).read().strip().split()
#     list_file = open('D:/rovision_project/datasets/sandRiver/%s.txt' % (image_set), 'w')
#
#     for image_id in image_ids:
#
#         list_file.write('D:/rovision_project/datasets/sandRiver/JPEGImages/%s.jpg\n' % (image_id))
#     list_file.close()

# for i in range(1,501):
#     file = open('D:/rovision_project/datasets/sandRiver/labels/%s.txt' % (i)).read().strip().split()
#     for line in file:
#         if line == "belt":
#             line="0"
#         elif line == "bottle":
#             line="1"
#         elif line == "branch":
#             line = "2"
#         elif line == "duck":
#             line = "3"
#         elif line == "fish":
#             line = "4"
#         elif line == "garbage":
#             line = "5"
#         elif line == "leaf":
#             line = "6"
#         elif line == "pocket":
#             line = "7"
#         elif line == "seaweed":
#             line = "8"
#         elif line == "ship":
#             line = "9"
#         elif line == "sign":
#             line = "10"

for i in range(1, 501):
    new_file = ""
    with open(("D:/rovision_project/datasets/sandRiver/labels/%s.txt" % i), "r", encoding="utf-8") as file:
        print(file)
        for line in file:
            for word in line.strip().split():
                if word == "pocket":
                    word = "0"
                elif word == "bottle":
                    word = "1"
                elif word == "leaf":
                    word = "2"
                elif word == "plant":
                    word = "3"
                elif word == "branch":
                    word = "4"
                elif word == "sign":
                    word = "5"
                elif word == "ship":
                    word = "6"
                elif word == "pole":
                    word = "7"
                elif word == "belt":
                    word = "8"
                elif word == "fish":
                    word = "9"
                elif word == "duck":
                    word = "10"
                new_file += (word + " ")
            new_file = new_file.rstrip()
            new_file += "\n"
        print(new_file)
    with open(("D:/rovision_project/datasets/sandRiver/labels/%s.txt" % i), "w", encoding="utf-8") as file:
        file.write(new_file)

# for i in range(1, 501):
#     new_file = ""
#     with open(("D:/rovision_project/datasets/sandRiver/labels/%s.txt" % i), "r", encoding="utf-8") as file:
#         print(file)
#         for line in file:
#             for word in line.strip().split():
#                 if word == line.strip().split()[0]:
#                     if word == "4":
#                         word = "5"
#                     elif word == "5":
#                         word = "6"
#                     elif word == "6":
#                         word = "7"
#                     elif word == "7":
#                         word = "8"
#                     elif word == "8":
#                         word = "9"
#                     elif word == "9":
#                         word = "10"
#                 new_file += (word + " ")
#             new_file = new_file.rstrip()
#             new_file += "\n"
#         print(new_file)
#     with open(("D:/rovision_project/datasets/sandRiver/labels/%s.txt" % i), "w", encoding="utf-8") as file:
#         file.write(new_file)


# new_file=""
# with open(("D:/rovision_project/datasets/sandRiver/labels/1.txt"), "r", encoding="utf-8") as file:
#         print(file)
#         for line in file:
#             for word in line.strip().split():
#                 if(word==line.strip().split()[0]):
#                     if(word=="5"):
#                         word="4"
#                 new_file += (word + " ")
#             new_file = new_file.rstrip()
#             new_file += "\n"
#         print(new_file)
# with open(("D:/rovision_project/datasets/sandRiver/labels/1.txt"), "w", encoding="utf-8") as file:
#         file.write(new_file)


