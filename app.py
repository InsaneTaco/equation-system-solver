#gets values
slope1 = input("First slope: ")
y_intercept1 = input("First y-intercept: ")
print(f"""
    Got it! y = {slope1}x + {y_intercept1}
""")

slope2 = input("Second slope: ")
y_intercept2 = input("Second y-intercept: ")
print(f"""
    y = {slope2}x + {y_intercept2}
""")

#checks to make sure there are actually only integers
try:
    slope1 = float(slope1)
    y_intercept1 = float(y_intercept1)
    slope2 = float(slope2)
    y_intercept2 = float(y_intercept2)

    if slope1 == slope2 and y_intercept1 == y_intercept2:
        print("infinite solutions")

    elif slope1 == slope2 and not y_intercept1 == y_intercept2:
        print("no solutions pal")

    else:
        #solves using substitution method
        #mx + b = mx + b 
        sdif = slope1 - slope2
        ydif = y_intercept2 - y_intercept1
        #sdif(x) = ydif
        x = ydif / sdif
        #after getting x value, calculator now plugs it into first equation
        y = (slope1 * x) + y_intercept1

        #rounds to make sure there are no weird numbers like 0.300000000004
        x = round(x, 3)
        y = round(y, 3)

        #prints solution again
        print(f"""
    ({x}, {y})
    """)

except:
    print(f'bro last time i checked y = {slope1}x + {y_intercept1} and y = {slope2}x + {y_intercept2} isnt a system')