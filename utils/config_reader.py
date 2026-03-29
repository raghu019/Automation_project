# import yaml

# def load_config():
#     with open("config/config.yaml", "r") as file:
#         return yaml.safe_load(file)


#----------------------After implement step 10 environment management---------------------

# import yaml

# def load_config():
#     with open("config/config.yaml") as file:
#         config = yaml.safe_load(file)

#     env = config["env"]

#     return config[env] 




import yaml

def load_config():
    with open("config/config.yaml") as file:
        config = yaml.safe_load(file)

    env = config["env"]

    # merge env config + credentials
    env_config = config[env]
    env_config["username"] = config["credentials"]["username"]
    env_config["password"] = config["credentials"]["password"]

    return env_config


# now env_config will have all the data from the env config and credentials, 
# so we can use this env_config in our test cases to get the base url and credentials
#  without having to load the config file multiple times in our test cases.