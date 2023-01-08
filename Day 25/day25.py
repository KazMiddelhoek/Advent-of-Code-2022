import math
f = open("Day 25\input.txt","r")
numbers=f.read().splitlines()

decimal_numbers=[]
for number in numbers:
    decimal_number=0
    for i, n in enumerate(reversed(number)):
        if n=="-":
            decimal_number-=5**i*1            
        elif n=="=":
            decimal_number-=5**i*2        
        else:
            decimal_number+=5**i*int(n)
    decimal_numbers.append(decimal_number)

def convert_to_snafu(number):
    snafu_number=""
    curr_digit=round(math.log(abs(number),5))
    while curr_digit>=0:
        if number == 0 or abs(number/(5**curr_digit))<0.5:
            snafu_number+="0"
            curr_digit-=1
            continue

        if number < 0:
            if abs(number/(5**curr_digit))>1.5:
                snafu_number+="="
                number+=2*5**curr_digit
            else:
                snafu_number+="-"
                number+=5**curr_digit

        elif abs(number/(5**curr_digit))>1.5:
            snafu_number+="2"
            number-=2*5**curr_digit
        else:
            snafu_number+="1"
            number-=5**curr_digit
        curr_digit-=1
    return snafu_number
      
number=sum(decimal_numbers)

print(convert_to_snafu(number))
