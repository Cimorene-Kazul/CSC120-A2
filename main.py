#Let's try using the classes we wrote to do the same thing main did previously.

# Import the classes we previously wrote
from computer import Computer
from oo_resale_shop import ResaleShop

def main():
    
    # First, let's make a computer
    computer1:Computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)

    # Make a Resale Store
    first_store:ResaleShop = ResaleShop()

    # Add it to the resale store's inventory (and get its id in the process)
    computer_id = first_store.buy(computer1)

    # Make sure it worked by checking inventory
    first_store.print_inventory()

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    first_store.refirbish(computer_id, new_OS)
    
    # Now, let's sell it!
    first_store.sell(computer_id)
    
    # Make sure it worked by checking inventory
    first_store.print_inventory()

# Calls the main() function when this file is run
if __name__ == "__main__": main()
