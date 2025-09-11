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
        model - description of PC, typically model - EX: "Mac Pro (Late 2013)",
        processor - description of PC's processor - EX: "3.5 GHc 6-Core Intel Xeon E5"
        hd_capacity - number of gigabites of memory in hard drive - EX: 1024
        mem - number of gigabites of RAM - EX: 64
        os - operating system - EX: "macOS Big Sur"
        year - the year the computer was made - EX: 2013
        cost - the price in dollars of the computer - EX: 1500
        """
        # save all the input statistics about the computer
        self.description:str = des
        self.processor_type:str = processor
        self.hard_drive_capacity:str = hd_capacity
        self.memory:int = mem
        self.operating_system:str = os
        self.year_made:int = year
        self.price:int = cost

    # What methods will you need?