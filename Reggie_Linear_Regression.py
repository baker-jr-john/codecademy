print()
print("Project: Linear Regression")
print()
print("Reggie is a mad scientist who has been hired by the local fast food joint to")
print("build their newest ball pit in the play area. As such, he is working on")
print("researching the bounciness of different balls to optimize the hole. Reggie is")
print("running an experiment on bouncy balls of various sizes, and then fitting lines")
print("to the data points he records. Reggie has heard of linear regression but needs")
print("your help to implement a linear regression in Python.")
print()
print("Linear Regression is when you have a group of points on a graph, on which you")
print("find a line that approximately resembles that group of points. A good Linear")
print("Regression algorithm minimizes the error, the distance from each end to the")
print("line. A line with the least error is the line that fits the data the best. We")
print("call this a line of best fit.")
print()
print("We will use loops, lists, and arithmetic to create a function that will find a")
print("line of best fit when given a set of data.")
print()
print("Part 1: Calculating Error")
print()
print("The line we will end up with will have a formula that looks like:")
print()
print("  y = m*x + b")
print()
print("m is the line's slope, and b is the intercept, where the line crosses the")
print("y-axis.")
print()
print("Create a function, get_y(), that takes in m, b, and x and returns what the y")
print("value would be for that x on that line!")
print()
print("def get_y(m, b, x):")
print("  y = m*x + b")
print("  return y")
def get_y(m, b, x):
  y = m*x + b
  return y
print()
print("get_y(1, 0, 7)")
print("y ==", get_y(1, 0, 7))
print()
print("get_y(5, 10, 3)")
print("y ==", get_y(5, 10, 3))
print()
print("Reggie wants to try many different m values and b values and see which line")
print("produces the least error. To calculate the error between a point and a line, he")
print("wants a function called calculate_error(), which will take in m, b, and an [x,")
print("y] point named point and return the distance between the line and the point.")
print()
print("To find the distance:")
print()
print("  1. Get the x-value from the point and store it in a variable called x_point")
print("  2. Get the y-value from the point and store it in a variable called y_point")
print("  3. Use get_y() to get the y-value that x_point would be on the line")
print("  4. Find the difference between the y from get_y and y_point")
print("  5. Return the absolute value of the distance (You can use the built-in")
print("     function abs() to do this.)")
print()
print("The distance represents the error between the line y = m*x + b and the point")
print("given.")
print()
print("def calculate_error(m, b, point):")
print("  x_point, y_point = point")
print("  y = m*x_point + b")
print("  distance = abs(y - y_point)")
print("  return distance")
def calculate_error(m, b, point):
  x_point, y_point = point
  y = m*x_point + b
  distance = abs(y - y_point)
  return distance
print()
print("Let's test this function!")
print()
print("this is a line that looks like y = x, so (3, 3) should lie on it. thus, error")
print("should be 0:")
print("calculate_error(1, 0, (3, 3))")
print("distance ==", calculate_error(1, 0, (3, 3)))
print("the point (3, 4) should be 1 unit away from the line y = x:")
print("calculate_error(1, 0, (3, 4))")
print("distance ==", calculate_error(1, 0, (3, 4)))
print("the point (3, 3) should be 1 unit away from the line y = x - 1:")
print("calculate_error(1, -1, (3, 3))")
print("distance ==", calculate_error(1, -1, (3, 3)))
print("the point (3, 3) should be 5 units away from the line y = -x + 1:")
print("calculate_error(-1, 1, (3, 3))")
print("distance ==", calculate_error(-1, 1, (3, 3)))
print()
print("Great! Reggie's datasets will be sets of points. For example, he ran an")
print("experiment comparing the width of bouncy balls to how high they bounce:")
print()
print("datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]")
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
print()
print("The first data point, (1, 2), means that his 1cm bouncy ball bounced 2 meters.")
print("The 4cm bouncy ball bounced 4 meters.")
print()
print("As we try to fit a line to this data, we will need a function called")
print("calculate_all_error, which takes m and b that describe a line, and points, a set")
print("of data like the example above.")
print()
print("calculate_all_error should iterate through each point in points and calculate")
print("the error from that point to the line (using calculate_error). It should keep a")
print("running total of the error, and then return that total after the loop.")
print()
print("def calculate_all_error(m, b, points):")
print("    total_error = 0")
print("    for point in datapoints:")
print("        point_error = calculate_error(m, b, point)")
print("        total_error += point_error")
print("    return total_error")
def calculate_all_error(m, b, points):
    total_error = 0
    for point in datapoints:
        point_error = calculate_error(m, b, point)
        total_error += point_error
    return total_error
