from random import randint


def randomUserAgent():
    with open('Agents/solo.txt', encoding='utf-8') as f:
        alls = f.readlines()
        
    user_agent = alls[randint(0, 1107)].strip()
    
    return user_agent