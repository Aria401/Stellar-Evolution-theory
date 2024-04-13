#ui.createLabel({text:"1",row:0,column:0,}),
#ui.createLabel({text:element_symbols[1],row:0,column:1,}),
#ui.createLabel({text:element_names[1],row:0,column:2,}),
#ui.createLabel({text:"Practically Infinite",row:0,column:3,})
out = ""
for i in range(1,119):
    #out += str(i)
    #out += "\",row:"
    #out += str(i-1)
    #out += ",column:0,}),ui.createLabel({text:element_symbols["
    #out += str(i)
    #out += "],row:"
    #out += str(i-1)
    #out += ",column:1,}),ui.createLabel({text:element_names["
    #out += str(i)
    #out += "],row:"
    #out += str(i-1)
    #out += ",column:2,}),ui.createLabel({text:()=> {try{return element_amount["
    #out += str(i)
    #out += "].value.toString()+\"kg\"}catch{return \"\"}},row:"
    #out += str(i-1)
    #out += ",column:3,}),"
    out+="createElementButton("+str(i)+"),\n"
print(out)


