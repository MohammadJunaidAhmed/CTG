import pandas as pd
import numpy as np
import time

course_data = {}
#FORMAT: "CSE1008":{name:"Problem Solving with Python", slots: ["A1+TA1", "C2+TC2"]}

wishlist = ["CSE4006", "CSE3003", "LIB1001"]
# wishlist = ['CSE4006', 'ENG3003', 'MAT2004', 'LAW1003', 'MAT1002']
# wishlist = ['CSE4006']

# wishlist1 = []
wishlist1 = ["CSE4006", "CSE3003", "LIB1001"]
# wishlist2 = []
wishlist2 = ["CSE4006", "CSE3003", "LIB1001", "LAW1003"]

timetable = {
    "L1": None,
    "L2": None,
    "L3": None,
    "L4": None,
    "L5": None,
    "L6": None,
    "L7": None,
    "L8": None,
    "L9": None,
    "L10": None,
    "L11": None,
    "L12": None,
    "L13": None,
    "L14": None,
    "L15": None,
    "L16": None,
    "L17": None,
    "L18": None,
    "L19": None,
    "L20": None,
    "L21": None,
    "L22": None,
    "L23": None,
    "L24": None,
    "L25": None,
    "L26": None,
    "L27": None,
    "L28": None,
    "L29": None,
    "L30": None,
    "L31": None,
    "L32": None,
    "L33": None,
    "L34": None,
    "L35": None,
    "L36": None,
    "L37": None,
    "L38": None,
    "L39": None,
    "L40": None,
    "L41": None,
    "L42": None,
    "L43": None,
    "L44": None,
    "L45": None,
    "L46": None,
    "L47": None,
    "L48": None,
    "L49": None,
    "L50": None,
    "L51": None,
    "L52": None,
    "L53": None,
    "L54": None,
    "L55": None,
    "L56": None,
    "L57": None,
    "L58": None,
    "L59": None,
    "L60": None
}
theory_slots = {
    "A1": None,
    "A2": None,
    "B1": None,
    "B2": None,
    "C1": None,
    "C2": None,
    "D1": None,
    "D2": None,
    "E1": None,
    "E2": None,
    "F1": None,
    "F2": None,
    "A1+TA1+TAA1":  None,
    "A1+TA1": None,
    "TA1": None,
    "TAA1": None,
    "A2+TA2+TAA2": None,
    "A2+TA2": None,
    "TA2": None,
    "TAA2": None,
    "B1+TB1+TBB1":  None,
    "B1+TB1": None,
    "TB1": None,
    "TBB1": None,
    "B2+TB2+TBB2": None,
    "B2+TB2": None,
    "TB2": None,
    "TBB2": None,
    "C1+TC1+TCC1": None,
    "C1+TC1":None,
    "TC1": None,
    "TCC1": None,
    "C2+TC2+TCC2":None,
    "C2+TC2":None,
    "TC2": None,
    "TCC2": None,
    "D1+TD1+TDD1":  None,
    "D1+TD1": None,
    "TD1": None,
    "TDD1": None,
    "D2+TD2+TDD2": None,
    "D2+TD2": None,
    "TD2": None,
    "TDD2": None,
    "E1+TE1": None,
    "TE1": None,
    "E2+TE2": None,
    "TE2": None,
    "F1+TF1": None,
    "TF1": None,
    "F2+TF2": None,
    "TF2": None,
}
lab_slots = {}

