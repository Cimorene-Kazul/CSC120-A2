from typing import Dict, Optional
class Computer:
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    def __init__(self, model:str, processor:str, hd_capacity:int, mem:int, os:str, year:int, cost:int):
        """
        Creates a computer with the nessesary attributes as specified.
        model - description of PC, typically model - EX: "Mac Pro (Late 2013)",
        processor - description of PC's processor - EX: "3.5 GHc 6-Core Intel Xeon E5"
        hd_capacity - number of gigabites of memory in hard drive - EX: 1024
        mem - number of gigabites of RAM - EX: 64
        os - operating system - EX: "macOS Big Sur"
        year - the year the computer was made - EX: 2013
        cost - the price in dollars of the computer - EX: 1500
        """
        # save all the input statistics about the computer
        self.description:str = model
        self.processor_type:str = processor
        self.hard_drive_capacity:str = hd_capacity
        self.memory:int = mem
        self.operating_system:str = os
        self.year_made:int = year
        self.price:int = cost
    
    def print_details(self):
        """
        prints all the details in a readable format.
        """
        print(self.description)
        print("processor type: "+self.processor_type)
        print("hard drive capacity: "+str(self.hard_drive_capacity)+" GB memory")
        print("memory capacity: "+str(self.memory)+"GB RAM")
        print("operating system: "+self.operating_system)
        print("year made: "+str(self.year_made))
        print("price: $"+str(self.price))

    def year(self):
        """
        returns the year self was made - other classes are not allowed to directly modify class data
        """
        return self.year_made
    
    def name(self):
        """
        returns the description of self - other classes are not allowed to directly modify class data
        """
        return self.description
    
    def update_price(self, new_price:int):
        """
        changes price to new_price
        """
        self.price = new_price
    
    def update_os(self, new_os:str):
        """
        changes operating system to new_os
        """
        self.operating_system = new_os
    
    def refirbish_name(self):
        """
        adds " - refirbished" at the end of the description, if it is not there already
        """
        if self.description[-11:] != "refirbished":
            self.description += " - refirbished"