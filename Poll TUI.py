import random
print('Welcome to the Voting Poll!\nDeveloped by YUHANTH')
#Question Entering
while True:
    que = input('\nEnter the question for the poll: ')
    if len(que)==0 or que.isspace():
        print('**Field can\'t be empty**\n')
    else:
        print('Question: ',que)
        q_confirmation=input('Please confirm the question (y/n):')
        if q_confirmation.lower()=='y':
            break
def option_entering():
    while True:
        option = input("Enter an option (or 'done' to finish): ")
        if option.lower() == 'done':
            print('\nOptions entered successfully!')
            qno_lis()
            confirmation=input('Please confirm the options (y/n):')
            if confirmation.lower()=='y':
                break
            else:
                edit_options()
                break
        elif len(option)==0 or option.isspace():
            print('**Field can\'t be empty**\n')
        elif option not in options_lis:
            options_lis.append(option)
        else:
            print('**Option already entered**\n')
def edit_options():
    while True:
        edit_ops=['Remove an option','Add options','Exit menu']
        print('\nEdit menu')
        for i in range(len(edit_ops)):
            print(i+1,edit_ops[i])
        while True:
            try:
                eo=int(input('Enter the number corresponding to option: '))
                if eo<=len(edit_ops) and eo>0:
                    break
                else:
                    print('**Invalid option**')
            except:
                print('**Invalid option**')
        if eo==1:
            while True:
                try:
                    qno_lis()
                    rem=int(input('Enter the number corresponding to the option to remove: '))
                    if rem<=len(options_lis) and rem>0:
                        break
                    else:
                        print('\n**Invalid option**')
                except:
                    print('\n**Invalid option**')
            del options_lis[rem-1]
        elif eo==2:
                option_entering()
        elif eo==3:
            pass
        qno_lis()
        confirmation=input('Please confirm the options (y/n):')
        if confirmation.lower()=='y':
            break
def qno_lis():
    print('\nQuestion: ',que,'\n\nOptions:')
    for i in range(len(options_lis)):
        print(i+1,options_lis[i])
options_lis = []
option_entering()
#Voters Registration
input('\nPress enter to continue to Voters Registration')
print('\nVoters registration\n')
voters_lis=[]
voterid_lis=[]
voters_dict={}
while True:
    voter = input("Enter voter\'s name (or 'done' to finish): ")
    if voter.lower() == 'done':
        break
    while True:
        voter_id=random.randrange(1000,10000)
        if voter_id not in voterid_lis:
            voterid_lis.append(voter_id)
            break
    voters_lis.append(voter)
    print(voter,' your voter ID is: ',voter_id,'\nPLEASE REMEMBER\n')
    voters_dict[voter_id]=voter
#Polling
input('\nPress enter to start polling')
vote_dict={}
for i in options_lis:
    vote_dict[i]=0
print("\nVoting has started!\n")
while len(voterid_lis)>0:
    while True:
        try:
            id_ver=int(input('\nEnter voter ID to continue: '))
            break
        except:
            print('**Invalid Voter ID**')
    if id_ver in voterid_lis:
        print('\n',voters_dict[id_ver],'Please vote')
        qno_lis()
        try:
            vote=int(input('Enter the number corresponding to the option to vote: '))
        except:
            print('\n**Invalid vote**')
        if vote<=(len(options_lis)) and vote>0:
            vote_dict[options_lis[vote-1]]+=1
            voterid_lis.remove(id_ver)
            print(voters_dict[id_ver],'(',id_ver,') vote recorded.')
        else:
            print('\n**Invalid vote**')
    elif id_ver in voters_dict:
        print('\n',voters_dict[id_ver],' (',id_ver,') has already voted')
    else:
        print('\n**Invalid voter ID.**')
input('\n\nPolling completed!\tPress enter to continue')
#Results
input('\n\nPress enter to continue to the results')
vote_nos_lis=list(vote_dict.values())
max_vote=max(vote_dict.values())
t=vote_nos_lis.count(max_vote)
input('Press enter to publish the results')
if t>1:                                         #Checking for TIE in results
    winners=[]
    for i in vote_dict:
        if vote_dict[i]==max_vote:
            winners.append(i)
    print('\n\nIt is a tie.\nWinners are:')
    for i in winners:
        print(i)
else:
    for i in vote_dict:
        if vote_dict[i]==max_vote:
            print('\n\nThe winner is ',i)
input('\nPress enter to see the number of votes')
print('\nNumber of votes\n')
for i in vote_dict:
    print(i,' : ',vote_dict[i])
input('\nPress enter to quit')
