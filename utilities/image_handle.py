from os import walk
import pygame

def import_folder(path, size):
  path_list = []
  frame_list = []

  for path,folder,files in walk(path):
    for file_name in files:
      full_path = path + file_name
      path_list.append(full_path)
  path_list.sort()

  for path in path_list:
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (size, size))
    frame_list.append(img)
  return frame_list

# Get all frames will take a dictionary and 
def get_all_frames(dict, size = 64):
  new_dict = {}
  for key in dict:
    frame_list = import_folder(dict[key], size)
    new_dict.update({key : frame_list})
  return new_dict

def flip_frames(frame_list):
  new_list = []
  for frame in frame_list:
    flipped_frame = pygame.transform.flip(frame, True , False)
    flipped_frame.set_colorkey((0,0,0))
    new_list.append(flipped_frame)
  return new_list

def populate_image(dict):
  new_dict = {}
  for key in dict:
    img = pygame.image.load(dict[key]).convert_alpha()
    new_dict.update({key: img})
  return new_dict