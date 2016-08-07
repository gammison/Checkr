import profile
def makevector(bookfile_path,profile_path,isthem):
    profile = open(profile_path,'w')
    ps = profile.read();
    profile_string_array = ps.split("\n")
    solved = profile.get_x_vector()

    #0 is the name
    # path to the text file
    profile_string_array[1] = profile_string_array[1].insert(profile_string_array[1].length - 1," "+bookfile_path)
    # solved vector
    profile_string_array[2] = profile_string_array[1].insert(profile_string_array[1].length-1,","+solved)
    # is this set a real or fake
    profile_string_array[3] = profile_string_array[1].insert(profile_string_array[1].length - 1,"," +","+isthem)
    ps = profile_string_array[0]+"\n"+profile_string_array[1]+"\n"+profile_string_array[2]+"\n"+profile_string_array[3]
