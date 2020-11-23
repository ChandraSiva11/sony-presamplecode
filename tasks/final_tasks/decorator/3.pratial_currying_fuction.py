def change(a): 
    def w(b): 
        def x(c): 
            def y(d): 
                def z(e): 
                    print(a, b, c, d, e) 
                return z 
            return y 
        return x 
    return w    
change(10)(20)(30)(40)(50) 