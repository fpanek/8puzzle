# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#from eight_puzzle import eight_puzzle_gui
#import gui
#from eight_puzzle import gui
import eight_puzzle_gui


def draw_puzzle(self):
    for i in range(3):
        for j in range(3):
            self.b[i].append(self.button())
            self.b[i][j].config(command=lambda row=i, col=j: self.fill(row, col))
            self.b[i][j].grid(row=i, column=j)
def fill(self, i, j):
    self.b[i][j].config(text=self.index, state=tk.DISABLED, bg="black", fg="white")
    self.algo_value[i * 3 + j] = self.index
    self.index += 1
    if self.index == 9:
        self.mark_tile()
        self.val.config(text=str(self.algo_value))

def print_array(array1):
    for x in array1:
        print(x)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    eight_puzzle_gui.build_gui(dim=(500, 500))
    #array1 = [9, 2, 3, 44]
    #print_array(array1)
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
