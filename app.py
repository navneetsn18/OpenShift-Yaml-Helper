import os
import ruamel.yaml
import time

yaml = ruamel.yaml.YAML(typ='rt')
# yaml.indent(mapping=2, sequence=2, offset=0)
yaml.preserve_quotes = True

envs = ["DEV", "INT", "QA", "QAB", "QAG", "PF","PF1", "PF2", "PF3", "PF4", "UAT", "PP", "PN", "PROD"]

data = None

def addUpdateEntryInYamlFile():
    choice = input("1. Add in all environments\n2. Add in specific environmets\nEnter your choice: ")
    if choice == "1":
        return modifyDataInAllEnv("ADD")
    elif choice == "2":
        return modifyDataInSpecificEnv("ADD")
    else:
        print("Invalid choice!")
    
def deleteEntryInYamlFile():
    choice = input("1. Delete in all environments\n2. Delete in specific environmets:\nEnter your choice: ")
    if choice == "1":
        return modifyDataInAllEnv("DELETE")
    elif choice == "2":
        return modifyDataInSpecificEnv("DELETE")
    else:
        print("Invalid choice!")

def modifyDataInAllEnv(operationType):
    os.system('cls||clear')
    key = input("Enter the new Key: ")
    value = None

    if operationType == "ADD":
        value = input("Enter the new Value: ")

        if value.isnumeric():
            value = int(value)
        elif value.lower() == "true" or value.lower() == "false":
            value = bool(value.lower() == "true")

    for config in data:
        if config["name"] == "Base Settings":
            for env in config:
                if env in envs and "COMMON_ENV_VARIABLES" in config[env]:
                    if operationType == "ADD":
                        config[env]["COMMON_ENV_VARIABLES"][key] = value
                    else:
                        try:
                            del config[env]["COMMON_ENV_VARIABLES"][key]
                        except:
                            print("Key not found in the environment {}".format(env))
                    print("Data modified in YAML file for environment {}".format(env))
    saveData(data)
    time.sleep(2)

def modifyDataInSpecificEnv(operationType):
    os.system('cls||clear')
    key = input("Enter the new Key: ")
    value = None

    if operationType == "ADD":
        value = input("Enter the new Value: ")

        if value.isnumeric():
            value = int(value)
        elif value.lower() == "true" or value.lower() == "false":
                value = bool(value.lower() == "true")

    env_input = input("Enter the environments with , sperated :").upper().split(",")

    for config in data:
        if config["name"] == "Base Settings":
            for env in config:
                if env in env_input and "COMMON_ENV_VARIABLES" in config[env]:
                    if operationType == "ADD":
                        config[env]["COMMON_ENV_VARIABLES"][key] = value
                    else:
                        try:
                            del config[env]["COMMON_ENV_VARIABLES"][key]
                        except:
                            print("Key not found in the environment {}".format(env))
                    print("Data modified in YAML file for environment {}".format(env))
    saveData(data)
    time.sleep(2)

def saveData(data):
    with open(YML_FILE, 'w') as file:
        yaml.dump(data, file)
    print("Data saved successfully in YAML file.")

if __name__ == '__main__':

    YML_FILES = [f for f in os.listdir() if f.endswith(".yaml") or f.endswith(".yml")]

    YML_FILE = None

    if len(YML_FILES) > 0:
        for i in YML_FILES:
            if "openshift" in i:
                YML_FILE = i
                break

    while True and YML_FILE!=None:

        os.system('cls||clear')

        with open(YML_FILE, 'r') as file:
            data = yaml.load(file)

        choice = input("Choose from the menu below\n 1. Add/Update Entry in Yaml file\n 2. Delete entry in Yaml file.\n 3. Any other key to exit.\n Enter you choice: ")
        
        os.system('cls||clear')
        
        if choice == "1":
            addUpdateEntryInYamlFile()
        elif choice == "2":
            deleteEntryInYamlFile()
        else:
            break
    if YML_FILE==None:
        print("No Openshift Params file found.")
    print("Exiting the program. Goodbye!")