print()
print("Let's test this function!")
print()
print("every point in this dataset lies upon y=x, so the total error should be zero:")
print("datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]")
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print("calculate_all_error(1, 0, datapoints)")
print("total_error ==", calculate_all_error(1, 0, datapoints))
print()
print("every point in this dataset is 1 unit away from y = x + 1, so the total error")
print("should be 4:")
print("datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]")
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print("total_error ==", calculate_all_error(1, 1, datapoints))
print()
print("every point in this dataset is 1 unit away from y = x - 1, so the total error")
print("should be 4:")
"datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]"
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print("calculate_all_error(1, -1, datapoints)")
print("total error ==", calculate_all_error(1, -1, datapoints))
print()
print("the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1,")
print("respectively, so total error should be 1 + 5 + 9 + 3 = 18")
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print("datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]")
print("calculate_all_error(-1, 1, datapoints))")
print("total error ==", calculate_all_error(-1, 1, datapoints))
print()
print("Great! It looks like we now have a function that can take in a line and Reggie's")
print("data and return how much error that line produces when we try to fit it to the")
print("data.")
print()
print("Our next step is to find the m and b that minimizes this error, and thus fits")
print("the data best!")
print()
print("Part 2: Try a bunch of slopes and intercepts!")
print()
print("The way Reggie wants to find a line of best fit is by trial and error. He wants")
print("to try a bunch of different slopes (m values) and a bunch of different")
print("intercepts (b values) and see which one produces the smallest error value for")
print("his dataset.")
print()
print("Using a list comprehension, let's create a list of possible m values to try.")
print("Make the list possible_ms that goes from -10 to 10 inclusive, in increments of")
print("0.1.")
print()
print("Hint: you can go through the values in the range(-100, 100) and multiply each")
print("one by 0.1")
print()
print("possible_ms = [m * 0.1 for m in range(-100, 101)]")
possible_ms = [m * 0.1 for m in range(-100, 101)]
print()
print("Now, let's make a list of possible_bs to check that would be the values from -20")
print("to 20 inclusive, in steps of 0.1:")
print()
print("possible_bs = [b * 0.1 for b in range(-200, 201)]")
possible_bs = [b * 0.1 for b in range(-200, 201)]
print()
print("We are going to find the smallest error. First, we will make every possible y")
print("= m*x + b line by pairing all of the likely ms with all possible bs. We will")
print("then see which y = m*x + b line produces the smallest total error with the data")
print("stored in the datapoint.")
print()
print("First, create the variables that we will be optimizing:")
print()
print("  • smallest_error — this should start at infinity (float(inf)) so that any")
print("    error we get at first will be smaller than our value of smallest_error")
print("  • best_m — we can begin this at 0")
print("  • best_b — we can start this at 0")
print()
print("We want to:")
print()
print("  • Iterate through each element m in possible_ms")
print("  • For every m value, take every b value in possible_bs")
print("  • If the value returned from calculate_all_error on this m value, this b value")
print("    and data points are less than our current smallest_error.")
print("  • Set best_m and best_b to be these values, and set smallest_error to this")
print("    error.")
print()
print("By the end of these nested loops, the smallest_error should hold the smallest")
print("error we have found, and best_m and best_b should be the values that produced")
print("that smallest error value.")
print()
print("Print out best_m, best_b, and smallest_error after the loops.")
print()
print("datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]")
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
print("smallest_error = float(\"inf\")")
print("best_m = 0")
print("best_b = 0")
print()
print("for m in possible_ms:")
print("    for b in possible_bs:")
print("     error = calculate_all_error(m, b, datapoints)")
print("     if error < smallest_error:")
print("         best_m = m")
print("         best_b = b")
print("         smallest_error = error")
smallest_error = float("inf")
best_m = 0
best_b = 0
print()
for m in possible_ms:
    for b in possible_bs:
     error = calculate_all_error(m, b, datapoints)
     if error < smallest_error:
         best_m = m
         best_b = b
         smallest_error = error
print("best m ==", best_m,)
print("best b ==", best_b)
print("smallest error ==", smallest_error)
print()
print("Part 3: What does our model predict?")
print()
print("The line that fits the data best has an m of 0.3 and a b of 1.7:")
print()
print("  y = 0.3x + 1.7")
print()
print("This line produced a total error of 5.")
print()
print("Using this m and this b, what does your line predict the bounce height of a ball")
print("with a width of 6 to be? In other words, what is the output of get_y() when we")
print("call it with:")
print()
print("  • m = 0.3")
print("  • b = 1.7")
print("  • x = 6")
print()
print("get_y(0.3, 1.7, 6)")
print("y = ", get_y(0.3, 1.7, 6))
print()
print("Our model predicts that the 6cm ball will bounce 3.5m.")
print()
print("Reggie can now use this model to predict the bounce of all kinds of sizes of")
print("balls he may choose to include in the ball pit!")
print()