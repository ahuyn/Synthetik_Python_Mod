#gui with tkinter
from ctypes.wintypes import WORD
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import filedialog
import getpass
import re
import os
from tkinter import messagebox
from typing import Text

#Turn safety to 1 so we can see what happens to the TEMPORARYSAVE
#uwu is gone. the uwu purge is complete.
# all global variables will be put up here
safety = 0
WI = "i"
Loadout = ["9","7","6","5","4","3","0"]
ITokIdents = ["ibonus","iplus","iminus"]
WTokIdents = ["wbonus","wplus","wminus"]
# $savefile currentclass is one of the things that could be used in a local save file for the mod.
Currentclass = "10"
items = []
#since the modules/pistols wont ever change, I just made it permanent
VarSmodules = ["obj_item130_riotguard","obj_item54_c4","obj_item132_dynamite","obj_item98_minisentry","obj_artefact_tactical","obj_artefact_instagib","obj_artefact_madness","obj_artefact_mysterybonus","obj_artefact_terrorlevel","obj_artefact_ricochet","obj_artefact_elemental","obj_artefact_friendlyfire","obj_artefact_ultradrop","obj_artefact_itemupgrade","obj_artefact_pistol","obj_artefact_buff","obj_artefact_powerup","obj_artefact_strafe","obj_artefact_crit","obj_artefact_shop","obj_artefact_healing","obj_artefact_slowdown","obj_artefact_weaponcarry","obj_perk_force","obj_perk_sunrise","obj_perk_dodgeheat","obj_perk_transmutate","obj_perk_heatcontrol","obj_perk_elementalpower","obj_perk_heatrecharge","obj_perk_itemcdvariant","obj_perk_focus","obj_perk_selfrepair","obj_perk_ammoregen","obj_perk_pistolextender","obj_perk_hframe","obj_perk_grenadier","obj_perk_heatup","obj_perk_statusextender","obj_perk_engineer","obj_perk_demolisher","obj_item110_spider","obj_item126_missiledrone","obj_item80_masterkey","obj_item38_grenade_toxic","obj_item71_sentry","obj_item101_resonator","obj_perk_drill","obj_perk_killer","obj_perk_cover","obj_perk_scarred","obj_perk_combo","obj_perk_holdbreath","obj_perk_wepupgrade","obj_perk_edge","obj_perk_reloadsurge","obj_perk_fieldration","obj_perk_drone1","obj_perk_specializedammo","obj_perk_powerstep","obj_perk_reloadstack","obj_perk_classweapon","obj_perk_raider","obj_perk_squadleader","obj_perk_assaultgunner","obj_perk_commando","obj_item124_gunner","obj_item86_commandoflare","obj_item123_cover","obj_item109_reloader2","obj_item55_stim","obj_item37_grenade_plasma","obj_item81_tanto","obj_perk_healthy","obj_perk_diehard","obj_perk_stealback","obj_perk_reactivereload","obj_perk_standstill","obj_perk_powertuning","obj_perk_specialized","obj_perk_perfection","obj_perk_longrange","obj_perk_discipline","obj_perk_dance","obj_perk_backstab","obj_perk_dodgeboost","obj_perk_ejectsurge","obj_perk_headshotammo","obj_perk_marksman","obj_perk_assassin","obj_item122_targetcpu","obj_item94_dagger","obj_item115_decoy","obj_item83_grenade_smoke","obj_item97_minelaser","obj_item82_flare","obj_item79_bolt","obj_item35_grenade_flash","obj_perk_reloadsurge2","obj_perk_return","obj_perk_berserk","obj_perk_scavengerbits","obj_perk_scraparmor","obj_perk_lowhpregen","obj_perk_shieldoc","obj_perk_shotgunmaster","obj_perk_enrage","obj_perk_fortify","obj_perk_killshield","obj_perk_aegis","obj_perk_closer","obj_perk_recovery","obj_perk_warmup","obj_perk_iframe","obj_perk_breacher","obj_perk_riotguard","obj_item99_battlecry","obj_item100_breachingcharge","obj_item12_reflector","obj_item33_shieldburst","obj_item121_tomahawk","obj_item69_taser","obj_item36_grenade_stun","obj_item6_reloader","obj_item64_chalice","obj_item63_cellreplacer","obj_item18_potion","obj_item8_injection","obj_item30_methadone","obj_item7_vial","obj_perk_randomperk"]
VarPistols =["obj_weapon_TEC_84","obj_weapon_SUP_67","obj_weapon_DE_94","obj_weapon_A9_55","obj_weapon_REP_11","obj_weapon_HLP_64","obj_weapon_LSP_21","obj_weapon_DE_61","obj_weapon_HON_34","obj_weapon_REV_9","obj_weapon_MC_62","obj_weapon_CP_38","obj_weapon_G17_63","obj_weapon_PXS_10","obj_weapon_PTL_6"]
#Shownmodules is going to be the more readable version of VarSmodules that will be used. I'm having Lawro#0858 make a list to use; done
ShownModules = ["Guardian", "Composite 4", "Neutrino Bomb", "Seth-Up Suitcase Sentry", "Mode: Tactical", "Mode: Hyper Adrenaline", "Mode: Madness", "Mode: Mystery Bonus", "PU-55", "Hobb-S", "Rynn", "Rhett", "Kevv", "Zion", "Luka", "Savnt", "Pure 759", "Cario", "Taro", "Aeon-FFD", "Kokova", "Mael", "Ensiferum","Force Unleashed", "Sun Rising", "Unceasing", "Transmutate", "Calculated", "Elemental Power", "Overdrive", "Well Oiled", "Focus", "Inner Fire", "Multiply", "Weapons Deal", "Chromatic Alloy", "Grenadier", "Forged By Fire", "Status Extender ", "Core: Drone Zeal", "Core: HE-Ammo", "Spider Mines", "Missile Drone", "Dragon’s Masterkey", "Acid Grenade", "LMG Sentry Turret", "Seismic Resonator","Drill", "Killer", "Take Cover", "Scarred", "Madness", "Hold Breath", "Pack A Punch", "On The Edge", "Press The Attack", "Field Rat0ons", "Drone Mod", "Specialized Ammo", "Charge", "Routine", "Weapon Drop", "Core: Looter", "Core: Squad Leader", "Core: Suppression", "Core: Commando", "Onslaught System", "Road Flare", "Hard Light Cover", "Special Ammo Supply", "Stim Pack", "Plasma Grenade", "Reverbing Blade", "Against The Odds", "Die Hard", "Blood Borne", "Keeping Cool", "Freeze!", "Power Tuning", "DMR Conversion", "Perfection", "Keeping Distance", "Discipline", "Shadow Dance", "Backstab", "Evasive Maneuvers", "Switch Position", "Head Hunter", "Core: Spotter", "Core: Professional", "Targeting Laser", "Scoundrel’s Dagger", "Decoy", "Smoke Grenade", "Laser Mine", "Flare Gun", "’Helsing’ Power Bolt", "TP Grenade Flash", "Push Forward", "Wicked", "Berserk", "Bits And Pieces", "Scrap Plating", "Stimulants", "Shield Overclock", "Weapon Mastery", "Enrage", "Fortify Position", "Shielded", "Aegis MK5 Platinum", "Into Battle", "Recovery", "Warmup", "I-Frame", "Core: Charge", "Core: Unyielding", "Battlecry Module", "Breaching Charge", "RV Rebuke System", "Shieldburst", "Tomahawk", "Auto Taser", "Stun Grenade","Field Supply", "Lifeblood", "Cell Replacer", "Unidentified Potion", "Overdose", "Methadone","Health Vial", "Random Module"]
ShownPistols = ["TEC-9.95 Personal","P25 Overdrive","Titanium Eagle","Auto 9/45","57 Fusion Classic","PPQ-H Laser Pistol","Kaida Laser Pistol","Desert Eagle .50","Kaida Model H","Last Breath","Master Chief","XM2 Coil Pistol","G17 Undercover","PXS Covert Ops","P33 Compact"]
DoubleModules = []
# Starting work on Token Frame functionality    
Tokens = []
ClassTokens = []
WeaponNumbers = range(99)
ShownWeapons = ["Null","Nemesis Prototype","Chaos Launcher","Object 29","Road Warrior","Apollon 5 LMG","P33 Compact","Tactical Observer","Mjolnir Chain LTN","Last Breath","PXS Covert Ops","57 Fusion Classic","Sour DMR","Spectre","Medic FMG-9","R5000 Sudden DMR","Vindicator Ultra","Raptor Laser SG","LS Laser Sub","Super 90","GM6 Lynx Evo","Kaida Laser Pistol","Eraser DMR","M32 Multipurpose","AMD 65","ION Obliterator","Armageddon","Enforcer Carbine","Damnnation","SS58 Plasma Charger","KI Vector","Spas 12","ML7000 Plus","M79 Terminator","Kaida Model H","FS5 Flametounge","Flak Heavy Cannon","RRX Coil Shotgun","XM2 Coil Pistol","Twin Mill Mk.2","SCR Laser Socom","AEK Special Elite","AS VAL","Battle Hymn","RPK Tundra","Ripjack","Liandry Railgun","MAG47 Heavy LMG","Kaida Nailgun","HIG-S Particle Cannon","Bren Anti-Air","X512 Experimental","Makeshift Firecannon","Ballistic CRX_Bow","420 Sniperdragon","Auto 9/45","K3 Boltcaster SMG","Human RPG","Kaida Medic ACR-X","Human Model 9800K","KSG 2000","Desert Eagle","Master Chief","G17 Undercover","PPQ-H Laser Pistol","UMP-9 Semi","Annilhilator","P25 overdrive","Yoko-Lagann","Super Shorty","W21 Lever Action","Pressurized Impaler","Gladiator","HMN Laser Cannon","AKS-74U","K98 Classic","UMP Tornado","T-8-00 Guage","Ares GL-16","Viking Riotshield","Eminince AR","A5-C Test Version","AN-94 Deathstalker","P9000 Supernova","TEC 9.95","LG2 Onslaught","Last Ditch M16","F14 Mini","Sturmgewher 44","Raider Scrap Cannon","Specialist M16-A5","Tuned M14 EBR","FMG-9 Personal","M75 Heavy Support","Titanium Eagle","PSG Emerald Sword","QBZ_Laser","Type-89 Tokko","K7 Competition","ModWeapon 0",]
ItemNumbers = range(151)
ShownItems = ["Unidentified0","Chaos Potion","Hyperfeed","Shock Impulse","Umbra Adaptive Cloak","Healing Crystal","Field Supply","Health Vial","Overdose",
"Fangs of Mordigan","Unstable Current","Divine Reconstructor","RV Rebuke System","Devil's Dice","Maddness Glasses","Refractor Crystal","Upgrade Kit",
"Orb of Iron","Unidentified Potion","Orb of Lightning","Orb of Fire","Orb of Wind","Blood Rite","Twin Link 2","Heart Core",
"Refresher","Core Upgrade Kit","Black Berserk Charm","Trophy System Drone?","Combat Amphetamine?","Methadone","Incubus","Tsunami Talisman",
"ShieldBurst","HE Grenade","Flash Grenade","Stun Grenade","Plasma Grenade","Acid Grenade","Psy Field","Heavy Steel Trap",
"PowerShot","R-Plating","Fast Sling","Facemelter","Uranium 235","Maverick MKV","Sidewinder","Fire Prism",
"Order 322","Last Stand","Stinger Jet Glider","Air Com","Power Array","Composite 4","Stim Pack","Phaser",
"Gun Drone Spawner","Heart Seeker","M205 Launcher","Target Cogitator","Rosarius","Reality Ripper","Cell Replacer","Lifeblood",
"Direct Current","Akira","Lightning Boots","Ring of Experience","Auto Taser","Blood Bolt","LMG sentry Turret","DMR Sentry Turret",
"Turret?","Module Core","Ring of Glass","Bloodthirsty Ring","Unsoldered Chip?","Ripjack Hyper Blade","'Helsing' Power Bolt","Dragon's Masterkey",
"Reverbing Blade","Flare Gun","Smoke Grenade","M26 MA Shotgun System","Kunai Throwing Knives","Road Flare","G87 Beamer","Icarus",
"Redline","Biting Throwing Stars","Z1 Sundering Shuriken","Fan of Knives","Infinity Drill Piece","Scoundrel's Dagger","ZR99 'Living Bomb'","ZK77 'Sticky Bomb'",
"Laser Mine","'Seth-Up' Suitcase Sentry","Battlecry Module","Breaching Charge","Seismic Resonator","Air Horn","Brawndo","Eclipse",
"Stun Mine (Null)","Acid Mine (Null)","Magic Mag","Auto-Overclocker","Special Ammo Supply","Spider Mines","Heat Sink","Black Market Teleporter",
"Maddness Button","Heat Spreader","Decoy","Shielded Decoy","GPS","Gold Nugget","Custom Upgrade Kit","Metal Detector",
"Tomahawk","Targeting Laser","Hard Light Cover","Onslaught System","Intensity Chamber","Missile Drone","Constructor?","Remove Building?",
"Research?","Guardian","High Command","Neutrino Bomb","Magnum","Bandana","Orbital Relay","Missile Control",
"Trapper's Teleporter","ShieldLink","Underbarrel Mod Chip","Shaker","Elemental Resonance","Fire Water","Energy Link","Nitroglycerine",
"Stun Mine","Acid Mine","Armageddon Shard","Orb of Fusion","Crux of the Laser Caster","PSY Cloud Grenade"]
CurTokShown = ShownWeapons
WeaponSpawnIds = []
ItemSpawnIds = []
username = getpass.getuser()
filename = "C:/Users/"+username+"/AppData/Local/Synthetik/Save.sav"
tfilename = "C:/Users/"+username+"/AppData/Local/Synthetik/TEMPORARYSAVE.txt"

