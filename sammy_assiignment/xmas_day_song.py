def xmas_day_song():
    day = int(input("Enter the day of xmas: "))
    day_song = ""
    match day:
        case 1:
            day_song = "First Day"
        case 2:
            day_song = "Second Day"
        case 3:
            day_song = "Third Day"
        case 4:
            day_song = "Fourth Day"
        case 5:
            day_song = "Fifth Day"
        case 6:
            day_song = "Sixth Day"
        case 7:
            day_song = "Seventh Day"
        case 8:
            day_song = "Eight Day"
        case 9:
            day_song = "Ninth Day"
        case 10:
            day_song = "Tenth Day"
        case 11:
            day_song = "Eleventh Day"
        case 12:
            day_song = "Twelve Day"
    match day_song:
        case 12:
            print("Twelve drummers drumming \n" +
                  "Eleven pipers piping \n" +
                  "Ten lords a-leaping \n" +
                  "nine ladies dancing \n" +
                  "Eight maids a-milking \n" +
                  "Seven swans a-swimming \n" +
                  "Six geese a-laying \n" +
                  "Five gold rings, \n" +
                  "Four calling birds, \n" +
                  "Three French hens,\n" +
                  "Two turtle doves,\n" +
                  "And a partridge in a pear tree.")
        case 11:
            print("Eleven pipers piping \n" +
                  "Ten lords a-leaping \n" +
                  "nine ladies dancing \n" +
                  "Eight maids a-milking \n" +
                  "Seven swans a-swimming \n" +
                  "Six geese a-laying \n" +
                  "Five gold rings, \n" +
                  "Four calling birds, \n" +
                  "Three French hens,\n" +
                  "Two turtle doves,\n" +
                  "And a partridge in a pear tree.", )
        case 10:
            print("Ten lords a-leaping \n" +
                  "nine ladies dancing \n" +
                  "Eight maids a-milking \n" +
                  "Seven swans a-swimming \n" +
                  "Six geese a-laying \n" +
                  "Five gold rings, \n" +
                  "Four calling birds, \n" +
                  "Three French hens,\n" +
                  "Two turtle doves,\n" +
                  "And a partridge in a pear tree.", )
        case 9:
            print("nine ladies dancing \n" +
                  "Eight maids a-milking \n" +
                  "Seven swans a-swimming \n" +
                  "Six geese a-laying \n" +
                  "Five gold rings, \n" +
                  "Four calling birds, \n" +
                  "Three French hens,\n" +
                  "Two turtle doves,\n" +
                  "And a partridge in a pear tree.", )
        case 8:
            print("Eight maids a-milking \n" +
                  "Seven swans a-swimming \n" +
                  "Six geese a-laying \n" +
                  "Five gold rings, \n" +
                  "Four calling birds, \n" +
                  "Three French hens,\n" +
                  "Two turtle doves,\n" +
                  "And a partridge in a pear tree.", )
        case 7:
            print("Seven swans a-swimming \n" +
                  "Six geese a-laying \n" +
                  "Five gold rings, \n" +
                  "Four calling birds, \n" +
                  "Three French hens,\n" +
                  "Two turtle doves,\n" +
                  "And a partridge in a pear tree.", )
        case 6:
            print("Six geese a-laying \n" +
                  "Five gold rings, \n" +
                  "Four calling birds, \n" +
                  "Three French hens,\n" +
                  "Two turtle doves,\n" +
                  "And a partridge in a pear tree.", )
        case 5:
            print("Five gold rings, \n" +
                  "Four calling birds, \n" +
                  "Three French hens,\n" +
                  "Two turtle doves,\n" +
                  "And a partridge in a pear tree.", )
        case 4:
            print("Four calling birds, \n" +
                  "Three French hens,\n" +
                  "Two turtle doves,\n" +
                  "And a partridge in a pear tree.", )
        case 3:
            print("Three French hens,\n" +
                  "Two turtle doves,\n" +
                  "And a partridge in a pear tree.", )
        case 2:
            print("Two turtle doves,\n" +
                  "And a partridge in a pear tree", )
        case 1:
            print("A partridge in a pear tree", )
