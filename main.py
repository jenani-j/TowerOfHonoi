class Peg:
    """
    It represents a peg in the Tower Of Honoi game.

    Attributes:
        name (int): unique identifier for the peg (1,2,3)
        rep (str): String representation of the peg ("|")
        disks (list): List to store the disk of objects on the peg

        Note that name, rep, disks are instance variables
    """
    def __init__(self,name):
        self.name = name
        self.rep = "|"
        self.disks = []

    def add_disk(self,disk):
        self.disks.append(disk)

    def add_color(self):
        if self.name == 1:
            colr_code = "\033[34m"
            return colr_code
        elif self.name == 2:
            colr_code = "\033[35m"
            return colr_code
        elif self.name == 3:
            colr_code = "\033[36m"
            return colr_code


class Disk:
    """
    It represents a disk in the Tower Of Honoi game.

    Attributes:
        size (int): The size of the disk.
        rep(str): The string representation of the disk.

    Method:
        __init__(size): Initializes a new disk with the given size.
    """
    def __init__(self,size):
        self.size = size
        self.rep = "00" * size

    def add_color(self):
        if self.size == 1:
            colr_code = "\033[31m"
            return colr_code
        elif self.size == 2:
            colr_code = "\033[32m"
            return colr_code
        elif self.size == 3:
            colr_code = "\033[33m"
            return colr_code
        elif self.size == 4:
             colr_code = "\033[34m"
             return colr_code
        elif self.size == 5:
            colr_code = "\033[35m"
            return colr_code
        elif self.size == 6:
            colr_code = "\033[36m"
            return colr_code


class TowerOfHonoi:
    def __init__(self):
        self.pegs = [Peg(1),Peg(2),Peg(3)]
        self.disk_count = 0
        self.create_disks()

    def create_disks(self):
        print("************** GAME RULES **************\n1.We can move one disk at a time into the peg.\n2.We can only place smaller disk on top of larger disk.\n3.Provide the number of disks to play between 3-6.\n")
        self.disk_count = int(input("Enter the number of Disks (3-6):"))
        if self.disk_count == 3 or self.disk_count == 4 or self.disk_count == 5 or self.disk_count == 6:
            for i in range(self.disk_count,0,-1):
                self.pegs[0].add_disk(Disk(i))
        else:
            print()
            print("Please enter the number of disks from (3-6)")
            exit(1)

    def print_pegs(self):
        """for i in range(len(self.pegs[0].disks)-1,-1,-1):
            print(f"{self.pegs[0].disks[i].rep:^15} {self.pegs[1].rep:^15} {self.pegs[2].rep:^15}")
        print()
        print(f"{"Peg-01":^15}{"Peg-02":^15}{"Peg-03":^15}")
        print("----------------------------------------------")"""

        hgt = max(len(peg.disks) for peg in self.pegs)
        for row_num in range(hgt,0,-1):
            for x in self.pegs:
                row_val = x.disks[row_num-1].rep if row_num <= len(x.disks) else x.rep
                print(f"{x.disks[row_num-1].add_color() if row_num <= len(x.disks) else x.add_color()}{row_val:^16}",end ="")
            print()
        print(f"{"\033[32m"}{"Peg-01":^16}{"Peg-02":^16}{"Peg-03":^16}")
        print("----------------------------------------------")
        print("\033[0m")

    def play_game(self):
        play_cnt = 0
        while (len(self.pegs[1].disks) != self.disk_count) and (len(self.pegs[2].disks) != self.disk_count):
            print()
            f_pos = int(input("Enter the Peg No for Disk taken from: "))
            t_pos = int(input("Enter the Peg No for Disk moved to: "))
            if len(self.pegs[t_pos-1].disks) > 0:
                if len(self.pegs[f_pos-1].disks[len(self.pegs[f_pos-1].disks) - 1].rep) > len(self.pegs[t_pos-1].disks[len(self.pegs[t_pos - 1].disks) - 1].rep):
                    print()
                    print("Please place smaller disk on top of larger disk.")
                    continue
            self.pegs[t_pos-1].disks.append(self.pegs[f_pos-1].disks[-1])
            self.pegs[f_pos-1].disks.remove(self.pegs[f_pos-1].disks[-1])
            print()
            self.print_pegs()
            play_cnt = play_cnt + 1
        print()
        print("****************  Game Over  *****************")
        print(f"Optimum Number Of Moves: {pow(2,self.disk_count)-1}")
        print(f"Total Number Of Moves: {play_cnt}")

game = TowerOfHonoi()
print()
game.print_pegs()
game.play_game()