slot_map = {
    "A1": ["L6", "L23", "L24"],
    "A2": ["L32", "L57", "L58"],
    "B1": ["L5", "L21", "L22"],
    "B2": ["L31","L55","L56"],
    "C1": ["L2", "L7", "L17"],
    "C2": ["L26", "L33", "L49"],
    "D1": ["L1", "L12", "L18"],
    "D2": ["L25", "L39", "L50"],
    "E1": ["L9", "L14", "L19"],
    "E2": ["L37", "L44", "L51"],
    "F1": ["L3", "L10", "L13"],
    "F2": ["L27", "L38", "L43"],
    "A1+TA1+TAA1":  ["L6", "L16", "L23", "L24", "L52"],
    "A1+TA1": ["L6", "L16", "L23", "L24"],
    "TA1": ["L16"],
    "TAA1": ["L52"],

    "A2+TA2+TAA2":  ["L20", "L32", "L46", "L57", "L58"],
    "A2+TA2": ["L32", "L46", "L57", "L58"],
    "TA2": ["L46"],
    "TAA2": ["L20"],

    "B1+TB1+TBB1":  ["L5", "L15", "L21", "L22", "L38"],
    "B1+TB1": ["L5", "L15", "L21", "L22"],
    "TB1": ["L15"],
    "TBB1": ["L38"],
    "B2+TB2+TBB2":  ["L10", "L31", "L45", "L55", "L56"],
    "B2+TB2": ["L31", "L45", "L55", "L56"],
    "TB2": ["L45"],
    "TBB2": ["L10"],


    "C1+TC1+TCC1":  ["L2", "L7", "L11", "L17", "L27"],
    "C1+TC1": ["L2", "L7", "L11", "L17"],
    "TC1": ["L11"],
    "TCC1": ["L27"],

    "C2+TC2+TCC2":  ["L3", "L26", "L33", "L40", "L49"],
    "C2+TC2": ["L26", "L33", "L40", "L49"],
    "TC2": ["L40"],
    "TCC2": ["L3"],


    "D1+TD1+TDD1":  ["L1", "L8", "L12", "L18", "L43"],
    "D1+TD1": ["L1", "L8", "L12", "L18"],
    "TD1": ["L8"],
    "TDD1": ["L43"],
    "D2+TD2+TDD2":  ["L13", "L25", "L34", "L39", "L50"],
    "D2+TD2": ["L25", "L34", "L39", "L50"],
    "TD2": ["L34"],
    "TDD2": ["L13"],

    "E1+TE1": ["L4", "L9", "L14", "L19"],
    "TE1": ["L4"],
    "E2+TE2": ["L28", "L37", "L44", "L51"],
    "TE2": ["L28"],

    "F1+TF1": ["L3", "L10", "L13", "L20"],
    "TF1": ["L20"],
    "F2+TF2": ["L27", "L38", "L43", "L52"],
    "TF2": ["L52"],
}

def setWl1(x):
    global wishlist1
    wishlist1 = x
def setWl2(x):
    global wishlist2
    wishlist2 = x

def setWishlist(x):
    global wishlist
    wishlist = x
    return

def canPlace(course, slot):
    for slots in slot_map[slot]:
        if(timetable[slots] != None):
            return False
    return True

def Place(course, slot):
    for slots in slot_map[slot]:
        timetable[slots] = course
    return
    
def removePlaced(course, slot):
    for slots in slot_map[slot]:
        timetable[slots] = None
    theory_slots[slot] = None
    return

def canLabPlace(course, slot):
    x = slot.rsplit('+')
    if(timetable[x[0]] == None and timetable[x[1]] == None):
        return True
    return False

def PlaceLab(course, slot):
    course_temp = course + "(LAB)"
    x = slot.rsplit('+')
    timetable[x[0]] = course_temp
    timetable[x[1]] = course_temp
    return

def removeLabPlaced(course, slot):
    x = slot.rsplit('+')
    timetable[x[0]] = None
    timetable[x[1]] = None
    return


def printTT():
    for i in timetable:
        if(timetable[i] != None):
            print(i, end=": ")
            print(timetable[i])

def printCD():
    for i in course_data:
        print(i, end=": ")
        print(course_data[i])

def getTT():
    ans = {}
    for i in timetable:
        if(timetable[i] != None):
            ans[i] = timetable[i]
    return ans
def getTslots():
    ans = {}
    for i in theory_slots:
        if(theory_slots[i] != None):
            ans[i] = theory_slots[i]
    return ans


