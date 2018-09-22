# import modules
from bs4 import BeautifulSoup as soup # parse HTML text

# init vars
htmlFiles = []
output = ''
i = 0

# array with files to parse
htmlFiles = ['winter2018.html', 'summer2019.html']


# engine
print("Your table is being parsed...")

for htmlFileName in htmlFiles:

    with open(htmlFileName, 'r') as htmlFile:
        pageHtml = htmlFile.read()
        htmlFile.close()


    pageSoup = soup(pageHtml, 'html.parser')
    data = []

    table = pageSoup.find('table')
    table_body = table.find('tbody')

    rows = table_body.findAll('tr')
    for row in rows:
        cols = row.findAll('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values


    data.pop(0) # get rid of the empty first element of the array

    for subject in data:

        id = subject[0]
        subjectName = subject[1]
        lecturer = subject[2]

        output += id + ') ' + subjectName + ', ' + lecturer

        if (data.index(subject) < len(data)-1):
            output += '\n'

    if (htmlFiles.index(htmlFileName) < len(htmlFiles)-1):
        output += '\n\n'

# write output to the text file
with open('output.txt', 'w') as outputFile:
    outputFile.write(output)
    print('Output was sucessfully written to the file "output.txt"!', end='\n\n')
    print("Result:")
    print(output)
