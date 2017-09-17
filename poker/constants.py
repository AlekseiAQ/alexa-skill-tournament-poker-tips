CARDS = "..23456789TJQKA"

HANDS = {
    "ace":   "A",
    "king":  "K",
    "queen": "Q",
    "jack":  "J",
    "ten":   "T",
    "nine":  "9",
    "eight": "8",
    "seven": "7",
    "six":   "6",
    "five":  "5",
    "four":  "4",
    "three": "3",
    "two":  "2",
}

UTG_POSITION = ['utg', 'early', 'early position', 'under the gun']
MP_POSITION = ['mp', 'middle', 'middle position']
CO_POSITION = ['co', 'cut-off', 'cut off']
BU_POSITION = ['bu', 'button']
SB_POSITION = ['sb', 'small blind']
BB_POSITION = ['bb', 'big blind']

positions = [UTG_POSITION, MP_POSITION, CO_POSITION, BU_POSITION, SB_POSITION,
             BB_POSITION]

POSITIONS = []
for pos in positions:
    POSITIONS.extend(pos)

UTG_PUSH_RANGE = {
    14: "77+,ATs+,KTs+,QTs+,JTs,AJo+",
    12: "55+,A9s+,KTs+,QTs+,JTs,AJo+",
    10: "44+,A8s+,KTs+,QTs+,JTs,T9s,ATo+,KQo",
    8:  "33+,A7s+,K9s+,Q9s+,J9s+,T9s,ATo+,KJo+",
    6:  "22+,A2s+,K8s+,Q9s+,J9s+,T9s,98s,A8o+,KTo+,QJo",
    5:  "22+,A2s+,K5s+,Q8s+,J8s+,T8s+,98s,87s,A5o+,KTo+,QTo+,JTo",
}

MP_PUSH_RANGE = {
    14: "55+,A9s+,KTs+,QTs+,JTs,ATo+,KQo",
    12: "44+,A7s+,K9s+,QTs+,JTs,T9s,ATo+,KQo",
    10: "22+,A2s+,K9s+,Q9s+,J9s+,T8s+,98s,A8o+,KJo+,QJo",
    8:  "22+,A2s+,K8s+,Q9s+,J9s+,T8s+,98s,87s,A7o+,KTo+,QJo",
    6:  "22+,A2s+,K7s+,Q9s+,J8s+,T8s+,98s,87s,A4o+,KTo+,QTo+,JTo",
    5:  "22+,A2s+,K2s+,Q5s+,J7s+,T7s+,97s+,87s,76s,A2o+,K7o+,Q9o+,J9o+,T9o",
}

CO_PUSH_RANGE = {
    14: "22+,A2s+,K9s+,Q9s+,J9s+,T9s,98s,A7o+,KTo+",
    12: "22+,A2s+,K9s+,Q9s+,J9s+,T8s+,98s,A5o+,KTo+,QJo",
    10: "22+,A2s+,K6s+,Q8s+,J8s+,T8s+,97s+,87s,76s,A2o+,KTo+,QTo+,JTo",
    8:  "22+,A2s+,K4s+,Q8s+,J8s+,T8s+,97s+,87s,76s,65s,A2o+,K9o+,QTo+,JTo",
    6:  "22+,A2s+,K2s+,Q5s+,J7s+,T7s+,97s+,87s,76s,65s,A2o+,K6o+,Q9o+,J9o+,T9o",
    5:  "22+,A2s+,K2s+,Q2s+,J5s+,T6s+,96s+,86s+,76s,65s,A2o+,K4o+,Q7o+,J8o+,T8o+,98o",
}

BU_PUSH_RANGE = {
    14: "22+,A2s+,K6s+,Q8s+,J8s+,T8s+,97s+,87s,76s,A2o+,KTo+,QTo+,JTo",
    12: "22+,A2s+,K4s+,Q8s+,J8s+,T7s+,97s+,87s,76s,A2o+,K9o+,QTo+,JTo",
    10: "22+,A2s+,K2s+,Q6s+,J7s+,T7s+,97s+,86s+,76s,65s,A2o+,K7o+,Q9o+,J9o+,T9o",
    8:  "22+,A2s+,K2s+,Q5s+,J7s+,T7s+,97s+,86s+,76s,65s,A2o+,K5o+,Q9o+,J9o+,T9o",
    6:  "22+,A2s+,K2s+,Q2s+,J5s+,T6s+,96s+,86s+,75s+,65s,A2o+,K2o+,Q7o+,J8o+,T9o",
    5:  "22+,A2s+,K2s+,Q2s+,J3s+,T6s+,96s+,86s+,75s+,65s,A2o+,K2o+,Q5o+,J7o+,T8o+,98o",
}

SB_PUSH_RANGE = {
    14: "22+,A2s+,K2s+,Q2s+,J5s+,T6s+,96s+,86s+,76s,65s,54s,A2o+,K2o+,Q7o+,J8o+,T8o+,98o",
    12: "22+,A2s+,K2s+,Q2s+,J3s+,T6s+,96s+,85s+,75s+,64s+,54s,A2o+,K2o+,Q5o+,J8o+,T8o+,98o,87o",
    10: "22+,A2s+,K2s+,Q2s+,J2s+,T3s+,95s+,84s+,74s+,64s+,53s+,43s,A2o+,K2o+,Q2o+,J6o+,T7o+,97o+,87o,76o",
    8:  "22+,A2s+,K2s+,Q2s+,J2s+,T2s+,94s+,84s+,74s+,64s+,53s+,43s,A2o+,K2o+,Q2o+,J4o+,T6o+,96o+,86o+,76o",
    6:  "22+,A2s+,K2s+,Q2s+,J2s+,T2s+,93s+,83s+,73s+,63s+,53s+,43s,A2o+,K2o+,Q2o+,J2o+,T5o+,95o+,86o+,76o,65o",
    5:  "22+,A2s+,K2s+,Q2s+,J2s+,T2s+,92s+,82s+,73s+,63s+,53s+,43s,A2o+,K2o+,Q2o+,J2o+,T2o+,95o+,85o+,75o+,65o",
}

PUSH_RANGES = {
    'utg': UTG_PUSH_RANGE,
    'mp': MP_PUSH_RANGE,
    'co': CO_PUSH_RANGE,
    'bu': BU_PUSH_RANGE,
    'sb': SB_PUSH_RANGE,
}
