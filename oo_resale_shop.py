from typing import Dict, Optional
from computer import Computer

class ResaleShop:
    inventory:list
    def __init__(self):
        self.inventory:list = []

         # Print a little banner
        print("=" * 21)
        print("COMPUTER RESALE STORE")
        print("=" * 21)
    
    def buy(self, computer:Computer):
        """
        Takes in a Computer object, which holds all of the data about the computer, adds it to the inventory, returns the assigned item_id.
        """
        print("Buying", computer.name())
        print("Adding to inventory...")
        self.inventory.append(computer)
        print("Done.\n")
        return self.inventory.index(computer)
    
    def update_price(self, item_id:int, new_price:int):
        """ 
        Takes in an item_id and a new price, updates the price of the associated computer if it is the inventory, prints error message otherwise.
        """
        if self.inventory[item_id] is not None:
            self.inventory[item_id].update_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
  
    def sell(self, item_id:int):
        """
        Takes in an item_id, removes the associated computer if it is the inventory, prints error message otherwise
        """
        print("Selling Item ID:", item_id)
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        """
        prints all the items in the inventory (if it isn't empty), prints error otherwise
        """
        print("Checking inventory...")
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print("-" * 21)
                print(f'Item ID: {self.inventory.index(item)}')
                item.print_details()
            print("-" * 21)
        else:
            print("No inventory to display.")
        print("Done.\n")

    def refirbish(self, item_id:int, new_os:Optional[str] = None):
        """
        refirbishes item number item_id if it exists (prints error otherwise), and changes the OS if specified.
        """
        print("Refurbishing Item ID:", item_id, ", updating OS to", new_os)
        print("Updating inventory...")
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer.update_price(0) # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer.update_price(250) # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer.update_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_price(1000) # recent stuff

        if new_os is not None:
            computer.update_os(new_os) # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
        print("Done.\n")