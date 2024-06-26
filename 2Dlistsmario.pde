# Example: 2D List
def setup():
    size(16,16)
    nRows = height
    nCols = width
    myList = [[255, 255, 255, 255, 255, 150, 150, 150, 150, 150, 255, 255, 255, 255, 255, 255],
              [255, 255, 255, 255, 150, 150, 150, 150, 150, 150, 150, 150, 150, 255, 255, 255],
              [255, 255, 255, 255, 001, 001, 001, 225, 225, 001, 225, 255, 255, 255, 255, 255],
              [255, 255, 255, 001, 225, 001, 225, 225, 225, 001, 225, 225, 225, 255, 255, 255],
              [255, 255, 255, 001, 225, 001, 001, 225, 225, 225, 001, 225, 225, 225, 255, 255],
              [255, 255, 255, 001, 001, 225, 225, 225, 225, 001, 001, 001, 001, 255, 255, 255],
              [255, 255, 255, 255, 255, 225, 225, 225, 225, 225, 225, 225, 255, 255, 255, 255],
              [255, 255, 255, 255, 150, 150, 80, 150, 150, 80, 150, 255, 255, 255, 255, 255],
              [255, 255, 255, 150, 150, 150, 80, 150, 150, 80, 150, 150, 150, 255, 255, 255],
              [255, 255, 150, 150, 150, 150, 80, 150, 150, 80, 150, 150, 150, 150, 255, 255],
              [255, 255, 225, 225, 150, 80, 255, 80, 80, 255, 80, 150, 225, 225, 255, 255],
              [255, 255, 225, 225, 225, 80, 80, 80, 80, 80, 80, 225, 225, 225, 255, 255],
              [255, 255, 225, 225, 80, 80, 80, 80, 80, 80, 80, 80, 225, 225, 255, 255],
              [255, 255, 255, 255, 80, 80, 80, 255, 255, 80, 80, 80, 255, 255, 255, 255],
              [255, 255, 255, 001, 001, 001, 255, 255, 255, 255, 001, 001, 001, 255, 255, 255],
              [255, 255, 001, 001, 001, 001, 255, 255, 255, 255, 001, 001, 001, 001, 255, 255]]
    
    print(myList)
    drawPoints(myList)
    


def drawPoints(pointList):
    for y in xrange(len(pointList)):
        for x in xrange(len(pointList[0])):
            stroke(pointList[y][x])
            rect(x,y,10,10)