'''
################################################
#  Program: Pod_leaders.py                     #
#  Author: Myles Wilkerson                     #
#  Date: 2/17/2021                             #
#  Description: Program to be used by the      #
#               POD Leaders in instructing     #
#               the POD members about Object   #
#               Oriented Programming concepts  #
#  The Hidden Genius Project                   #
#  OAK8 Cohort                                 #
################################################
'''

class Pod_leaders: #indicates that class is being created followed the name (Pod_leaders
 
    # Class Constructor method is called when an Object is instantiated
    def __init__(self, pod_leader): #Init is the constructor and is used when is is being initiated (start-up)
       self.pod_leader = {} #Instance variable because it is defined in the constructor

    # Class method to add a leader to the pod_leader dictionary      
    def add_leader(self, leader_to_add,cell_number): #adding attributes to the add_leader method
        self.pod_leader[leader_to_add] = cell_number
       
    # Class method to print the pod_leader and cell numbers  
    def display_leaders(self): #makes method that will display the pod leaders and their numbers
      print('POD Leaders')      
      for leader, number in self.pod_leader.items(): #for loop prints the leader and then a number for that leader
        print(leader, number) #prints the pod leader and number


pod = Pod_leaders("POD Leaders");
pod.add_leader("Richard","(510) 228-5623")
pod.add_leader("Jacore","(845) 200-6250")
pod.add_leader("Gabriel","(510) 326-5834")
pod.add_leader("Aris","(510) 229-6359 ")
pod.add_leader("Andrew","(925) 727-4611")
pod.display_leaders()
print('\n')


class Pod_members:

    def __init__(self, pod_member):
        self.pod_member = {}

    def add_member(self, member_to_add, cell_number):
            self.pod_member[member_to_add] = cell_number

    def display_members(self):
        print('POD Members')
        for member, number in self.pod_member.items():
            print(member, number)

pod = Pod_members("POD Members");
pod.add_member("Josiah","(111) 111-1111")
pod.add_member("Matthew","(111) 111-1111")
pod.add_member("Myles","(111) 111-1111")
pod.add_member("Kymari","(111) 111-1111")
pod.display_members()
