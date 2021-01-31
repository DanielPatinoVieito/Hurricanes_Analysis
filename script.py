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

#correct damages list
def correct_damages_values(damages):
  corrected_damages = []
  conversion = {"M": 1000000, "B": 1000000000}
  for damage in damages:
    if damage == "Damages not recorded":
      corrected_damages.append("Damages not recorded")
      continue
    else:
      if damage[-1] == "M":
        corrected_damages.append(float(damage[:-1]) * conversion["M"])
      elif damage[-1] == "B":
        corrected_damages.append(float(damage[:-1]) * conversion["B"])
  return corrected_damages

corrected_damages = correct_damages_values(damages)

#construct dictionary for all data
print("i.- HURRICANES DICTIONARY:")

def construct_dictionary(names, months, years, max_sustained_winds, areas_affected, corrected_damages, deaths):
  zipped_list = list(zip(names, months, years, max_sustained_winds, areas_affected, corrected_damages, deaths))
  hurricanes_dictionary = {name: {"Name": name, "Month": month, "Year": year, "Max Sustained Wind": max_sustained_wind, "Areas Affected": areas_affected, "Damage": damage, "Deaths": death} for name, month, year, max_sustained_wind, areas_affected, damage, death in zipped_list}
  return hurricanes_dictionary

hurricanes_dictionary = construct_dictionary(names, months, years, max_sustained_winds, areas_affected, corrected_damages, deaths)
print(hurricanes_dictionary.keys())
print(hurricanes_dictionary)

#construct dictionary per year
print("""
ii.- HURRICANES PER YEAR DICTIONARY:""")

def construct_dictionary_per_year(hurricanes_dictionary, years):
  years_dictionary = {year:[] for year in years}
  for name, values in hurricanes_dictionary.items():
    years_dictionary[values["Year"]].append(values)
  return(years_dictionary)

hurricanes_dictionary_per_year = construct_dictionary_per_year(hurricanes_dictionary, years)
print(hurricanes_dictionary_per_year.keys())
print(hurricanes_dictionary_per_year)

#frequency per area dictionary
print("""
iii.- COUNT PER AREA DICTIONARY:""")

def construct_dictionary_areas_count(hurricanes_dictionary, areas_affected):
  areas_dictionary = {area:0 for sublist in areas_affected for area in sublist}
  for name, values in hurricanes_dictionary.items():
    for area in values["Areas Affected"]:
      areas_dictionary[area] += 1
  return areas_dictionary

areas_dictionary_count = construct_dictionary_areas_count(hurricanes_dictionary, areas_affected)
print(areas_dictionary_count.keys())
print(areas_dictionary_count)

#area affected by most hurricanes
print("""
iv.- AREA AFFECTED BY MOST HURRICANES:""")

def top_hit_area(areas_dictionary_count):
  top_area = ""
  top_count = 0
  for area, count in areas_dictionary_count.items():
    if count > top_count:
      top_count = count
      top_area = area
  return top_area, top_count

top_hit_area, top_hit_count = top_hit_area(areas_dictionary_count)
print("The area affected by the most hurricanes is " + top_hit_area + ", affected by " + str(top_hit_count) + " hurricanes.")

#hurricane that caused the greatest number of deaths
print("""
v.- HURRICANE THAT CAUSED THE GREATEST NUMBER OF DEATHS:""")

def hurricane_top_deaths(hurricanes_dictionary):
  top_hurricane_deaths = ""
  top_deaths = 0
  for name, values in hurricanes_dictionary.items():
    if values["Deaths"] > top_deaths:
      top_deaths = values["Deaths"]
      top_hurricane_deaths = name
  return top_hurricane_deaths, top_deaths

top_hurricane_deaths, top_deaths = hurricane_top_deaths(hurricanes_dictionary)
print("The hurricane that caused the greatest number of deaths is " + top_hurricane_deaths + ", with " + str(top_deaths) + " deaths.")

#mortality scale 
print("""
vi.- HURRICANES MORTALITY SCALE DICTIONARY:""")

