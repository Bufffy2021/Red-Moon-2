import random, os, time, requests, datetime, colorama
from colorama import Fore
colorama.init()
    
def menu():
  print(f"""

{Fore.RED}██████╗░███████╗██████╗░  {Fore.LIGHTMAGENTA_EX}███╗░░░███╗░█████╗░░█████╗░███╗░░██╗
{Fore.RED}██╔══██╗██╔════╝██╔══██╗  {Fore.LIGHTMAGENTA_EX}████╗░████║██╔══██╗██╔══██╗████╗░██║
{Fore.RED}██████╔╝█████╗░░██║░░██║  {Fore.LIGHTMAGENTA_EX}██╔████╔██║██║░░██║██║░░██║██╔██╗██║
{Fore.RED}██╔══██╗██╔══╝░░██║░░██║  {Fore.LIGHTMAGENTA_EX}██║╚██╔╝██║██║░░██║██║░░██║██║╚████║
{Fore.RED}██║░░██║███████╗██████╔╝  {Fore.LIGHTMAGENTA_EX}██║░╚═╝░██║╚█████╔╝╚█████╔╝██║░╚███║
{Fore.RED}╚═╝░░╚═╝╚══════╝╚═════╝░  {Fore.LIGHTMAGENTA_EX}╚═╝░░░░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚══╝

{Fore.LIGHTWHITE_EX}███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝
  """)
  print("""
  """)
  print(f"""
  {Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTWHITE_EX}1{Fore.LIGHTMAGENTA_EX}]{Fore.WHITE} Nitro Generator + Checker
  {Fore.LIGHTMAGENTA_EX}[{Fore.LIGHTWHITE_EX}2{Fore.LIGHTMAGENTA_EX}]{Fore.WHITE} Exit{Fore.RESET}
  """)

  choice = int(input(f"[>] Choice: "))
  valid = 0
  valid_codes = []
  invalid = 0

  if choice == 10101010:
    amt = int(input("[>] How Many Nitro Codes Would You Like To Generate?: "))
    codeLen = 16
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123457890"
    k = open("NitroGenResults/Codes.txt", "w")
    for i in range(amt):
      print("[+] https://discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)))
      k.write("https://discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)) + "\n")
    k.close()
    print("[+] Codigos Guardados en Codes.txt")
  elif choice == 487814:
    with open("CodesToCheck.txt") as f:
      for line in f:
        s = requests.Session()
        nitro = line.strip("\n")
        start = datetime.datetime.now()


        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"


        r = s.get(url)

        if r.status_code == 200:
          print(f"[#] Valido | {nitro}".format(line.strip("\n")))
          valid_codes.append(nitro)
          valid += 1

          
          k = open("CheckerResults/Valids.txt", 'w')
          k.write(valid_codes)
        else:
          print(f"[!] Invalid | {nitro}".format(line.strip("\n")))
          invalid += 1
      print("\n")
      print(f"""
      Valids = {valid}
      Invalids = {invalid}
      Valid Codes: {', '.join(valid_codes)}
      """)
  elif choice == 1:
    amt = int(input('[+] Cuantos Codigos De Nitro Quieres Generar y Verificar?: '))
    codeLen = 16
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123457890"
    g = open("NG/1/AllCodes.txt", "w")
    u = open("NG/2/Valids.txt", "w")
    n = open("NG/3/Invalids.txt", "w")
    for i in range(amt):
      g.write("https://discord.gift/" + ''.join(random.choice(letters) for i in range(codeLen)) + "\n")
    g.close()

    with open("NG/1/AllCodes.txt") as f:
      for line in f:
        invalid_codes = []
        valid_codes = []
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        s = requests.Session()

        r = s.get(url)

        if r.status_code == 200:
          print(f"{Fore.GREEN}[+] Valid | {nitro}".format(line.strip("\n")))

          valid_codes.append(nitro)
          break
        else:
          print(f"{Fore.RED}[-] Invalid | {nitro}".format(line.strip("\n")))

          invalid_codes.append(nitro)



  elif choice == 2:
    os.system('cls')
    print(f"{Fore.LIGHTRED_EX}[!] Saliendo...{Fore.RESET}") 
    time.sleep(3)
    exit(0)   
menu()
