input_of_user_a = ''
import time,sys,winsound
#print("ANSHUL")
a="+----WELCOME TO THE VotingSoftware 1.0----------+"
b="|----Wrong Password-----------------------------|"
c="+----Enter admin password-----------------------+"
d="+----Correct Password---------------------------+"
e="+-Enter the candidates names separated by comma-+"
f="|----Enter no.of voters-------------------------|"
g="|----Enter 1 To Start Voting mode---------------|"
h="+----Voting has started-------------------------+"
i="+----Enter your Voter I.D-----------------------+"
j="|----The Candidates are:------------------------|"
k="|----Enter 1 for first candidate and so on------|"
l="|Thanks For Voting------------------------------|"
m="+----Your vote has been recorded----------------+"
n="|----You have voted OR you are not in the list--|\n"
n+="|----To Continue voting for others:Press ENTER:|\n"
o="|----The Voting has ended-----------------------|"
p="|----Warning:You have entered numbers below 1---|"
q="|-----------------------------------------------|"
r="|----MADE BY : Anshul Birajdar------------------|"
s="|----Results------------------------------------|"
t="|----SET UP MODE--------------------------------|"
u="|---VotingSoftware 1.0's Voting Has started-----|"
v="+-----------------------------------------------+"
w="|----So Sorry!The Election Cannot Start---------|"
x="|Enter the types of candidate for this election:|\n"
x+="|-(Type of the election)eg.Head Boy,Leader,etc--|"
y="|----Enter the day of election(ex.Day 1,2,etc)--|"
#="|----Press enter to vote------------------------|"




#final_list_answers = []
#final_list_answers_dict = {}
password = 123
done_voting_names =[]
total_votes=0
password=str(password)

#Start the Program



#print(r)
print(a)
print(r)
print(t)
print(c)

#----Data to be sent in dat file----
#types_of_candidates
#next_days_day_of_election
#candidates
#candidates_votes
#voters
#done_voting_names
#password
#total_votes



if password == input():
    print(d)
    print(v)
    print(x)
    print(v)
    types_of_candidates = input()
    '''print(v)
    print(y)
    print(v)'''
    day_of_election = '1'
    #next_days_day_of_election = int(day_of_election)+1
    print(v)
    print(e)
    print(v)
    candidates = (input().split(","))
    candidates_votes=[]
    for every_item in candidates:
        candidates_votes.append(0)

    print(v)
    print(f)
    print(v)

    voters = list(range(0, (int(input()) + 1)))
    print(v)
    print(g)
    print(v)

    start_voting_trigger = input()

    if start_voting_trigger =='1':
        print(h)
        print(u)
        done_voting = '1'
        while done_voting == '1':
            print("|----Press Enter to vote------------------------|")

            input_of_user = input().lower()
            if  input_of_user == '' or input_of_user == 'enter' or input_of_user == 'vote':
                print(v)
                print(j)
                print(v)
                counter_a = 0
                for every_person in candidates:
                    print(counter_a+1,":",candidates[counter_a])
                    counter_a+=1


                print(v)
                print(k)
                print(v)
                try:
                    candidate_selected = int(input())
                    candidate_selected -= 1
                    candidates_votes[candidate_selected] += 1
                except:
                    print("Enter Nos. Only")

                #print(candidates_votes)
                #done_voting_names.append(current_user)
                print(v)

                print(l)
                time.sleep(3)
                print(v)
                total_votes+=1
                winsound.PlaySound("laser.wav",winsound.SND_ALIAS)
                #print("|-Waiting for 5 seconds to prevent double voting")
                #time.sleep(1)

            else:
                print(n)
                input_of_user_a = input().lower()
            if input_of_user_a == '' or input_of_user_a == 'enter':
                done_voting = '1'
                print(m)

                #time.sleep(5)
            else:
                done_voting = 0
                print(m)
        print(v)
        print(s)
        print(v)
        #starts writing to file
        result =[None,0]
        #biggest_votes = ""
        file_write = open("results.txt", 'a')
        file_write.write("\n")
        file_write.write("Total Votes:")
        file_write.write(" ")
        file_write.write(str(total_votes))
        file_write.write(" ")
        file_write.write(" \n Day of election:")
        file_write.write(" ")
        file_write.write(day_of_election)
        file_write.write(" \n Type of Candidate: ")
        file_write.write(types_of_candidates)
        print("Types of Candidates:", types_of_candidates, "\nDay of election:", day_of_election)

        for every_item_of_candidates in range(0,len(candidates)):
            #final_list_answers.append(candidates[every_item_of_candidates],every_item_of_candidates/total_votes*100,"%")
            print(candidates[every_item_of_candidates],":",candidates_votes[every_item_of_candidates],"vote(s)",",",int(candidates_votes[every_item_of_candidates])/total_votes*100,"%")

            file_write.write("\n")
            file_write.write("Name: ")
            file_write.write(str(candidates[every_item_of_candidates]))
            file_write.write(" ")
            file_write.write(":")
            file_write.write(" ")
            file_write.write(str(candidates_votes[every_item_of_candidates]))
            file_write.write(" ")
            file_write.write("vote(s) , ")
            file_write.write(" ")
            file_write.write(str(int(candidates_votes[every_item_of_candidates])/total_votes*100))
            file_write.write(" ")
            file_write.write("%")
            file_write.write(" ")

            '''winner = ["None",0]
        for every_item_of_candidates_in_file in candidates_votes:
            if every_item_of_candidates_in_file > winner[1]:
                winner = [every_item_of_candidates_in_file,candidates_votes[every_item_of_candidates_in_file]]
            elif every_item_of_candidates_in_file == winner[1]:
                winner= [every_item_of_candidates_in_file,candidates_votes[every_item_of_candidates_in_file],candidates[every_item_of_candidates_in_file]]
                '''
            percent_votes =[]
            for every_item in candidates_votes:
                percent_votes.append(int(every_item)/total_votes*100)
            winner = 'No One'
            winner_value = -1
            count = 0
            for every_item in percent_votes:

                if every_item > winner_value:
                    winner_value = every_item
                    winner = candidates[count]
                elif every_item == winner_value:
                    winner +=" and "
                    winner += candidates[count]
                count += 1

        file_write.write("\nWinner is(are): ")
        file_write.write(winner)
        print("Winner is", winner)
        file_write.write("\nALL Votes done for day ")
        file_write.write(day_of_election)
        file_write.write("\n\n\n\n")

        print("total votes = ",total_votes)
        file_write.close()

        print("file closed")
    else:
        print(v)
        print(w)
        print(v)
        print("\n")

else:
    print(v)
    print(b)
    print(v)
    print('\n')
print(v)
print(o)
print(v)










print("Results Saved in results.txt")










#time.sleep(1200)

print("your file is stored in results.txt in this folder")
print("|----This file is closing in -------------------|")
time.sleep(3)
print(3)
time.sleep(3)
print(2)
time.sleep(3)
print(1)
time.sleep(3)
print(0)
sys.exit()




