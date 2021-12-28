def cocktailSort(the_list, key=lambda x: x, reverse=False):
    n = len(the_list)
    swapped = True
    start = 0
    end = n - 1
    if reverse == False:
        while swapped == True:

            # reset the swapped flag on entering the loop,
            # because it might be true from a previous
            # iteration.
            swapped = False

            # loop from left to right same as the bubble
            # sort
            for i in range(start, end):
                if key(the_list[i]) > key(the_list[i + 1]):
                    the_list[i], the_list[i + 1] = the_list[i + 1], the_list[i]

                    swapped = True

                # if nothing moved, then array is sorted.
            if swapped == False:
                break

                # otherwise, reset the swapped flag so that it
                # can be used in the next stage
            swapped = False

            # move the end point back by one, because
            # item at the end is in its rightful spot
            end = end - 1

            # from right to left, doing the same
            # comparison as in the previous stage
            for i in range(end - 1, start - 1, -1):
                if key(the_list[i]) > key(the_list[i + 1]):
                    the_list[i], the_list[i + 1] = the_list[i + 1], the_list[i]
                    swapped = True

                # increase the starting point, because
                # the last stage would have moved the next
                # smallest number to its rightful spot.
            start = start + 1
    else:
        while swapped == True:

            # reset the swapped flag on entering the loop,
            # because it might be true from a previous
            # iteration.
            swapped = False

            # loop from left to right same as the bubble
            # sort
            for i in range(start, end):
                if key(the_list[i]) < key(the_list[i + 1]):
                    the_list[i], the_list[i + 1] = the_list[i + 1], the_list[i]

                    swapped = True

                # if nothing moved, then array is sorted.
            if swapped == False:
                break

                # otherwise, reset the swapped flag so that it
                # can be used in the next stage
            swapped = False

            # move the end point back by one, because
            # item at the end is in its rightful spot
            end = end - 1

            # from right to left, doing the same
            # comparison as in the previous stage
            for i in range(end - 1, start - 1, -1):
                if key(the_list[i]) < key(the_list[i + 1]):
                    the_list[i], the_list[i + 1] = the_list[i + 1], the_list[i]
                    swapped = True

                # increase the starting point, because
                # the last stage would have moved the next
                # smallest number to its rightful spot.
            start = start + 1


def selectionSort(the_list, key=lambda x: x, reverse=False):
    """
    sort the element of the list
    l - list of element
    return the ordered list (l[0]<l[1]<...)
    """
    if reverse == False:
        for i in range(0, len(the_list) - 1):
            ind = i
            # find the smallest element in the rest of the list
            for j in range(i + 1, len(the_list)):
                if key(the_list[j]) < key(the_list[ind]):
                    ind = j
            if (i < ind):
                # interchange
                aux = the_list[i]
                the_list[i] = the_list[ind]
                the_list[ind] = aux
    else:
        for i in range(0, len(the_list) - 1):
            ind = i
            # find the smallest element in the rest of the list
            for j in range(i + 1, len(the_list)):
                if key(the_list[j]) > key(the_list[ind]):
                    ind = j
            if (i < ind):
                # interchange
                aux = the_list[i]
                the_list[i] = the_list[ind]
                the_list[ind] = aux