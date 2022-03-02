import csv
import re
debug = False
param = []
label = []

def finds(file):
    data  = []
    h     = []
    goal  = ''
    label.clear()
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        i = 0
        for row in csv_reader:
            if(i==0):
                for col in row:
                    label.append(re.sub('[^a-zA-Z -]', '', col))
                    h.append('x')
                h.pop()
            if(i>0):
                data.append(row)
                goal = data[i-1].pop()
            i+=1

        if(debug):
            print('label:')
            for x in label:
                print(x,end=', ')
            print(f'\n\ngoal: {goal}')
            print('\ndata:')
            for x in range(len(data)):
                print(f'{x+1}. {data[x]}')
            print('\nproses')

        for x in range(len(data)):
            print(f'h{x} = {h}')
            for y in range(len(label)-1):
                if(debug):
                    print(f'{h[y]} == {data[x][y]}')
                if((h[y] == data[x][y]) or (h[y]=='x')):
                    h[y] = data[x][y]
                else:
                    h[y] = '?'
            if(debug):
                 print('')
        print(f'h{len(data)} = {h}')
        param.append(h)
        param.append(goal)

def main():
    data=[]
    ans='?'
    print(f'\nyes\n')
    finds('data_yes.csv')
    print('\nno\n')
    finds('data_no.csv')
    for x in range(len(label)):
        if(x<len(label)-1):
            data.append(input(f'{label[x]}: '))
            for y in range(2):
                if((data[x]==param[y*2][x])):
                    if(ans != 'x'):
                        if(ans == param[y*2+1] or ans == '?'):
                            ans = param[y*2+1]
                        else:
                            ans = 'x'
    print(f'{label[len(label)-1]}? {ans}')

if __name__ == '__main__':
   main()
