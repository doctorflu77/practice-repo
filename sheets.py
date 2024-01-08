class books:
    def book_cost(n_pages, hardback ):
        c= 40 #base cost
        c = c +(n_pages *1)
        if hardback == True:
            c = c + 60
        else:
            pass 
        return {f' The cost of the book is Rs {c}'}
    
    cost1 = book_cost(n_pages= 240, hardback= True)
    print (cost1)
