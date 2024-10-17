import random

# Parameters for species
Species = ["Human","Vulcan","Andorian" ]
probabilities_1 = {
    "Human": 0.75,
    "Vulcan": 0.25,
    "Andorian": 0.25
}

weighted_list_1 = []
for item, prob in probabilities_1.items():
    weighted_list_1.extend([item] * int(prob * 100))

random_item_1 = random.choice(weighted_list_1)

# Parameters for gender
Gender = ["Male", "Female"]
probabilities_2 = {
    "Male": 0.50,
    "Female": 0.50
}

weighted_list_2 = []
for item, prob in probabilities_2.items():
    weighted_list_2.extend([item] * int(prob * 100))

random_item_2 = random.choice(weighted_list_2)

# Parameters for Division
Division = ["Science Division", "Medical Division", "Engineering Division", "Operation Division", "Security Division", "Tactical Division"]
probabilities_3 = {
    "Science Division": 0.20,
    "Medical Division": 0.10,
    "Engineering Division": 0.30,
    "Operations Division": 0.20,
    "Security Division": 0.15,
    "Tactical Division": 0.05
}

weighted_list_3 = []
for item, prob in probabilities_3.items():
    weighted_list_3.extend([item] * int(prob * 100))

random_item_3 = random.choice(weighted_list_3)

# Parameters for position once division is selected

random_division = random.choice(Division)

positions = {
    "Science Division": {
        "Chief Science officer": 0.10,
        "Physics Specialist": 0.20,
        "Chemistry Specialist": 0.20,
        "Biology Specialist": 0.20,
        "Anthropology Specialist": 0.20,
        "Junior Science officer": 0.10
    },
    "Medical Division": {
        "Chief Medical officer": 0.10,
        "Psychology Specialist": 0.10,
        "Surgury Specialist": 0.10,
        "Medic": 0.30,
        "Nurse": 0.30,
        "Junior Medical officer": 0.10
    },
    "Engineering Division": {
        "Chief Engineer": 0.10,
        "Warp Specialist": 0.40,
        "Maintenance Technician": 0.40,
        "Junior Engineer": 0.10
    },
    "Operations Division": {
        "Chief Operations officer": 0.10,
        "Communications officer": 0.20,
        "Deflector Specialist": 0.15,
        "Yeomen": 0.30,
        "Junior Operations officer": 0.25
    },
    "Security Division": {
        "Chief Security Officer": 0.10,
        "Armory officer": 0.10,
        "Alpha Group": 0.15,
        "Beta Group": 0.15,
        "Gamma Group": 0.15,
        "Delta Group": 0.15,
        "Junior Security officer": 0.20
    },
    "Tactical Division": {
        "Chief Tactical officer": 0.10,
        "Helms officer": 0.20,
        "Navigation officer": 0.20,
        "Torpedo Specialist": 0.20,
        "Beam array Specialist": 0.20,
        "Junior Tactical officer": 0.10
    }
}

selected_positions  = positions[random_item_3]
weighted_list_position = []
for position, prob in selected_positions.items():
    weighted_list_position.extend([position] * int(prob * 100))

random_position = random.choice(weighted_list_position)

# Rank factors

rank = {
    "Chief Science officer": {
        "Commander": 0.30,
        "Lieutenant-commander": 0.50,
        "Lieutenant": 0.20
    },
    "Chief Medical officer": {
        "Commander": 0.30,
        "Lieutenant-commander": 0.30,
        "Lieutenant": 0.40
    },
     "Chief Engineer": {
         "Commander": 0.30,
         "Lieutenant-commander": 0.30,
         "Lieutenant": 0.40
     },
    "Chief Operations officer": {
        "Lieutenant-commander": 0.60,
        "Lieutenant": 0.40
    },
    "Chief Security officer": {
        "Lieutenant-commander": 0.50,
        "Lieutenant": 0.50
    },
    "Chief Tactical officer": {
        "Lieutenant-commander": 0.50,
        "Lieutenant": 0.50
    },
    "Physics Specialist": {
        "Lieutenant": 0.25,
        "Lieutenant junior grade": 0.75
    },
    "Chemistry Specialist": {
        "Lieutenant": 0.40,
        "Lieutenant junior grade": 0.60
    },
    "Biology Specialist": {
        "Lieutenant": 0.40,
        "Lieutenant junior grade": 0.60
    },
    "Anthropology Specialist": {
        "Lieutenant": 0.40,
        "Lieutenant junior grade": 0.60
    },
    "Psychology Specialist": {
        "Lieutenant-commander": 0.50,
        "Lieutenant": 0.50
    },
     "Surgury Specialist": {
         "Lieutenant-commander": 0.50,
         "Lieutenant": 0.50
     },
    "Medic": {
        "Lieutenant": 0.30,
        "Lieutenant Junior grade": 0.70
    },
    "Nurse": {
        "Lieutenant": 0.50,
        "Lieutenant Junior grade": 0.50
    },
    "Warp Specialist": {
        "Lieutenant": 0.20,
        "Lieutenant Junior grade": 0.80
    },
    "Maintenance Technician": {
        "Lieutenant": 0.20,
        "Lieutenant Junior grade": 0.80
    },
    "Communications officer": {
        "Lieutenant": 0.30,
        "Lieutenant Junior grade": 0.70
    },
    "Deflector Specialist": {
        "Lieutenant": 0.40,
        "Lieutenant Junior grade": 0.60
    },
    "Yeomen": {
        "Lieutenant Junior grade": 1.00
    },
    "Armory officer": {
        "Lieutenant": 0.70,
        "Lieutenant Junior grade": 0.30
    },
    "Alpha Group": {
        "Lieutenant": 0.20,
        "Lieutenant Junior grade": 0.80
    },
    "Beta Group": {
        "Lieutenant": 0.20,
        "Lieutenant Junior grade": 0.80
    },
    "Gamma Group": {
        "Lieutenant": 0.20,
        "Lieutenant Junior grade": 0.80
    },
    "Delta Group": {
        "Lieutenant": 0.20,
        "Lieutenant Junior grade": 0.80
    },
    "Helms officer": {
        "Lieutenant": 0.50,
        "Lieutenant Junior grade": 0.50
    },
    "Navigation officer": {
        "Lieutenant": 0.50,
        "Lieutenant Junior grade": 0.50
    },
    "Torpedo Specialist": {
        "Lieutenant Junior grade": 1.00
    },
    "Beam array Specialist": {
        "Lieutenant Junior grade": 1.00
    },
    "Junior Science officer": {
        "Ensign": 1.00
    },
    "Junior Medical officer": {
        "Ensign": 1.00
    },
    "Junior Engineer": {
        "Ensign": 1.00
    },
    "Junior Operations officer": {
        "Ensign": 1.00
    },
    "Junior Security officer": {
        "Ensign": 1.00
    },
    "Junior tactical officer": {
        "Ensign": 1.00
    }
}

selected_rank = rank[random_position]
weighted_list_rank = []
for rank, prob in selected_rank.items():
    weighted_list_rank.extend([rank] * int(prob * 100))

random_rank = random.choice(weighted_list_rank)

print("The new officer transfered to your ship is ")
print(f"Species: {random_item_1}")
print(f"Gender: {random_item_2}")
print(f"Department: {random_item_3}")
print(f"Position: {random_position}")
print(f"Rank: {random_rank}")
