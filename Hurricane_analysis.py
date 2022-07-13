# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def dmg_conversion(damages):
  converted_dmg = []
  for item in damages:
    if item == "Damages not recorded":
      converted_dmg.append(item)
    elif "M" in item:
      converted_dmg.append(float(item.strip("M"))*conversion["M"])
    elif "B" in item:
      converted_dmg.append(float(item.strip("B"))*conversion["B"])
  return converted_dmg

# test function by updating damages
# print(damages)
updated_damages = dmg_conversion(damages)
# print(updated_damages)
# print("\n \n \n")

# 2 
# Create a Table
def hurricane_compiler(name, month, year, max_winds, areas, damage, deaths):
  hurricanes_dictionary = {}
  for i in range(len(name)):
    hurricanes_info = {}
    hurricanes_info["Name"] = name[i]
    hurricanes_info["Month"] = month[i]
    hurricanes_info["Year"] = year[i]
    hurricanes_info["Max Sustained Wind"] = max_winds[i]
    hurricanes_info["Areas Affected"] = areas[i]
    hurricanes_info["Damage"] = damage[i]
    hurricanes_info["Deaths"] = deaths[i]
    hurricanes_dictionary[name[i]] = hurricanes_info
  return hurricanes_dictionary
# Create and view the hurricanes dictionary
hurricanes = hurricane_compiler(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print("\t Here is a dictionary of hurricanes: \n")
print(hurricanes)

print("\n \n")
# 3
# Organizing by Year
def hurricanes_years(hurricanes_dict):
  years_dict= {}
  for x in hurricanes_dict:
    temp_list = []
    temp_year = hurricanes_dict[x].get("Year")
    if temp_year in years_dict:
      temp_list = (years_dict.get(temp_year))
    temp_list.append(hurricanes_dict[x])
    years_dict[hurricanes_dict[x].get("Year")] = temp_list
  return years_dict
# create a new dictionary of hurricanes with year and key
years_dictionary = hurricanes_years(hurricanes)
# print("\t Here is a dictionary of hurricanes in years: \n \n")
# print(years_dictionary)

# 4
# Counting Damaged Areas
def count_areas_affected(hurricanes):
  count_areas = {}
  for x in hurricanes.values():
    for i in (x.get("Areas Affected")):
      if count_areas.get(i.title()) is None:
        count_areas[i.title()] = 1
      else:
        count_areas[i.title()] = count_areas[i.title()] + 1
  return count_areas
# # create dictionary of areas to store the number of hurricanes involved in
areas_affected_counts = count_areas_affected(hurricanes)
# print(areas_affected_counts)

# 5 
# Calculating Maximum Hurricane Count
def most_impacted_area(aff_areas_dict):
  most_aff = ""
  high_count = 0
  for area,count in aff_areas_dict.items():
    # print(area,count,type(area), type(count))
    if aff_areas_dict[area] > high_count:
      high_count = aff_areas_dict[area]
      most_aff = area
    else:
      continue
  print(str.format("The area affected most by hurricanes is {} which was hit {} times by hurricanes.", most_aff, high_count))

# find most frequently affected area and the number of hurricanes involved in
most_impacted_area(areas_affected_counts)

# 6
# Calculating the Deadliest Hurricane
def deadly_hurricane(hurricanes_dict):
  most_deadly = ""
  high_count = 0
  # for hurr,count in hurricanes_dict.items():
  for items in hurricanes_dict.values():
    if items.get("Deaths") > high_count:
      high_count = items.get("Deaths")
      most_deadly = items.get("Name")
    else:
      continue
  print(str.format("The most deadly hurricane was {} with {} deaths recorded.", most_deadly, high_count))
# find highest mortality hurricane and the number of deaths
deadly_hurricane(hurricanes)
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
def mortality_rating(hurricanes_dict):
  list4 = []
  list3 = []
  list2 = []
  list1 = []
  list0 = []
  for item in hurricanes_dict.values():
    if item.get("Deaths") > mortality_scale[4]:
      list4.append(item)
    elif item.get("Deaths") >= mortality_scale[3]:
      list3.append(item)
    elif item.get("Deaths") >= mortality_scale[2]:
      list2.append(item)
    elif item.get("Deaths") >= mortality_scale[1]:
      list1.append(item)
    elif item.get("Deaths") >= mortality_scale[0]:
      list0.append(item)
  rating_dict = {}
  rating_dict[4] = list4
  rating_dict[3] = list3
  rating_dict[2] = list2
  rating_dict[1] = list1
  rating_dict[0] = list0
  return rating_dict

# categorize hurricanes in new dictionary with mortality severity as key
mortality_scaled_hurricanes = mortality_rating(hurricanes)
print(mortality_scaled_hurricanes[2])

# 8 Calculating Hurricane Maximum Damage
def highest_damage(hurricanes_dict):
  cost = 0
  name = ""
  for item in hurricanes_dict.values():
    if item.get("Damage") == "Damages not recorded":
      continue
    if item.get("Damage") > cost:
      cost = item.get("Damage")
      name = item.get("Name")
  print(str.format("The hurricane with the highest damage cost was {} with ${} in damages", name, cost))

# find highest damage inducing hurricane and its total cost
highest_damage(hurricanes)
print("\n \n")
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_rating(hurricanes_dict):
  list4 = []
  list3 = []
  list2 = []
  list1 = []
  list0 = []
  for item in hurricanes_dict.values():
    if item.get("Damage") == "Damages not recorded":
      continue
    elif item.get("Damage") > damage_scale[4]:
      list4.append(item)
    elif item.get("Damage") >= damage_scale[3]:
      list3.append(item)
    elif item.get("Damage") >= damage_scale[2]:
      list2.append(item)
    elif item.get("Damage") >= damage_scale[1]:
      list1.append(item)
    elif item.get("Damage") >= damage_scale[0]:
      list0.append(item)
  rating_dict = {}
  rating_dict[4] = list4
  rating_dict[3] = list3
  rating_dict[2] = list2
  rating_dict[1] = list1
  rating_dict[0] = list0
  return rating_dict

# categorize hurricanes in new dictionary with damage severity as key
damaging_hurricanes_dict = damage_rating(hurricanes)
print("Dictionary of Damage Rating hurricanes: \n" + str(damaging_hurricanes_dict))
