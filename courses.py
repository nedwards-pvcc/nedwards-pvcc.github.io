# NAME: Nathan Edwards
# Program Purpose: This program uses PYTHON SETS to display PVCC
#   REQUIRED courses & TECHNICAL ELECTIVE courses for:
#   --CSC certificate in Computer & Network Support Technologies:
#       --required courses
#       --plus 3 technical electives
#   --AAS degree in Information Technology:
#       --required courses
#       --plus 4 technical electives

# create sets for CERTIFICATE, Computer & Network Support Technologies
network_req = {'CSC 110', 'ETR 164', 'ITN 101'}

network_elect = {'CSC 201', 'CSC 202', 'CSC 205',
                 'ETR 113', 'ETR 149', 'ETR 203', 'ETR 290',
                 'ITN 106', 'ITN 102', 'ITN 151', 'ITN 170', 'ITN 260', 'ITN 290',
                 'ITP 120', 'ITP 132', 'ITP 200', 'ITP 220', 'ITP 290',
                 'MTH 131', 'MTH 161', 'MTH 162', 'MTH 263'}

#create sets for ASSOCIATE degree, Information Technology degree:
info_req = {'CSC 110', 'ENG 111', 'ENG 112', 'ETR 149', 'ETR 164', 'ITD 110',
            'ITD 132', 'ITE 182', 'ITE 215', 'ITN 101', 'ITN 106', 'ITN 111',
            'ITP 120', 'MTH 131'}

info_elect = {'ITN 170', 'ITN 208', 'ITN 261',
              'ITN 276', 'ITN 277', 'ITP 132', 'ITP 136', 'ITP 150', 'ITP 220'}

dash_line = "---------------------------------------------------------"
output_file = "output.txt"

def main():
    with open(output_file, "w") as f:
        f.write("*********PIEDMONT VIRGINIA COMMUNITY COLLEGE************\n")
        process_network_courses()
        display_network_courses(f)

        process_info_courses(info_req)
        display_info_courses(f, info_req)

        process_courses_in_both(network_req, info_req, f)

def process_network_courses():
    global network_elect, num_net_req, num_net_elect, tot_net, all_net_courses
    temp_set = set() #create a temporary set empty set

    for course in network_elect: #Fixed: using correct variable name
        asterisk_course = "*" + course #insert an asterisk in front of ELECTIVE course name
        temp_set.add(asterisk_course)  #then add the new course name to a temporary set

    network_elect.clear() #remove all courses from set of elective sourses
    network_elect = temp_set.copy() #COPY all the courses from the temporary set back into the elective set

    num_net_req = len(network_req)
    num_net_elect = len(network_elect)
    tot_net = num_net_req + num_net_elect
    all_net_courses = network_req.union(network_elect) #UNION: create a new set with ALL network courses

def display_network_courses(out_file):
    global out
    out = out_file
    out.write("\nCERTIFICATE: Computer & Network Support Technologies\n")
    out.write(dash_line + "\n")
    out.write("Number of required courses   : " + str(num_net_req) + "\n")
    out.write("Number of elective courses   : " + str(num_net_elect) + "\n")
    out.write("Total number of Cert. courses: " + str(tot_net) + "\n")
    out.write(dash_line + "\n")
    out.write("ALL Certificate courses: \n")
    num = 1
    for course in all_net_courses:
        out.write(course + " ")
        num += 1
        if num % 5 == 0:
            out.write("\n")
    out.write("\nNOTES:\n")
    out.write("  *Asterisk indicates ELECTIVE course\n")
    out.write("  Students choose 3 technical elective courses\n")
    out.write(dash_line + "\n")

def process_info_courses(info_courses):
    info_req = set(info_courses)
    print("processing info courses...")

def display_info_courses(info_courses):
    print("printing info courses...")
    for course in info_courses:
        print(course)

def process_courses_in_both(network_req, info_req):
    both_req = network_req.intersection(info_req)
    print(dash_line)
    print("REQUIRED courses in both programs:")
    num = 1
    for course in both_req:
        print(course, end=" ")
        num += 1
        if num % 5 == 0:
            print()
    print(dash_line)
