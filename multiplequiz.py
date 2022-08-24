import pyInputplus as pyip 
import random , time 
numberofques = 10
correctanswers = 0
for quesnumber in range(numberofques):
    x = random.randint(0,9)
    y = random.randint(0,9)
    prompt = '#%s : %s * %s = '%(quesnumber,x,y)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$'%(x*y)],
                      blockRegexes=[('.*','Incorrect!')],
                      timeout=10,limit=3)
    except pyip.TimeoutException :
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries')
    else :
        print('Correct')
        correctanswers += 1
    time.sleep(1)
print('Score : %s / %s'%(correctanswers,numberofques))