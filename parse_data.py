day_num = {
    'Mandag'    : 1,
    'Tirsdag'   : 2,
    'Onsdag'    : 3,
    'Torsdag'   : 4,
    'Fredag'    : 5
}

def main():
    with open('./data.txt','r') as file:
        for line in file.readlines():
            line = line.strip().split('\t')
            line[0] = int(line[0])
            line[1] = ' '.join(line[2:])
            for i in range(2,len(line)):
                first_space = line[i].find(' ')
                day = line[i][:first_space]
                kl = line[i][first_space+1:]
                start = int(kl[:2])
                stop = int(kl[8:10])
                line[i] = tuple([day_num[day],tuple(range(start,stop))])
            print(f'{tuple(line)},')

if __name__ == '__main__':
    main()