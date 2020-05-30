from fpdf import FPDF
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=13)

f=open("my","r")
for x in f:
    pdf.cell(200,10,txt=x,ln=1,align='c')
pdf.output("nishan.pdf")
