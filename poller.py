class Participant:
    def __init__(self, name, polled, correct, attempted, excused):
        self.name = name
        self.polled = polled
        self.correct = correct
        self.attempted = attempted
        self.excused = excused

    def __str__(self):
        return self.name + "," + str(self.polled) + "," + str(self.correct) + "," + str(self.attempted) + "," + str(self.excused)

import random
class Poller:
    def __init__(self, file_name):
        self.file_name = file_name
        self.num_people_polled = 0

    def __enter__(self):
        self.file = open(self.file_name, "r+")

        for person in self.file:
            person_size = person.split(",")

            if(len(person_size) < 5 or len(person_size) > 5):
                raise ValueError
            elif(not self.has_correct_attributes(person_size)):
                raise ValueError

        self.file.seek(0)
        return self

    def has_correct_attributes(self, attributes):
        correct_attributes = True
        passed = True
        for i in range(len(attributes) - 1):
            if(len(attributes[i + 1]) > 1):
                tot = 0
                j = 0
      
                for char in attributes[i + 1]:
                    tot += ord(char)
                    j+=1

                if(tot > j * 57):
                    passed = False
        
            elif(ord(attributes[i + 1]) < 48 or ord(attributes[i + 1]) > 57):
                correct_attributes = False
    
        return (correct_attributes and passed)

    def total(self):
        return self.num_people_polled

    def __iter__(self):
        self.participants = self.create_participants()
        return self

    def __next__(self):
        rand_participant = random.randint(0, len(self.participants) - 1)
        self.current_participant = self.participants[rand_participant]
        self.num_people_polled += 1
        return self.current_participant

    def stop(self):
        raise StopIteration

    def create_participants(self):
        participants = []

        for person in self.file:
            poll_data = person.split(',')
            name = poll_data[0]
            polled = poll_data[1]
            correct = poll_data[2]
            attempted = poll_data[3]
            excused = poll_data[4]
            participants.append(Participant(name, int(polled), int(correct), int(attempted), int(excused)))
        self.file.close()
        return participants

    def correct(self):
        self.current_participant.correct += 1
        self.current_participant.polled += 1
        
    def attempted(self):
        self.current_participant.attempted += 1
        self.current_participant.polled += 1

    def excused(self):
        self.current_participant.excused += 1
        self.current_participant.polled += 1

    def missing(self):
        self.current_participant.polled += 1
        
    def __exit__(self, type, value, traceback):
        self.file = open(self.file_name, "w")
        for participant in self.participants:
            self.file.write(str(participant) + "\n")
        self.file.close()
        
       