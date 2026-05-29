#Search for music based on artist, title, medium or genre
#Read MusicInfo, use .split to convert each line to an array, reference items location in array
def MusicSearch():
    #y = False
    f = open("Music_Info.txt", 'r').readlines()
    #while y == False:
    search = input("Enter an Artist, Title, Medium or Genre: ")
    for row in f:
        x = row.split(',')
        for i in range(6):
            if x[i-1] == search:
                print("We found a record with:\n\nArtist Name: {}\nTitle: {}\nMedium: {}\nGenre: {}\n".format(x[1], x[2], x[3], x[4])) #Make more pretty
                    #x = True
        #if x != True:
            #y = False
MusicSearch()
#Make caps not matter
#Remove \n
#Use .strip to make spaces not matter
