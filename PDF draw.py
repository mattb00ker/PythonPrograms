from reportlab.graphics.spapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)
s = String(50, 50, 'Hello world!', textAnchor = 'middle')

d.add(s)

renderPDF.drawToFile(d, 'Hello.pdf', 'A simple PDF file')
