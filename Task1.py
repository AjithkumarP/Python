def QuestionsMarks(str): 
    num_count=ques_count=0
    flag=False
    for char1 in str[::-1]:
        if(char1.isdigit()):
            num_count+=1
        if(char1=='?'):
            ques_count+=1
        if(num_count > 0 and num_count % 2 ==0):
            if(ques_count >=3 and ques_count >0):
                flag= True
                ques_count=num_count=0
            else:
                flag=False
                break
    return flag

    
print(QuestionsMarks(input()))
print(QuestionsMarks("abc8???3abcvd1???3"))

