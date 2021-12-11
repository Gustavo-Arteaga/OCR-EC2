class JsonProccessing:
    def __init__(self):
        pass

    def run(self, result):
        
        elec_param_motor = {
            'HP': '',
            'Voltage': '',
            'amperage': '',
            'powerfactor': '',
            'efficiency': '',
            'servicefactor': '',
            'rpm': '',
            'HZ': '',
            'phases': ''
            }
        
        gral_param_motor = {
            'insulationclass': '',
            'manufacturer': '',
            'serialnumber': '',
            'enclousure': '',
            'modelnumber': '',
            'CAT': '',
            'Weight': '',
            'DATE': '',
            'temperature': '',
            'frame': '',
            'duty': ''
        
        }

        i=0
        words={}
        for word in result["words"]:
            if (word["word_text"] != "|"):
                words[i]=word["word_text"]
                i+=1
        print (words)
        print(len(words))
        j=0
        hz_count = 0
        insulation_count = 0
        frame_count = 0
        volt_count = 0
        for position in words:
            #Electric parameters
            if (words[j] == "HP") or (words[j] == "Power") or (words[j] == "KW") or (words[j] =="KW(HP-cv)") or (words[j] == "H.P.") or (words[j] == "HP:") or (words[j] =="HP/KW") or (words[j] == "HP."):
                value_HP = words[j+1]
                print("HP: "+value_HP)
                elec_param_motor["HP"] = value_HP

            elif (words[j][-2:] == "HP"):
                value_HP = words[j][0:-2]
                print("HP: "+value_HP)
                elec_param_motor["HP"] = value_HP

            elif (words[j] == "VOLT") or (words[j] == "V" ) or (words[j] == "VOLTS") or (words[j] == "VOLT") or (words[j] == "V.") or (words[j] == "VOLTS.") or (words[j].lower() =="volts:"):
                value_Voltage = words[j+1]
                print("Voltage: "+value_Voltage)
                elec_param_motor["Voltage"] = value_Voltage
            
            elif (words[j][-1] == "V"): 
                if volt_count == 0:
                    value_Voltage = words[j][0:-1]
                    print("Voltage: "+value_Voltage)
                    elec_param_motor["Voltage"] = value_Voltage
                    volt_count += 1
        
            elif (words[j] == "AMP") or (words[j].lower() == "amps") or (words[j] == "Current") or (words[j] =="A.")or (words[j] == "AMPS") or (words[j] == "A:") or (words[j] == "ELAMP") or (words[j].lower() == "amps:"):
                value_amperage = words[j+1]
                print("Amperage: "+value_amperage)
                elec_param_motor["amperage"] = value_amperage
        
            elif (words[j] == "FP") or (words[j] == "Cosα")or (words[j] =="F.P.") or (words[j] == "F.P.P.F.")or (words[j] == "F.P.")or (words[j] == "cosφ") or (words[j] =="P.F.") or (words[j] =="PF")or (words[j] =="P.F")or (words[j] =="PF.") or (words[j] =="P.F.:") or (words[j] =="P.F.."):
                value_powerfactor = words[j+1]
                print("powerfactor: "+value_powerfactor)
                elec_param_motor["powerfactor"] = value_powerfactor
        
            elif (words[j] == "EF") or (words[j] == "EFF") or (words[j] == "EFF%")or (words[j] =="REN(%)")or (words[j] =="REN(%) NOM.EFF.") or (words[j].lower() =="eff.") or (words[j].lower() =="eff:") or (words[j] =="NOM. EFF.") or (words[j] == "NEMA NOM.EFF."):
                value_efficiency = words[j+1]
                print("efficiency: "+value_efficiency)
                elec_param_motor["efficiency"] = value_efficiency
        
            elif (words[j] == "S.F") or (words[j] == "SF") or (words[j] == "Serv") or (words[j] =="FS SF") or (words[j] =="S.F.") or (words[j] =="SER.F.") or (words[j] =="SER.FACT.") or (words[j] =="F.") or (words[j] == "IS.F.") or (words[j] == "SF:"):
                value_servicefactor = words[j+1]
                print("servicefactor: "+value_servicefactor)
                elec_param_motor["servicefactor"] = value_servicefactor
        
            elif (words[j] == "RPM") or (words[j] == "RPM:") or (words[j] == "Vel") or (words[j] == "r/min") or (words[j] == "speed") or (words[j] == "R.P.M.") or (words[j] == "RPM min-1") or (words[j] =="min-1"):
                value_rpm = words[j+1]
                print("rpm: "+value_rpm)
                elec_param_motor["rpm"] = value_rpm
        
            elif (words[j] == "HZ") or (words[j] == "Hz") or (words[j] == "FREQ") or (words[j] == "Frequency") or (words[j] =="hz.") or (words[j].lower() == "hz:") or (words[j].lower() == "hertz"):
                if hz_count == 0:
                    value_hz = words[j+1]
                    print("Hz:"+value_hz)
                    elec_param_motor["HZ"] = value_hz
                    hz_count += 1
        
            elif (words[j] == "PH") or (words[j] == "phases") or (words[j] =="~") or (words[j] =="phase") or (words[j] =="PH.") or (words[j] =="P.H.") or (words[j] =="PHASE") or (words[j] =="AC"):
                try:
                    value_phases = int(words[j+1])
                    value_phases = str(value_phases)
                except:
                    value_phases = words[j-1]
                print("phases: "+value_phases)
                elec_param_motor["phases"] = value_phases
        
            #General parameters
            elif (words[j] == "CLASS") or (words[j] == "INS.CL") or (words[j] == "CL") or (words[j] == "INS.CL,") or (words[j] == "AISL.CL") or (words[j] == "IS.CL") or (words[j] == "ISOL.CL.") or (words[j] == "AISL. CLASE") or (words[j] =="ISOL INSL") or (words[j] =="CLASS INSUL:") or (words[j] =="INS.") or (words[j] =="CLASS.") or (words[j] =="INS") or (words[j] =="Ins:"):
                if insulation_count == 0:
                    value_insulationclass = ''
                    if len(words[j+1]) > 1:
                        if (words[j+2] == 'A') or (words[j+2] == 'B') or (words[j+2] == 'F') or (words[j+2] == 'H'):  
                            value_insulationclass = words[j+2]
                    else:
                        if (words[j+1] == 'A') or (words[j+1] == 'B') or (words[j+1] == 'F') or (words[j+1] == 'H'): 
                            value_insulationclass = words[j+1]
                    gral_param_motor["insulationclass"] = value_insulationclass
                    insulation_count += 1
        
            elif (words[j] == "LESSON") or (words[j] == "SIEMENS") or (words[j] == "WEG") or (words[j] == "Westinghouse") or (words[j] == "TOSHIBA") or (words[j] == "BALDOR") or (words[j] == "Crown") or (words[j] == "INDUSTRIAL"):
                value_manufacturer = words[j]
                print("manufacturer: "+value_manufacturer)
                gral_param_motor["manufacturer"] = value_manufacturer
        
            elif (words[j] == "SER") or (words[j] == "serial") or (words[j] == "SERIAL Nr:") or (words[j] == "SER. NO.") or (words[j] == "SERIAL NO:") or (words[j] == "SN") or (words[j] == "SER.") or (words[j] == "SN:"):
                value_serialnumber = ''
                if (words[j+1] == "NO") or (words[j+1] == "NO."):
                    value_serialnumber = words[j+2] + words[j+3]
                else:
                    value_serialnumber = words[j+1]
                print("serialnumber: "+value_serialnumber)
                gral_param_motor["serialnumber"] = value_serialnumber
        
            #elif (words[j] == "ENCL.") or (words[j] == "ENCLO") or (words[j] =="IP:") or (words[j] == "IP") or (words[j] == "ENCL.") or (words[j] == "IP."):
            #    value_enclousure = words[j+1]
            #    print("enclousure: "+value_enclousure)
            #    gral_param_motor["enclousure"] = value_enclousure
            
            elif (words[j] == "TEFC") or (words[j][-4:] == "TEFC"):
                value_enclousure = words[j]
                print("enclousure: "+value_enclousure)
                gral_param_motor["enclousure"] = value_enclousure
        
            elif (words[j] == "MOD") or (words[j].lower() == "model") or (words[j] == "MODEL. NO.") or (words[j] == "MODEL.") or (words[j].lower() == "model:") or (words[j] == "SPEC.") or (words[j] == "SPEC..") or (words[j] == "SPEC"):
                value_modelnumber = ''
                if (words[j+1] == "NO") or (words[j+1] == "NO."):
                    value_modelnumber = words[j+2]
                else:
                    value_modelnumber = words[j+1]
                print("modelnumber: "+value_modelnumber)
                gral_param_motor["modelnumber"] = value_modelnumber
        
            elif (words[j] == "CAT") or (words[j] == "categ") or (words[j] == "CAT. NO.") or (words[j] == "CAT.") or (words[j] == "CAT.NO.") or (words[j] == "Cat.") or (words[j] == "Cat"):
                value_cat = ''
                if (words[j+1] == "NO") or (words[j+1] == "NO.") or (words[j+1] == "No") or (words[j+1] == "No."):
                    value_cat = words[j+2]
                else:
                    value_cat = words[j+1]
                print("CAT: "+value_cat)
                gral_param_motor["CAT"] = value_cat
        
            elif (words[j] == "Kg") or (words[j] == "WT:") or (words[j].lower() == "weight") or (words[j] == "Kg.") or (words[j] == "net:") or (words[j] == "net") or (words[j] == "WT.") or (words[j] == "Lbs"):
                value_weight = words[j+1]
                print("Weight: "+value_weight)
                gral_param_motor["Weight"] = value_weight
        
            elif (words[j].lower() == "date") or (words[j].lower() == "date:"):
                value_date = words[j+1]
                print("DATE: "+value_date)
                gral_param_motor["DATE"] = value_date
        
            #elif (words[j] == "temp") or (words[j] == "AMB") or (words[j] == "AMB:") or (words[j] == "AMB.") or (words[j] == "MAX. AMB.") or (words[j] == "RATING") or (words[j] == "RATING."):
            #    value_temperature = words[j+1]
            #    print("temperature: "+value_temperature)
            #    gral_param_motor["temperature"] = value_temperature
        
            elif (words[j] == '40C') or (words[j][0:2] == '40') or (words[j][-3:] == '40C') :
                value_temperature = words[j]
                print("temperature: "+value_temperature)
                gral_param_motor["temperature"] = value_temperature

            elif (words[j].lower() == "frame") or (words[j].lower() == "frame.") or (words[j] == "CARC. FRAME.") or (words[j] == "FR:") or (words[j] == "FR"):
                if frame_count == 0:
                    value_frame = words[j+1]
                    print("frame: "+value_frame)
                    gral_param_motor["frame"] = value_frame
                    frame_count += 1
        
            #elif (words[j] == "SER") or (words[j] == "DUTY") or (words[j] == "DUTY.") or (words[j] == "REG") or (words[j] == "DUTY:") or (words[j] == "RATING"):
            #    value_duty = words[j+1]
            #    print("duty: "+value_duty)
            #    gral_param_motor["duty"] = value_duty 
            elif (words[j] == "CONT") or (words[j] == "CONT.") or (words[j] == "AMB-CONT") or (words[j] == "AMB-CONT.") or (words[j] == "S1"):
                value_duty = words[j]
                print("duty: "+value_duty)
                gral_param_motor["duty"] = value_duty        
            j+=1
        
        #-----------------------end json proccessing  
        return elec_param_motor, gral_param_motor
    
    