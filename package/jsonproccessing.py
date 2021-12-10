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
            words[i]=word["word_text"]
            i+=1
        
        j=0
        for position in words:
            #Electric parameters
            if (words[j] == "HP") or (words[j] == "Power") or (words[j] == "KW") or (words[j] =="KW(HP-cv)") or (words[j] == "H.P.") or (words[j] == "HP:") or (words[j] =="HP/KW") or (words[j] == "HP."):
                value_HP = words[j+1]
                print("HP: "+value_HP)
                elec_param_motor["HP"] = value_HP
            elif (words[j] == "VOLT") or (words[j] == "V" ) or (words[j] == "VOLTS") or (words[j] == "VOLT") or (words[j] == "V.") or (words[j] == "VOLTS.") or (words[j] =="VOLTS:"):
                value_Voltage = words[j+1]
                print("Voltage: "+value_Voltage)
                elec_param_motor["Voltage"] = value_Voltage
        
            elif (words[j] == "A") or (words[j] == "AMP") or (words[j] == "Amps") or (words[j] == "Current") or (words[j] =="A.")or (words[j] == "AMPS") or (words[j] == "A:") or (words[j] == "ELAMP"):
                value_amperage = words[j+1]
                print("Amperage: "+value_amperage)
                elec_param_motor["amperage"] = value_amperage
        
            elif (words[j] == "FP") or (words[j] == "Cosα")or (words[j] =="F.P.") or (words[j] == "F.P.P.F.")or (words[j] == "F.P.")or (words[j] == "cosφ") or (words[j] =="P.F."):
                value_powerfactor = words[j+1]
                print("powerfactor: "+value_powerfactor)
                elec_param_motor["powerfactor"] = value_powerfactor
        
            elif (words[j] == "EF") or (words[j] == "EFF") or (words[j] == "EFF%")or (words[j] =="REN(%)")or (words[j] =="REN(%) NOM.EFF.")or (words[j] =="EFF.")or (words[j] =="NOM. EFF.") or (words[j] == "NEMA NOM.EFF."):
                value_efficiency = words[j+1]
                print("efficiency: "+value_efficiency)
                elec_param_motor["efficiency"] = value_efficiency
        
            elif (words[j] == "S.F") or (words[j] == "SF") or (words[j] == "Serv") or (words[j] =="FS SF") or (words[j] =="S.F.") or (words[j] =="SER.F.") or (words[j] =="SER.FACT."):
                value_servicefactor = words[j+1]
                print("servicefactor: "+value_servicefactor)
                elec_param_motor["servicefactor"] = value_servicefactor
        
            elif (words[j] == "RPM") or (words[j] == "Vel") or (words[j] == "r/min") or (words[j] == "speed") or (words[j] == "R.P.M.") or (words[j] == "RPM min-1") or (words[j] =="min-1"):
                value_rpm = words[j+1]
                print("rpm: "+value_rpm)
                elec_param_motor["rpm"] = value_rpm
        
            elif (words[j] == "HZ") or (words[j] == "Hz") or (words[j] == "FREQ") or (words[j] == "F") or (words[j] == "Frequency") or (words[j] =="hz.") or (words[j] == "hz:"):
                value_hz = words[j+1]
                print("Hz:"+value_hz)
                elec_param_motor["HZ"] = value_hz
        
            elif (words[j] == "PH") or (words[j] == "phases") or (words[j] =="~") or (words[j] =="phase") or (words[j] =="PH.") or (words[j] =="P.H."):
                value_phases = words[j+1]
                print("phases: "+value_phases)
                elec_param_motor["phases"] = value_phases
        
            #General parameters
            elif (words[j] == "CLASS") or (words[j] == "INS.CL") or (words[j] == "CL") or (words[j] == "INS.CL,") or (words[j] == "AISL.CL") or (words[j] == "IS.CL") or (words[j] == "ISOL.CL.") or (words[j] == "AISL. CLASE") or (words[j] =="ISOL INSL") or (words[j] =="CLASS INSUL:") or (words[j] =="INS.") or (words[j] =="CLASS."):
                value_insulationclass = words[j+1]
                print("insulationclass: "+value_insulationclass)
                gral_param_motor["insulationclass"] = value_insulationclass
        
            elif (words[j] == "LESSON") or (words[j] == "SIEMENS") or (words[j] == "WEG") or (words[j] == "Westinghouse") or (words[j] == "TOSHIBA") or (words[j] == "BALDOR"):
                value_manufacturer = words[j+1]
                print("manufacturer: "+value_manufacturer)
                gral_param_motor["manufacturer"] = value_manufacturer
        
            elif (words[j] == "SER") or (words[j] == "serial") or (words[j] == "SERIAL Nr:") or (words[j] == "SER. NO.") or (words[j] == "SERIAL NO:") or (words[j] == "SN"):
                value_serialnumber = words[j+1]
                print("serialnumber: "+value_serialnumber)
                gral_param_motor["serialnumber"] = value_serialnumber
        
            elif (words[j] == "CODE") or (words[j] == "ENCLO") or (words[j] =="IP:") or (words[j] == "IP") or (words[j] == "ENCL.") or (words[j] == "IP."):
                value_enclousure = words[j+1]
                print("enclousure: "+value_enclousure)
                gral_param_motor["enclousure"] = value_enclousure
        
            elif (words[j] == "MOD") or (words[j] == "model") or (words[j] == "MODEL. NO.") or (words[j] == "MODEL."):
                value_modelnumber = words[j+1]
                print("modelnumber: "+value_modelnumber)
                gral_param_motor["modelnumber"] = value_modelnumber
        
            elif (words[j] == "CAT") or (words[j] == "categ") or (words[j] == "CAT. NO."):
                value_cat = words[j+1]
                print("CAT: "+value_cat)
                gral_param_motor["CAT"] = value_cat
        
            elif (words[j] == "Kg") or (words[j] == "Weigth") or (words[j] == "Kg.") or (words[j] == "net:") or (words[j] == "net") or (words[j] == "WT.") or (words[j] == "Lbs"):
                value_weight = words[j+1]
                print("Weight: "+value_weight)
                gral_param_motor["Weight"] = value_weight
        
            elif (words[j] == "DATE") or (words[j] == "date"):
                value_date = words[j+1]
                print("DATE: "+value_date)
                gral_param_motor["DATE"] = value_date
        
            elif (words[j] == "CONT") or (words[j] == "temp") or (words[j] == "AMB") or (words[j] == "AMB:") or (words[j] == "AMB.") or (words[j] == "MAX. AMB.") or (words[j] == "RATING") or (words[j] == "RATING."):
                value_temperature = words[j+1]
                print("temperature: "+value_temperature)
                gral_param_motor["temperature"] = value_temperature
        
            elif (words[j] == "TYPE") or (words[j] == "frame") or (words[j] == "FRAME.") or (words[j] == "CARC. FRAME."):
                value_frame = words[j+1]
                print("frame: "+value_frame)
                gral_param_motor["frame"] = value_frame
        
            elif (words[j] == "SER") or (words[j] == "DUTY") or (words[j] == "DUTY.") or (words[j] == "REG") or (words[j] == "DUTY:"):
                value_duty = words[j+1]
                print("duty: "+value_duty)
                gral_param_motor["duty"] = value_duty        
            j+=1
        #-----------------------end json proccessing  
        return elec_param_motor, gral_param_motor
    
    