def construct_clasification_per_mortality(hurricanes_dictionary):
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  mortality_dictionary = {1: [], 2: [], 3: [], 4: [], 5:[]}
  for name, values in hurricanes_dictionary.items():
    if values["Deaths"] <= mortality_scale[1]:
      mortality_dictionary[1].append(values)
    elif values["Deaths"] > mortality_scale[1] and values["Deaths"] <= mortality_scale[2]:
      mortality_dictionary[2].append(values)
    elif values["Deaths"] > mortality_scale[2] and values["Deaths"] <= mortality_scale[3]:
      mortality_dictionary[3].append(values)
    elif values["Deaths"] > mortality_scale[3] and values["Deaths"] <= mortality_scale[4]:
      mortality_dictionary[4].append(values)
    elif values["Deaths"] > mortality_scale[4]:
      mortality_dictionary[5].append(values)
  return mortality_dictionary

mortality_dictionary = construct_clasification_per_mortality(hurricanes_dictionary)
print(mortality_dictionary)
print("""
vi.1.- HURRICANES OF MORTALITY 1:""")
print(mortality_dictionary[1])
print("""
vi.2.- HURRICANES OF MORTALITY 2:""")
print(mortality_dictionary[2])
print("""
vi.3.- HURRICANES OF MORTALITY 3:""")
print(mortality_dictionary[3])
print("""
vi.4.- HURRICANES OF MORTALITY 4:""")
print(mortality_dictionary[4])
print("""
vi.5.- HURRICANES OF MORTALITY 5:""")
print(mortality_dictionary[5])


#hurricane that caused the most damage
print("""
vii.- HURRICANE THAT CAUSED THE MOST DAMAGE:""")

def top_damaging_hurricane(hurricanes_dictionary):
  top_hurricane_damage = ""
  top_damage = 0.0
  for name, values in hurricanes_dictionary.items():
    if values["Damage"] == "Damages not recorded":
      continue
    elif float(values["Damage"]) > top_damage:
      top_hurricane_damage = name
      top_damage = float(values["Damage"])
  return top_hurricane_damage, top_damage

top_hurricane_damage, top_damage = top_damaging_hurricane(hurricanes_dictionary)
print("The hurricane that caused the greatest damage was " + top_hurricane_damage + " with a total cost of " + str(top_damage) + ".")

#damage scale 
print("""
viii.- HURRICANES DAMAGE SCALE DICTIONARY:""")

def construct_clasification_per_damages(hurricanes_dictionary):
  damage_scale = {0: 0.0, 1: 100000000.0, 2: 1000000000.0, 3: 10000000000.0, 4: 50000000000.0}
  damage_dictionary = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for name, values in hurricanes_dictionary.items():
    if values["Damage"] == "Damages not recorded":
      damage_dictionary[0].append(values)
    elif float(values["Damage"]) <= damage_scale[1]:
      damage_dictionary[1].append(values)
    elif float(values["Damage"]) > damage_scale[1] and float(values["Damage"]) <= damage_scale[2]:
      damage_dictionary[2].append(values)
    elif float(values["Damage"]) > damage_scale[2] and float(values["Damage"]) <= damage_scale[3]:
      damage_dictionary[3].append(values)
    elif float(values["Damage"]) > damage_scale[3] and float(values["Damage"]) <= damage_scale[4]:
      damage_dictionary[4].append(values)
    elif float(values["Damage"]) > damage_scale[4]:
      damage_dictionary[5].append(values)
  return damage_dictionary

damage_dictionary = construct_clasification_per_damages(hurricanes_dictionary)
print(damage_dictionary)
print("""
viii.0.- HURRICANES OF DAMAGE 0:""")
print(damage_dictionary[0])
print("""
viii.1.- HURRICANES OF DAMAGE 1:""")
print(damage_dictionary[1])
print("""
viii.2.- HURRICANES OF DAMAGE 2:""")
print(damage_dictionary[2])
print("""
viii.3.- HURRICANES OF DAMAGE 3:""")
print(damage_dictionary[3])
print("""
viii.4.- HURRICANES OF DAMAGE 4:""")
print(damage_dictionary[4])
print("""
viii.5.- HURRICANES OF DAMAGE 5:""")
print(damage_dictionary[5])
