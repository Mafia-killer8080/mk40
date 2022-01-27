import os, sys
if __name__ == "__MK__":
	if len(sys.argv) == 2:
		if sys.argv[1] == "remove":
			os.system("rm -f .__apikey__.txt")
			exit(" [!] Succesfull Deleted")
		else:
			print(" [?] Wellcome : ")
			exit(" [!] Run : python file.py remove")
	try:
		__import__("mk40").__main_MK()
	except Exception as e:
		exit(str(e))


	
	
	
	
		

	


