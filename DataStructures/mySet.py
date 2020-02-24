class mySet:

    def __init__(self):
        self.links = []

    def add(self, link):
        if not self.__contains__(link):
            self.links.append(link)

    def remove(self, link):
        if link in self.links:
            self.links.remove(link)

    def __contains__(self, link):
        if link in self.links:
            return True
        else:
            return False

    def __iter__(self):
        return iter(self.links.copy())

    def __or__(self, other):
        endList = mySet()

        for a in other:
            if not endList.__contains__(a):
                endList.add(a)

        for a in self:
            if not endList.__contains__(a):
                endList.add(a)
        return endList

    def __and__(self, other):
        endList = mySet()

        for a in other:
            if self.__contains__(a):
                endList.add(a)

        return endList

    def __sub__(self, other):
        endList = mySet()

        for a in self:
            if not other.__contains__(a):
                endList.add(a)

        return endList

    def komlpement(self, other):
        endList = mySet()

        for a in other:
            if not self.__contains__(a):
                endList.add(a)

        return endList

    def __len__(self):
        return len(self.links)

    def get(self, i):
        return self.links[i]
