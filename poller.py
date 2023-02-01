class Participant:
    def __init__(self, name, polled, correct, attempted, excused):
         self.name = name
         self.polled = polled
         self.correct = correct
         self.attempted = attempted
         self.excused = excused

    def toString(Self):
         return self.name + "," + self.polled + "," + self.correct + "," + self.attempted + "," + self.excused

class Poller:
    import random

     def __init__(self, file_name):
         self.file_name = file_name
         self.participant_list = self.createParticipants(self.file_name)
         self.current_participant = None

     def createParticipants(self, file_name):
         file = open(file_name, "r")
         participant_list = []

         for person in file:
             poll_data = person.split(',')
             name = poll_data[0]
             polled = poll_data[1]
             correct = poll_data[2]
             attempted = poll_data[3]
             excused = poll_data[4]
             participant_list.append(Participant(name, int(polled), int(correct), int(attempted), int(excused)))

         file.close()
         return participant_list

     def correct(self):
         self.current_participant.correct += 1
         self.current_participant.polled += 1
        
     def __exit__(self):
         file = open(self.file_name, "w") 

         for participant in self.participant_list:
             file.write(participant.toString() + "\n")
        
         file.close()

     def __iter__(self):
         return self

     def __next__(self):
         
         
        def __enter__(self):
            
        
     def attempted():
         pass