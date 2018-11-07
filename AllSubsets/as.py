def getSubsets(set,startIndex):
    #all_subsets = []

    if startIndex == len(set):
        return [[]]
    #print('startIndex -> %d'%(startIndex))
    all_subsets = getSubsets(set, startIndex + 1)
    #print('All sub_sets before add->', all_subsets)
    item_to_add = set[startIndex]
    current_subsets = []
    for subset in all_subsets:
        #print('subset ->',  subset )
        new_subset = [item_to_add]
        new_subset.extend(subset)
        current_subsets.append(new_subset)
    all_subsets.extend(current_subsets)

    return all_subsets

if __name__ == '__main__':
    set = [1,2,3,4,5]
    all_subsets = getSubsets(set, 0)

    print(all_subsets)
