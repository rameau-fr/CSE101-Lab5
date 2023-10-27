import csv

def read_database(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            for i in range(len(row)):
                if(row[i].strip().isdecimal()):
                    row[i] = int(row[i].strip())
            data.append(row)
        return data
    
def EuclideanDistance(person1, person2):
    """ This function computes the Euclidean
    distance between the characterists of 
    tow persons
    
    Args:
        person1 (list): Age1, Height1, Income1
        person1 (list): Age2, Height2, Income2
    
    Returns:
        float: the distance between the two inputs
    """
    val = 1
    return 1

def ComputeAllDistances(candidates_list, client):
    """ This function computes the Euclidean
    distance between the characterists of 
    two persons
    
    Args:
        candidates_list (nested lists): List of candidates Name, Age, Height, Income
        client (list): Age, Height, Income
    
    Returns:
        list: return all the distances between our client
        and the candidates in the database
    """
    return [1,1]

def FindMin(list):
    """ This function returns the minimum value
    in a list as well as its index
    
    Args:
        list (list): List of numbers (float or int)
    
    Returns: 
        a tuple with: (float, int)
            float: value of the minimum
            int  : index of the minimum value
    """
    return (1,1)

def main():
    # 1. Read the database (either the males or females!)
    # name | age | height | income(k$)
    candidates_list = read_database('list_males.csv')
    #candidates_list = read_database('list_females.csv')
    candidates_list = candidates_list[1:] # the remove the first row that contain the labels

    # 2. Here are characteristics of the clients (Pamela or George)
    Pamela = [25, 157, 65]
    #George = [27, 168, 51]

    # 3. Compute the distance between the client and one person
    person = ["Madison", 30, 178, 45]
    dist = EuclideanDistance(Pamela, person[1:])

    # 4. Compute the distance between the client and the candidates
    list_dist = ComputeAllDistances(candidates_list, Pamela)

    # 5. Find the best candidate! (minimum in the list)
    val, idx = FindMin(list_dist)
    print(candidates_list[idx]) # Print the best candidate for the client
    
if __name__ == "__main__": # Run the main!
    main()
        