

while (True):
    sr = str(input())
    st = list()

    if (sr == "."):
        break

    for cr in sr:
        if (cr == "(" or cr == "["):
            st.append(cr)

        if (cr == ")"):
            if (st and st[-1] == "("):
                st.pop()
            else:
                st.append(cr)
                break
        elif (cr == "]"):
            if (st and st[-1] == "["):
                st.pop()
            else:
                st.append(cr)
                break

    if (st):
        print("no")
    else:
        print("yes")
