from typing import Dict, Optional
class ResaleShop:
    inventory:list
    def __init__(self):
        self.inventory:list = []
    
    def buy(self, computer:Computer):
        """
        Takes in a Computer object, which holds all of the data about the computer, adds it to the inventory, returns the assigned item_id.
        """
        self.inventory.append(computer)
        return inventory.index(computer)
    
    def update_price(self, item_id:int, new_price:int):
        """ 
        Takes in an item_id and a new price, updates the price of the associated computer if it is the inventory, prints error message otherwise.
        """
        
    
    def sell(self, item_id:int):
        """
        Takes in an item_id, removes the associated computer if it is the inventory, prints error message otherwise
        """

    def print_inventory(self):
        """
        prints all the items in the inventory (if it isn't empty), prints error otherwise
        """

    def refirbish(self, item_id:int, new_OS:Optional[str] = None):
        """
        refirbishes item number item_id if it exists (prints error otherwise), and changes the OS if specified.
        """
    