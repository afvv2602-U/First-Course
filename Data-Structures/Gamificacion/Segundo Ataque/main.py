def main():
    listOfNums = fillList()
    print('The sum of all the items in the list is : '+str(numsToWords(sum(listOfNums))))
    print('The sum of all the items in the list plus 9 is : '+str(numsToWords(sum(listOfNums)*9)))
    print('The higher value in the list is: '+str(numsToWords(max(listOfNums))))
    print('The lower value in the list is: '+str(numsToWords(min(listOfNums))))
    print('Amount of items in the list: '+str(numsToWords(len(listOfNums))))

def fillList():
    listOfNums = []
    while True:
        try:
            num = int(input('Insert number with two digits: '))
            if len(str(num)) == 2:
                listOfNums.append(num)
                ch = str(input('Do you want to continue? y/n : '))
                if ch[0].lower() == 'n':
                    break
            else:
                print('Please insert numbers with only 2 digits\n')
        except ValueError:
            print('Please insert numbers.')
    return listOfNums

def numsToWords(num): 
	under_20 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen'] 
	tens = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'] 
	above_100 = {100: 'Hundred',1000:'Thousand', 1000000:'Million', 1000000000:'Billion'} 
	if num < 20: 
		return under_20[num] 
	if num < 100: 
		return tens[(int)(num/10)-2] + ('' if num%10==0 else ' ' + under_20[num%10]) 
	# find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550 
	pivot = max([key for key in above_100.keys() if key <= num]) 
	return numsToWords((int)(num/pivot)) + ' ' + above_100[pivot] + ('' if num%pivot==0 else ' ' + numsToWords(num%pivot)) 

if __name__ == '__main__':
    main()