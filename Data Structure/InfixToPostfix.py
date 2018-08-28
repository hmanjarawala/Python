def tokenGenerator(expression):
    nums=''
    prevOperator=''

    for i in range(len(expression)):
        token = expression[i]
        if token in '+-/*%':
            prevOperator += token
            if nums != '':  yield (nums);   nums = ''
        elif len(token.strip()) == 0:   continue
        elif token in ')]}':
            if nums != '':  yield (nums);   nums = ''
            nums += token
        elif token in '({[':
            if prevOperator != '':   yield (prevOperator); prevOperator=''
            prevOperator += token
        else:
            nums += token
            if prevOperator != '':   yield (prevOperator); prevOperator=''

    if nums != '':  yield (nums);   nums = ''
    if prevOperator != '':   yield (prevOperator); prevOperator=''

 

def infixToPostfix(infixExpression):
    prec = {"**":4,"*":3,"/":3,"//":3,"%":3,"+":2,"-":2,"(":1,"[":1,"{":1}
    lstPostfix = []
    lstOperatorStack = []   

    for token in tokenGenerator(infixExpression):
	
        if token in "+-*/**//%":
            top = len(lstOperatorStack)
            while top != 0 and prec[lstOperatorStack[top-1]] >= prec[token]:
                lstPostfix.append(lstOperatorStack.pop(-1))
                top = len(lstOperatorStack)
            lstOperatorStack.append(token)
        elif token in "([{":
            lstOperatorStack.append(token)
        elif token == ")":
            topToken = lstOperatorStack.pop(-1)
            while topToken != '(':
                lstPostfix.append(topToken)
                topToken = lstOperatorStack.pop(-1)
        elif token == "]":
            topToken = lstOperatorStack.pop(-1)
            while topToken != '[':
                lstPostfix.append(topToken)
                topToken = lstOperatorStack.pop(-1)
        elif token == "}":
            topToken = lstOperatorStack.pop(-1)
            while topToken != '{':
                lstPostfix.append(topToken)
                topToken = lstOperatorStack.pop(-1)
        else:
            lstPostfix.append(token)

    while len(lstOperatorStack) != 0:
        lstPostfix.append(lstOperatorStack.pop(-1))
    return "".join(lstPostfix)

 
if __name__ == '__main__':
	print(infixToPostfix("(A+B*(C/D)**E)//F"))
	print(infixToPostfix("a+b*(c**d)**(f*g+h)-i"))