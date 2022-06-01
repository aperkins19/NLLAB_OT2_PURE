move_file = True
using_standard_curve = False
save_figures = True



# experiment specific parameters

chromatics_designations = {
'635_680_1': '3000',
'485_520_2': '800',
'485_520_3': '1500',
}

metadata = {
'Reaction Temperature (°C)': '30',
'Performed by':'Alex Perkins',
'Instrument':'BMG POLARstar Omega',
'Experiment #':'8'

}




triplicate = 2
number_of_chromatics_measured = 3

# well designation
well_designation = {


'C03' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'8',
'K_Glutamate_mM': '20',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},


'C06' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'8',
'K_Glutamate_mM': '20',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

'C09' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'8',
'K_Glutamate_mM': '30',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},

'C12' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'8',
'K_Glutamate_mM': '30',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

'C15' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'8',
'K_Glutamate_mM': '40',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},

'C18' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'8',
'K_Glutamate_mM': '40',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

##########################################################################################################


'F03' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'9',
'K_Glutamate_mM': '20',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},


'F06' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'9',
'K_Glutamate_mM': '20',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

'F09' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'9',
'K_Glutamate_mM': '30',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},

'F12' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'9',
'K_Glutamate_mM': '30',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

'F15' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'9',
'K_Glutamate_mM': '40',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},

'F18' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'9',
'K_Glutamate_mM': '40',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

#######################################################################################

'I03' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'10',
'K_Glutamate_mM': '20',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},


'I06' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'10',
'K_Glutamate_mM': '20',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

'I09' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'10',
'K_Glutamate_mM': '30',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},

'I12' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'10',
'K_Glutamate_mM': '30',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

'I15' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'10',
'K_Glutamate_mM': '40',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},

'I18' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'10',
'K_Glutamate_mM': '40',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

#####################################################################################################


'L03' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'11',
'K_Glutamate_mM': '20',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},


'L06' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'11',
'K_Glutamate_mM': '20',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

'L09' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'11',
'K_Glutamate_mM': '30',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},

'L12' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'11',
'K_Glutamate_mM': '30',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

'L15' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'11',
'K_Glutamate_mM': '40',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},

'L18' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'11',
'K_Glutamate_mM': '40',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

#################################################################


'O03' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'11.8',
'K_Glutamate_mM': '100',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 1
},


'O06' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'11.8',
'K_Glutamate_mM': '100',
'Amplicon DNA Template': 'T7_GFP_MGA',
'Replicate': 2
},

####################################################

'O09' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'11.8',
'K_Glutamate_mM': '100',
'Amplicon DNA Template': 'No Template',
'Replicate': 1
},

'O12' : {
'Reaction Type': 'TXTL',
'System':'OnePotPure B2',
'Energy Solution':'Grassman ES',
'Mg_Acetate_mM':'11.8',
'K_Glutamate_mM': '100',
'Amplicon DNA Template': 'No Template',
'Replicate': 2
},

#########################################################

'O15' : {
'Reaction Type': 'Blank',
'System':'NA',
'Amplicon DNA Template': 'None',
'Replicate': 1
},

'O18' : {
'Reaction Type': 'Blank',
'System':'NA',
'Amplicon DNA Template': 'None',
'Replicate': 2
},



}




## don't touch these parameters. They are standardised across the platereader data

metadataheader = 2
gap = 3
