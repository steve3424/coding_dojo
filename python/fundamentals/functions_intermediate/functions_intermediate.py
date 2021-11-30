from menu import RunMenu, FuncObj

def UpdateValsInDictionary():
    x = [ [5,2,3], [10,8,9] ] 
    print("Old x:")
    print(x)
    x[1][0] = 15
    print("New x:")
    print(x)
    print('\n')
    
    students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
    ]
    print("Old students:")
    print(students)
    students[0]["last_name"] = "Bryant"
    print("New student:")
    print(students)
    print('\n')

    sports_directory = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer' : ['Messi', 'Ronaldo', 'Rooney']
    }
    print("Old dir:")
    print(sports_directory)
    sports_directory["soccer"][0] = "Andres"
    print("New dir:")
    print(sports_directory)
    print('\n')

    z = [ {'x': 10, 'y': 20} ]
    print("Old z:")
    print(z)
    z[0]['y'] = 30
    print("New z:")
    print(z)
    print('\n')


def IterateDictionary():
    students = [
        {"first_name" : "Michael", "last_name" : "Jordan"},
        {"first_name" : "John",    "last_name" : "Rosales"},
        {"first_name" : "Mark",    "last_name" : "Guillen"},
        {"first_name" : "KB",      "last_name" : "Tonel"},
    ]
    for d in students:
        print("first_name - {0} \tlast_name - {1}".format(d["first_name"], d["last_name"]))
    print('\n')

def IterateDictionary2():
    k = "last_name"
    students = [
        {"first_name" : "Michael", "last_name" : "Jordan"},
        {"first_name" : "John",    "last_name" : "Rosales"},
        {"first_name" : "Mark",    "last_name" : "Guillen"},
        {"first_name" : "KB",      "last_name" : "Tonel"},
    ]
    for d in students:
        print(f"{d[k] if k in d.keys() else 'none'}")
    print('\n')

def PrintInfo():
    dojo = {
        "locations" : ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
        "instructors" : ["Michael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Minh", "Devon"],
    }
    for key,val in dojo.items():
        print(f"{len(val)} {key}")
        for i in val:
            print(i)
        print('\n')

if __name__ == "__main__":
    functions = [FuncObj(UpdateValsInDictionary), FuncObj(IterateDictionary), FuncObj(IterateDictionary2), FuncObj(PrintInfo)]
    func_to_run = functions[RunMenu("Choose a function below", functions)]
    func_to_run.func()