def initialize_course_data(): #TIME COMPLEXITY (O(N*(M^N)))
    global course_data #Make it Null! Incase previous generation has left some data!
    course_data = {}
    data = pd.read_csv('DataFolder/data.csv')
    lab_data = pd.read_csv('DataFolder/labs.csv')
    course_codes = data['course_code'].dropna().tolist()
    course_codes = list(set(course_codes))
    lab_codes = list(set(lab_data['course_code'].dropna().tolist()))

    for i in course_codes:
        d = data[data['course_code'] == i]
        course_data[i] = {"name": d.iloc[0]["course_name"], "slots": []}
        slot1_values = list(set(d['slot1'].dropna().tolist()))
        slot2_values = list(set(d['slot2'].dropna().tolist()))
        slot3_values = list(set(d['slot3'].dropna().tolist()))
        slot4_values = list(set(d['slot4'].dropna().tolist()))
        slot5_values = list(set(d['slot5'].dropna().tolist()))
        slot6_values = list(set(d['slot6'].dropna().tolist()))

        slots_temp = slot1_values + slot2_values + slot3_values + slot4_values + slot5_values + slot6_values
        course_data[i]["slots"] = slots_temp

    for i in lab_codes:
        d1 = lab_data[lab_data['course_code'] == i]
        if(i not in course_data):
            course_data[i] = {"name": d1.iloc[0]["course_name"], "slots": [], "labs": []}
        slot1_values = list(set(d1['slot1'].dropna().tolist()))
        slot2_values = list(set(d1['slot2'].dropna().tolist()))
        slot3_values = list(set(d1['slot3'].dropna().tolist()))
        slot4_values = list(set(d1['slot4'].dropna().tolist()))
        slot5_values = list(set(d1['slot5'].dropna().tolist()))
        slot6_values = list(set(d1['slot6'].dropna().tolist()))
        slots_temp = slot1_values + slot2_values + slot3_values + slot4_values + slot5_values + slot6_values
        course_data[i]["labs"] = slots_temp

    # print(Course_data)
    # course_data = Course_data

def allocate_courses(idx, all_combi, all_tslots):
    if(idx >= len(wishlist)):
        if(len(getTT()) != 0):
            # print(len(getTT()))
            # printTT()
            x = getTT()
            f = True
            for a in x:
                if(x[a] == None):
                    f = False
            # print("\n\n\n")
            if(f):
                all_combi.append(x)
                all_tslots.append(getTslots())
        return True
    if "labs" in course_data[wishlist[idx]]:
        #TODO: BACKTRACKING FOR BOTH THEORY AND LABS
        # print(wishlist[idx]["slots"])
        for slot in course_data[wishlist[idx]]["slots"]:
            #print("YES")
            if(canPlace(wishlist[idx], slot)):
                theory_slots[slot] = wishlist[idx]
                Place(wishlist[idx], slot)
            else:
                return False
            idxl = 0
            while(idxl < len(course_data[wishlist[idx]]["labs"])):
                if(canLabPlace(wishlist[idx], course_data[wishlist[idx]]["labs"][idxl])):
                    PlaceLab(wishlist[idx], course_data[wishlist[idx]]["labs"][idxl])
                    success = allocate_courses(idx+1, all_combi, all_tslots)
                    # allocate_courses(idx+1, all_combi)
                    # if(success):
                    #     return True
                    removeLabPlaced(wishlist[idx], course_data[wishlist[idx]]["labs"][idxl])
                idxl += 1
            removePlaced(wishlist[idx], slot) #Remove Theory!
        return False
    else:
        #BACKTRACKING ONLY FOR THEORY
        if(idx >= len(wishlist)):
            return True
        for slot in course_data[wishlist[idx]]["slots"]: #iterate in all slots and check if placing is possible!
            if(canPlace(wishlist[idx], slot)):
                theory_slots[slot] = wishlist[idx]
                Place(wishlist[idx], slot)
                success = allocate_courses(idx+1,all_combi, all_tslots)
                # allocate_courses(idx+1,all_combi)
                # if(success): #This stops from remaining combinations!
                #     return True
                removePlaced(wishlist[idx], slot)
        return False

