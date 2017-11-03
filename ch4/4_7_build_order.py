class Project():
    def __init__(self, name = None):
        self.name = name 
        self.children = []
        self.map = {}
        self.dependencies = 0

    def addChild(self, child):
        if child.name not in self.map.keys():
            self.children.append(child)
            self.map[child.name] = child
            child.incrementDependencies()

    def incrementDependencies(self):
        self.dependencies += 1

    def decrementDependencies(self):
        self.dependencies -= 1

    def __repr__(self):
        res = self.name
        res += "\n\tChildren: "
        for child in self.children:
            res += child.name + " "
        res += "\n\tDependencies: {}".format(self.dependencies)
        res += "\n"
        return res
        
class Graph():
    def __init__(self):
        self.projects = []
        self.map = {}

    def getOrCreateProject(self, name):
        if name not in self.map.keys():
            project = Project(name)
            self.projects.append(project)
            self.map[name] = project

        return self.map[name]

    def addEdge(self, startName, endName):
        start = self.map[startName]
        end = self.map[endName]
        start.addChild(end)

    def printGraph(self):
        print("============== Graph ==============")
        for project in self.projects:
            print(project)
        print("\n")

def buildGraph(projects, dependencies):
    graph = Graph()
    for name in projects:
        graph.getOrCreateProject(name)

    for dependency in dependencies:
        startName = dependency[0]
        endName = dependency[1]
        graph.addEdge(startName, endName)

    return graph

def findNextProj(graph):
    for p in graph.projects:
        if p.dependencies == 0:
            return p
    return None

def solution(graph):
    res = []
    while graph.projects != []:
        n = findNextProj(graph)
        if n == None:
            return None
        else:
            # print("find: ", n)
            res.append(n)
            graph.projects.remove(n)
            for child in n.children:
                child.decrementDependencies()
    return res
    
if __name__ == "__main__":
    projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    dependencies = [('f', 'c'),
            ('f', 'b'),
            ('f', 'a'),
            ('c', 'a'),
            ('b', 'a'),
            ('a', 'e'),
            ('b', 'h'),
            ('d', 'g')] 
    graph = buildGraph(projects, dependencies)
    graph.printGraph()
    res = solution(graph)
    print(res)
