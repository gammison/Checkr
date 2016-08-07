import CreateVector
def writetoprofile(bookfile_path,profile_path):
    profile = open(profile_path,'a')
    ps = profile.read()
    profile_string_array = ps.split("\n")
    solved = CreateVector.createVector(bookfile_path)

    #0 is the name
    # path to the text file
    profile_string_array[1] = profile_string_array[1].insert(len(profile_string_array[1]) - 1," "+bookfile_path)
    # solved vector
    profile_string_array[2] = profile_string_array[1].insert(len(profile_string_array[2])-1,","+solved)
    # is this set a real or fake
    ps = profile_string_array[0]+"\n"+profile_string_array[1]+"\n"+profile_string_array[2]+"\n"+profile_string_array[3]
