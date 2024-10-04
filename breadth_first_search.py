from collections import deque

def works_in_abc(name):
    if name == "random_person":
        return True
    else:
        return False
def bfs(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        print("current person: " + person)
        if person not in searched:
            if works_in_abc(person):
                print(person + " works in ABC")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
        else:
            print(person + " already searched")
    return False


graph = {}
graph["me"] = ["sudhagar","vijay","bala", "kamran"]
graph["sudhagar"] = ["kamran", "vijay", "srini", "raghu"]
graph["vijay"] = ["bala", "friendofVijay"]
graph["bala"] = ["sudhagar", "random_person"]
graph["kamran"] = ["friendofKamran", "random_person"]
graph["friendofVijay"] = []
graph["random_person"] = []
graph["srini"] = []
graph["raghu"] = []
graph["friendofKamran"] = []


bfs("me")