def browse_files(save_filename, temp_save_filename):
    filepath = save_filename.rsplit("/",1)[0]
    new_save_filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("Save files","*.sav*"),("All files","*.*")))
    if new_save_filename:
        save_filename = new_save_filename
        filepath = save_filename.rsplit("/",1)[0]
        temp_save_filename = filepath +"/TEMPORARYSAVE.txt"
    print(filepath[0])

    return save_filename, temp_save_filename

if not os.path.exists(filename):
    messagebox.showinfo('Synthetik','Sorry, your save file is not where I thought it would be! Could you please find it for me?')
    filename, tfilename = browse_files(filename, tfilename)

# setup main tkinter window name and frame. Configure frame to fill white space and for widgets to expand to fill space
root = tk.Tk()
root.title("Synthetik Loadout Editor")
main_frame = ttk.Frame(root, padding=(20))
main_frame.grid(column=0, row=0) #, sticky=('N', 'W', 'E', 'S'))
Button_frame = ttk.Frame(main_frame,borderwidth=5)
Button_frame.grid(column=0,row=0)
Power_frame = ttk.Frame(main_frame,borderwidth=5)
Power_frame.grid(column=1,row=0)
Token_frame = ttk.Frame(main_frame)
Token_frame.grid(column=2,row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


OptionMod1 = tk.StringVar(main_frame)
OptionMod2 = tk.StringVar(main_frame)
OptionMod3 = tk.StringVar(main_frame)
OptionMod4 = tk.StringVar(main_frame)
OptionMod5 = tk.StringVar(main_frame)
OptionMod6 = tk.StringVar(main_frame)
PistolMod = tk.StringVar(main_frame)

PowerMod1 = tk.StringVar(main_frame)
PowerMod2 = tk.StringVar(main_frame)
PowerMod3 = tk.StringVar(main_frame)
PowerMod4 = tk.StringVar(main_frame)
PowerMod5 = tk.StringVar(main_frame)
PowerMod6 = tk.StringVar(main_frame)

#power token
PTokNum1 = tk.StringVar(main_frame)
PTokNum2 = tk.StringVar(main_frame)
PTokNum3 = tk.StringVar(main_frame)
PTokNum4 = tk.StringVar(main_frame)
#up token
UTokNum1 = tk.StringVar(main_frame)
UTokNum2 = tk.StringVar(main_frame)
UTokNum3 = tk.StringVar(main_frame)
UTokNum4 = tk.StringVar(main_frame)
#down token
DTokNum1 = tk.StringVar(main_frame)
DTokNum2 = tk.StringVar(main_frame)
DTokNum3 = tk.StringVar(main_frame)
DTokNum4 = tk.StringVar(main_frame)
#lists of token vars
BonusTok = [PTokNum1,PTokNum2,PTokNum3,PTokNum4]
UpTok = [UTokNum1,UTokNum2,UTokNum3,UTokNum4]
DownTok =[DTokNum1,DTokNum2,DTokNum3,DTokNum4]
def setsave():
    global DoubleModules
    DoubleModules.clear()
    with open(filename, "r") as Save:
        for line in Save:
            if line.startswith("tpoints_obj_perk") or line.startswith("tpoints_obj_artefact") or line.startswith("tpoints_obj_item"):
                P = re.search('"-?\d+(\.\d+)?"',line).group()
                P = re.search('-?\d+(\.\d+)?',P).group()
                DoubleModules.append(P)
            #weapon or item
setsave()




def Testfunc(subclass):
    global Currentclass
    Currentclass = subclass
    items.clear()
    Tokens.clear()
    with open(filename, "r") as Save:
        for line in Save:
            if line.startswith("perkslot"):
                for num in Loadout:
                    if line.startswith("perkslot"+num+"class"+Currentclass):
                        P = re.search("obj_\w+(\d+)?_\w+",line).group()
                        items.append(P)
                    else:
                        continue
            elif line.startswith("wbonus") or line.startswith("wplus") or line.startswith("wminus"):
                Tokens.append(line)
            elif line.startswith("ibonus") or line.startswith("iplus") or line.startswith("iminus"):
                Tokens.append(line)
            else:
                continue
    PistolMod.set(ShownPistols[VarPistols.index(items[0])])
    OptionMod1.set(ShownModules[VarSmodules.index(items[6])])
    OptionMod2.set(ShownModules[VarSmodules.index(items[5])])
    OptionMod3.set(ShownModules[VarSmodules.index(items[4])])
    OptionMod4.set(ShownModules[VarSmodules.index(items[3])])
    OptionMod5.set(ShownModules[VarSmodules.index(items[2])])
    OptionMod6.set(ShownModules[VarSmodules.index(items[1])])

    PowerMod6.set(DoubleModules[VarSmodules.index(items[1])])
    PowerMod5.set(DoubleModules[VarSmodules.index(items[2])])
    PowerMod4.set(DoubleModules[VarSmodules.index(items[3])])
    PowerMod3.set(DoubleModules[VarSmodules.index(items[4])])
    PowerMod2.set(DoubleModules[VarSmodules.index(items[5])])
    PowerMod1.set(DoubleModules[VarSmodules.index(items[6])])
    Pistolchangecolor()
    Regchangecolor(OptionMod6,Mod2)
    Regchangecolor(OptionMod5,Mod1) 
    Regchangecolor(OptionMod4,Item2) 
    Regchangecolor(OptionMod3,Item1)
    Regchangecolor(OptionMod2,StartItem)
    Regchangecolor(OptionMod1,Core)
    tokenset(WI)


def tokenset(wi):
    Sclass = spliting(Currentclass)
    #make bonus tokens show up, should be split into own function
    for tok in Tokens:
        if tok.startswith(wi):
            if re.search(Sclass,tok) != None:
                ClassTokens.append(tok)
    global WI
    global CurTokShown
    if wi == "w":
        WI = "w"
        CurTokShown = ShownWeapons
    elif wi == "i":
        WI = "i"
        CurTokShown = ShownItems
    Token1['values'] = CurTokShown
    Token2['values'] = CurTokShown
    Token3['values'] = CurTokShown
    Token4['values'] = CurTokShown
    Token5['values'] = CurTokShown
    Token6['values'] = CurTokShown
    Token7['values'] = CurTokShown
    Token8['values'] = CurTokShown
    Token9['values'] = CurTokShown
    Token10['values'] = CurTokShown
    Token11['values'] = CurTokShown
    Token12['values'] = CurTokShown
    if ClassTokens == []:
        for B in BonusTok:
            B.set("")
        for U in UpTok:
            U.set("")
        for D in DownTok:
            D.set("")
    for B in BonusTok:
        #what is a tracking variable. it tracks whether or not there is a 'wbonus' in the classtokens list
        what = 0
        for T in ClassTokens:
            if T.startswith(wi+"bonus"):
                what += 1
                P = re.search('"-?\d+(\.\d+)?"',T).group()
                P = float(P[1:-1])
                P = int(P)
                if wi == "w":
                    B.set(ShownWeapons[P])
                else:
                    B.set(ShownItems[P])
                ClassTokens.remove(T)
                break
            else:
                B.set("")
                continue
        else:
            if what < 1:
                B.set("")
        
    for U in UpTok:
        what = 0
        for T in ClassTokens:
            if T.startswith(wi+"plus"):
                what += 1
                P = re.search('"-?\d+(\.\d+)?"',T).group()
                P = float(P[1:-1])
                P = int(P)
                if wi == "w":
                    U.set(ShownWeapons[P])
                else:
                    U.set(ShownItems[P])
                ClassTokens.remove(T)
                break
            else:
                U.set("")
                continue
        else:
            if what < 1:
                U.set("")
    for D in DownTok:
        what = 0
        for T in ClassTokens:
            if T.startswith(wi+"minus"):
                what += 1
                P = re.search('"-?\d+(\.\d+)?"',T).group()
                P = float(P[1:-1])
                P = int(P)
                if wi == "w":
                    D.set(ShownWeapons[P])
                else:
                    D.set(ShownItems[P])
                ClassTokens.remove(T)
                break
            else:
                D.set("")
                continue
        else:
            if what < 1:
                D.set("")


def SubmitLoadout():
    subclass = spliting(Currentclass)
    x = 0
    with open(filename, "r") as Save, open(tfilename, "w") as Tsave:
        for line in Save:
            if line.startswith("perkslot"+Loadout[0]+"class"+Currentclass):
                Tsave.write(re.sub("obj_\w+(\d+)?_\w+",VarPistols[ShownPistols.index(PistolMod.get())],line))
            elif line.startswith("perkslot"+Loadout[6]+"class"+Currentclass):
                Tsave.write(re.sub("obj_\w+(\d+)?_\w+",VarSmodules[ShownModules.index(OptionMod1.get())],line))
            elif line.startswith("perkslot"+Loadout[5]+"class"+Currentclass):
                Tsave.write(re.sub("obj_\w+(\d+)?_\w+",VarSmodules[ShownModules.index(OptionMod2.get())],line))
            elif line.startswith("perkslot"+Loadout[4]+"class"+Currentclass):
                Tsave.write(re.sub("obj_\w+(\d+)?_\w+",VarSmodules[ShownModules.index(OptionMod3.get())],line))
            elif line.startswith("perkslot"+Loadout[3]+"class"+Currentclass):
                Tsave.write(re.sub("obj_\w+(\d+)?_\w+",VarSmodules[ShownModules.index(OptionMod4.get())],line))
            elif line.startswith("perkslot"+Loadout[2]+"class"+Currentclass):
                Tsave.write(re.sub("obj_\w+(\d+)?_\w+",VarSmodules[ShownModules.index(OptionMod5.get())],line))
            elif line.startswith("perkslot"+Loadout[1]+"class"+Currentclass):
                Tsave.write(re.sub("obj_\w+(\d+)?_\w+",VarSmodules[ShownModules.index(OptionMod6.get())],line))
            elif line.startswith("tpoints_"):
                if line.startswith("tpoints_"+VarSmodules[ShownModules.index(OptionMod1.get())]):
                    Tsave.write(re.sub('"-?\d+(\.\d+)?"','"'+PowerMod1.get()+'"',line))
                elif line.startswith("tpoints_"+VarSmodules[ShownModules.index(OptionMod2.get())]):
                    Tsave.write(re.sub('"-?\d+(\.\d+)?"','"'+PowerMod2.get()+'"',line))
                elif line.startswith("tpoints_"+VarSmodules[ShownModules.index(OptionMod3.get())]):
                    Tsave.write(re.sub('"-?\d+(\.\d+)?"','"'+PowerMod3.get()+'"',line))
                elif line.startswith("tpoints_"+VarSmodules[ShownModules.index(OptionMod4.get())]):
                    Tsave.write(re.sub('"-?\d+(\.\d+)?"','"'+PowerMod4.get()+'"',line))
                elif line.startswith("tpoints_"+VarSmodules[ShownModules.index(OptionMod5.get())]):
                    Tsave.write(re.sub('"-?\d+(\.\d+)?"','"'+PowerMod5.get()+'"',line))
                elif line.startswith("tpoints_"+VarSmodules[ShownModules.index(OptionMod6.get())]):
                    Tsave.write(re.sub('"-?\d+(\.\d+)?"','"'+PowerMod6.get()+'"',line))
                else:
                    Tsave.write(line)
            elif line.startswith("wunlock0"):
                Tsave.write(line)
                if WI == "w":
                    y = 0
                    for B in BonusTok:
                        Y = str(y)
                        if B.get() == '' or None:
                            continue
                        B = ShownWeapons.index(B.get())
                        B = str(B)
                        Tsave.write("wbonus_"+subclass+"__"+Y+'="'+B+'.000000"\n')
                        y+=1
                    y = 0
                    for U in UpTok:
                        Y = str(y)
                        if U.get() == '' or None:
                            continue
                        U = ShownWeapons.index(U.get())
                        U = str(U)
                        Tsave.write("wplus_"+subclass+"__"+Y+'="'+U+'.000000"\n')
                        y+=1
                    y = 0
                    for D in DownTok:
                        Y = str(y)
                        if D.get() == '' or None:
                            continue
                        D = ShownWeapons.index(D.get())
                        D = str(D)
                        Tsave.write("wminus_"+subclass+"__"+Y+'="'+D+'.000000"\n')
                        y+=1
            elif (WI == "w") and (line.startswith("wbonus") or line.startswith("wplus") or line.startswith("wminus")):
                if re.search(subclass,line) != None:
                    continue
                else:
                    Tsave.write(line)
            elif line.startswith("iintel 0"):
                Tsave.write(line)
                if WI == "i":
                    y = 0
                    for B in BonusTok:
                        Y = str(y)
                        if B.get() == '' or None:
                            continue
                        B = ShownItems.index(B.get())
                        B = str(B)
                        Tsave.write("ibonus_"+subclass+"__"+Y+'="'+B+'.000000"\n')
                        y+=1
                    y = 0
                    for U in UpTok:
                        Y = str(y)
                        if U.get() == '' or None:
                            continue
                        U = ShownItems.index(U.get())
                        U = str(U)
                        Tsave.write("iplus_"+subclass+"__"+Y+'="'+U+'.000000"\n')
                        y+=1
                    y = 0
                    for D in DownTok:
                        Y = str(y)
                        if D.get() == '' or None:
                            continue
                        D = ShownItems.index(D.get())
                        D = str(D)
                        Tsave.write("iminus_"+subclass+"__"+Y+'="'+D+'.000000"\n')
                        y+=1
            elif (WI == "i") and (line.startswith("ibonus") or line.startswith("iplus") or line.startswith("iminus")):
                if re.search(subclass,line) != None:
                    continue
                else:
                    Tsave.write(line)
            else:
                Tsave.write(line)
    Safetywindow()


def Safetywindow():
    if safety == 0:
        CopytoSave()
    else:
        SafetyWindow = tk.Toplevel(root)
        SafetyWindow.title("ALERT!")
        tk.Label(SafetyWindow, text ="Do you want to overwrite your Save File?").pack()
        tk.Button(SafetyWindow, text = "Yes", command=lambda: [CopytoSave(),SafetyWindow.destroy()]).pack()

def changeWI():
    if WI == "w":
        WI = "i"
    else:
        WI = "w"

def CopytoSave():
    with open(filename, "w") as Save, open(tfilename, "r") as Tsave:
        for line in Tsave:
            Save.write(line)
    setsave()


def AutoModuleEdit(power):
    if re.search("(-?(0|[1-9]\d*)?(\.\d+)?(?<=\d)(e-?(0|[1-9]\d*))?|0x[0-9a-f]+)",power) == None:
        messagebox.showinfo('Power error','Sorry, you pressed the AutoModule button without putting an interger input in! Try using only numbers this time, okay?')
        return
    with open(filename, "r") as Save, open(tfilename, "w") as Tsave:
        TruePower = '"' + power + '"'
        for line in Save:
            if line.startswith("tpoints_obj_perk_"):
                Tsave.write(re.sub('"-?\d+(\.\d+)?"', TruePower, line))
                continue
            Tsave.write(line)
    Safetywindow()

def OPModuleEdit():
    OPpower=["10.000000","2.500000","2.000000","3.000000","-7.000000","7.000000","30.000000","50.000000","10.000000","15.000000","6.000000","4.000000","4.000000","5.000000","10.000000","3.000000","1.000000","1.000000","8.000000","7.000000","5.000000","10.000000","7.000000","2.500000","40.000000","7.000000","5.000000","20.000000","-0.000100","10.000000","7.000000","7.000000","3.000000","1","1","1","1","15.000000","10.000000","8.000000","4.000000","5.500000","2.900000","1.600000","10.000000","7.000000","5.000000","6.000000","20.000000","20.000000","2.500000","10.000000","1","1","10.000000","20.000000","20.000000","30.000000","20.00000","20.000000","4.000000","5.000000","10.000000","2.500000","10.000000","2.00000","7.000000","7.000000","-34.000000","12.000000","1","1","1"]
    messagebox.showinfo("Ymmv","Overpowered module power editing (your mileage may vary)")
    with open(filename, "r") as Save, open(tfilename, "w") as Tsave:
        j = 0
        for line in Save:
            if line.startswith("tpoints_obj_perk_"):
                item = OPpower[j]
                ActiveLine = '"' + item + '"'
                Tsave.write(re.sub('"-?\d+(\.\d+)?"', ActiveLine, line))
                j += 1
                continue
            Tsave.write(line)
    Safetywindow()

def NewDailyRun():
    with open(filename,"r") as Save, open(tfilename,"w") as Tsave:
        for line in Save:
            if line.startswith("drun"):
                Tsave.write(re.sub('"-?\d+(\.\d+)?"','"1.000000"',line))
            else:
                Tsave.write(line)
    Safetywindow()

def MaxData():
    with open(filename,"r") as Save, open(tfilename,"w") as Tsave:
        for line in Save:
            if line.startswith("currency"):
                Tsave.write(re.sub('"-?\d+(\.\d+)?"','"1000.000000"',line))
            else:
                Tsave.write(line)
    Safetywindow()

def CheatCodeReturn():
    with open(filename,"r") as Save, open(tfilename,"w") as Tsave:
        for line in Save:
            if line.startswith("statist"):
                Tsave.write(re.sub('"-?\d+(\.\d+)?"','"0.000000"',line))
            else:
                Tsave.write(line)
    Safetywindow()



def spliting(Class):
    Lis = [char for char in Class]
    return (Lis[0] + "_" + Lis [1])

def AutoWeaponSpawnEdit():
    realclass = spliting(Currentclass)
    weplist = list()
    with open(filename, "r") as Save:
        for line in Save:
            if line.startswith("wbonus_"+realclass):
                wepID = re.search('"\d+\.', line)
                wepID = wepID.group()
                weplist.append(wepID[1:-1])
        if len(weplist) == 0:
            messagebox.showinfo("Token Error","Sorry, would you go add a power token to the weapon(s) you want?")
            return
    with open(filename, "r") as Save, open(tfilename, "w") as Tsave:
        if len(weplist) != 0:
            for line in Save:
                if line.startswith("wdropchange"):
                    for weapon in weplist:
                        if line.startswith("wdropchange"+weapon+"="):
                            Tsave.write(re.sub('"-?\d+\.\d+"','"10.000000"',line))
                            break
                        else:
                            continue
                    if not(line.startswith("wdropchange"+weapon+"=")):
                        Tsave.write(re.sub('"-?\d+\.\d+"','"-8.000000"',line))
                elif line.startswith("wunlock"):
                    if len(weplist) == 0:
                        if re.search('"\d.',line).group() == '"0.':
                            Tsave.write(re.sub('"-?\d+\.\d+"','"1.000000"',line))
                            continue
                        else:
                            Tsave.write(line)
                            continue
                    for weapon in weplist:
                        if line.startswith("wunlock"+weapon+"="):
                            Tsave.write(re.sub('"-?\d+\.\d+"','"1.000000"',line))
                            weplist.remove(weapon)
                            break
                        elif re.search('"\d.',line).group() == '"0.':
                            Tsave.write(re.sub('"-?\d+\.\d+"','"1.000000"',line))
                            break
                        if weapon == weplist[-1]:
                            Tsave.write(line)
                else:
                    Tsave.write(line)
                    continue

    Safetywindow()

def AutoItemSpawnEdit():
    subclass = spliting(Currentclass)
    itemlist = list()
    with open(filename, "r") as Save:
        for line in Save:
            if line.startswith("ibonus_"+subclass):
                itemID = re.search('"\d+\.', line)
                itemID = itemID.group()
                itemlist.append(itemID[1:-1])
        if len(itemlist) == 0:
            messagebox.showinfo("Token Error","Sorry, would you go add a power token for the item you want?")
            return
    with open(filename, "r") as Save, open(tfilename, "w") as Tsave:
        if len(itemlist) != 0:
            for line in Save:
                if line.startswith("idropchange"):
                    for item in itemlist:
                        if line.startswith("idropchange "+item+"="):
                            Tsave.write(re.sub('"-?\d+\.\d+"','"10.000000"',line))
                            break
                        else:
                            continue                        
                    if not(line.startswith("idropchange "+item+"=")):
                        Tsave.write(re.sub('"-?\d+\.\d+"','"-8.000000"',line))
                else:
                    Tsave.write(line)
    Safetywindow()

def weaponspawnreset():
    with open(filename,"r") as Save, open(tfilename,"w") as Tsave:
        for line in Save:
            if line.startswith("wdropchange"):
                # this is the fix for armageddon shard showing up (yay its fixed)
                if line.startswith("wdropchange147"):
                    Tsave.write(re.sub('"-?\d+\.\d+"','"-10.000000"',line))
                else:
                    Tsave.write(re.sub('"-?\d+\.\d+"','"0.000000"',line))
            else:
                Tsave.write(line)
    Safetywindow()
    

def itemspawnreset():
    with open(filename,"r") as Save, open(tfilename,"w") as Tsave:
        for line in Save:
            if line.startswith("idropchange"):
                Tsave.write(re.sub('"-?\d+\.\d+"','"0.000000"',line))
            else:
                Tsave.write(line)
    Safetywindow()

def undoresearch():
    with open(filename,"r") as Save, open(tfilename,"w") as Tsave:
        for line in Save:
            if line.startswith("resunlock"):
                Tsave.write(re.sub('"-?\d+\.\d+"','"0.000000"',line))
            else:
                Tsave.write(line)
    Safetywindow()

def openSave():
    os.startfile(filename)


def safetyFunc():
    global safety
    if safety != 0:
        safety = 0
    if safety == 0:
        safety = 1
#here's the styles for the comboboxes
style=ttk.Style()
style.theme_use('alt')
style.configure("Gaurdian.TCombobox",fieldbackground="blue")
style.configure("Rouge.TCombobox",fieldbackground="darkblue")
style.configure("Commando.TCombobox",fieldbackground="darkgreen")
style.configure("Specialist.TCombobox",fieldbackground="red")
style.configure("Other.TCombobox",fieldbackground="white")
style.configure("Mode.TCombobox",fieldbackground="lightblue")
style.configure("Artefact.TCombobox",fieldbackground="lightgreen")

#here's the 2 functions that change the colors of the comboboxes
def Pistolchangecolor():
    Curpistol = PistolMod.get()
    if Curpistol == ShownPistols[11] or Curpistol == ShownPistols[10]:
        Gun.configure(style="Gaurdian.TCombobox",foreground="white")
    elif Curpistol == ShownPistols[12] or Curpistol == ShownPistols[13]:
        Gun.configure(style="Rouge.TCombobox",foreground="white")
    elif Curpistol == ShownPistols[7] or Curpistol == ShownPistols[8]:
        Gun.configure(style="Commando.TCombobox",foreground="white")
    elif Curpistol == ShownPistols[5] or Curpistol == ShownPistols[6]:
        Gun.configure(style="Specialist.TCombobox",foreground="white")
    else:
        Gun.configure(style="Other.TCombobox",foreground="black")
    
def Regchangecolor(Modulation,Ident):
    Cur = Modulation.get()
    for i in range (4,8):
        if Cur == ShownModules[i]:
            Ident.configure(style="Mode.TCombobox",foreground="black")
    for i in range (8,23):
        if Cur == ShownModules[i]:
            Ident.configure(style="Artefact.TCombobox",foreground="black")
    for i in range (23,47):
        if Cur == ShownModules[i]:
            Ident.configure(style="Specialist.TCombobox",foreground="white")
    for i in range (47,73):
        if Cur == ShownModules[i]:
            Ident.configure(style="Commando.TCombobox",foreground="white")
    for i in range (73,98):
        if Cur == ShownModules[i]:
            Ident.configure(style="Rouge.TCombobox",foreground="white")
    for i in range (98,123):
        if Cur == ShownModules[i]:
            Ident.configure(style="Gaurdian.TCombobox",foreground="white")
    for i in range (0,4):
        if Cur == ShownModules[i]:
            Ident.configure(style="Other.TCombobox",foreground="black")
    for i in range (123,131):
        if Cur == ShownModules[i]:
            Ident.configure(style="Other.TCombobox",foreground="black")
    

def about():
    messagebox.showinfo('Synthetik Python Mod','By: Builder_Roberts\nMade for Synthetik 1!\n With help from: Tactu, Arti, Lawro, Saper, ElectricOldMen')

def notworking():
    messagebox.showinfo('Actual help','first: try opening and closing synthetik. Make sure Synthetik is closed. That will reset the save file to what Synthetik Needs.\nSecond: message @Mason on the discord. He is the creator of this after all.')

WeaponSpawnNames = 'Nemesis Prototype,Chaos Launcher,Object 29,Road Warrior,Apollon 5 LMG,P33 Compact,Tactical Observer,Mjolnir Chain LTN,Last Breath,PXS Covert Ops,57 Fusion Classic,Sour DMR,Spectre,Medic FMG-9,R5000 Sudden DMR,Vindicator Ultra,Raptor Laser SG,LS Laser Sub,Super 90,GM6 Lynx Evo,Kaida Laser Pistol,Eraser DMR,M32 Multipurpose,AMD 65,ION Obliterator,Armageddon,Enforcer Carbine,Damnnation,SS58 Plasma Charger,KI Vector,Spas 12,ML7000 Plus,M79 Terminator,Kaida Model H,FS5 Flametounge,Flak Heavy Cannon,RRX Coil Shotgun,XM2 Coil Pistol,Twin Mill Mk.2,SCR Laser Socom,AEK Special Elite,AS VAL,Battle Hymn,RPK Tundra,Ripjack,Liandry Railgun,MAG47 Heavy LMG,Kaida Nailgun,HIG-S Particle Cannon,Bren Anti-Air,X512 Experimental,Makeshift Firecannon,Ballistic CRX_Bow,420 Sniperdragon,Auto 9/45,K3 Boltcaster SMG,Human RPG,Kaida Medic ACR-X,Human Model 9800K,KSG 2000,Desert Eagle,Master Chief,G17 Undercover,PPQ-H Laser Pistol,UMP-9 Semi,Annilhilator,P25 overdrive,Yoko-Lagann,Super Shorty,W21 Lever Action,Pressurized Impaler,Gladiator,HMN Laser Cannon,AKS-74U,K98 Classic,UMP Tornado,T-8-00 Guage,Ares GL-16,Viking Riotshield,Eminince AR,A5-C Test Version,AN-94 Deathstalker,P9000 Supernova,TEC 9.95,LG2 Onslaught,Last Ditch M16,F14 Mini,Sturmgewher 44,Raider Scrap Cannon,Specialist M16-A5,Tuned M14 EBR,FMG-9 Personal,M75 Heavy Support,Titanium Eagle,PSG Emerald Sword,QBZ_Laser,Type-89 Tokko,K7 Competition'
def WNewSpawn():
    SpawnWindow = tk.Toplevel(main_frame)
    howtotext = tk.Label(SpawnWindow,text="Here's a list of every weapon in the game. delete every name you don't want to show up")
    howtotext.pack()
    WeaponNames = tk.Text(SpawnWindow,wrap="word")
    WeaponNames.insert('1.0',WeaponSpawnNames)
    WeaponNames.pack()
    warningtext = tk.Label(SpawnWindow,text="Make sure to copy your finished list, this application doesn't remember.\n You'll need to use this frequently; the game eventually restores the original spawn list.")
    warningtext.pack()
    Makethesespawn = tk.Button(SpawnWindow,text="Confirm Spawn List",command= lambda:WGetspawn(WeaponNames))
    Makethesespawn.pack()

def WGetspawn(identity):
    content = identity.get('1.0','end')
    Clist = list(map(str,content.split(',')))
    Clist[-1] = Clist[-1].replace('\n','')
    WeaponSpawnIds.clear()
    for item in Clist:
        if item not in ShownWeapons:
            Clist.remove(item)
        else:
            WeaponSpawnIds.append(str(ShownWeapons.index(item)))
    weplist = WeaponSpawnIds
    with open(filename, "r") as Save, open(tfilename, "w") as Tsave:
        if len(weplist) != 0:
            for line in Save:
                if line.startswith("wdropchange"):
                    for weapon in weplist:
                        if line.startswith("wdropchange"+weapon+"="):
                            Tsave.write(re.sub('"-?\d+\.\d+"','"10.000000"',line))
                            break
                        else:
                            continue
                    if not(line.startswith("wdropchange"+weapon+"=")):
                        Tsave.write(re.sub('"-?\d+\.\d+"','"-8.000000"',line))
                elif line.startswith("wunlock"):
                    for weapon in weplist:
                        if line.startswith("wunlock"+weapon+"="):
                            Tsave.write(re.sub('"-?\d+\.\d+"','"1.000000"',line))
                            weplist.remove(weapon)
                            break
                        elif re.search('"\d.',line).group() == '"0.':
                            Tsave.write(re.sub('"-?\d+\.\d+"','"1.000000"',line))
                            break
                        if weapon == weplist[-1]:
                            Tsave.write(line)
                else:
                    Tsave.write(line)
                    continue

    Safetywindow()

ItemSpawnNames = '''Chaos Potion,Hyperfeed,Shock Impulse,Umbra Adaptive Cloak,Healing Crystal,Field Supply,Health Vial,Overdose,Fangs of Mordigan,Unstable Current,Divine Reconstructor,RV Rebuke System,Devil's Dice,Maddness Glasses,Refractor Crystal,Upgrade Kit,Orb of Iron,Unidentified Potion,Orb of Lightning,Orb of Fire,Orb of Wind,Blood Rite,Twin Link 2,Heart Core,Refresher,Core Upgrade Kit,Black Berserk Charm,Trophy System Drone?,Combat Amphetamine?,Methadone,Incubus,Tsunami Talisman,ShieldBurst,HE Grenade,Flash Grenade,Stun Grenade,Plasma Grenade,Acid Grenade,Psy Field,Heavy Steel Trap,PowerShot,R-Plating,Fast Sling,Facemelter,Uranium 235,Maverick MKV,Sidewinder,Fire Prism,Order 322,Last Stand,Stinger Jet Glider,Air Com,Power Array,Composite 4,Stim Pack,Phaser,Gun Drone Spawner,Heart Seeker,M205 Launcher,Target Cogitator,Rosarius,Reality Ripper,Cell Replacer,Lifeblood,Direct Current,Akira,Lightning Boots,Ring of Experience,Auto Taser,Blood Bolt,LMG sentry Turret,DMR Sentry Turret,Turret?,Module Core,Ring of Glass,Bloodthirsty Ring,Unsoldered Chip?,Ripjack Hyper Blade,'Helsing' Power Bolt,Dragon's Masterkey,Reverbing Blade,Flare Gun,Smoke Grenade,M26 MA Shotgun System,Kunai Throwing Knives,Road Flare,G87 Beamer,Icarus,Redline,Biting Throwing Stars,Z1 Sundering Shuriken,Fan of Knives,Infinity Drill Piece,Scoundrel's Dagger,ZR99 'Living Bomb',ZK77 'Sticky Bomb',Laser Mine,'Seth-Up' Suitcase Sentry,Battlecry Module,Breaching Charge,Seismic Resonator,Air Horn,Brawndo,Eclipse,Stun Mine (Null),Acid Mine (Null),Magic Mag,Auto-Overclocker,Special Ammo Supply,Spider Mines,Heat Sink,Black Market Teleporter,Maddness Button,Heat Spreader,Decoy,Shielded Decoy,GPS,Gold Nugget,Custom Upgrade Kit,Metal Detector,Tomahawk,Targeting Laser,Hard Light Cover,Onslaught System,Intensity Chamber,Missile Drone,Constructor?,Remove Building?,Research?,Guardian,High Command,Neutrino Bomb,Magnum,Bandana,Orbital Relay,Missile Control,Trapper's Teleporter,ShieldLink,Underbarrel Mod Chip,Shaker,Elemental Resonance,Fire Water,Energy Link,Nitroglycerine,Stun Mine,Acid Mine,Armageddon Shard,Orb of Fusion,Crux of the Laser Caster,PSY Cloud Grenade'''

def INewSpawn():
    SpawnWindow = tk.Toplevel(main_frame)
    howtotext = tk.Label(SpawnWindow,text="Here's a list of every Item in the game. delete every item you don't want to show up")
    howtotext.pack()
    ItemNames = tk.Text(SpawnWindow,wrap="word")
    ItemNames.insert('1.0',ItemSpawnNames)
    ItemNames.pack()
    warningtext = tk.Label(SpawnWindow,text="Make sure to copy your finished list, this application doesn't remember.\n You'll need to use this frequently; the game eventually restores the original spawn list.")
    warningtext.pack()
    Makethesespawn = tk.Button(SpawnWindow,text="Confirm Spawn List",command= lambda:IGetSpawn(ItemNames))
    Makethesespawn.pack()

def IGetSpawn(identity):
    content = identity.get('1.0','end')
    Clist = list(map(str,content.split(',')))
    Clist[-1] = Clist[-1].replace('\n','')
    ItemSpawnIds.clear()
    for item in Clist:
        if item not in ShownItems:
            Clist.remove(item)
        else:
            ItemSpawnIds.append(str(ShownItems.index(item)))
    itemlist = ItemSpawnIds
    with open(filename, "r") as Save, open(tfilename, "w") as Tsave:
        if len(itemlist) != 0:
            for line in Save:
                if line.startswith("idropchange"):
                    for item in itemlist:
                        if line.startswith("idropchange "+item+"="):
                            Tsave.write(re.sub('"-?\d+\.\d+"','"10.000000"',line))
                            break
                        else:
                            continue                        
                    if not(line.startswith("idropchange "+item+"=")):
                        Tsave.write(re.sub('"-?\d+\.\d+"','"-8.000000"',line))
                else:
                    Tsave.write(line)
    Safetywindow()
#Button frame start

Class10 = tk.Button(Button_frame, text="Riot Guard",fg="white", bg="blue",command=lambda: Testfunc("10"))
Class10.grid(row=0,column=0)
Class11 = tk.Button(Button_frame, text="Breacher",fg="white", bg="blue",command=lambda: Testfunc("11"))
Class11.grid(row=1,column=0)
Class20 = tk.Button(Button_frame, text="Sniper",fg="white", bg="darkblue",command=lambda: Testfunc("20"))
Class20.grid(row=2,column=0)
Class21 = tk.Button(Button_frame, text="Assassin",fg="white", bg="darkblue",command=lambda: Testfunc("21"))
Class21.grid(row=3,column=0)
Class30 = tk.Button(Button_frame, text="Raider",fg="white", bg="darkgreen",command=lambda: Testfunc("30"))
Class30.grid(row=4,column=0)
Class31 = tk.Button(Button_frame, text="Heavy Gunner",fg="white", bg="darkgreen",command=lambda: Testfunc("31"))
Class31.grid(row=5,column=0)
Class40 = tk.Button(Button_frame, text="Engineer",fg="white", bg="red",command=lambda: Testfunc("40"))
Class40.grid(row=6,column=0)
Class41 = tk.Button(Button_frame, text="Demolisher",fg="white", bg="red",command=lambda: Testfunc("41"))
Class41.grid(row=7,column=0)
#Button frame end

# Power_frame start
Gun = ttk.Combobox(Power_frame, textvariable = PistolMod)
Gun['values'] = ShownPistols
Gun.grid(row=0,column=1,columnspan=2)
Gun.bind("<<ComboboxSelected>>", lambda _ :Pistolchangecolor())


Core = ttk.Combobox(Power_frame, textvariable = OptionMod1)
Core['values'] = ShownModules
Core.grid(row=1,column=1)
Core.bind("<<ComboboxSelected>>", lambda _ : Regchangecolor(OptionMod1,Core))

CorePower = ttk.Combobox(Power_frame, textvariable = PowerMod1)
CorePower.grid(row=1,column=2)

StartItem = ttk.Combobox(Power_frame, textvariable = OptionMod2)
StartItem['values'] = ShownModules
StartItem.grid(row=2,column=1)
StartItem.bind("<<ComboboxSelected>>", lambda _ : Regchangecolor(OptionMod2,StartItem))

SIPower = ttk.Combobox(Power_frame, textvariable = PowerMod2)
SIPower.grid(row=2,column=2)

Item1 = ttk.Combobox(Power_frame, textvariable = OptionMod3)
Item1['values'] = ShownModules
Item1.grid(row=3,column=1)
Item1.bind("<<ComboboxSelected>>", lambda _ : Regchangecolor(OptionMod3,Item1))

I1Power = ttk.Combobox(Power_frame,textvariable= PowerMod3)
I1Power.grid(row=3,column=2)

Item2 = ttk.Combobox(Power_frame,textvariable = OptionMod4)
Item2['values'] = ShownModules
Item2.grid(row=4,column=1)
Item2.bind("<<ComboboxSelected>>", lambda _ : Regchangecolor(OptionMod4,Item2))

I2Power = ttk.Combobox(Power_frame,textvariable= PowerMod4)
I2Power.grid(row=4,column=2)

Mod1 = ttk.Combobox(Power_frame, textvariable =OptionMod5)
Mod1['values'] = ShownModules
Mod1.grid(row=5,column=1)
Mod1.bind("<<ComboboxSelected>>", lambda _ : Regchangecolor(OptionMod5,Mod1))

M1Power = ttk.Combobox(Power_frame,textvariable=PowerMod5)
M1Power.grid(row=5,column=2)

Mod2 = ttk.Combobox(Power_frame,textvariable = OptionMod6)
Mod2['values'] = ShownModules
Mod2.grid(row=6,column=1)
Mod2.bind("<<ComboboxSelected>>", lambda _ : Regchangecolor(OptionMod6,Mod2))

M2Power = ttk.Combobox(Power_frame,textvariable=PowerMod6)
M2Power.grid(row=6,column=2)

Submit = tk.Button(Power_frame,text="submit",command=SubmitLoadout)
Submit.grid(row=7,column=1,columnspan=2)
Auto = tk.Button(Power_frame,text="Auto Module Edit", command=lambda: AutoModuleEdit(Autopower.get()))
Auto.grid(row=8,column=1)
Autopower = ttk.Entry(Power_frame)
Autopower.grid(row=8,column=2)

#power frame end

#Token_frame start
TokWeapon = tk.Button(Token_frame,text="Weapons",command=lambda:tokenset("w"))
TokWeapon.grid(row=0,column=0)
TokItems = tk.Button(Token_frame,text="Items",command=lambda:tokenset("i"))
TokItems.grid(row=0,column=1)

#Bonus tokens
Bonus_Frame = ttk.Frame(Token_frame,borderwidth=5)
Bonus_Frame.grid(column=0,row=1,columnspan=2)
BonusLabel = tk.Label(Bonus_Frame,text="Power tokens")
BonusLabel.grid(row=0,column=0)
Token1 =  ttk.Combobox(Bonus_Frame,textvariable=PTokNum1)
Token1['values'] = CurTokShown
Token1.grid(row=1,column=0)
Token2 = ttk.Combobox(Bonus_Frame,textvariable=PTokNum2)
Token2['values'] = CurTokShown
Token2.grid(row=2,column=0)
Token3 = ttk.Combobox(Bonus_Frame,textvariable=PTokNum3)
Token3['values'] = CurTokShown
Token3.grid(row=3,column=0)
Token4 = ttk.Combobox(Bonus_Frame,textvariable=PTokNum4)
Token4['values'] = CurTokShown
Token4.grid(row=4,column=0)

#up tokens
UP_Frame = ttk.Frame(Token_frame, borderwidth=5)
UP_Frame.grid(column=0,row=2,columnspan=2)
UPLabel = tk.Label(UP_Frame,text="Supply UP tokens")
UPLabel.grid(row=0,column=0)
Token5 = ttk.Combobox(UP_Frame,textvariable=UTokNum1)
Token5['values'] = CurTokShown
Token5.grid(row=6,column=0)
Token6 = ttk.Combobox(UP_Frame,textvariable=UTokNum2)
Token6['values'] = CurTokShown
Token6.grid(row=7,column=0)
Token7 = ttk.Combobox(UP_Frame,textvariable=UTokNum3)
Token7['values'] = CurTokShown
Token7.grid(row=8,column=0)
Token8 = ttk.Combobox(UP_Frame,textvariable=UTokNum4)
Token8['values'] = CurTokShown
Token8.grid(row=9,column=0)

#down tokens
DOWN_Frame = ttk.Frame(Token_frame,borderwidth=5)
DOWN_Frame.grid(column=0,row=3,columnspan=2)
DownLabel = tk.Label(DOWN_Frame,text="Supply Down tokens")
DownLabel.grid(row=0,column=0)
Token9 = ttk.Combobox(DOWN_Frame,textvariable=DTokNum1)
Token9['values'] = CurTokShown
Token9.grid(row=10,column=0)
Token10 = ttk.Combobox(DOWN_Frame,textvariable=DTokNum2)
Token10['values'] = CurTokShown
Token10.grid(row=11,column=0)
Token11 = ttk.Combobox(DOWN_Frame,textvariable=DTokNum3)
Token11['values'] = CurTokShown
Token11.grid(row=12,column=0)
Token12 = ttk.Combobox(DOWN_Frame,textvariable=DTokNum4)
Token12['values'] = CurTokShown
Token12.grid(row=13,column=0)
#Token_frame end

MenuBar = Menu(main_frame)
file = Menu(MenuBar,tearoff=0)
file.add_command(label="Open",command=lambda: browse_files(filename, tfilename))
file.add_command(label="Show",command=openSave)
file.add_command(label="Exit",command=root.quit)
MenuBar.add_cascade(label="File",menu=file)

power = Menu(MenuBar,tearoff=0)
power.add_command(label="OPauto",command=OPModuleEdit)
power.add_command(label="Quick 1.6x",command=lambda: AutoModuleEdit("1.60000"))
MenuBar.add_cascade(label="Power",menu=power)

misc = Menu(MenuBar,tearoff=0)
misc.add_command(label="Daily Run Reset",command=NewDailyRun)
misc.add_command(label="Max Data",command=MaxData)
misc.add_command(label="Undo Research",command=undoresearch)
misc.add_command(label="Cheat Code Reset",command=CheatCodeReturn)
misc.add_command(label="Safety On/Off", command=safetyFunc)
MenuBar.add_cascade(label="Misc",menu=misc)

spawn = Menu(MenuBar,tearoff=0)
spawn.add_command(label="Weapon spawn",command=WNewSpawn)
spawn.add_command(label="Item spawn",command=INewSpawn)
spawn.add_command(label="Reset Item Spawn",command=itemspawnreset)
spawn.add_command(label="Reset Weapon Spawn",command=weaponspawnreset)
spawn.add_command(label="Old Weapon Spawn", command=AutoWeaponSpawnEdit)
spawn.add_command(label="Old Item Spawn",command=AutoItemSpawnEdit)
MenuBar.add_cascade(label="Spawn",menu=spawn)

Helpbar = Menu(MenuBar,tearoff=0)
Helpbar.add_command(label="About",command=about)
Helpbar.add_command(label="Not working?",command=notworking)
MenuBar.add_cascade(label="Help",menu=Helpbar)


Testfunc(Currentclass)
tokenset(WI)
root.configure(menu = MenuBar)
root.mainloop()