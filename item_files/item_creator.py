from item_files.item import Item
from utilities.image_handle import populate_image

class Item_creator():
  def __init__(self):
    # Dictionary to keep track of path to assets
    self.item_file_path = {"cheese": "assets/items/cheese.png",
                           "egg": "assets/items/egg.png",
                           "steak":  "assets/items/steak.png"}
    
    self.item_images = populate_image(self.item_file_path)

  def item(self, ID, spawn_point):
    return Item(ID, self.item_images[ID], spawn_point)