from icecream import ic # It shows :the output, the function and its arguments

class TempTracker:
    rec_temp = [] # records temperatures

    def insert(self, insert_temp): # add new temperatures
        if insert_temp in range(0, 110):
            self.rec_temp.append(insert_temp)
        else:
            print("Not in the range")

    def get_max(self):
        return max(self.rec_temp)

    def get_min(self):
        return min(self.rec_temp)

    def get_mean(self):
        return sum(self.rec_temp)/len(self.rec_temp)
#######################################################
# TEST
test = TempTracker()
test.insert(40)
test.insert(1)
test.insert(13)
test.insert(45)
test.insert(56)
test.insert(90)
test.insert(78)
test.insert(87)
test.insert(33)
test.insert(45)
test.insert(5)
test.insert(45)
test.insert(99)
test.insert(11)
print("Maximum value: "+ str(test.get_max()) + " \n Minimum Value: "+ str(test.get_min()) + \
     " \n Average value: "+ str(test.get_mean()))