def fitness(a,b):
    #TODO: GIVE THE FITNESS VALUE OF TWO DICTIONARIES
    '''
        Fitness rules:
            -> If course and slots match (+10points)
            -> For each common slot (Even if the course is not same) (+3Points) [This is to make sure that friends can roam together whenever they don't have any class!]
            -> If both of them have took same course but the slots are not matching (-5points)
            -> If both of them don't have matching courses (0Points)
        Survival of the fittest😎

        type(a) = type(b) = dictionary!
        Example:
            a = {'L5': 'LIB1001', 'L6': 'CSE3003', 'L15': 'LIB1001', 
            'L16': 'CSE3003', 'L21': 'LIB1001', 'L22': 'LIB1001', 
            'L23': 'CSE3003', 'L24': 'CSE3003', 'L26': 'CSE4006', 
            'L33': 'CSE4006', 'L40': 'CSE4006', 'L43': 'CSE3003(LAB)', 
            'L44': 'CSE3003(LAB)', 'L49': 'CSE4006'}
    '''
    points = 0
    # for x in a:
    #     if x == 'L29' or x == '30' or x == 'L35' or x == 'L36' or x == 'L41' or x == 'L42'or x == 'L47' or x == 'L48'or x == 'L53' or x == 'L54'or x == 'L59' or x == 'L60':
    #         points -= 3
    # for x in b:
    #     if x == 'L29' or x == '30' or x == 'L35' or x == 'L36' or x == 'L41' or x == 'L42'or x == 'L47' or x == 'L48'or x == 'L53' or x == 'L54'or x == 'L59' or x == 'L60':
    #         points -= 3
    for x in a:
        if x in b: #Same slot!
            if(a[x] == b[x]):
                points += 10
            else:
                points += 5 #Slot matches! But different course

    return points

def findBest(w1, w2, t1,t2):
    maxi = -1
    w1_best = w1[0]
    w2_best = w2[0]
    t1best = {}
    t2best = {}
    for i in range(0,len(w1)):
        for j in range(0,len(w2)):
            a = w1[i]
            b = w2[j]
            score = fitness(a, b)
            if(score > maxi):
                maxi = score
                w1_best = a
                w2_best = b
                t1best = t1[i]
                t2best = t2[j]
    return [w1_best,w2_best, t1best, t2best]

def frndTT():
    global wishlist
    global all_combi
    wishlist = wishlist1
    print("WISHLIST1: ", wishlist1)
    all_combi = []
    all_tslots = []
    allocate_courses(0, all_combi=all_combi, all_tslots=all_tslots)
    all_combi1 = all_combi
    all_tslots1 = all_tslots
    # print(all_combi1)
    # print(len(all_combi1))
    if(len(all_combi1) == 0):
        print("NOT POSSIBLE!")
        return
    print("TOTAL COMBINATIONS P1: ", len(all_combi1))
    

    wishlist = wishlist2
    print("WISHLIST2: ", wishlist2)
    all_combi = []
    all_tslots = []
    allocate_courses(0, all_combi=all_combi, all_tslots=all_tslots)
    all_combi2 = all_combi
    all_tslots2 = all_tslots
    # print(all_combi2)
    if(len(all_combi2) == 0):
        print("NOT POSSIBLE!")
        return
    try:
        x = findBest(all_combi1, all_combi2, all_tslots1, all_tslots2)
        print("TOTAL COMBINATIONS P2: ",len(all_combi2))
        print("\n\n")
        print(x[0])
        print("\n\n\n")
        print(x[1])
        print("\n\n\n")
        print(x[2])
        print("\n\n\n")
        print(x[3])
        return x
    except:
        print("SOMETHING WENT WRONG!")
        return []
    return x


if __name__ == "__main__":
    ts1 = time.time()
    initialize_course_data()
    frndTT()
    ts2 = time.time()
    print("\n\n\nTime Taken (in seconds): ", ts2 - ts1)
    # printCD()
    # printCD()
    # print(course_data)
    # global all_combi
    # all_combi = []
    # all_tslots = []
    # allocate_courses(0, all_combi=all_combi, all_tslots=all_tslots)
    # print(all_combi[0])
    # print(all_tslots[0])
    # for x in all_combi:
    #     print(x)
    #     print("\n\n\n")
    # print(all_combi)
    # for x in all_combi:
    #     print(x)
    #     print("\n\n\n\n")
    # printTT()
    # print(getTT())