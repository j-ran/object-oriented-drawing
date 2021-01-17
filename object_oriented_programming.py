"""note: ran this on repl.it"""

import cs1graphics as cg 
paper = cg.Canvas()
paper.setBackgroundColor('skyBlue')
paper.setWidth(800)
paper.setHeight(600)

sun = cg.Circle()
paper.add(sun)

sun.setFillColor('steelBlue')
sun.setRadius(350)
sun.moveTo(200, 300)

sun2 = cg.Circle(50, cg.Point(700,100))
sun2.setFillColor('lightYellow')
paper.add(sun2)



facade = cg.Square(200, cg.Point(400, 350))
facade.setFillColor('white')
paper.add(facade)

chimney = cg.Rectangle(50, 70, cg.Point(450, 215))
chimney.setFillColor('red')
paper.add(chimney)

tree = cg.Polygon(cg.Point(150, 220),
                   cg.Point(120, 380),
                   cg.Point(180, 380))
tree.setFillColor('darkGreen')
paper.add(tree)


sunraySW = cg.Path(cg.Point(660, 140), cg.Point(635, 165))
sunraySW.setBorderColor('blueViolet')
sunraySW.setBorderWidth(6)
paper.add(sunraySW)

sunraySE = cg.Path(cg.Point(740, 140), cg.Point(765, 165))
sunraySE.setBorderColor('yellow')
sunraySE.setBorderWidth(6)
paper.add(sunraySE)

sunrayNE = cg.Path(cg.Point(740, 60), cg.Point(765, 35))
sunrayNE.setBorderColor('blueViolet')
sunrayNE.setBorderWidth(6)
paper.add(sunrayNE)

sunrayNW = cg.Path(cg.Point(660, 60), cg.Point(635, 35))
sunrayNW.setBorderColor('yellow')
sunrayNW.setBorderWidth(6)
paper.add(sunrayNW)

grass = cg.Rectangle(800, 300, cg.Point(400, 450))
grass.setFillColor('green')
grass.setBorderColor('green')
# must be behind house and tree
grass.setDepth(75) 
paper.add(grass)

#roof = cg.Polygon()

# . . .
# some extra code:
# sun = cg.Circle()
# sun.setFillColor('steelBlue')
# sun.setRadius(200)
# sun.moveTo(250, 300)
# sun.setDepth(65)
# #paper.add(sun)

# sun2 = cg.Circle(50, cg.Point(700,100))
# sun2.setFillColor('lightYellow')
# #paper.add(sun2)

# sun, sun2 as suns
# paper.add(suns)